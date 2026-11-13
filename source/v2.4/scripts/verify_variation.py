#!/usr/bin/env python3
"""Exact symbolic certificates for the local variational derivation.

Independent calculations, not a replacement for the accompanying analytic proof.
All expressions are exact SymPy expressions; no numerical tolerances are used.
"""
from pathlib import Path
import json
import sympy as s

checks = []
def zero(name, value):
    value = s.simplify(s.expand(value))
    if value != 0:
        raise AssertionError((name, value))
    checks.append({"name": name, "residual": "0", "status": "passed"})

t, r = s.symbols('t r', positive=True)
x = (t, r)
eta = s.diag(-1, 1)
rho = t*r
P = s.log(t/r)
F = s.Function('F')
U = s.Function('U')
W = s.Function('W')
V = s.Function('V')
z = s.symbols('z', positive=True)
Fp = s.diff(F(z), z).subs(z, rho)
Fpp = s.diff(F(z), z, 2).subs(z, rho)
Up = s.diff(U(z), z).subs(z, rho)
Wp = s.diff(W(z), z).subs(z, rho)
Vp = s.diff(V(z), z).subs(z, rho)
grad = lambda f: s.Matrix([s.diff(f, y) for y in x])
dot = lambda a, b: (a.T*eta*b)[0]
box = lambda f: -s.diff(f, t, 2)+s.diff(f, r, 2)
X = dot(grad(rho), grad(rho))
M = s.diag(t/r, r/t)
J = [s.simplify(M.inv()*s.diff(M, y)) for y in x]
T = s.Matrix(2, 2, lambda a,b: s.trace(J[a]*J[b]))
traceT = sum(eta[a,b]*T[a,b] for a in range(2) for b in range(2))
zero('chart_area_gradient', X-(t*t-r*r))
zero('chart_area_harmonic', box(rho))
zero('chart_shape_metric_tt', T[0,0]-2/t**2)
zero('chart_shape_metric_rr', T[1,1]-2/r**2)
zero('chart_shape_metric_tr', T[0,1]+2/rho)
E = s.Matrix(2,2,lambda a,b:
    eta[a,b]*box(F(rho))-s.diff(F(rho),x[a],x[b])
    +U(rho)*(s.diff(rho,x[a])*s.diff(rho,x[b])-eta[a,b]*X/2)
    -W(rho)/4*(T[a,b]-eta[a,b]*traceT/2)
    -eta[a,b]*V(rho)/2)
S = t*t+r*r
expected = [
    -Fpp*t*t+U(rho)*S/2-W(rho)*S/(4*rho**2)+V(rho)/2,
    -Fpp*r*r+U(rho)*S/2-W(rho)*S/(4*rho**2)-V(rho)/2,
    -(rho*Fpp+Fp)+rho*U(rho)+W(rho)/(2*rho)]
for name, expr, target in zip(('tt','rr','tr'), (E[0,0],E[1,1],E[0,1]), expected):
    zero('metric_chart_'+name, expr-target)
zero('metric_trace', -E[0,0]+E[1,1]-(box(F(rho))-V(rho)))
Erho = -Up*X-2*U(rho)*box(rho)-Wp*traceT/4+Vp
zero('area_chart', Erho-(X*(-Up-Wp/(2*rho**2))+Vp))
EP = -s.diff(W(rho)*s.diff(P,t),t)+s.diff(W(rho)*s.diff(P,r),r)
zero('shape_chart', EP-S/rho*(W(rho)/rho-Wp))
a,b = s.symbols('a b', real=True)
selected={F:s.Lambda(z,a*z+b),U:s.Lambda(z,a/(2*z)),W:s.Lambda(z,a*z),V:s.Lambda(z,0)}
for name, expr in [('tt',E[0,0]),('rr',E[1,1]),('tr',E[0,1]),('area',Erho),('shape',EP)]:
    zero('selected_'+name,s.expand(expr).subs(selected).doit())
zero('independent_area_shape_covectors',s.det(s.Matrix([[s.diff(rho,t),s.diff(rho,r)],[s.diff(P,t),s.diff(P,r)]]))+2)

# Target metric: compute J from the actual positive determinant-one matrix.
p,q,pt,pr,qt,qr=s.symbols('p q pt pr qt qr', real=True)
Mt=s.Matrix([[s.exp(p),s.exp(p)*q],[s.exp(p)*q,s.exp(-p)+s.exp(p)*q*q]])
Jt=Mt.inv()*(Mt.diff(p)*pt+Mt.diff(q)*qt)
Jr=Mt.inv()*(Mt.diff(p)*pr+Mt.diff(q)*qr)
zero('target_determinant',Mt.det()-1)
zero('target_trace_tt',s.trace(Jt*Jt)/2-pt**2-s.exp(2*p)*qt**2)
zero('target_trace_rr',s.trace(Jr*Jr)/2-pr**2-s.exp(2*p)*qr**2)
zero('target_trace_tr',s.trace(Jt*Jr)/2-pt*pr-s.exp(2*p)*qt*qr)

