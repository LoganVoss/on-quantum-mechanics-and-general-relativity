"""Bounded reciprocal moving-parcel control in the fixed-mode Brown Hamiltonian.
Flat prescribed background; one retained chi mode, lambda=1; Gaussian probes.
No geometric-cutoff or nonlinear Einstein-continuum claim.
"""
from pathlib import Path
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
import json,hashlib
c,p,X,Px,Py,u,v,b=s.symbols('c p X Px Py u v b',real=True)
chi=c*s.sin(X)
E=((chi-u)**2+(1-v)**2)/(4*v)
ud=b*(v*v-1-(u-chi)**2);vd=2*b*v*(chi-u)
assert s.simplify(s.diff(E,u)*ud+s.diff(E,v)*vd)==0
# Internal energy has no explicit Y dependence; all species carry positive rest1.
# Htot=(c²+p²)/2 + integral sqrt(Px²+Py²+(1+E)²).
T=.55;times=np.linspace(0,T,31)
def run(kind,m,rtol=3e-12):
 if kind=='midpoint':
  aa=(np.arange(m)+.5)/m;ww=np.full(m,1/m)
 else:
  aa,ww=leggauss(m);aa=(aa+1)/2;ww=ww/2
 a,d=np.meshgrid(aa,aa,indexing='ij');weights=(ww[:,None]*ww[None,:]).ravel()
 xx=(2*np.pi*a).ravel();yy=(2*np.pi*d).ravel();n=len(xx)
 pp=.3+.08*np.cos(xx)*np.cos(yy);py=.06*np.sin(yy)
 uu=.2*np.sin(xx)+.1*np.cos(yy);vv=1.25+.1*np.cos(xx)*np.sin(yy)
 initial=np.r_[.15,.04,xx,yy,pp,py,uu,vv]
 def parts(z):return (z[0],z[1],*z[2:].reshape(6,n))
 def rhs(t,z):
  cc,pc,x,y,px,py,u,v=parts(z);chi=cc*np.sin(x)
  en=((chi-u)**2+(1-v)**2)/(4*v);eps=1+en
  energy=np.sqrt(px*px+py*py+eps*eps);clock=eps/energy
  Ec=(chi-u)/(2*v)
  return np.r_[pc,-cc-np.dot(weights,clock*Ec*np.sin(x)),px/energy,py/energy,
   -clock*Ec*cc*np.cos(x),np.zeros(n),clock*(v*v-1-(u-chi)**2),2*clock*v*(chi-u)]
 def energy(z):
  cc,pc,x,y,px,py,u,v=parts(z);en=((cc*np.sin(x)-u)**2+(1-v)**2)/(4*v)
  return .5*(cc*cc+pc*pc)+np.dot(weights,np.sqrt(px*px+py*py+(1+en)**2))
 sol=solve_ivp(rhs,(0,T),initial,t_eval=times,rtol=rtol,atol=rtol/100,method='DOP853')
 assert sol.success and np.isfinite(sol.y).all()
 final=parts(sol.y[:,-1]);emin=float(min(np.min(z[2:].reshape(6,n)[5])for z in sol.y.T))
 assert emin>0
 drift=max(abs(energy(z)-energy(initial))for z in sol.y.T);assert drift<1e-10,drift
 cc,pc,x,y,px,py,u,v=final
 observables=np.r_[cc,pc,np.dot(weights,np.sin(x)),np.dot(weights,np.cos(x)),np.dot(weights,px),np.dot(weights,u),np.dot(weights,v)]
 return observables,{'energy_drift':float(drift),'minimum_probe_height':emin,'mean_x_displacement':float(np.dot(weights,x-xx)),
   'mean_y_displacement':float(np.dot(weights,y-yy))},sol.y[:2]
ref24,refmeta,_=run('gauss',24);ref32,_,_=run('gauss',32)
refgap=float(np.max(abs(ref24-ref32)));assert refgap<2e-10,refgap
ref_tight,_,_=run('gauss',32,rtol=3e-13)
timegap=float(np.max(abs(ref_tight-ref32)));assert timegap<2e-10,timegap
rows=[]
for m in (4,8,12,16):
 result,meta,trajectory=run('midpoint',m)
 err=float(np.max(abs(result-ref32)))
 rows.append({'material_grid_per_direction':m,'parcel_count':m*m,'observable_max_error':err,**meta})
assert rows[-1]['observable_max_error']<1e-8
assert abs(rows[-1]['mean_x_displacement'])>.05
report={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'model':'H=(pc²+c²)/2 + integral sqrt(px²+py²+[1+E(c sinX,1;u,v)]²) over two-dimensional material labels; properclock multiplies Gaussian Schrodinger flow.',
 'geometry':'one retained chi mode on flat prescribed 2+1 background; lambda held1 in this Galerkin subspace',
 'time':[0,T],'initial_shape':[.15,.04],'Gauss_reference_difference':refgap,'tolerance_refinement_difference':timegap,'rows':rows,
 'limits':['This is a reciprocal fixed-mode material-quadrature control, not a fullquantum many-body evolution or nonlinear geometric UV proof.','Periodic smooth data may converge faster than the general second-order bound; no universal order inferred from these samples.']}
Path(__file__).with_name('moving_parcels_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
