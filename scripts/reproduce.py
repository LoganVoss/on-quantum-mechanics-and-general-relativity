#!/usr/bin/env python3
"""Run bounded scientific checks into a separate output directory.

Does not install dependencies, publish, or overwrite archived evidence.
Use --lean after preparing the exact dependencies in formal/.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'work/reproduction')
    parser.add_argument('--lean', action='store_true')
    args = parser.parse_args()
    out = args.output_dir.resolve()
    protected = [ROOT / n for n in ('source', 'evidence', 'archive', 'formal', 'docs', 'paper', 'scripts', 'figures', '.git')]
    if out == ROOT or ROOT.is_relative_to(out) or any(out == p or out.is_relative_to(p) for p in protected):
        parser.error('Use a separate output directory, such as work/reproduction.')
    out.mkdir(parents=True, exist_ok=True)
    source = ROOT / 'source/v2.4'
    jobs = [
        ('source_suite', 'verify_source_suite.py', ['--source-root', str(source), '--output-dir', str(out / 'source_suite')]),
        ('quantum_geometry', 'verify_quantum_geometry.py', ['--output-dir', str(out / 'quantum_geometry')]),
        ('numerical_controls', 'verify_numerical_controls.py', ['--source-root', str(source), '--output-dir', str(out / 'numerical_controls')]),
        ('extensions', 'verify_extensions.py', ['--output-dir', str(out / 'extensions')]),
        ('continuum', 'verify_continuum.py', ['--output-dir', str(out / 'continuum')]),
    ]
    if args.lean:
        jobs.append(('lean', 'verify_lean.py', ['--project', str(ROOT / 'formal'), '--output', str(out / 'lean')]))
    rows = []
    for name, filename, arguments in jobs:
        script = ROOT / 'scripts' / filename
        log = out / (name + '.log')
        with log.open('w') as handle:
            try:
                result = subprocess.run([sys.executable, str(script), *arguments], cwd=ROOT,
                                        stdout=handle, stderr=subprocess.STDOUT, timeout=900, check=False)
                code = result.returncode
            except subprocess.TimeoutExpired:
                code = 124
        rows.append({'task': name, 'script': 'scripts/' + filename,
                     'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
                     'exit_code': code, 'log': log.name,
                     'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest()})
        print(f'{name}: {"PASS" if code == 0 else "FAIL"}', flush=True)
        if code:
            print(log.read_text()[-5000:])
            break
    passed = len(rows) == len(jobs) and all(row['exit_code'] == 0 for row in rows)
    receipt = {'schema': 'voss.reproduction.v1', 'status': 'PASS' if passed else 'FAIL',
               'executed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'python': platform.python_version(), 'lean_requested': args.lean, 'runs': rows,
               'scope': 'Exact checks and bounded synthetic numerical controls; see individual assumptions and receipts.'}
    (out / 'reproduction_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
