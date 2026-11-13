#!/usr/bin/env python3
"""Independent exact quadratic-curvature response audit; finite bounded checks."""
from pathlib import Path
import sympy as s
import json,hashlib,platform,time
start=time.monotonic(); checks=[]
def eq(name,e):
 r=s.factor(e)
 assert r==0,(name,r)
 checks.append({'name':name,'residual':'0'})
eta=s.diag(-1,1,1,1)
k=s.Matrix(s.symbols('k0:4',real=True)); ku=eta*k; z=(k.T*eta*k)[0]
variables=s.symbols('h00 h01 h02 h03 h11 h12 h13 h22 h23 h33',real=True)
indices=[(i,j) for i in range(4) for j in range(i,4)]
h=s.zeros(4)
for q,(i,j) in zip(variables,indices):h[i,j]=h[j,i]=q
tr=s.trace(eta*h)
Ric=s.Matrix(4,4,lambda i,j:s.expand((-k[i]*(ku.T*h)[j]-k[j]*(ku.T*h)[i]+z*h[i,j]+k[i]*k[j]*tr)/2))
R=s.expand(s.trace(eta*Ric)); G=Ric-eta*R/2
D=-z*eta+k*k.T
a,b,kappa=s.symbols('a b kappa',real=True)
quadratic=a*R**2+b*s.trace(eta*Ric*eta*Ric)
grad=s.zeros(4)
for q,(i,j) in zip(variables,indices):
 grad[i,j]=grad[j,i]=s.diff(quadratic,q)/(1 if i==j else 2)
# h is covariant; E^{ab}=-δS/δh_ab. Lower with background eta.
Efromaction=-eta*grad*eta
Eexpected=-b*z*G+(2*a+b)*D*R
for i,j in indices:eq(f'full_symbol_from_action_{i}{j}',Efromaction[i,j]-Eexpected[i,j])
for j in range(4):
 eq(f'linear_Bianchi_{j}',(ku.T*G)[j])
 eq(f'quadratic_Bianchi_{j}',(ku.T*Eexpected)[j])
eq('full_trace',s.trace(eta*(G+Eexpected))+(1+(6*a+2*b)*z)*R)
# Reviewer Hessian-sector values, independently recomputed.
x=s.symbols('x',positive=True); static={k[0]:0,k[1]:x,k[2]:0,k[3]:0}
TT=s.diag(0,0,1,-1); CF=2*eta
sector={}
for name,H in [('TT',TT),('conformal',CF)]:
 sub={q:H[i,j] for q,(i,j) in zip(variables,indices)}|static
 rr=Ric.subs(sub);sc=R.subs(sub)
 sector[name]=[s.factor(sc**2),s.factor(s.trace(eta*rr*eta*rr))]
eq('review_TT_R2',sector['TT'][0]);eq('review_TT_Ric2',sector['TT'][1]-x**4/2)
eq('review_conformal_R2',sector['conformal'][0]-36*x**4);eq('review_conformal_Ric2',sector['conformal'][1]-12*x**4)
eq('review_discriminant',s.Matrix([[0,s.Rational(1,2)],[36,12]]).det()+18)
# Gauge variations give zero linear curvature for arbitrary covector and vector.
xi=s.Matrix(s.symbols('xi0:4',real=True)); gauge=k*xi.T+xi*k.T
gsub={q:gauge[i,j] for q,(i,j) in zip(variables,indices)}
for i,j in indices:eq(f'gauge_Ricci_{i}{j}',Ric[i,j].subs(gsub,simultaneous=True))
# TT and transverse scalar amplitudes diagonalize response independently.
Z=s.symbols('z',positive=True)
Tamp=s.symbols('tau',real=True)
theta=eta-k*k.T/z
for H,label,factor in [(TT,'TT',1-b*x**2),(2*theta,'scalar',1+(6*a+2*b)*z)]:
 sub={q:H[i,j] for q,(i,j) in zip(variables,indices)}
 evalG=G.subs(sub,simultaneous=True);evalE=(G+Eexpected).subs(sub,simultaneous=True)
 if label=='TT':evalG=evalG.subs(static);evalE=evalE.subs(static)
 for i,j in indices:eq(f'{label}_transfer_{i}{j}',evalE[i,j]-factor*evalG[i,j])
r2=1/(1-b*Z);r0=1/(1+(6*a+2*b)*Z)
y2=(1/r2-1)/Z;y0=(1/r0-1)/Z
eq('inverse_b',-y2-b);eq('inverse_a',(y0+2*y2)/6-a)
eq('inverse_response_map_determinant',s.Matrix([[0,-1],[6,2]]).det()-6)
# Bare scalar vs tensor pole locations and TT opposite residues.
m0,m2=s.symbols('m0 m2',positive=True)
eq('TT_partial_fractions',1/(Z*(1+Z/m2**2))-(1/Z-1/(Z+m2**2)))
eq('scalar_pole',1+(6*a+2*b)*(-1/(6*a+2*b)))
eq('tensor_pole',1-b*(1/b))
# Static point-mass potential: independently solve actual 00,22 field equations.
Phi,Psi,mass=s.symbols('Phi Psi mass',real=True)
hpot=s.diag(-2*Phi,-2*Psi,-2*Psi,-2*Psi)
psub={q:hpot[i,j] for q,(i,j) in zip(variables,indices)}|static
Ep=(G+Eexpected).subs(psub,simultaneous=True)
sol=s.solve([Ep[0,0]-kappa*mass,Ep[2,2]],(Phi,Psi),dict=True)[0]
Phi_expected=-kappa*mass/2*(1/x**2+s.Rational(1,3)/(x**2+m0**2)-s.Rational(4,3)/(x**2+m2**2))
Psi_expected=-kappa*mass/2*(1/x**2-s.Rational(1,3)/(x**2+m0**2)-s.Rational(2,3)/(x**2+m2**2))
coefmap={b:-1/m2**2,a:(1/m0**2+2/m2**2)/6}
eq('point_source_Phi',sol[Phi].subs(coefmap)-Phi_expected)
eq('point_source_Psi',sol[Psi].subs(coefmap)-Psi_expected)
for i,j in indices:
 eq(f'point_source_full_equation_{i}{j}',Ep[i,j].subs(sol)-(kappa*mass if i==j==0 else 0))
