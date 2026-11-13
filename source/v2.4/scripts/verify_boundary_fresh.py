#!/usr/bin/env python3
"""Fresh same-coefficient nonlinear runs and charge boundary-flux accounting."""
from pathlib import Path
import json,csv,hashlib,platform
import numpy as np
import scipy
from scipy.integrate import quad,trapezoid
BASE=Path(__file__).resolve().parent
SRC=BASE.parent/'reference/pde_repro.py'
OUT=BASE.parent/'evidence/boundary'; OUT.mkdir(exist_ok=True,parents=True)
text=SRC.read_text();ns={};exec(compile(text.split('res = {}')[0],str(SRC),'exec'),ns)
original=ns['data']

def integrands(r):
 p,c,pt,ct=original(np.array(r));w=r*np.exp(-2*p)
 return float(w*ct),float(w*np.exp(-(r/1.2)**2))
num,nerr=quad(lambda r:integrands(r)[0],0,np.inf,epsabs=1e-13,epsrel=1e-12)
den,derr=quad(lambda r:integrands(r)[1],0,np.inf,epsabs=1e-13,epsrel=1e-12)
coeff=-num/den
corr,qerr=quad(lambda r:integrands(r)[0]+coeff*integrands(r)[1],0,np.inf,epsabs=1e-13,epsrel=1e-12)
def data(R):
 p,c,pt,ct=original(R);return p,c,pt,ct+coeff*np.exp(-(R/1.2)**2)
ns['data']=data

def charge(y,R):return float(trapezoid(R*np.exp(-2*y[0])*y[3],R))
def boundary_flux(y,R,dR):
 p,c,pt,ct=y
 pr=(3*p[-1]-4*p[-2]+p[-3])/(2*dR)
 cr=(3*c[-1]-4*c[-2]+c[-3])/(2*dR)
 return np.array([R[-1]*np.exp(-2*p[-1])*cr,
  R[-1]*(pt[-1]*pr+np.exp(-2*p[-1])*ct[-1]*cr)])
def charge_rate(y,dy,R):
 return float(trapezoid(R*np.exp(-2*y[0])*(dy[3]-2*dy[0]*y[3]),R))

def run_monitored(N,L=8.,Tend=.8):
 R=np.linspace(0,L,N+1);dr=R[1]-R[0];dt=.16*dr
 ini=np.asarray(data(R));y=ini.copy();g0=ns['energy_gamma'](y,R,dr)
 steps=int(round(Tend/dt));dt=Tend/steps
 fluxint=np.zeros(2);rateint=0.;maxflux=np.zeros(2)
 for step in range(steps):
  k1=ns['rhs'](y,R,dr);y2=y+.5*dt*k1
  k2=ns['rhs'](y2,R,dr);y3=y+.5*dt*k2
  k3=ns['rhs'](y3,R,dr);y4=y+dt*k3
  k4=ns['rhs'](y4,R,dr)
  fs=np.array([boundary_flux(v,R,dr) for v in [y,y2,y3,y4]])
  rs=np.array([charge_rate(v,k,R) for v,k in zip([y,y2,y3,y4],[k1,k2,k3,k4])])
  fluxint+=dt/6*(fs[0]+2*fs[1]+2*fs[2]+fs[3])
  rateint+=dt/6*(rs[0]+2*rs[1]+2*rs[2]+rs[3])
  maxflux=np.maximum(maxflux,np.max(np.abs(fs),axis=0))
  y=y+dt/6*(k1+2*k2+2*k3+k4)
  y[0,-1],y[1,-1]=ini[0,-1],ini[1,-1]
 g1=ns['energy_gamma'](y,R,dr)
 q0,q1=charge(ini,R),charge(y,R)
 tail0,tailerr=quad(lambda r:integrands(r)[0]+coeff*integrands(r)[1],L,np.inf,epsabs=1e-16,epsrel=1e-11)
 row={'intervals':N,'outer_radius':L,'final_time':Tend,'dR':float(dr),'dt':float(dt),'steps':steps,
 'gamma_initial':float(g0[-1]),'gamma_final':float(g1[-1]),
 'relative_energy_drift':float(abs(g1[-1]-g0[-1])/g0[-1]),'max_exp_gamma':float(np.exp(g1.max())),
 'initial_discrete_twist':q0,'final_discrete_twist':q1,'twist_drift':q1-q0,
 'integrated_outer_twist_flux':float(fluxint[0]),'twist_balance_defect':float(q1-q0-fluxint[0]),
 'integrated_outer_energy_flux':float(fluxint[1]),'energy_balance_defect':float(g1[-1]-g0[-1]-fluxint[1]),
 'max_abs_outer_twist_flux':float(maxflux[0]),'max_abs_outer_energy_flux':float(maxflux[1]),
 'integrated_semidiscrete_charge_rate':float(rateint),'time_integration_charge_identity_error':float(q1-q0-rateint),
 'initial_tail_twist_beyond_L':float(tail0),'initial_tail_quadrature_error':float(tailerr),
 'axis_flux':0.0,'outer_boundary':'frozen field values; historical solver unchanged',
 'outer_flux_derivative':'second-order one-sided derivative, not overwritten interior gradient'}
 np.savez_compressed(OUT/f'corrected_L{int(L)}_N{N}.npz',R=R,y=y,gamma=g1)
 return row,(R,y)

