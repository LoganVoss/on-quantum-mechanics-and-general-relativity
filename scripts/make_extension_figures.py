#!/usr/bin/env python3
"""Render frozen extension formulas and recorded regulator responses.

No unitary evolution, numerical integration, optimization, or new model solving
is performed here. Install requirements-figures.txt and run from the repo root:
    python scripts/make_extension_figures.py
"""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker
import numpy as np

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
parser.add_argument("--output-dir",type=Path)
args=parser.parse_args()
root=args.root.resolve()
out=args.output_dir.resolve() if args.output_dir else root/"figures"
out.mkdir(parents=True,exist_ok=True)
source=root/"evidence/extensions/dynamics/dynamical_extension_receipt.json"
data=json.loads(source.read_text())
assert data["status"]=="PASS"
runs={row["Hilbert_dimension"]:row for row in data["full_quantum_regulator_controls"]}
assert set(runs)=={512,768}
for row in runs.values():
    assert row["shape_grid"]==[4,8]
    assert row["shape_radius"]==1.2
    assert len(row["times"])==len(row["shape_response_plus"])==len(row["shape_response_minus"])==len(row["uncoupled_shape_response"])==8
    assert row["times"][-1]==0.35
    assert all(np.isfinite(row[key]).all() for key in ("times","shape_response_plus","shape_response_minus","uncoupled_shape_response"))

navy="#132B43"; teal="#00887E"; muted="#607487"; grid="#DFE6EC"
plt.rcParams.update({
    "font.family":"DejaVu Sans","font.size":10,"axes.titlesize":12,
    "axes.titleweight":"semibold","axes.labelsize":10,"axes.labelcolor":navy,
    "text.color":navy,"xtick.color":muted,"ytick.color":muted,
    "axes.edgecolor":"#B2C0CC","axes.spines.top":False,"axes.spines.right":False,
    "axes.linewidth":0.8,"xtick.major.size":4,"ytick.major.size":4,
    "legend.fontsize":9,"legend.frameon":False,"savefig.facecolor":"white",
    "figure.facecolor":"white","mathtext.fontset":"dejavusans",
    "pdf.fonttype":42,"ps.fonttype":42,
})
fig,(left,right)=plt.subplots(1,2,figsize=(11.6,4.9))
fig.subplots_adjust(left=.075,right=.975,top=.85,bottom=.27,wspace=.34)
left.set_title("A  Energy and source from overlap",loc="left",pad=17)
right.set_title("B  Opposite quantum shape responses",loc="left",pad=17)

# Frozen identities in the centered pure Gaussian domain. Delta=hbar*omega.
fidelity=np.linspace(.4,1,701)
energy=fidelity**-2-1
source_norm=np.sqrt(energy*(energy+1))
left.plot(fidelity,energy,color=navy,lw=2.2,label=r"$e=E/\Delta=\mathcal{F}^{-2}-1$")
left.plot(fidelity,source_norm,color=teal,lw=2.2,label=r"$s=\|\nabla_M E\|_G/\Delta=\sqrt{e(e+1)}$")
left.scatter([4/5],[9/16],s=48,edgecolors=navy,facecolors="white",lw=1.8,zorder=4)
left.scatter([4/5],[15/16],s=48,edgecolors=teal,facecolors="white",lw=1.8,zorder=4)
left.plot([4/5,4/5],[0,15/16],color=muted,lw=.9,ls=":",zorder=1)
left.annotate(r"$\mathcal{F}=4/5$"+"\n"+r"$e=9/16,\quad s=15/16$",xy=(4/5,15/16),xytext=(.64,2.05),
              fontsize=10,ha="left",va="center",color=navy,
              arrowprops={"arrowstyle":"-","color":muted,"lw":.9},
              bbox={"facecolor":"white","edgecolor":"none","alpha":.92,"pad":2})
left.set(xlim=(.39,1.015),ylim=(-.08,6.15),
         xlabel=r"Squared fidelity, $\mathcal{F}$ (dimensionless)",
         ylabel=r"Energy or source / calibrated gap (dimensionless)")
left.xaxis.set_major_locator(ticker.MultipleLocator(.1))
left.yaxis.set_major_locator(ticker.MultipleLocator(1))
left.grid(color=grid,lw=.6);left.set_axisbelow(True)
left.legend(loc="upper right",handlelength=2.1,borderaxespad=.7)

