#!/usr/bin/env python3
"""Bounded exact 4D dust + electrovac curvature-squared calibration checks."""
from pathlib import Path
import sympy as s
import json,hashlib,time,platform
started=time.monotonic();checks=[]
def eq(name,e):
 v=s.simplify(e)
 assert v==0,(name,v)
 checks.append({'name':name,'residual':'0'})
t,r,th,ph=s.symbols('t r theta phi',positive=True)
coords=[t,r,th,ph]
def connections(g):
 gi=g.inv();G=[[[0]*4 for _ in range(4)] for _ in range(4)]
 for a in range(4):
  for b in range(4):
   for c in range(4):
    G[a][b][c]=s.simplify(sum(gi[a,d]*(s.diff(g[d,c],coords[b])+s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d])) for d in range(4))/2)
 return gi,G

def ricci(G):
 return s.Matrix(4,4,lambda a,b:s.simplify(sum(s.diff(G[c][a][b],coords[c])-s.diff(G[c][a][c],coords[b])+sum(G[c][c][d]*G[d][a][b]-G[c][b][d]*G[d][a][c] for d in range(4)) for c in range(4))))
# Dust FLRW, regular patch t>0.
gd=s.diag(-1,t**s.Rational(4,3),t**s.Rational(4,3),t**s.Rational(4,3))
gdi,Gd=connections(gd);Rd=ricci(Gd);scalar_d=s.simplify(s.trace(gdi*Rd))
eq('dust_R_scalar',scalar_d-4/(3*t*t))
boxR=s.simplify(-s.diff(t*t*s.diff(scalar_d,t),t)/(t*t))
eq('dust_BoxR',boxR+8/(3*t**4))
Ein_d=Rd-gd*scalar_d/2
for a in range(4):
 for b in range(4):eq(f'dust_Einstein_component_{a}{b}',Ein_d[a,b]-(4/(3*t*t) if a==b==0 else 0))
eq('dust_conservation',s.diff(4/(3*t*t),t)+2/t*4/(3*t*t))
# One exact charged, asymptotically flat electrovac calibration (M=1,Q=1/2).
Q=s.Rational(1,2);f=1-2/r+Q**2/r**2
g=s.diag(-f,1/f,r*r,r*r*s.sin(th)**2);gi,G=connections(g);Ric=ricci(G);R=s.simplify(s.trace(gi*Ric))
eq('RN_R_scalar',R)
expected=s.diag(f*Q**2/r**4,-Q**2/(f*r**4),Q**2/r**2,Q**2*s.sin(th)**2/r**2)
for a in range(4):
 for b in range(4):eq(f'RN_Ricci_component_{a}{b}',Ric[a,b]-expected[a,b])
# F_tr=Q/r² with Maxwell action -1/4 F² and kappa=2 in chosen units.
F=s.zeros(4);F[0,1]=Q/r**2;F[1,0]=-F[0,1]
F2=s.simplify(sum(gi[a,a]*gi[b,b]*F[a,b]**2 for a in range(4) for b in range(4)))
T=F*gi*F.T-g*F2/4
for a in range(4):
 for b in range(4):eq(f'RN_Einstein_Maxwell_component_{a}{b}',Ric[a,b]-2*T[a,b])
for b in range(4):
 # Maxwell divergence density, sqrt(-g)=r²sin(theta).
 eq(f'RN_Maxwell_equation_{b}',sum(s.diff(r*r*s.sin(th)*gi[a,a]*gi[b,b]*F[a,b],coords[a]) for a in range(4)))
# Covariant derivative of Ricci, then tensor d'Alembertian.
C=[[[s.simplify(s.diff(Ric[b,c],coords[a])-sum(G[d][a][b]*Ric[d,c]+G[d][a][c]*Ric[b,d] for d in range(4))) for c in range(4)] for b in range(4)] for a in range(4)]
boxRic=s.zeros(4)
for b in range(4):
 for c in range(4):
  boxRic[b,c]=s.simplify(sum(gi[a,a]*(s.diff(C[a][b][c],coords[a])-sum(G[d][a][a]*C[d][b][c]+G[d][a][b]*C[a][d][c]+G[d][a][c]*C[a][b][d] for d in range(4))) for a in range(4)))
