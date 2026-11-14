#!/usr/bin/env python3
"""Reproduce the frozen continuum calculations and bounded independent controls.

All programs run from byte-identical temporary copies. This verifies the declared
estimates and controls; it does not assert a nonlinear geometric UV theorem.
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
    ('meanfield', 'verify_meanfield_bridge.py', 'meanfield_receipt.json'),
    ('field', 'verify_field_continuum.py', 'field_continuum_receipt.json'),
    ('obstructions', 'verify_obstructions.py', 'obstruction_receipt.json'),
    ('synthesis', 'verify_synthesis.py', 'synthesis_receipt.json'),
    ('moving_parcels', 'verify_moving_parcels.py', 'moving_parcels_receipt.json'),
    ('independent_review', 'review_positive_bridge.py', 'review_receipt.json'),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error('Scientific assertions require Python without optimization.')
    output = args.output_dir.resolve()
    if output == ROOT or ROOT.is_relative_to(output) or any(
            output.is_relative_to(ROOT / p) for p in
            ('scripts', 'evidence', 'formal', 'source', 'archive', '.git')):
        parser.error('Use a separate working output directory.')
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    with tempfile.TemporaryDirectory(prefix='voss-continuum-') as temporary:
        tmp = Path(temporary)
        for label, name, receipt_name in JOBS:
            work = tmp / label
            work.mkdir()
            source = ROOT / 'scripts/continuum_checks' / name
            script = work / name
            shutil.copy2(source, script)
            dest = output / label
            dest.mkdir(parents=True, exist_ok=True)
            with (dest / 'execution.log').open('w') as log:
                try:
                    result = subprocess.run([sys.executable, str(script)], cwd=work,
                                            stdout=log, stderr=subprocess.STDOUT,
                                            timeout=300, check=False)
                    code = result.returncode
                except subprocess.TimeoutExpired:
                    code = 124
            for path in work.iterdir():
                if path.is_file() and path != script:
                    shutil.copy2(path, dest / path.name)
            record = None
            if (dest / receipt_name).exists():
                record = json.loads((dest / receipt_name).read_text())
            passed = (code == 0 and record is not None
                      and str(record.get('status', '')).lower() == 'pass')
            rows.append({'task': label, 'script': 'scripts/continuum_checks/' + name,
                         'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                         'exit_code': code, 'status': 'PASS' if passed else 'FAIL',
                         'receipt': label + '/' + receipt_name,
                         'exact_check_count': None if record is None else record.get('exact_check_count')})
            print(label + ': ' + rows[-1]['status'], flush=True)
            if not passed:
                print((dest / 'execution.log').read_text()[-5000:])
                break
    passed = len(rows) == len(JOBS) and all(r['status'] == 'PASS' for r in rows)
    receipt = {
        'schema': 'voss.controlled-continuum-reproduction.v1',
        'status': 'PASS' if passed else 'FAIL',
        'executed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'python': platform.python_version(), 'runs': rows,
        'scope': 'Controlled augmented matter-sector limit at fixed geometric cutoffs, '
                 'separate linearized spatial limit, and explicit obstruction controls. '
                 'No full nonlinear geometric/Einstein-constraint continuum is asserted.',
    }
    (output / 'continuum_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
