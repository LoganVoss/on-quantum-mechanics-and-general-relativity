#!/usr/bin/env python3
"""Exact symbolic checks for the simultaneous Voss chart model; no empirical data."""
from pathlib import Path
import json
import sympy as s

out=Path(__file__).resolve().parents[1]/'evidence'
out.mkdir(exist_ok=True)
t,r,z,ph=s.symbols('t r z phi', positive=True, real=True)
a=s.symbols('a', positive=True, real=True)
b,k=s.symbols('b k', real=True)
coords=(t,r,z,ph)
rho=t*r
h=s.diag(-1,1)
hi=h
M=s.diag(t/r,r/t)
g=s.diag(-1,1,t*t,r*r)
gi=g.inv()
S=lambda x:s.simplify(s.expand(x))
checks={}
def check(name,expr):
    if isinstance(expr,s.MatrixBase):
        ok=all(S(e)==0 for e in expr)
    else: ok=S(expr)==0
    if not ok: raise AssertionError((name,expr))
    checks[name]=True

check('orbit_determinant',M.det()-1)
check('orbit_block',rho*M-g[2:4,2:4])
check('block_determinant',g.det()+rho*rho)
X=s.Matrix([t*s.cosh(z),r*s.cos(ph),r*s.sin(ph),t*s.sinh(z)])
Jac=X.jacobian(coords)
check('exact_minkowski_pullback',Jac.T*s.diag(-1,1,1,1)*Jac-g)
Gamma={}
for l in range(4):
 for i in range(4):
  for j in range(4):
   Gamma[l,i,j]=S(sum(gi[l,m]*(s.diff(g[m,j],coords[i])+s.diff(g[m,i],coords[j])-s.diff(g[i,j],coords[m]))/2 for m in range(4)))
for l in range(4):
 for i in range(4):
  for j in range(4):
   for q in range(4):
    val=s.diff(Gamma[l,q,i],coords[j])-s.diff(Gamma[l,j,i],coords[q])+sum(Gamma[l,j,m]*Gamma[m,q,i]-Gamma[l,q,m]*Gamma[m,j,i] for m in range(4))
    check(f'riemann_{l}{i}{j}{q}',val)

P=s.log(t/r)
J=[M.inv()*M.diff(c) for c in (t,r)]
G=s.Matrix(2,2,lambda i,j:s.trace(J[i]*J[j])/2)
G_expected=s.Matrix(2,2,lambda i,j:s.diff(P,(t,r)[i])*s.diff(P,(t,r)[j]))
check('shape_tensor',G-G_expected)
rg=s.Matrix([s.diff(rho,t),s.diff(rho,r)])
Xrho=(rg.T*hi*rg)[0]
Y=s.trace(hi*G)
check('reference_invariant_relation',rho*rho*Y-Xrho)
F=a*rho+b; U=a/(2*rho); W=a*rho; V=0
box=lambda f:-s.diff(f,t,2)+s.diff(f,r,2)
E=s.Matrix(2,2,lambda i,j:h[i,j]*box(F)-s.diff(F,(t,r)[i],(t,r)[j])+U*(rg[i]*rg[j]-h[i,j]*Xrho/2)-W*(G[i,j]-h[i,j]*Y/2)/2-h[i,j]*V/2)
check('all_metric_euler_lagrange_components',E)
check('area_euler_lagrange',a*Xrho/(2*rho*rho)-a*Y/2)
check('P_euler_lagrange',-s.diff(W*s.diff(P,t),t)+s.diff(W*s.diff(P,r),r))
check('Q_euler_lagrange',s.Integer(0))

kap=s.Function('k')(rho)
Pfun=s.Function('P')(t,r);Qfun=s.Function('Q')(t,r)
Lodd=2*kap*s.exp(Pfun)*(s.diff(Pfun,t)*s.diff(Qfun,r)-s.diff(Pfun,r)*s.diff(Qfun,t))
EoddQ=-s.diff(s.diff(Lodd,s.diff(Qfun,t)),t)-s.diff(s.diff(Lodd,s.diff(Qfun,r)),r)
oddchart=EoddQ.subs(Pfun,P).doit()
kprime=s.Subs(s.Derivative(s.Function('k')(s.Symbol('_xi_1')),s.Symbol('_xi_1')),s.Symbol('_xi_1'),rho)
check('parity_odd_chart_equation',oddchart+4*t/r*kprime)

v=s.symbols('v', positive=True)
x=s.symbols('x', real=True)
psi=(v/s.pi)**s.Rational(1,4)*s.exp(-v*x*x/2)
check('canonical_gaussian_norm',s.integrate(psi*psi,(x,-s.oo,s.oo))-1)
q2=s.integrate(x*x*psi*psi,(x,-s.oo,s.oo))
p2=s.integrate(psi*(-s.diff(psi,x,2)),(x,-s.oo,s.oo))
check('canonical_gaussian_Q_variance',q2-1/(2*v))
check('canonical_gaussian_P_variance',p2-v/2)
check('canonical_uncertainty_saturation',q2*p2-s.Rational(1,4))
check('canonical_orbit_soldering',s.diag(2*q2,2*p2).subs(v,r/t)-M)

sig=s.Function('sigma')(t,r)
gsig=s.diag(-s.exp(2*sig),s.exp(2*sig),t*t,r*r)
check('conformal_volume',gsig.det()+s.exp(4*sig)*rho*rho)
for i in range(2):
 check(f'conformal_base_density_{i}',s.exp(2*sig)*rho*gsig.inv()[i,i]-rho*hi[i,i])
phi=s.Function('phi')(t,r)
D0=sum(s.diff(rho*hi[i,i]*s.diff(phi,(t,r)[i]),(t,r)[i]) for i in range(2))/rho
check('exact_reduced_probe_operator',D0-(-s.diff(phi,t,2)-s.diff(phi,t)/t+s.diff(phi,r,2)+s.diff(phi,r)/r))

result={'status':'PASS','verification_kind':'exact_symbolic_model_checks','empirical_measurements':False,'sympy':s.__version__,'check_count':len(checks),'riemann_components_checked':256,'checks':checks}
(out/'physical_premises_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
