#!/usr/bin/env python3
"""Run the five delivered verification programs and retain fresh logs."""
from pathlib import Path
import datetime
import hashlib
import json
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
OUT.mkdir(exist_ok=True)
SCRIPTS = [
    "verify_variation.py",
    "verify_physical_premises.py",
    "verify_integrability_complete.py",
    "verify_levi_civita_deformation.py",
    "verify_boundary_fresh.py",
]


def main():
    results = []
    for name in SCRIPTS:
        path = ROOT / "scripts" / name
        log = OUT / name.replace(".py", ".log")
        with log.open("w") as stream:
            result = subprocess.run(
                [sys.executable, str(path)],
                cwd=ROOT,
                stdout=stream,
                stderr=subprocess.STDOUT,
                check=False,
            )
        row = {
            "script": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "exit_code": result.returncode,
            "log": str(log.relative_to(ROOT)),
        }
        results.append(row)
        print(f"{name}: {'PASS' if result.returncode == 0 else 'FAIL'}", flush=True)
        if result.returncode:
            print(log.read_text()[-6000:])
            break
    receipt = {
        "status": "PASS" if len(results) == len(SCRIPTS) and all(r["exit_code"] == 0 for r in results) else "FAIL",
        "executed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python": platform.python_version(),
        "runs": results,
    }
    (OUT / "python_suite_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