# Plot only primitive arrays from the frozen receipt, with straight joins.
for dim,row in sorted(runs.items(),reverse=True):
    t=np.array(row["times"])
    for key,color in (("shape_response_plus",teal),("shape_response_minus",navy)):
        values=np.array(row[key])
        if dim==768:
            right.plot(t,values,color=color,lw=2.0,zorder=2)
        else:
            right.scatter(t,values,s=28,edgecolors=color,facecolors="white",lw=1.4,zorder=3)
    right.plot(t,row["uncoupled_shape_response"],color=muted,lw=1.2,ls="--",alpha=.8,zorder=1)
right.set(xlim=(-.008,.36),ylim=(-.033,.033),xlabel=r"Time, $t$ (model units)",
          ylabel=r"Shape response, $\langle X_1\rangle$ (dimensionless)")
right.xaxis.set_major_locator(ticker.MultipleLocator(.05))
right.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
right.yaxis.set_major_locator(ticker.MultipleLocator(.01))
right.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
right.grid(color=grid,lw=.6);right.set_axisbelow(True)
right.legend(handles=[Line2D([0],[0],color=teal,lw=2,label="Positive preparation"),
                      Line2D([0],[0],color=navy,lw=2,label="Negative preparation"),
                      Line2D([0],[0],color=muted,lw=1.2,ls="--",label="Uncoupled control")],
             loc="upper left",handlelength=2.0,borderaxespad=.7)
right.text(.98,.50,r"$t=0.35:$"+"\n"+r"$\langle X_1\rangle\simeq\pm0.02621937$",
           transform=right.transAxes,ha="right",va="center",fontsize=9,
           bbox={"facecolor":"white","edgecolor":"none","alpha":.9,"pad":2})

fig.text(.075,.12,r"Centered pure Gaussian probe; $\Delta=\hbar\omega$ is calibrated.",fontsize=9,color=muted)
fig.text(.075,.078,"Exact model identities; no measured data.",fontsize=9,color=muted)
fig.text(.59,.12,"Lines: dimension 768. Circles: dimension 512.",fontsize=9,color=muted)
fig.text(.59,.078,"Fixed 4-by-8 shape grid; Fock-cutoff check only.",fontsize=9,color=muted)
fig.text(.59,.036,"Responses overlap at this scale; no shape-continuum claim.",fontsize=9,color=muted)
png=out/"extensions.png";pdf=out/"extensions.pdf"
fig.savefig(png,dpi=300)
fig.savefig(pdf,metadata={"Title":"Calibrated energy-shape identities and finite quantum response",
                         "Author":"Logan Voss","Subject":"Frozen analytic identities and finite-regulator quantum response",
                         "Creator":"scripts/make_extension_figures.py (Matplotlib)","CreationDate":None,"ModDate":None})
plt.close(fig)
receipt={
    "status":"PASS","python":platform.python_version(),"matplotlib":matplotlib.__version__,"numpy":np.__version__,
    "plot_script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "input":str(source.relative_to(root)),"input_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
    "outputs":{path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in (png,pdf)},
    "dimensions_inches":[11.6,4.9],"png_dpi":300,
    "panel_A":{"domain":"centered pure uncertainty-saturating Gaussian probe, calibrated gap Delta=hbar*omega",
               "fidelity_plot_interval":[.4,1],"energy_formula":"e=E/Delta=F^(-2)-1","source_formula":"s=norm(grad_M E)_G/Delta=sqrt(e(e+1))",
               "exact_point":{"squared_fidelity":"4/5","normalized_energy":"9/16","normalized_source":"15/16"}},
    "panel_B":{"Hilbert_dimensions":[512,768],"shape_grid":[4,8],"shape_radius":1.2,
               "primitive_series":[{key:row[key] for key in ("Hilbert_dimension","oscillator_cutoff","times","shape_response_plus","shape_response_minus","uncoupled_shape_response")} for row in runs.values()],
               "interpolation":"straight line joins between recorded samples; no resimulation",
               "cutoff_response_difference_from_receipt":data["Fock_cutoff_response_difference"]},
    "note":"Only frozen formulas and primitive receipt data are rendered. No new evolution or solving. Synthetic finite-regulator results are not measurements or shape-grid continuum evidence."
}
(out/"extensions_figure_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","outputs":[str(png),str(pdf)]},indent=2))
