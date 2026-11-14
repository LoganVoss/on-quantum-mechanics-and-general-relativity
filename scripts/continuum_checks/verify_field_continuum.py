#!/usr/bin/env python3
"""Bounded scratch checks of reciprocal continuum sectors and current limits.

This does not prove a full nonlinear quantum/gravity continuum. It checks the
derived finite-mode/material estimates and the exact linearized covariant sector.
"""
from pathlib import Path
import hashlib,json,platform,math
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss
import sympy as s

OUT=Path(__file__).resolve().parent
checks=[]
def eq(name,expr):
    residual=s.simplify(expr)
    assert residual==0,(name,residual)
    checks.append({'name':name,'residual':'0'})

# Einstein-dust background in 2+1 dimensions, computed from its connection.
t,x,y=s.symbols('t x y',positive=True)
coords=[t,x,y];g=s.diag(-1,t*t,t*t);gi=g.inv()
Gamma=[[[s.simplify(sum(gi[a,d]*(s.diff(g[d,c],coords[b])+s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d])) for d in range(3))/2)for c in range(3)]for b in range(3)]for a in range(3)]
Ric=s.Matrix(3,3,lambda a,b:s.simplify(sum(s.diff(Gamma[c][a][b],coords[c])-s.diff(Gamma[c][a][c],coords[b])+sum(Gamma[c][c][d]*Gamma[d][a][b]-Gamma[c][b][d]*Gamma[d][a][c] for d in range(3))for c in range(3))))
Ein=Ric-g*s.trace(gi*Ric)/2
for a in range(3):
 for b in range(3):eq(f'dust_Einstein_{a}{b}',Ein[a,b]-(1/t**2 if a==b==0 else 0))
eq('dust_number_conservation',s.diff(t*t/t**2,t))

# Quadratic tangent action about the dust-supported matched ground configuration.
f,n,hbar,omega,k2=s.symbols('f n hbar omega k2',positive=True)
alpha=n*hbar*omega/2;J=s.Matrix([[0,-1],[1,0]])
B=s.zeros(6);A=s.zeros(6);S=s.zeros(6)
for j in range(2):
 B[j,j]=f*k2+alpha;B[j+2,j+2]=1/(f*t*t);B[j+4,j+4]=alpha
 B[j,j+4]=B[j+4,j]=-alpha
 A[j,j+2]=1/(f*t*t);A[j+2,j]=-(f*k2+alpha);A[j+2,j+4]=alpha
 S[j,j+2]=1;S[j+2,j]=-1
for j in range(2):
 for l in range(2):
  A[j+4,l]=2*omega*J[j,l];A[j+4,l+4]=-2*omega*J[j,l]
  S[j+4,l+4]=-4*J[j,l]/(n*hbar)
for j in range(6):
 for l in range(6):
  eq(f'linear_Hamiltonian_generator_{j}{l}',(A-S*B)[j,l])
  eq(f'linear_energy_exchange_{j}{l}',(A.T*B+B*A)[j,l])
eq('explicit_cosmological_work',s.diff(B[2,2],t)+2/(f*t**3))
# Linear total twist current closure: t² C^0=-f t² χ_t+nℏ(1-z2)/4.
chi,chip,chipp,lapchi,z1,z2dot=s.symbols('chi chip chipp lapchi z1 z2dot')
divC=-f*(2*t*chip+t*t*chipp)+f*lapchi-n*hbar*z2dot/4
divC=divC.subs({chipp:-2*chip/t+lapchi/t**2-alpha*(chi-z1)/(f*t*t),z2dot:2*omega*(chi-z1)})
eq('linear_total_twist_current_closure',divC)
# Ground-state matter carries the shear Noether charge even at χ=0.
# The repaired local connection therefore has constant spatial background flux.
J0=n*hbar/(4*t*t)
F12=-n*hbar/(4*f)
eq('background_twist_flux_closed',s.diff(F12,t))
eq('background_shifted_curvature_zero',F12+n*hbar/(4*f))
eq('background_total_current_density_constant',s.diff(t*t*J0,t))

# Midpoint-rule constant and strong-current balancing exponents (d=2).
h=s.symbols('h',positive=True)
eta=h**s.Rational(2,5)
eq('current_bias_order',eta**2-h**s.Rational(4,5))
eq('midpoint_current_order',h*h/eta**3-h**s.Rational(4,5))
eq('quantum_position_order',h**s.Rational(8,5)/eta**2-h**s.Rational(4,5))
eq('population_exponent',s.Rational(26,5)/2-1-s.Rational(8,5))