# Boundary identity for the metric curvature term on a flat normal frame.
# This checks every first and second derivative of arbitrary variation fields.
f=s.Function('f')(t,r)
A=s.Function('A')(t,r)
B=s.Function('B')(t,r)
C=s.Function('C')(t,r)
v=s.Matrix([[A,B],[B,C]])
vtrace=-A+C
deltaR=box(vtrace)-sum(s.diff(v[i,j],x[i],x[j]) for i in range(2) for j in range(2))
bulk=sum((eta[i,j]*box(f)-s.diff(f,x[i],x[j]))*v[i,j] for i in range(2) for j in range(2))
Theta=[]
for i in range(2):
    raised_di=sum(eta[i,j]*s.diff(vtrace,x[j]) for j in range(2))
    divv=sum(s.diff(v[i,j],x[j]) for j in range(2))
    raised_df=sum(eta[i,j]*s.diff(f,x[j]) for j in range(2))
    Theta.append(f*(raised_di-divv)-vtrace*raised_df+sum(v[i,j]*s.diff(f,x[j]) for j in range(2)))
zero('curvature_variation_integration_by_parts',f*deltaR-bulk-sum(s.diff(Theta[i],x[i]) for i in range(2)))

# Exact odd-sector variation: epsilon^{tr}=+1/sqrt(-h).
K=s.Function('k')
rh=s.Function('rho')(t,r)
pf=s.Function('p')(t,r)
qf=s.Function('q')(t,r)
Lodd=2*K(rh)*s.exp(pf)*(s.diff(pf,t)*s.diff(qf,r)-s.diff(pf,r)*s.diff(qf,t))
EQodd=s.diff(Lodd,qf)-sum(s.diff(s.diff(Lodd,s.diff(qf,y)),y) for y in x)
chart_sub={rh:rho,pf:P,qf:s.Integer(0)}
EQodd=s.simplify(EQodd.subs(chart_sub).doit())
zero('odd_shape_chart',EQodd+4*t/r*s.diff(K(z),z).subs(z,rho))

# Direct four-dimensional Christoffel/Ricci calculation at generic local jets.
# A constant target congruence and base rescaling set M(0)=I, s(0)=0;
# all first and second jets remain arbitrary.
coords=s.symbols('x0:4')
x0,x1=coords[:2]
R=s.symbols('R', positive=True)
symbols={}
def jets(name,constant):
    a0,a1,a00,a01,a11=s.symbols(name+'0 '+name+'1 '+name+'00 '+name+'01 '+name+'11', real=True)
    symbols[name]=(a0,a1,a00,a01,a11)
    return constant+a0*x0+a1*x1+a00*x0*x0/2+a01*x0*x1+a11*x1*x1/2
rhj=jets('r',R)
sj=jets('s',0)
pj=jets('p',0)
qj=jets('q',0)
base=s.diag(-s.exp(2*sj),s.exp(2*sj))
orbit=rhj*s.Matrix([[s.exp(pj),s.exp(pj)*qj],[s.exp(pj)*qj,s.exp(-pj)+s.exp(pj)*qj*qj]])
g=s.diag(1,1,1,1)
g[:2,:2]=base
g[2:,2:]=orbit
at={x0:0,x1:0}
g0=g.subs(at)
gi=g0.inv()
dg=[g.diff(c).subs(at) if i<2 else s.zeros(4) for i,c in enumerate(coords)]
ddg=[[g.diff(ci,cj).subs(at) if i<2 and j<2 else s.zeros(4) for j,cj in enumerate(coords)] for i,ci in enumerate(coords)]
dgi=[-gi*d*gi for d in dg]
def low(l,m,n):return (dg[m][l,n]+dg[n][l,m]-dg[l][m,n])/2
Gam=[[[sum(gi[l,k]*low(k,m,n) for k in range(4)) for n in range(4)] for m in range(4)] for l in range(4)]
def dgam(a,l,m,n):
    return sum(dgi[a][l,k]*low(k,m,n)+gi[l,k]*(ddg[a][m][k,n]+ddg[a][n][k,m]-ddg[a][k][m,n])/2 for k in range(4))
Ric=s.Matrix(4,4,lambda m,n:sum(dgam(l,l,m,n)-dgam(n,l,m,l) for l in range(4))+sum(Gam[l][l][k]*Gam[k][m][n]-Gam[l][n][k]*Gam[k][m][l] for l in range(4) for k in range(4)))
for i in range(2):
    for j in range(2,4):
        zero('mixed_ricci_'+str(i)+str(j),Ric[i,j])
Rg=s.simplify(sum(gi[m,n]*Ric[m,n] for m in range(4) for n in range(4)))
r0,r1,r00,r01,r11=symbols['r']
s0,s1,s00,s01,s11=symbols['s']
p0,p1,p00,p01,p11=symbols['p']
q0,q1,q00,q01,q11=symbols['q']
Rh=2*(s00-s11)
Xj=-r0*r0+r1*r1
boxrho=(-r00+r11) # s(0)=0 in two dimensions
boxlog=boxrho/R-Xj/R**2
TrJJ=2*(-p0*p0-q0*q0+p1*p1+q1*q1)
target=Rh-2*boxlog-s.Rational(3,2)*Xj/R**2-TrJJ/4
zero('four_dimensional_generic_jet_scalar_curvature',Rg-target)
zero('einstein_density_boundary',R*Rg-(R*Rh+Xj/(2*R)-R*TrJJ/4-2*boxrho))

out={"status":"passed","arithmetic":"exact symbolic","sympy_version":s.__version__,"check_count":len(checks),"checks":checks}
(Path(__file__).resolve().parents[1]/'evidence'/'variation_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
