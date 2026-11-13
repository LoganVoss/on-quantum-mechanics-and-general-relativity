#!/usr/bin/env python3
"""Scratch research verification: selected quantum/shape coupling.
No repository sources imported or modified. All computations bounded.
"""
from pathlib import Path
import json, hashlib, platform, math, time
import numpy as np
import scipy
import sympy as s
from scipy.integrate import solve_ivp, quad
from scipy.linalg import expm
from scipy.sparse import csr_matrix, diags, eye, kron, block_diag
from scipy.sparse.linalg import expm_multiply

OUT=Path(__file__).resolve().parent
checks=[]
def eq(name,value):
    value=s.simplify(value)
    assert value==0,(name,value)
    checks.append({'name':name,'residual':'0'})

x,u=s.symbols('x u',real=True)
y,v,omega,hbar,mu=s.symbols('y v omega hbar mu',positive=True)
xd,yd=s.symbols('xd yd',real=True)
J=s.Matrix([[0,1],[-1,0]])
def shape(x,y):return s.Matrix([[1,x],[x,x*x+y*y]])/y
M=shape(x,y);N=shape(u,v);K=omega*M.inv()
E=hbar*omega*(s.trace(M.inv()*N)-2)/4
eq('excess_energy_positive_distance_form',E-hbar*omega*((x-u)**2+(y-v)**2)/(4*y*v))
eq('calibrated_symplectic_gap',K.det()-omega**2)
eq('matched_ground_stationary_covariance',(J*K*M-M*K*J)[0,0])
eq('matched_ground_stationary_covariance_offdiag',(J*K*M-M*K*J)[0,1])
force2=y*y*(s.diff(E,x)**2+s.diff(E,y)**2)
eq('pure_force_energy_identity',force2-E*(E+hbar*omega))
du=omega*(v*v-y*y-(u-x)**2)/y
dv=2*omega*v*(x-u)/y
dN=N.diff(u)*du+N.diff(v)*dv
cov=J*K*N-N*K*J
for i in range(2):
 for j in range(2):eq(f'covariance_equation_{i}{j}',dN[i,j]-cov[i,j])
ax=2*xd*yd/y-hbar*omega*y*(x-u)/(2*mu*v)
ay=(yd*yd-xd*xd)/y+hbar*omega*(v*v+(x-u)**2-y*y)/(4*mu*v)
energy=mu*(xd*xd+yd*yd)/(2*y*y)+E
flow=[xd,yd,ax,ay,du,dv]
variables=[x,y,xd,yd,u,v]
eq('reciprocal_total_energy_conservation',sum(s.diff(energy,z)*dz for z,dz in zip(variables,flow)))
charge=mu*xd/y**2-hbar/(4*v)
eq('shear_Noether_charge',sum(s.diff(charge,z)*dz for z,dz in zip(variables,flow)))

# General centered covariance: the force inequality's exact slack is uncertainty.
n11,n12,n22=s.symbols('n11 n12 n22',real=True)
NN=s.Matrix([[n11,n12],[n12,n22]])
EE=hbar*omega*(s.trace(M.inv()*NN)-2)/4
eq('general_covariance_force_identity',y*y*(s.diff(EE,x)**2+s.diff(EE,y)**2)-EE*(EE+hbar*omega)+(hbar*omega)**2*(NN.det()-1)/4)
eq('force_x_at_isotropic_shape',(-y*y*s.diff(EE,x)).subs({x:0,y:1})-hbar*omega*n12/2)
eq('force_y_at_isotropic_shape',(-y*y*s.diff(EE,y)).subs({x:0,y:1})+hbar*omega*(n11-n22)/4)

# Arbitrary unimodular frame, using an open algebraic chart.
a,b,c=s.symbols('a b c',real=True,nonzero=True)
A=s.Matrix([[a,b],[c,(1+b*c)/a]])
Mp=A*M*A.T;Np=A*N*A.T
for i in range(2):
 for j in range(2):eq(f'equivariant_inverse_{i}{j}',Mp.inv()[i,j]-(A.inv().T*M.inv()*A.inv())[i,j])
eq('joint_frame_energy_invariance',s.trace(Mp.inv()*Np)-s.trace(M.inv()*N))

