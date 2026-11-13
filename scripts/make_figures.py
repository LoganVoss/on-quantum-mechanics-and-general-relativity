#!/usr/bin/env python3
"""Render the research figure from recorded verification data, without rerunning science.

Run from the repository root after installing requirements-figures.txt:
    python scripts/make_figures.py

The optional --root and --output-dir arguments select another evidence bundle
and output location. Outputs are a 300-dpi PNG, a vector PDF, plotted data, and
a receipt with input/output hashes. No measurements or fitted results are added.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import math
import platform
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
parser.add_argument("--output-dir",type=Path)
args=parser.parse_args()
root=args.root.resolve()
out=args.output_dir.resolve() if args.output_dir else root/"figures"
out.mkdir(parents=True,exist_ok=True)
quantum_path=root/"evidence/quantum_geometry/quantum_geometry_receipt.json"
errors_path=root/"evidence/numerical_controls/exact_solution_errors.csv"
control_path=root/"evidence/numerical_controls/independent_controls_receipt.json"
quantum=json.loads(quantum_path.read_text())
controls=json.loads(control_path.read_text())
assert quantum["status"]=="pass" and controls["status"]=="PASS"
assert len(quantum["quadrature_checks"])==5
assert controls["domain"]["outer_radius"]==8 and controls["domain"]["final_time"]==0.8 and controls["domain"]["amplitude"]==1.6
max_recorded_discrepancy=max(row["absolute_error"] for row in quantum["quadrature_checks"])
discrepancy_mantissa,discrepancy_exponent=f"{max_recorded_discrepancy:.2e}".split("e")
points=[]
for row in quantum["quadrature_checks"]:
    u,v=row["first"]; up,vp=row["second"]
    distance=math.acosh(1+((u-up)**2+(v-vp)**2)/(2*v*vp))
    measured=row["squared_fidelity_quadrature"]
    prediction=1/math.cosh(distance/2)
    assert abs(prediction-row["sech_distance_prediction"])<1e-14
    points.append({"distance":distance,"quadrature_squared_fidelity":measured,
                   "theory_squared_fidelity":prediction,"absolute_difference":abs(measured-prediction)})
with errors_path.open(newline="") as stream:
    errors=[row for row in csv.DictReader(stream) if row["case"]=="nonlinear_geodesic"]
errors.sort(key=lambda row:int(row["intervals"]))
N=np.array([int(row["intervals"]) for row in errors])
E=np.array([float(row["all_field_linf"]) for row in errors])
assert list(N)==[64,128,256,512] and np.all(E>0)
last_order=float(errors[-1]["observed_order"])
navy="#132B43"; teal="#00887E"; muted="#607487"; grid="#DFE6EC"
plt.rcParams.update({
    "font.family":"DejaVu Sans","font.size":10,"axes.titlesize":12,
    "axes.titleweight":"semibold","axes.labelsize":10,"axes.labelcolor":navy,
    "text.color":navy,"xtick.color":muted,"ytick.color":muted,
    "axes.edgecolor":"#B2C0CC","axes.spines.top":False,"axes.spines.right":False,
    "axes.linewidth":0.8,"xtick.major.size":4,"ytick.major.size":4,
    "legend.fontsize":9,"legend.frameon":False,"savefig.facecolor":"white",
    "figure.facecolor":"white","mathtext.fontset":"dejavusans",
    "pdf.fonttype":42,"ps.fonttype":42,"svg.hashsalt":"voss-verification-v1",
})
fig,(left,right)=plt.subplots(1,2,figsize=(11.2,4.6))
fig.subplots_adjust(left=0.075,right=0.975,top=0.85,bottom=0.25,wspace=0.32)
left.set_title("A  Gaussian fidelity",loc="left",pad=17)
right.set_title("B  Nonlinear solver convergence",loc="left",pad=17)
d=np.linspace(0,5,801)
left.plot(d,1/np.cosh(d/2),color=navy,lw=2.2,label=r"Exact $\mathcal{F}=\mathrm{sech}(d/2)$")
left.scatter([p["distance"] for p in points],[p["quadrature_squared_fidelity"] for p in points],
             s=54,facecolors="white",edgecolors=teal,linewidths=1.8,zorder=3,label="Wavefunction quadrature")
left.set(xlim=(-0.10,5.05),ylim=(0,1.07),
         xlabel=r"Intrinsic hyperbolic distance, $d$ (dimensionless)",
         ylabel=r"Squared fidelity, $\mathcal{F}$ (dimensionless)")
left.xaxis.set_major_locator(ticker.MultipleLocator(1))
left.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
left.grid(color=grid,linewidth=.6)
left.set_axisbelow(True)
left.legend(loc="lower left",handlelength=2.6,borderaxespad=.7)
left.text(.98,.95,"Centered pure Gaussian states",ha="right",va="top",
          transform=left.transAxes,color=muted,fontsize=9)

right.loglog(N,E,"o-",color=teal,lw=2.2,markersize=6,markerfacecolor="white",
             markeredgewidth=1.8,label="Maximum error over four fields")
# A scale guide is offset for legibility; it is not fitted to the results.
refN=np.geomspace(64,512,200)
right.loglog(refN,0.38*E[0]*(refN/N[0])**-2,"--",color=navy,lw=1.5,
             label=r"$N^{-2}$ reference (offset)")
right.set(xlim=(52,630),ylim=(1e-7,6e-5),
          xlabel=r"Radial intervals, $N$",ylabel=r"Maximum absolute error (model units)")
right.set_xticks(N)
right.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
right.get_xaxis().set_minor_locator(ticker.NullLocator())
right.yaxis.set_major_locator(ticker.LogLocator(base=10))
right.yaxis.set_minor_locator(ticker.LogLocator(base=10,subs=(2,5)))
right.yaxis.set_minor_formatter(ticker.NullFormatter())
right.grid(which="major",color=grid,linewidth=.6)
right.grid(which="minor",axis="y",color=grid,linewidth=.4,alpha=.5)
right.set_axisbelow(True)
right.legend(loc="upper right",handlelength=2.4,borderaxespad=.65)
right.text(.06,.10,f"Finest-grid order: {last_order:.4f}\n"+r"$T=0.8,\ L=8,\ A=1.6$",
           transform=right.transAxes,ha="left",va="bottom",fontsize=9,color=navy,
           bbox={"facecolor":"white","edgecolor":"none","alpha":.9,"pad":3})

fig.text(.075,.091,"Five quadratures; two overlap near zero distance.",fontsize=9,color=muted)
fig.text(.075,.051,rf"Largest recorded discrepancy: ${discrepancy_mantissa}\times10^{{{int(discrepancy_exponent)}}}$.",fontsize=9,color=muted)
fig.text(.587,.091,r"Exact control: $\psi=-\log\cosh f,\ \chi=\tanh f$.",fontsize=9,color=muted)
fig.text(.587,.051,r"$f=1.6\,J_0(kR)\cos(kT)$ with $J_0(8k)=0$.",fontsize=9,color=muted)
png=out/"verification.png"; pdf=out/"verification.pdf"
fig.savefig(png,dpi=300)
fig.savefig(pdf,metadata={"Title":"Quantum geometry and nonlinear solver verification",
                         "Author":"Logan Voss","Subject":"Exact Gaussian fidelity and finite-time analytic-oracle convergence",
                         "Creator":"scripts/make_figures.py (Matplotlib)","CreationDate":None,"ModDate":None})
plt.close(fig)

with (out/"fidelity_points.csv").open("w",newline="") as stream:
    writer=csv.DictWriter(stream,fieldnames=points[0]); writer.writeheader();writer.writerows(points)
receipt={
    "status":"PASS","python":platform.python_version(),"matplotlib":matplotlib.__version__,
    "numpy":np.__version__,"plot_script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "inputs":{str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest() for path in (quantum_path,errors_path,control_path)},
    "outputs":{path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in (png,pdf,out/"fidelity_points.csv")},
    "dimensions_inches":[11.2,4.6],"png_dpi":300,"quadrature_points":len(points),"nonlinear_grids":N.tolist(),
    "note":"Theory curve and recorded synthetic checks; no experimental data. Reference slope is explicitly offset, not fitted."
}
(out/"figure_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","outputs":[str(path) for path in (png,pdf)]},indent=2))
