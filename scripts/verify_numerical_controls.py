#!/usr/bin/env python3
"""Bounded exact-solution and time-refinement controls for the supplied solver.

The nonlinear analytic oracle is independently derived from a hyperbolic-target
geodesic: psi=-log cosh(f), chi=tanh(f), with f a radial linear wave.
This checks an exactly solvable subfamily, not arbitrary nonlinear stability.
"""
from pathlib import Path
import argparse
import csv
import datetime
import hashlib
import json
import platform
import time
import numpy as np
import scipy
import sympy as s
from scipy.special import j0, jn_zeros
from scipy.integrate import quad

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-root", type=Path, required=True,
                    help="Path to the original v2.4 package, containing reference/pde_repro.py")
parser.add_argument("--output-dir", type=Path, required=True)
args = parser.parse_args()
SOURCE = args.source_root.resolve() / "reference/pde_repro.py"
OUT = args.output_dir.resolve()
if OUT.is_relative_to(args.source_root.resolve()):
    parser.error("output-dir must be outside source-root to preserve archived evidence")
OUT.mkdir(exist_ok=True, parents=True)
raw = SOURCE.read_bytes()
ns = {}
exec(compile(raw.decode().split("res = {}")[0], str(SOURCE), "exec"), ns)

# Exact symbolic geodesic identities reduce the full nonlinear system to Box f=0.
z=s.symbols("z", real=True)
P=-s.log(s.cosh(z)); C=s.tanh(z)
identities={
    "psi_geodesic": s.simplify(s.diff(P,z,2)+s.exp(-2*P)*s.diff(C,z)**2),
    "chi_geodesic": s.simplify(s.diff(C,z,2)-2*s.diff(P,z)*s.diff(C,z)),
    "energy_isometry": s.simplify(s.diff(P,z)**2+s.exp(-2*P)*s.diff(C,z)**2-1),
}
assert all(v==0 for v in identities.values()), identities

L=8.0; T=0.8; AMPLITUDE=1.6
K=float(jn_zeros(0,1)[0]/L)

def exact_state(R,t,nonlinear):
    f=AMPLITUDE*j0(K*R)*np.cos(K*t)
    ft=-AMPLITUDE*K*j0(K*R)*np.sin(K*t)
    if nonlinear:
        return np.array([-np.log(np.cosh(f)),np.tanh(f),-np.tanh(f)*ft,ft/np.cosh(f)**2])
    return np.array([f,np.zeros_like(f),ft,np.zeros_like(f)])

def evolve(initial,N,cfl):
    R=np.linspace(0,L,N+1); dr=L/N
    steps=int(np.ceil(T/(cfl*dr))); dt=T/steps
    y=np.asarray(initial(R)).copy(); frozen=y[:2,-1].copy()
    for _ in range(steps):
        k1=ns["rhs"](y,R,dr)
        k2=ns["rhs"](y+dt*k1/2,R,dr)
        k3=ns["rhs"](y+dt*k2/2,R,dr)
        k4=ns["rhs"](y+dt*k3,R,dr)
        y += dt*(k1+2*k2+2*k3+k4)/6
        y[:2,-1]=frozen
    assert np.isfinite(y).all()
    return R,y,{"intervals":N,"dR":dr,"dt":dt,"steps":steps,"requested_cfl":cfl}

started=time.monotonic(); exact_rows=[]
for nonlinear in (False,True):
    case="nonlinear_geodesic" if nonlinear else "linear_bessel"
    last_error=None
    for N in (64,128,256,512):
        R,y,row=evolve(lambda r:exact_state(r,0,nonlinear),N,0.16)
        exact=exact_state(R,T,nonlinear)
        err=np.max(np.abs(y-exact),axis=1)
        row.update(case=case,field_linf_errors=err.tolist(),all_field_linf=float(err.max()))
        if last_error is not None:
            row["observed_order"]=float(np.log2(last_error/err.max()))
            assert 1.8<row["observed_order"]<2.2,row
        last_error=err.max()
        exact_rows.append(row)
        np.savez_compressed(OUT/f"{case}_N{N}.npz",R=R,numerical=y,exact=exact)

