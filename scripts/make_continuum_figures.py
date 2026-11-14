#!/usr/bin/env python3
"""Plot recorded continuum-control data without rerunning any evolution.

Install requirements-figures.txt, then run from the repository root:
    python scripts/make_continuum_figures.py

Both panels use primitive values from the published JSON receipts. The bound
is read from the source receipt, not fitted or recomputed. No extrapolation,
integration, regression, or new model solving is performed by this script.
"""
from pathlib import Path
import argparse
import hashlib
import json
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
meanfield_path=root/"evidence/continuum/meanfield/meanfield_receipt.json"
field_path=root/"evidence/continuum/field/field_continuum_receipt.json"
meanfield=json.loads(meanfield_path.read_text())
field=json.loads(field_path.read_text())
assert meanfield["status"]==field["status"]=="PASS"
population_rows=sorted(meanfield["parcel_rows"],key=lambda row:row["population"])
label_control=field["nonlinear_reciprocal_label_limit"]
label_rows=sorted(label_control["rows"],key=lambda row:row["h"])
N=np.array([row["population"] for row in population_rows])
trace_error=np.array([row["trace_norm_error"] for row in population_rows])
trace_bound=np.array([row["analytic_trace_bound"] for row in population_rows])
h=np.array([row["h"] for row in label_rows])
geometry_error=np.array([row["geometry_endpoint_error"] for row in label_rows])
assert list(N)==[1,2,4,8,16,32,64,128,256,512]
assert len(label_rows)==4 and all(row["retained_shape_modes"]==1 for row in label_rows)
assert all(np.isfinite(array).all() and np.all(array>0) for array in (N,trace_error,trace_bound,h,geometry_error))
assert np.all(trace_error<=trace_bound+2e-13)
assert meanfield["parcel_parameters"]["time"]==.8 and label_control["time"]==[1,1.5]
finest=label_rows[0]
navy="#132B43";teal="#00887E";muted="#607487";grid="#DFE6EC"
plt.rcParams.update({
    "font.family":"DejaVu Sans","font.size":10,"axes.titlesize":12,
    "axes.titleweight":"semibold","axes.labelsize":10,"axes.labelcolor":navy,
    "text.color":navy,"xtick.color":muted,"ytick.color":muted,
    "axes.edgecolor":"#B2C0CC","axes.spines.top":False,"axes.spines.right":False,
    "axes.linewidth":.8,"xtick.major.size":4,"ytick.major.size":4,
    "legend.fontsize":9,"legend.frameon":False,"savefig.facecolor":"white",
    "figure.facecolor":"white","mathtext.fontset":"dejavusans","pdf.fonttype":42,"ps.fonttype":42,
})
fig,(left,right)=plt.subplots(1,2,figsize=(11.6,4.9))
fig.subplots_adjust(left=.08,right=.975,top=.85,bottom=.27,wspace=.34)
left.set_title("A  One-probe mean-field error",loc="left",pad=17)
right.set_title("B  Reciprocal material quadrature",loc="left",pad=17)
left.loglog(N,trace_bound,"s--",color=navy,lw=1.6,markersize=4.5,
            markerfacecolor="white",markeredgewidth=1.2,label="Proved trace-norm upper bound")
left.loglog(N,trace_error,"o-",color=teal,lw=2.2,markersize=5.5,
            markerfacecolor="white",markeredgewidth=1.6,label="Recorded one-probe trace-norm error")
left.set(xlim=(.78,650),ylim=(1e-5,.45),xlabel=r"Probe population, $N$",
         ylabel="One-probe trace-norm error (dimensionless)")
left.set_xticks([1,8,64,512])
left.xaxis.set_major_formatter(ticker.ScalarFormatter())
left.xaxis.set_minor_locator(ticker.LogLocator(base=2,subs=[1]))
left.xaxis.set_minor_formatter(ticker.NullFormatter())
left.yaxis.set_major_locator(ticker.LogLocator(base=10))
left.yaxis.set_minor_locator(ticker.NullLocator())
left.legend(loc="lower left",handlelength=2.3,borderaxespad=.7)
left.text(.97,.94,r"$t=0.8$",transform=left.transAxes,ha="right",va="top",fontsize=10,color=muted)

