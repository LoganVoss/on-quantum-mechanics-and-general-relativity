#!/usr/bin/env python3
"""Reproduce frozen extension calculations in an isolated temporary workspace.

Each program is copied byte-for-byte before execution. Archived sources and
receipts remain unchanged. This includes independently implemented controls.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import platform
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    ('dynamics', 'verify_dynamical_extension.py', 'dynamical_extension_receipt.json'),
    ('curvature_response', 'verify_curvature_response.py', 'curvature_response_receipt.json'),
    ('sourced_calibrations', 'verify_sourced_calibrations.py', 'sourced_calibration_receipt.json'),
    ('one_killing', 'verify_one_killing.py', 'one_killing_receipt.json'),
    ('generic_reduction', 'verify_generic_reduction.py', 'generic_reduction_receipt.json'),
    ('projection', 'verify_projection.py', 'projection_receipt.json'),
    ('independent_rn', 'verify_rn_variation_independent.py', 'independent_rn_receipt.json'),
    ('independent_review', 'verify_independent_review.py', 'receipt.json'),
]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir', type=Path, required=True)
    args = p.parse_args()
    if sys.flags.optimize:
        p.error('Scientific assertions require Python without -O / PYTHONOPTIMIZE.')
    output = args.output_dir.resolve()
    if output == ROOT or ROOT.is_relative_to(output) or any(output.is_relative_to(ROOT / x) for x in ('source', 'scripts', 'evidence', 'formal', 'archive', '.git')):
        p.error('Use a separate working output directory.')
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    with tempfile.TemporaryDirectory(prefix='voss-extensions-') as temp:
        tmp = Path(temp)
        # Recreate the review's original relative provenance paths. Its
        # independent calculations import none of these proposed verifiers.
        sources = {
            'work/extension_joint/verify_projection.py': 'scripts/extension_checks/verify_projection.py',
            'work/extension_joint/verify_rn_variation_independent.py': 'scripts/extension_checks/verify_rn_variation_independent.py',
            'work/extension_symmetry/verify_one_killing.py': 'scripts/extension_checks/verify_one_killing.py',
            'work/extension_symmetry/verify_generic_reduction.py': 'scripts/extension_checks/verify_generic_reduction.py',
            'work/extension_symmetry/FROZEN_ONE_KILLING_FINDINGS.md': 'evidence/extensions/frozen/FROZEN_ONE_KILLING_FINDINGS.md',
            'work/extension_curvature/FROZEN_CURVATURE_FINDINGS.md': 'evidence/extensions/frozen/FROZEN_CURVATURE_FINDINGS.md',
            'work/extension_curvature/verify_sourced_calibrations.py': 'scripts/extension_checks/verify_sourced_calibrations.py',
            'work/extension_dynamics/verify_dynamical_extension.py': 'scripts/extension_checks/verify_dynamical_extension.py',
            'work/extension_dynamics/DYNAMICS_FROZEN.md': 'evidence/extensions/frozen/DYNAMICS_FROZEN.md',
        }
        for relative, original in sources.items():
            dest = tmp / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / original, dest)
        for label, filename, receipt_name in JOBS:
            work = tmp / 'runs' / label
            work.mkdir(parents=True)
            source = ROOT / 'scripts/extension_checks' / filename
            script = work / filename
            shutil.copy2(source, script)
            out = output / label
            out.mkdir(parents=True, exist_ok=True)
            with (out / 'execution.log').open('w') as handle:
                try:
                    proc = subprocess.run([sys.executable, str(script)], cwd=tmp, stdout=handle,
                                          stderr=subprocess.STDOUT, timeout=300, check=False)
                    code = proc.returncode
                except subprocess.TimeoutExpired:
                    code = 124
            for artifact in work.iterdir():
                if artifact.is_file() and artifact != script:
                    shutil.copy2(artifact, out / artifact.name)
            record = None
            if (out / receipt_name).exists():
                record = json.loads((out / receipt_name).read_text())
            passed = code == 0 and record is not None and str(record.get('status', '')).lower() == 'pass'
            rows.append({'task': label, 'script': 'scripts/extension_checks/' + filename,
                         'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                         'exit_code': code, 'status': 'PASS' if passed else 'FAIL',
                         'receipt': label + '/' + receipt_name,
                         'exact_check_count': None if record is None else record.get('exact_check_count', record.get('check_count'))})
            print(label + ': ' + rows[-1]['status'], flush=True)
            if not passed:
                print((out / 'execution.log').read_text()[-5000:])
                break
    passed = len(rows) == len(JOBS) and all(x['status'] == 'PASS' for x in rows)
    receipt = {'schema': 'voss.extensions-reproduction.v1', 'status': 'PASS' if passed else 'FAIL',
               'executed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'python': platform.python_version(), 'runs': rows,
               'scope': 'Frozen mathematical identities and bounded synthetic controls; no experimental observations or interacting quantum continuum.'}
    (output / 'extensions_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