# Independent recomputation of the continuum correction, then fixed-grid RK4 test.
def integrand(r):
    p,c,pt,ct=ns["data"](np.array(r)); w=r*np.exp(-2*p)
    return float(w*ct),float(w*np.exp(-(r/1.2)**2))
numerator=quad(lambda r:integrand(r)[0],0,np.inf,epsabs=1e-13,epsrel=1e-12)[0]
denominator=quad(lambda r:integrand(r)[1],0,np.inf,epsabs=1e-13,epsrel=1e-12)[0]
coefficient=-numerator/denominator
def corrected(R):
    p,c,pt,ct=ns["data"](R)
    return np.array([p,c,pt,ct+coefficient*np.exp(-(R/1.2)**2)])

time_rows=[]; solutions=[]
for cfl in (0.64,0.32,0.16,0.08,0.04):
    R,y,row=evolve(corrected,128,cfl)
    solutions.append(y); time_rows.append(row)
diffs=[float(np.max(np.abs(a-b))) for a,b in zip(solutions,solutions[1:])]
coarse_time_order=float(np.log2(diffs[0]/diffs[1]))
time_order=float(np.log2(diffs[2]/diffs[3]))
assert 3.5<time_order<4.5,(diffs,time_order)
report={
    "status":"PASS","kind":"independent_analytic_oracle_and_temporal_refinement",
    "executed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,"sympy":s.__version__,
    "source_sha256":hashlib.sha256(raw).hexdigest(),
    "control_source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "domain":{"outer_radius":L,"final_time":T,"amplitude":AMPLITUDE,"bessel_wave_number":K},
    "symbolic_residuals":{k:str(v) for k,v in identities.items()},
    "exact_solution_rows":exact_rows,
    "time_refinement":{"initial_data":"corrected historical nonlinear benchmark","c_star":coefficient,"rows":time_rows,"successive_linf_differences":diffs,"observed_order":time_order,
        "accepted_steps":[0.01,0.005,0.0025],"accepted_order_interval":[3.5,4.5],
        "coarse_exploration":{"steps":[0.04,0.02,0.01],"observed_order":coarse_time_order,
            "status":"does_not_meet_expected_asymptotic_order",
            "interpretation":"Coarse timesteps do not establish fourth-order convergence; the finer regime resolves it. Coarse result retained, not discarded."}},
    "elapsed_seconds":time.monotonic()-started,
    "limits":["Finite T=0.8 bounded controls; no global or arbitrary-data stability theorem.","Exact geodesic solution is an integrable commuting-current subfamily, not generic nonlinear scattering.","Time refinement holds spatial grid fixed; spatial refinement uses a separate exact continuum oracle."]
}
(OUT/"independent_controls_receipt.json").write_text(json.dumps(report,indent=2)+"\n")
with (OUT/"exact_solution_errors.csv").open("w",newline="") as stream:
    fields=["case","intervals","dR","dt","steps","all_field_linf","observed_order","psi_linf","chi_linf","psi_T_linf","chi_T_linf"]
    writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader()
    for row in exact_rows:
        result={key:row.get(key,"") for key in fields}
        result.update(dict(zip(fields[-4:],row["field_linf_errors"])))
        writer.writerow(result)
with (OUT/"time_refinement.csv").open("w",newline="") as stream:
    fields=["intervals","dt","steps","requested_cfl","linf_difference_to_next_step"]
    writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader()
    for index,row in enumerate(time_rows):
        result={key:row.get(key,"") for key in fields}
        result["linf_difference_to_next_step"]=diffs[index] if index<len(diffs) else ""
        writer.writerow(result)
print(json.dumps(report,indent=2))