right.loglog(h,geometry_error,"o-",color=teal,lw=2.2,markersize=6,
             markerfacecolor="white",markeredgewidth=1.7,label="Recorded geometry endpoint error")
right.set(xlim=(.025,.31),ylim=(1e-6,3.3e-4),
          xlabel=r"Material-label spacing, $h$ (dimensionless)",
          ylabel="Geometry endpoint 2-norm error (model units)")
right.set_xticks([1/32,1/16,1/8,1/4],labels=[r"$1/32$",r"$1/16$",r"$1/8$",r"$1/4$"])
right.xaxis.set_minor_locator(ticker.NullLocator())
right.yaxis.set_major_locator(ticker.LogLocator(base=10))
right.yaxis.set_minor_locator(ticker.LogLocator(base=10,subs=(2,5)))
right.yaxis.set_minor_formatter(ticker.NullFormatter())
right.legend(loc="upper left",handlelength=2.2,borderaxespad=.7)
right.text(.97,.09,f"Finest observed order: {finest['observed_order']:.4f}\n"+r"$t:1\ \to\ 1.5$",
           transform=right.transAxes,ha="right",va="bottom",fontsize=9,
           bbox={"facecolor":"white","edgecolor":"none","alpha":.92,"pad":3})
for ax in (left,right):
    ax.grid(which="major",color=grid,lw=.6)
    ax.set_axisbelow(True)
right.grid(which="minor",axis="y",color=grid,lw=.4,alpha=.5)
fig.text(.08,.12,"Solvable parcel with a fixed internal cutoff.",fontsize=9,color=muted)
fig.text(.08,.078,"The conservative bound is recorded, not fitted.",fontsize=9,color=muted)
fig.text(.595,.12,"One retained homogeneous shape mode; reciprocal probes.",fontsize=9,color=muted)
fig.text(.595,.078,"Label quadrature refinement on the prescribed background.",fontsize=9,color=muted)
fig.text(.595,.036,"No nonlinear spatial-cutoff removal is asserted.",fontsize=9,color=muted)
png=out/"continuum.png";pdf=out/"continuum.pdf"
fig.savefig(png,dpi=300)
fig.savefig(pdf,metadata={"Title":"Population and reciprocal material-continuum controls",
                         "Author":"Logan Voss","Subject":"Recorded one-probe trace error, proved bound, and fixed-mode material quadrature error",
                         "Creator":"scripts/make_continuum_figures.py (Matplotlib)","CreationDate":None,"ModDate":None})
plt.close(fig)
receipt={
    "status":"PASS","python":platform.python_version(),"matplotlib":matplotlib.__version__,"numpy":np.__version__,
    "plot_script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "inputs":{str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest() for path in (meanfield_path,field_path)},
    "outputs":{path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in (png,pdf)},
    "dimensions_inches":[11.6,4.9],"png_dpi":300,
    "panel_A":{"parameters":meanfield["parcel_parameters"],
               "primitive_series":[{key:row[key] for key in ("population","trace_norm_error","analytic_trace_bound")} for row in population_rows],
               "scope":meanfield["scope"]},
    "panel_B":{"fixed_background":label_control["fixed_background"],"time":label_control["time"],
               "reference_crosscheck_difference":label_control["gauss_reference_difference"],"primitive_series":label_rows,
               "scope":"Nonlinear reciprocal material-label quadrature with one fixed homogeneous shape mode; no nonlinear spatial Galerkin cutoff removal."},
    "rendering":"Straight joins between recorded samples; no new evolution, integration, regression, or extrapolation."
}
(out/"continuum_figure_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","outputs":[str(png),str(pdf)]},indent=2))