# A hard Fock projection does not preserve the full shear Noether identity.
# Exact projected quadratic matrices are used; the defect is a boundary effect.
dcut=6;chicut=s.Rational(1,3);vcut=s.Integer(2)
acut=s.Matrix(dcut,dcut,lambda i,j:s.sqrt(j) if j==i+1 else 0)
a2cut=acut*acut;diagcut=s.diag(*[2*j+1 for j in range(dcut)])
Q2cut=(a2cut+a2cut.T+diagcut)/2
P2cut=(-a2cut-a2cut.T+diagcut)/2
Ccut=(a2cut-a2cut.T)/(2*s.I)
Hcut=((chicut**2+vcut**2)*Q2cut+P2cut-2*chicut*Ccut)/(2*vcut)-s.eye(dcut)/2
Gcut=Q2cut/2
shear_defect=s.simplify((chicut*Q2cut-Ccut)/vcut+s.I*(Hcut*Gcut-Gcut*Hcut))
assert shear_defect!=s.zeros(dcut)
low=shear_defect[:dcut-2,:dcut-2]
eq('finite_Fock_shear_defect_vanishes_below_boundary',s.trace(low.conjugate().T*low))
assert s.trace(shear_defect.conjugate().T*shear_defect)>0

# Exact linear reciprocity and Fourier lattice convergence on the dust background.
def mat(tt,kk):
 a=np.zeros((6,6));jj=np.array([[0.,-1.],[1.,0.]])
 a[:2,2:4]=np.eye(2)/(tt*tt)
 a[2:4,:2]=-(kk+1)*np.eye(2);a[2:4,4:]=np.eye(2)
 a[4:,:2]=2*jj;a[4:,4:]=-2*jj
 return a
Y0=np.array([.8,-.2,.15,.1,-.3,.25]);t0=1.;T=2.;kk=5.
def linear_run(kk):
 sol=solve_ivp(lambda tt,Y:mat(tt,kk)@Y,(t0,T),Y0,rtol=2e-12,atol=2e-14,method='DOP853')
 assert sol.success
 return sol.y[:,-1]
def linear_energy(Y,tt,kk):
 return .5*np.dot(Y[2:4],Y[2:4])/(tt*tt)+.5*kk*np.dot(Y[:2],Y[:2])+.5*np.dot(Y[:2]-Y[4:],Y[:2]-Y[4:])
reference=linear_run(kk);linear_rows=[];previous=None
kmin=4*kk/(np.pi*np.pi)
bmin=min(1/T**2,kmin/(kmin+2));bmax=max(kk+2,1/t0**2)
for m in (16,32,64,128):
 dx=2*np.pi/m;kh=sum((2/dx*np.sin(k*dx/2))**2 for k in (1,2))
 difference=linear_run(kh)-reference
 err=float(np.linalg.norm(difference));symbol_bound=dx*dx*17/12
 bound=(bmax/bmin)*(T-t0)*symbol_bound*np.linalg.norm(Y0)
 assert 0<=kk-kh<=symbol_bound*(1+1e-12)
 assert err<=bound
 energy_error=float(np.sqrt(linear_energy(difference,T,kk)))
 energy_bound=np.log(T/t0)*(kk-kh)/np.sqrt(kh)*np.sqrt(linear_energy(Y0,t0,kh))
 smooth_bound=np.pi/24*dx*dx*np.log(T/t0)*kk**1.5*np.sqrt(linear_energy(Y0,t0,kk))
 assert energy_error<=energy_bound*(1+1e-10)
 assert energy_bound<=smooth_bound*(1+1e-10)
 row={'grid_per_direction':m,'h':dx,'symbol_error':kk-kh,'symbol_bound':symbol_bound,'endpoint_error':err,'rigorous_Duhamel_bound':bound,
      'energy_error':energy_error,'sharp_energy_estimate':energy_bound,'smooth_mode_bound':smooth_bound}
 if previous is not None:
  row['observed_order']=float(np.log2(previous/err));assert 1.8<row['observed_order']<2.2
 previous=err;linear_rows.append(row)