# Isotropy alone fixes a symmetric quadratic form to a scalar.
k11,k12,k22=s.symbols('k11 k12 k22',real=True)
KK=s.Matrix([[k11,k12],[k12,k22]])
rot=J.T*KK*J-KK
eq('isotropy_off_diagonal_constraint',rot[0,1]+2*k12)
eq('isotropy_diagonal_constraint',rot[0,0]-(k22-k11))

# Hyperboloid identities used for the fully quantum matched-spectrum response.
XX=[(1+x*x+y*y)/(2*y),(1-x*x-y*y)/(2*y),x/y]
eta=s.diag(1,-1,-1)
for i in range(3):
 for j in range(3):
  eq(f'hyperboloid_gradient_{i}{j}',y*y*(s.diff(XX[i],x)*s.diff(XX[j],x)+s.diff(XX[i],y)*s.diff(XX[j],y))-XX[i]*XX[j]+eta[i,j])
for i in range(3):eq(f'hyperboloid_laplacian_{i}',y*y*(s.diff(XX[i],x,2)+s.diff(XX[i],y,2))-2*XX[i])
YY=[(n11+n22)/2,(n11-n22)/2,n12]
eq('energy_hyperboloid_bilinear',EE-hbar*omega*(sum(eta[i,i]*XX[i]*YY[i] for i in range(3))-1)/2)
for i in (1,2):
 eq(f'force_observable_identity_{i}',y*y*(s.diff(XX[i],x)*s.diff(EE,x)+s.diff(XX[i],y)*s.diff(EE,y))-hbar*omega*(XX[i]*sum(eta[j,j]*XX[j]*YY[j] for j in range(3))-YY[i])/2)

# Linearized reciprocal semiclassical equations have two positive sidebands.
g,om,z=s.symbols('g om z',positive=True)
lin=s.Matrix([[0,0,1,0,0,0],[0,0,0,1,0,0],[-g,0,0,0,g,0],[0,-g,0,0,0,g],[0,-2*om,0,0,0,2*om],[2*om,0,0,0,-2*om,0]])
eq('linear_response_characteristic',(z*s.eye(6)-lin).det()-z*z*(z**4+(4*om*om+2*g)*z*z+g*g))
op=s.sqrt(om*om+g)+om;on=s.sqrt(om*om+g)-om
eq('sideband_product',op*on-g)
eq('sideband_separation',op-on-2*om)

# Relaxing quadraticity preserves equivariance, ground state and the first gap.
zz,tau=s.symbols('zz tau',positive=True)
pgf=s.sqrt(1-tau)/s.sqrt(1-tau*zz**2)
nbar=tau/(1-tau)
eq('squeezed_number_mean',s.diff(pgf,zz).subs(zz,1)-nbar)
eq('squeezed_number_factorial_second_moment',s.diff(pgf,zz,2).subs(zz,1)-(3*nbar*nbar+nbar))

def rhs(t,state):
 x,y,xd,yd,u,v=state
 return [xd,yd,2*xd*yd/y-y*(x-u)/v,
 (yd*yd-xd*xd)/y+(v*v+(x-u)**2-y*y)/(2*v),
 (v*v-y*y-(u-x)**2)/y,2*v*(x-u)/y]
def numerical_energy(state):
 x,y,xd,yd,u,v=state
 return .25*(xd*xd+yd*yd)/(y*y)+((x-u)**2+(y-v)**2)/(4*y*v)
times=np.linspace(0,20,401)
initial=np.array([.15,1.1,.05,-.03,-.35,1.6])
sols=[];ode_rows=[]
for tol in (1e-9,1e-11):
 sol=solve_ivp(rhs,(0,20),initial,method='DOP853',t_eval=times,rtol=tol,atol=tol/100)
 assert sol.success and np.isfinite(sol.y).all()
 assert np.min(sol.y[[1,5]])>0
 es=numerical_energy(sol.y)
 drift=float(np.max(np.abs(es-es[0])))
 assert drift<2e-8
 q=.5*sol.y[2]/sol.y[1]**2-1/(4*sol.y[5])
 ode_rows.append({'rtol':tol,'max_energy_drift':drift,'max_shear_charge_drift':float(np.max(abs(q-q[0]))),'minimum_positive_coordinate':float(np.min(sol.y[[1,5]]))})
 sols.append(sol.y)