Ric2=s.simplify(s.trace(gi*Ric*gi*Ric));Rup=gi*Ric*gi
RiemRic=s.zeros(4)
for a in range(4):
 for b in range(4):
  terms=[]
  for c in range(4):
   # R_{a c b c}=g_aa R^a_{c b c} for diagonal metric.
   value=g[a,a]*(s.diff(G[a][c][c],coords[b])-s.diff(G[a][b][c],coords[c])+sum(G[a][b][d]*G[d][c][c]-G[a][c][d]*G[d][b][c] for d in range(4)))
   terms.append(value*Rup[c,c])
  RiemRic[a,b]=s.simplify(sum(terms))
# R=0, so H_(Ric²)=Box Ric+2Riem.Ric−1/2g Ric² =2B.
H2=s.simplify(boxRic+2*RiemRic-g*Ric2/2)
H2mixed=s.simplify(gi*H2)
eq('RN_H2_trace',s.trace(H2mixed))
# Direct covariant divergence of H2 must vanish as a diffeomorphism identity.
for b in range(4):
 div=sum(gi[a,a]*(s.diff(H2[a,b],coords[a])-sum(G[c][a][a]*H2[c,b]+G[c][a][b]*H2[a,c] for c in range(4))) for a in range(4))
 eq(f'RN_H2_divergence_{b}',div)
point={r:3,th:s.pi/2}
point_H2=[s.factor(H2mixed[a,a].subs(point)) for a in range(4)]
assert point_H2[0]!=0
# At r=3, the lapse is 13/36>0 and the point is outside outer horizon.
eq('RN_regular_lapse',f.subs(r,3)-s.Rational(13,36))
alpha,beta=s.symbols('alpha beta',real=True)
yD=(6*alpha+2*beta)*boxR.subs(t,1)
yR=beta*point_H2[0]
eq('nonlinear_residual_beta_inverse',-s.Rational(8748,13)*yR-beta)
eq('nonlinear_residual_alpha_inverse',-yD/16+s.Rational(2916,13)*yR-alpha)
response=s.Matrix([[-16,-s.Rational(16,3)],[0,-s.Rational(13,8748)]])
eq('nonlinear_residual_map_determinant',response.det()-s.Rational(52,2187))
epsD,epsR=s.symbols('epsD epsR',nonnegative=True)
for d in [-1,1]:
 for rr in [-1,1]:
  A=-d*epsD/16+s.Rational(2916,13)*rr*epsR
  B=-s.Rational(8748,13)*rr*epsR
  eq(f'sharp_corner_dust_{d}_{rr}',yD.subs({alpha:A,beta:B})-d*epsD)
  eq(f'sharp_corner_RN_{d}_{rr}',yR.subs({alpha:A,beta:B})-rr*epsR)
report={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'exact_check_count':len(checks),'checks':checks,'dust':{'metric':'diag(-1,t^(4/3),t^(4/3),t^(4/3))','R':str(scalar_d),'BoxR':str(boxR)},'electrovac':{'metric_f':str(f),'R':str(R),'H_Ricci_squared_mixed_diagonal':[str(s.factor(H2mixed[a,a])) for a in range(4)],'point':{'r':3,'theta':'pi/2'},'point_H2_mixed_diagonal':[str(x) for x in point_H2],'Bach_mixed_diagonal_at_point':[str(x/2) for x in point_H2],'matter':'Minimal Maxwell -F²/4, F_tr=1/(2r²), kappa=2 in selected geometric units.'},'calibration_response_matrix':str(response),'selection':'Unchanged calibrated dust FLRW forces 3alpha+beta=0; unchanged calibrated charged electrovac forces beta=0; hence alpha=beta=0 modulo constant Euler density. All variations are unrestricted4D. These additional source/background calibrations are hypotheses, not derived from the original flat-vacuum selection.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-started}
Path(__file__).with_name('sourced_calibration_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','exact_check_count','elapsed_seconds']}))
print(report['electrovac'])