# Nonlinear reciprocal material continuum at one retained spatial mode.
# Fixed h3 background a(t)=t. The scalar mean and all Gaussian probes exchange
# energy; this is not prescribed q. Matter velocity is comoving in this sector.
def parcel_run(rule,m):
 if rule=='midpoint':
  p=(np.arange(m)+.5)/m;ww=np.full(m,1/m)
 else:
  p,ww=leggauss(m);p=(p+1)/2;ww=ww/2
 aa,bb=np.meshgrid(p,p,indexing='ij');weights=(ww[:,None]*ww[None,:]).ravel()
 u0=(.2+.3*aa*aa+.1*bb).ravel();v0=(1.2+.1*aa*bb).ravel();count=len(u0)
 initial=np.r_[.1,1.1,.03,-.02,u0,v0]
 def rhs(tt,z):
  xx,yy,vx,vy=z[:4];uu=z[4:4+count];vv=z[4+count:]
  ax=2*vx*vy/yy-2*vx/tt-yy*np.dot(weights,(xx-uu)/vv)/(2*tt*tt)
  ay=(vy*vy-vx*vx)/yy-2*vy/tt+np.dot(weights,(vv*vv+(xx-uu)**2-yy*yy)/vv)/(4*tt*tt)
  ud=(vv*vv-yy*yy-(uu-xx)**2)/yy;vd=2*vv*(xx-uu)/yy
  return np.r_[vx,vy,ax,ay,ud,vd]
 sol=solve_ivp(rhs,(1,1.5),initial,rtol=2e-11,atol=2e-13,method='DOP853')
 assert sol.success and np.isfinite(sol.y).all()
 assert np.min(sol.y[1])>0 and np.min(sol.y[4+count:])>0
 return sol.y[:4,-1],float(np.min(sol.y[4+count:]))
ref16,_=parcel_run('gauss',16);ref24,_=parcel_run('gauss',24)
reference_gap=float(np.linalg.norm(ref16-ref24));assert reference_gap<2e-11
parcel_rows=[];previous=None
for m in (4,8,16,32):
 result,vmin=parcel_run('midpoint',m);err=float(np.linalg.norm(result-ref24))
 row={'material_grid_per_direction':m,'h':1/m,'retained_shape_modes':1,'geometry_endpoint_error':err,'minimum_probe_height':vmin}
 if previous is not None:
  row['observed_order']=float(np.log2(previous/err));assert 1.8<row['observed_order']<2.2
 previous=err;parcel_rows.append(row)

