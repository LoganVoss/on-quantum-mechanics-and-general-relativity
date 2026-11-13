#!/usr/bin/env python3
"""Exact reduced N^2 deformation and curved-reference discrimination."""
from pathlib import Path
import json
import sympy as s
OUT=Path(__file__).resolve().parents[1]/'evidence'
OUT.mkdir(exist_ok=True)
T,R,z,phi=s.symbols('T R z phi',real=True,positive=True)
c,a=s.symbols('c a',real=True)
b,g0=s.symbols('b gamma_0',real=True)
D=c*(c-2)
f=s.exp(g0)*R**(D/2)
h=s.diag(-f,f);hi=h.inv();sqrt=f
rho=R;P=(c-1)*s.log(R);Q=s.Integer(0)
coords=[T,R,z,phi]
g=s.diag(-f,f,R**c,R**(2-c));gi=g.inv()
S=lambda e:s.simplify(s.powsimp(s.expand(e),force=True))
checks={}
def check(name,expr):
 vals=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
 if any(S(e)!=0 for e in vals):raise AssertionError((name,[S(e) for e in vals]))
 checks[name]=True
# General inverse-metric variation of sqrt(-h) Lambda N^2, including factor-two off diagonal.
A,B,C,kt,kr,km,L=s.symbols('A B C Ktt Krr Ktr Lambda',real=True)
inv=s.Matrix([[A,B],[B,C]]);met=inv.inv();vol=1/s.sqrt(B*B-A*C)
N=A*kt+2*B*km+C*kr;dens=vol*L*N*N
for var,i,j,K,mult in [(A,0,0,kt,1),(B,0,1,km,2),(C,1,1,kr,1)]:
 check('generic_metric_variation_'+str(var),s.diff(dens,var)-mult*vol*L*(2*N*K-met[i,j]*N*N/2))
check('generic_trace',sum(inv[i,j]*L*(2*N*s.Matrix([[kt,km],[km,kr]])[i,j]-met[i,j]*N*N/2) for i in range(2) for j in range(2))-L*N*N)
# All independent Ricci components for exact 4D Levi-Civita family.
Gamma={}
for l in range(4):
 for i in range(4):
  for j in range(4):
   Gamma[l,i,j]=S(sum(gi[l,m]*(s.diff(g[m,j],coords[i])+s.diff(g[m,i],coords[j])-s.diff(g[i,j],coords[m]))/2 for m in range(4)))
Ric=s.Matrix(4,4,lambda i,j:S(sum(s.diff(Gamma[k,i,j],coords[k])-s.diff(Gamma[k,i,k],coords[j])+sum(Gamma[k,i,j]*Gamma[l,k,l]-Gamma[l,i,k]*Gamma[k,j,l] for l in range(4)) for k in range(4))))
for i in range(4):
 for j in range(4):check(f'levi_civita_ricci_{i}{j}',Ric[i,j])
# Exact shape invariant and selected base equations.
Pa=s.Matrix([s.diff(P,T),s.diff(P,R)]);ra=s.Matrix([0,1]);G=Pa*Pa.T
X=(ra.T*hi*ra)[0];Y=s.trace(hi*G);N=S(R*R*Y-X)
check('levi_civita_N',N-D/f)
Gh={(l,i,j):S(sum(hi[l,m]*(s.diff(h[m,j],coords[i])+s.diff(h[m,i],coords[j])-s.diff(h[i,j],coords[m]))/2 for m in range(2))) for l in range(2) for i in range(2) for j in range(2)}
Rh=s.Matrix(2,2,lambda i,j:S(sum(s.diff(Gh[k,i,j],coords[k])-s.diff(Gh[k,i,k],coords[j])+sum(Gh[k,i,j]*Gh[l,k,l]-Gh[l,i,k]*Gh[k,j,l] for l in range(2)) for k in range(2))))
curv=S(s.trace(hi*Rh));check('base_scalar_curvature',curv-D/(2*R*R*f))
F=a*R+b;U=a/(2*R);W=a*R
hess=s.Matrix(2,2,lambda i,j:s.diff(F,coords[i],coords[j])-sum(Gh[k,i,j]*s.diff(F,coords[k]) for k in range(2)))
boxF=s.trace(hi*hess)
E=h*boxF-hess+U*(ra*ra.T-h*X/2)-W*(G-h*Y/2)/2
check('selected_metric_EL',E)
check('selected_area_EL',a*curv+a*X/(2*R*R)-a*Y/2)
check('selected_P_EL',s.diff(W*s.diff(P,R),R)/f)
# Deformation full Euler-Lagrange residuals with arbitrary function Lambda(rho).
Lam=s.Function('Lambda')(R);Lp=s.diff(Lam,R)
K=R*R*G-ra*ra.T
Ed=Lam*(2*N*K-h*N*N/2)
Erho=Lp*N*N+4*Lam*R*N*Y+4*s.diff(Lam*N,R)/f
EP=-4*s.diff(Lam*R*R*N*s.diff(P,R),R)/f
EQ=s.Integer(0)
check('deformation_metric_tt',Ed[0,0]-Lam*D*D/(2*f))
check('deformation_metric_rr',Ed[1,1]-3*Lam*D*D/(2*f))
check('deformation_metric_tr',Ed[0,1])
check('deformation_metric_trace',s.trace(hi*Ed)-Lam*D*D/(f*f))
check('deformation_area_EL',Erho-(Lp*D*(D+4)+2*Lam*D*(D+2)/R)/(f*f))
check('deformation_P_EL',EP+4*D*(c-1)*(R*Lp+Lam*(1-D/2))/(f*f))
check('deformation_Q_EL',EQ)
# Flat reference invariants.
t,r=s.symbols('t r',positive=True)
for name,rr,pp in [('constant_product',s.Integer(2),s.Integer(0)),('cylindrical',r,-s.log(r)),('milne_polar',t*r,s.log(t/r))]:
 xx=-s.diff(rr,t)**2+s.diff(rr,r)**2;yy=-s.diff(pp,t)**2+s.diff(pp,r)**2
 check('N_zero_'+name,rr*rr*yy-xx)
# Positive open-patch nonzero witness c=1; all selected equations still zero.
check('c_one_trace_is_nonzero_coefficient',S(s.trace(hi*Ed).subs(c,1))-Lam*s.exp(-2*g0)*R)
result={'status':'PASS','sympy':s.__version__,'check_count':len(checks),'checks':checks,
 'D':'c(c-2)','conformal_factor_e_2s':'exp(gamma_0) R^(D/2)',
 'N':'D exp(-2s)',
 'metric_EL_tt':'Lambda D^2 exp(-2s)/2','metric_EL_rr':'3 Lambda D^2 exp(-2s)/2',
 'metric_EL_tr':'0','metric_trace':'Lambda D^2 exp(-4s)',
 'area_EL':'exp(-4s) [Lambda_prime D(D+4)+2 Lambda D(D+2)/R]',
 'P_EL':'-4 D(c-1) exp(-4s) [R Lambda_prime+Lambda(1-D/2)]','Q_EL':'0',
 'coefficient_isolation':'For any fixed c not in {0,2}, stationarity at every R>0 implies Lambda(R)=0.',
 'source_type':'exact_symbolic_proof_no_measurements'}
(OUT/'levi_civita_deformation_receipt.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