# Exterior potentials and exact two-observable inversion at a radius r>0.
r=s.symbols('r',positive=True);e0,e2=s.symbols('e0 e2',positive=True)
U=1+e0/3-4*e2/3;V=1-e0/3-2*e2/3
eq('Yukawa_e0_inverse',U-2*V+1-e0);eq('Yukawa_e2_inverse',(2-U-V)/2-e2)
eq('potential_response_determinant',s.Matrix([[s.Rational(1,3),-s.Rational(4,3)],[-s.Rational(1,3),-s.Rational(2,3)]]).det()+s.Rational(2,3))
# Exact finite examples are synthetic controls of response and inverse.
trials=[]
for aa,bb,zz in [(s.Rational(1,2),s.Rational(-1,2),s.Rational(1,4)),(s.Rational(2,3),s.Rational(-1,3),s.Rational(3,2)),(0,0,s.Rational(2)),(s.Rational(1,5),0,s.Rational(1,3)),(s.Rational(1,3),s.Rational(-1),s.Rational(3,5))]:
 rr0=s.factor(r0.subs({a:aa,b:bb,Z:zz}));rr2=s.factor(r2.subs({a:aa,b:bb,Z:zz}))
 reca=s.factor(((1/rr0-1)+2*(1/rr2-1))/(6*zz));recb=s.factor((1-1/rr2)/zz)
 assert (reca,recb)==(aa,bb)
 trials.append({'a':str(aa),'b':str(bb),'z':str(zz),'r0':str(rr0),'r2':str(rr2),'recovered_a':str(reca),'recovered_b':str(recb)})
# Sharp coefficient bounds from independent inverse-response errors.
eps0,eps2=s.symbols('eps0 eps2',nonnegative=True)
for p,q in [(1,1),(1,-1),(-1,1),(-1,-1)]:
 da=(p*eps0+2*q*eps2)/6;db=-q*eps2
 if p==q:eq(f'sharp_a_corner_{p}',da-p*(eps0+2*eps2)/6)
 eq(f'sharp_b_corner_{p}_{q}',db+q*eps2)
# Unknown Einstein normalization: three measurements identify kappa,a,b.
z1,z2=s.symbols('z1 z2',positive=True)
X21=(1-b*z1)/kappa;X22=(1-b*z2)/kappa
X01=(1+(6*a+2*b)*z1)/kappa;X02=(1+(6*a+2*b)*z2)/kappa
intercept=(z2*X21-z1*X22)/(z2-z1)
slope2=(X22-X21)/(z2-z1)
slope0=(X01-intercept)/z1
eq('unknown_kappa_recovery',1/intercept-kappa)
eq('unknown_b_recovery',-slope2/intercept-b)
eq('unknown_a_recovery',(slope0+2*slope2)/(6*intercept)-a)
eq('unknown_calibration_rank',s.Matrix([[1,z1,0],[1,z2,0],[1,0,z1]]).det()-z1*(z2-z1))
eq('fourth_response_consistency',z2*X01-z1*X02-z2*X21+z1*X22)
# A six-derivative counterexample can mimic the scalar transfer at one scale.
extra,z0=s.symbols('extra z0',real=True)
c=6*a+2*b
extended=1/(1+(c-extra*z0)*Z+extra*Z**2)
eq('higher_order_single_scale_negative_control',(extended-r0).subs(Z,z0))
eq('higher_order_detected_off_scale',s.factor(1/extended-1/r0)-extra*Z*(Z-z0))
report={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'exact_check_count':len(checks),'checks':checks,'synthetic_inverse_trials':trials,'action':'(2 kappa)^-1 integral sqrt(-g) [R+a R^2+b Ricci^2]+S_m','conventions':'signature(-+++),R_ab=∂cΓc_ab−∂bΓc_ac+..., Fourier exp(i k.x), z=k.k, spacelike z>0','transfer_functions':{'r2':str(r2),'r0':str(r0)},'reviewer_hessian_credit':'The two curvature Hessian sectors are supplied in the November13 review; this script independently recomputes them. New work adds full operator, source transfer, robust inverse and point-source potentials.','limits':['Constant-coefficient parity-even local 4D class, modulo constant Euler density.','Fixed physical metric and minimal source identification.','No curvature-squared exclusion is inferred from Ricci-flat stationarity alone.','No observational data; no worldwide novelty claim.','Higher/nonlocal operators and EFT validity require separate analysis.'],'elapsed_seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('curvature_response_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','exact_check_count','elapsed_seconds']}))