endpoint_difference=float(np.max(abs(sols[0][:,-1]-sols[1][:,-1])))
assert endpoint_difference<2e-7
np.savez_compressed(OUT/'reciprocal_semiclassical_trajectory.npz',times=times,state=sols[-1])

# Actual fully quantum positive finite-volume/Galerkin regulator; no averaging.
def full_quantum_control(cutoff):
 nr=4;nt=8;rmax=1.2;dr=rmax/nr;dt=2*np.pi/nt
 rs=(np.arange(nr)+.5)*dr;theta=np.arange(nt)*dt
 weights=np.repeat(np.sinh(rs)*dr*dt,nt)
 L=np.zeros((nr*nt,nr*nt))
 def edge(i,j,w):
  L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
 for i,r in enumerate(rs):
  for j in range(nt):
   ix=i*nt+j
   edge(ix,i*nt+(j+1)%nt,dr/(np.sinh(r)*dt))
   if i+1<nr:edge(ix,(i+1)*nt+j,np.sinh((i+1)*dr)*dt/dr)
   else:L[ix,ix]+=2*np.sinh(rmax)*dt/dr
 T=csr_matrix(L/np.sqrt(weights[:,None]*weights[None,:])) # hbar=1,I=1/2
 n=np.arange(cutoff)
 aa=np.diag(np.sqrt(np.arange(1,cutoff)),1)
 a2=aa@aa
 blocks=[];X1=[];perm=[]
 for i,r in enumerate(rs):
  for j,th in enumerate(theta):
   X0=np.cosh(r);x1=np.sinh(r)*np.cos(th);x2=np.sinh(r)*np.sin(th)
   MM=np.array([[X0+x1,x2],[x2,X0-x1]])
   KK=np.linalg.inv(MM)
   H=(KK[0,0]+KK[1,1])*np.diag(2*n+1)/4
   H=H.astype(complex)+(KK[0,0]-KK[1,1]-2j*KK[0,1])*a2/4+(KK[0,0]-KK[1,1]+2j*KK[0,1])*a2.T/4-np.eye(cutoff)/2
   assert np.min(np.linalg.eigvalsh(H))>-2e-12
   blocks.append(csr_matrix(H));X1.append(x1);perm.append(i*nt+(j+nt//2)%nt)
 HP=block_diag(blocks,format='csr');HT=kron(T,eye(cutoff),format='csr');HH=HT+HP
 Uq=diags(np.exp(-.5j*np.pi*n));Us=csr_matrix((np.ones(nr*nt),(perm,np.arange(nr*nt))),shape=(nr*nt,nr*nt))
 U=kron(Us,Uq,format='csr')
 comm=U@HH-HH@U;commnorm=float(np.linalg.norm(comm.data))
 assert commnorm<1e-10
 radial=np.repeat(np.exp(-rs**2/(2*.4**2)),nt)*np.sqrt(weights)
 radial/=np.linalg.norm(radial)
 r=.8;squeeze=r/2
 qp=np.zeros(cutoff,complex)
 for k in range((cutoff+1)//2):
  if 2*k<cutoff:qp[2*k]=math.sqrt(math.factorial(2*k))/(2**k*math.factorial(k))*np.tanh(squeeze)**k/np.sqrt(np.cosh(squeeze))
 omitted=1-float(np.vdot(qp,qp).real);qp/=np.linalg.norm(qp)
 qm=Uq@qp;vp=np.kron(radial,qp);vm=np.kron(radial,qm)
 assert np.max(abs(U@vp-vm))<1e-13
 obs=diags(np.repeat(X1,cutoff))
 def initial_acc(vec):
  Hv=HH@vec;H2v=HH@Hv
  return float(-(np.vdot(vec,obs@H2v)+np.vdot(H2v,obs@vec)-2*np.vdot(Hv,obs@Hv)).real)
 accp=initial_acc(vp);accm=initial_acc(vm)
 assert abs(accp+accm)<1e-9 and abs(accp)>1e-4
 ts=np.linspace(0,.35,8)
 yp=expm_multiply(-1j*HH,vp,start=0,stop=.35,num=8)
 ym=expm_multiply(-1j*HH,vm,start=0,stop=.35,num=8)
 xp=np.array([np.vdot(q,obs@q).real for q in yp]);xm=np.array([np.vdot(q,obs@q).real for q in ym])
 norms=[np.vdot(q,q).real for q in yp]
 energies=[np.vdot(q,HH@q).real for q in yp]
 shape_energies=[float(np.vdot(q,HT@q).real) for q in yp]
 probe_energies=[float(np.vdot(q,HP@q).real) for q in yp]
 def entropy(vec):
  values=np.linalg.svd(vec.reshape(nr*nt,cutoff),compute_uv=False)**2
  values=values[values>1e-15]
  return float(-sum(values*np.log2(values)))
 coupled_entropy=entropy(yp[-1]);assert coupled_entropy>1e-3
 assert np.max(abs(xp+xm))<2e-11
 assert max(abs(np.array(norms)-1))<2e-11
 assert max(abs(np.array(energies)-energies[0]))<2e-9
 uncoupled=kron(T,eye(cutoff),format='csr')+kron(eye(nr*nt),diags(n.astype(float)),format='csr')
 yn=expm_multiply(-1j*uncoupled,vp,start=0,stop=.35,num=8)
 xn=np.array([np.vdot(q,obs@q).real for q in yn]);assert np.max(abs(xn))<1e-12
 uncoupled_entropy=entropy(yn[-1]);assert abs(uncoupled_entropy)<1e-11
 return {'oscillator_cutoff':cutoff,'shape_grid':[nr,nt],'shape_radius':rmax,'Hilbert_dimension':HH.shape[0],
 'joint_symmetry_commutator_norm':commnorm,'discarded_initial_Fock_probability':omitted,
 'initial_shape_acceleration_plus':accp,'initial_shape_acceleration_minus':accm,
 'times':ts.tolist(),'shape_response_plus':xp.tolist(),'shape_response_minus':xm.tolist(),
 'uncoupled_shape_response':xn.tolist(),'max_norm_error':max(abs(np.array(norms)-1)),
 'max_energy_error':max(abs(np.array(energies)-energies[0])),
 'shape_energy':shape_energies,'probe_energy':probe_energies,
 'final_shape_probe_entanglement_bits':coupled_entropy,'uncoupled_entanglement_bits':uncoupled_entropy,
 'scope':'Positive finite-volume/Galerkin model, no shape-grid continuum claim; exact discrete symmetry tested.'}

quantum=[full_quantum_control(n) for n in (16,24)]
cutoff_diff=float(np.max(abs(np.array(quantum[0]['shape_response_plus'])-quantum[1]['shape_response_plus'])));
assert cutoff_diff<2e-5,cutoff_diff

# Exact continuum packet coefficient for a declared smooth compact bump.
def bump(r):return np.exp(-2/(1-r*r)) if r<1 else 0.
Z=quad(lambda r:bump(r)*np.sinh(r),0,1,epsabs=1e-14,epsrel=1e-12)[0]
kappa=quad(lambda r:bump(r)*np.sinh(r)**3,0,1,epsabs=1e-14,epsrel=1e-12)[0]/(2*Z)
report={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'environment':{'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'scipy':scipy.__version__},
 'exact_check_count':len(checks),'exact_checks':checks,'semiclassical_control':{'rows':ode_rows,'endpoint_tolerance_difference':endpoint_difference},
 'full_quantum_regulator_controls':quantum,'Fock_cutoff_response_difference':cutoff_diff,
 'continuum_compact_packet':{'wavefunction':'C exp[-1/(1-r^2)] for r<1, zero otherwise','kappa':kappa,'formula':'initial_acceleration_O=+/- hbar*omega*(1+kappa)*sinh(r_probe)/(2I)', 'observable':'O=zeta(r_shape)*X1, smooth compact radial zeta equals one on a neighborhood of initial packet support; unbounded X1 later-time moments not asserted'},
 'limits':['Selected centered quadratic no-derivative coupling with calibrated gap, not uniqueness in arbitrary interactions.',
 'Fully quantum finite shape/probe model, not full constrained quantum gravity.',
 'Sourced one-Killing twist reconstruction requires generalized total current; vacuum dictionary alone fails.',
 'No laboratory measurement or worldwide novelty claim.']}
(OUT/'dynamical_extension_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'quantum_dimensions':[q['Hilbert_dimension'] for q in quantum],'cutoff_response_difference':cutoff_diff,'kappa':kappa},indent=2))