rows=[];states={}
for L,nsizes in [(8.,[128,256,512,1024]),(12.,[384,768,1536])]:
 for N in nsizes:
  row,state=run_monitored(N,L);rows.append(row);states[L,N]=state
  print(json.dumps(row),flush=True)
orders=[]
for L,N in [(8.,128),(8.,256),(12.,384)]:
 a=states[L,N][1];b=states[L,2*N][1][:,::2];c=states[L,4*N][1][:,::4]
 for j,name in enumerate(['psi','chi','psi_T','chi_T']):
  orders.append({'outer_radius':L,'coarse_intervals':N,'field':name,'observed_order':float(np.log2(np.linalg.norm(a[j]-b[j])/np.linalg.norm(b[j]-c[j])))})
# Historical numbers are checked at the same settings, without reading generated files as inputs.
historical=json.loads((SRC.parent/'corrected_boundary_summary_v22.json').read_text())
comparison=[]
for old,new in zip(historical['rows'],rows[:4]):
 comparison.append({'intervals':new['intervals'],'max_abs_difference':max(abs(new[k]-old[k]) for k in old if k!='intervals')})
assert max(r['max_abs_difference'] for r in comparison)<1e-12
assert abs(corr)<1e-13
assert den>0
assert all(r['relative_energy_drift']<3e-4 for r in rows)
assert all(1.8<o['observed_order']<2.2 for o in orders)
# Flux-balanced charge errors should converge at approximately second order.
for L in [8.,12.]:
 rr=[r for r in rows if r['outer_radius']==L]
 assert all(abs(y['twist_balance_defect'])<abs(x['twist_balance_defect']) for x,y in zip(rr,rr[1:]))
report={'status':'PASS','python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
 'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'source_file':str(SRC),
 'correction_formula':'chi_T += c_star exp[-(R/1.2)^2]',
 'c_star':coeff,'original_continuum_twist':num,'original_quadrature_error':nerr,
 'correction_denominator':den,'denominator_quadrature_error':derr,
 'corrected_continuum_twist':corr,'corrected_quadrature_error':qerr,
 'same_continuum_coefficient_on_all_grids':True,
 'rows':rows,'orders':orders,'historical_v22_comparison':comparison,
 'continuum_charge_identity':'d/dT integral_0^L R exp(-2 psi) chi_T dR = [R exp(-2 psi) chi_R]_0^L',
 'continuum_energy_identity':'d/dT gamma(L) = [R (psi_T psi_R + exp(-2 psi) chi_T chi_R)]_0^L',
 'notes':['Synthetic nonlinear finite-domain evolution; no empirical measurements.',
 'Finite-grid charge drift is measured, not labeled exact conservation.',
 'L=8 outer twist flux is nonzero; it is explicitly integrated and separated from spatial error.',
 'L=12 uses the same spacings as matching L=8 runs to test the outer-tail effect.']}
(OUT/'boundary_fresh_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
with (OUT/'boundary_fresh_convergence.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(json.dumps({'status':report['status'],'c_star':coeff,'original_twist':num,'corrected_twist':corr,'orders':orders,'historical_comparison':comparison},indent=2))
