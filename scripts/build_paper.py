#!/usr/bin/env python3
"""Build the paper using Tectonic, rejecting final-pass layout warnings.

Install Tectonic separately. Its first run may fetch TeX resources.
This does not replace visual review of the resulting PDF.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=root / 'work/paper')
parser.add_argument('--source', type=Path, default=root / 'paper/On_Quantum_Mechanics_and_General_Relativity.tex')
args = parser.parse_args()
out = args.output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
source = args.source.resolve()
result = subprocess.run(['tectonic', '--keep-logs', '--outdir', str(out), str(source)],
                        cwd=source.parent, capture_output=True, text=True, timeout=900)
(out / 'compiler.log').write_text(result.stdout + result.stderr)
if result.returncode:
    print(result.stdout + result.stderr)
    raise SystemExit(result.returncode)
log = out / (source.stem + '.log')
issues = re.findall(r'Warning:|Overfull|Underfull|Missing character', log.read_text())
pdf = out / (source.stem + '.pdf')
receipt = {'status': 'PASS' if not issues else 'FAIL', 'final_pass_issue_count': len(issues),
           'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
           'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
           'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest(),
           'visual_review': 'Required separately; this command checks compilation and log only.'}
(out / 'build_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
raise SystemExit(0 if not issues else 1)