# Strong-current mollification control on a torus, computed independently by
# exact sampled Fourier aliasing, rather than evaluating a dense kernel matrix.
# J^0=2+0.3cos(x)cos(y), spatial J=0, fixed regular coordinates.
coeff={(0,0):2.0,(-1,-1):.075,(-1,1):.075,(1,-1):.075,(1,1):.075}
current_rows=[]
for m in (16,32,64):
 dx=2*np.pi/m;eta=dx**.4
 modes=np.arange(-2*m,2*m+1);K,L=np.meshgrid(modes,modes,indexing='ij')
 sampled=np.zeros_like(K,dtype=float);target=np.zeros_like(K,dtype=float)
 for (a,b),value in coeff.items():
  mask=((a-K)%m==0)&((b-L)%m==0)
  sampled[mask]+=value*(-1.0)**(((a-K[mask])//m)+((b-L[mask])//m))
  target[(K==a)&(L==b)]=value
 smoothed=sampled*np.exp(-eta*eta*(K*K+L*L)/2)
 L2=float(2*np.pi*np.sqrt(np.sum((smoothed-target)**2)))
 raw_contact=-float(np.sum(smoothed**2));limit_contact=-sum(v*v for v in coeff.values())
 # Coefficient-array truncation tail is exponentially below the retained error.
 assert np.max(abs(smoothed[np.maximum(abs(K),abs(L))==2*m]))<1e-18
 row={'material_grid_per_direction':m,'h':dx,'eta':eta,'current_L2_error':L2,
      'contact_mean_error':abs(raw_contact-limit_contact),'rate_normalized_L2':L2/dx**.8}
 current_rows.append(row)
assert all(current_rows[i+1]['current_L2_error']<current_rows[i]['current_L2_error'] for i in range(2))

# Independent Fock Galerkin cutoff control along an exact Gaussian path.
# For constant M, ||exp(JK t)||<=exp(d_G(I,M)), giving a uniform tail parameter.
MM=np.array([[1,.3],[.3,.3**2+1.2**2]])/1.2
KK=np.linalg.inv(MM);Jcanonical=np.array([[0.,1.],[-1.,0.]])
Tosc=1.6;SS=expm(Jcanonical@KK*Tosc);NN=SS@SS.T
uu=NN[0,1]/NN[0,0];vv=1/NN[0,0]
zz=(1-vv+1j*uu)/(1+vv-1j*uu)
c0=np.sqrt(2)*vv**.25/np.sqrt(1+vv-1j*uu)
exact=np.zeros(128,complex)
for j in range(64):exact[2*j]=c0*math.sqrt(math.factorial(2*j))/(2**j*math.factorial(j))*zz**j
assert abs(np.vdot(exact,exact).real-1)<2e-13
theta=float(np.tanh(np.arccosh(np.trace(MM)/2)))
beta=abs((KK[0,0]-KK[1,1]-2j*KK[0,1])/4)
fock_rows=[]
for D in (8,12,16,24,32):
 aa=np.diag(np.sqrt(np.arange(1,D)),1);a2=aa@aa;num=np.arange(D)
 HH=(KK[0,0]+KK[1,1])*np.diag(2*num+1)/4
 HH=HH.astype(complex)+(KK[0,0]-KK[1,1]-2j*KK[0,1])*a2/4+(KK[0,0]-KK[1,1]+2j*KK[0,1])*a2.T/4-np.eye(D)/2
 vacuum=np.zeros(D,complex);vacuum[0]=1
 state=expm(-1j*HH*Tosc)@vacuum
 overlap=abs(np.vdot(exact[:D],state));ray_error=float(np.sqrt(max(0,2-2*overlap)))
 tail_bound=theta**(D/2)/np.sqrt(1-theta)
 error_bound=(1+beta*Tosc*(D+2))*tail_bound
 assert ray_error<=error_bound+2e-8
 Q2=(a2+a2.T+np.diag(2*num+1))/2
 P2=(-a2-a2.T+np.diag(2*num+1))/2
 C=(a2-a2.T)/(2j)
 observed=np.array([[2*np.vdot(state,Q2@state).real,2*np.vdot(state,C@state).real],[2*np.vdot(state,C@state).real,2*np.vdot(state,P2@state).real]])
 fock_rows.append({'cutoff':D,'ray_error':ray_error,'rigorous_uniform_tail_Duhamel_bound':error_bound,'covariance_error':float(np.max(abs(observed-NN)))})
assert fock_rows[-1]['covariance_error']<2e-12

report={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'scipy':scipy.__version__,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_check_count':len(checks),'checks':checks,
 'linearized_covariant_spatial_limit':{'background':'2+1Einstein dust: a=t,n=n0/t²,n0*m0=2f; shape/probe matched ground. First-order density/velocity/metric perturbations zero.',
 'parameters':{'f':1,'n0':2,'m0':1,'hbar':1,'omega':1,'mode':[1,2],'time':[t0,T]},'rows':linear_rows,
 'local_reconstruction':'Ground-state shear current J0=n0*hbar/(4t²) gives F12=-n0*hbar/(4f), a closed nonzero flux. Global torus exactness/flux quantization is not assumed.',
 'global_field_bound':'For Q²=sum|k|^6 H_k(t0)<infinity and spectralprojectioninitialdata: sqrt(continuum_errorenergy)<=(pi/2)*delta_initial+(pi/24)h²log(T/t0)Q+(h/pi)^3Q. delta_initial² bounds initial lattice quantum fluctuation energy; H_k<=pi²*H_h/4 on resolved modes. This is the quadratic linearized theory.',
 'zero_mode_caveat':'The energy seminorm does not control the common constant configuration variance. Localization and separate finite-dimensional covariance propagation of that mode are additionally required for configuration-observable claims.'},
 'nonlinear_reciprocal_label_limit':{'fixed_background':'a=t; one retained homogeneous shape mode; continuumGaussianinternalprobes','time':[1,1.5],
 'gauss_reference_difference':reference_gap,'rows':parcel_rows},
 'strong_current_and_contact_control':{'profile':'J0=2+0.3cos x cos y on torus; spatialcurrentzero','rows':current_rows},
 'Gaussian_internal_cutoff':{'constant_shape':MM.tolist(),'time':Tosc,'uniform_tail_theta':theta,'rows':fock_rows},
 'finite_Fock_shear_boundary_defect':{'cutoff':dcut,'chi':'1/3','lambda':2,'defect_diagonal':[str(shear_defect[j,j])for j in range(dcut)],
 'frobenius_squared':str(s.trace(shear_defect.conjugate().T*shear_defect)),
 'scope':'P_D h P_D and the compressed Q² generator do not satisfy the full shear Noether identity. Full selected Gaussian/current identities are recovered in the ordered D→infinity limit with weighted tail control, not exactly at finite D.'},
 'limits':['No nonlinear spatial Galerkin cutoff removal is proved.','The material positions/current architecture and gradient couplings are additions to the shipped single-cell quantum regulator.',
 'Finite-time linearized spatial theorem and nonlinear fixed-mode material theorem have distinct scopes.','Strong-current/contact result uses smoothing; unsmoothed point-current squares are undefined.']}
(OUT/'field_continuum_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'linear_orders':[r.get('observed_order')for r in linear_rows[1:]],'reciprocal_label_orders':[r.get('observed_order')for r in parcel_rows[1:]],'current_errors':[r['current_L2_error']for r in current_rows]},indent=2))
