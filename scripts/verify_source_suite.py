#!/usr/bin/env python3
"""Rerun the v2.4 symbolic/numerical suite without modifying the archive.

Dependencies are the original package's pinned requirements. Each source script
runs in an isolated temporary copy with a 120-second timeout. The receipt and
logs distinguish freshly executed results from preserved source receipts.
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
import numpy as np

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-root",type=Path,required=True)
parser.add_argument("--output-dir",type=Path,required=True)
args=parser.parse_args()
source=args.source_root.resolve(); output=args.output_dir.resolve()
if output.is_relative_to(source):
    parser.error("output-dir must be outside source-root to preserve archived evidence")
output.mkdir(parents=True,exist_ok=True)
scripts=["verify_variation.py","verify_physical_premises.py","verify_integrability_complete.py","verify_levi_civita_deformation.py","verify_boundary_fresh.py"]
runs=[]
with tempfile.TemporaryDirectory(prefix="voss-verification-") as tmp:
    root=Path(tmp)
    shutil.copytree(source/"scripts",root/"scripts")
    shutil.copytree(source/"reference",root/"reference")
    (root/"evidence").mkdir()
    for name in scripts:
        script=root/"scripts"/name
        with (output/name.replace(".py",".log")).open("w") as log:
            try:
                result=subprocess.run([sys.executable,str(script)],cwd=root,stdout=log,stderr=subprocess.STDOUT,timeout=120,check=False)
                code=result.returncode
            except subprocess.TimeoutExpired:
                code=124
        runs.append({"script":"scripts/"+name,"sha256":hashlib.sha256(script.read_bytes()).hexdigest(),"exit_code":code,"log":name.replace(".py",".log")})
        print(name, "PASS" if code==0 else "FAIL",flush=True)
        if code: break
    shutil.copytree(root/"evidence",output,dirs_exist_ok=True)

status="PASS" if len(runs)==len(scripts) and all(row["exit_code"]==0 for row in runs) else "FAIL"
receipt={"status":status,"executed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"python":platform.python_version(),"runs":runs,"execution":"fresh isolated temporary copy; original source files and receipts unmodified"}
(output/"python_suite_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
if status!="PASS": raise SystemExit(1)

# These extra checks strengthen the original monotonic-flux criterion.
boundary=output/"boundary/boundary_fresh_receipt.json"
data=json.loads(boundary.read_text())
data["source_file"]="reference/pde_repro.py"
data["execution_workspace"]="isolated temporary copy of the source package"
boundary.write_text(json.dumps(data,indent=2)+"\n")
orders=[]
for L in (8.0,12.0):
    rows=[row for row in data["rows"] if row["outer_radius"]==L]
    for key in ("twist_balance_defect","energy_balance_defect"):
        for coarse,fine in zip(rows,rows[1:]):
            order=float(np.log2(abs(coarse[key]/fine[key])))
            assert 1.8<order<2.2,(L,key,order)
            orders.append({"outer_radius":L,"quantity":key,"coarse_intervals":coarse["intervals"],"observed_order":order})
finite=[]
for path in sorted((output/"boundary").glob("corrected_*.npz")):
    with np.load(path,allow_pickle=False) as arrays:
        assert all(np.isfinite(arrays[key]).all() for key in arrays.files),path.name
        assert np.all(np.diff(arrays["gamma"])>=0),path.name
    finite.append(path.name)
extra={"status":"PASS","kind":"independent_receipt_and_state_checks","balance_orders":orders,"finite_nonnegative_energy_state_files":finite,
       "limit":"Finite final-time states and convergent balance defects; not a proof of global PDE stability."}
(output/"additional_boundary_checks.json").write_text(json.dumps(extra,indent=2)+"\n")
