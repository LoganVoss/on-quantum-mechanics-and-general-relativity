#!/usr/bin/env python3
"""Exact scratch verification of the one-Killing helical calibration and sector map.
No public claims are generated here. All calculations use finite symbolic tensors.
"""
from pathlib import Path
import sympy as s, json, hashlib, platform, datetime
checks=[]
def equal(name,expr):
 r=s.simplify(expr)
 if r!=0: raise AssertionError((name,r))
 checks.append({'name':name,'residual':'0'})
def geometry(g,x):
 n=len(x);inv=s.simplify(g.inv())
 C=[[[s.simplify(sum(inv[a,d]*(s.diff(g[d,c],x[b])+s.diff(g[d,b],x[c])-s.diff(g[b,c],x[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
 Ric=s.Matrix(n,n,lambda a,b:s.simplify(sum(s.diff(C[c][a][b],x[c])-s.diff(C[c][a][c],x[b])+sum(C[c][c][d]*C[d][a][b]-C[c][b][d]*C[d][a][c] for d in range(n)) for c in range(n))))
 return inv,C,Ric
T,r,x,y,O=s.symbols('T r x y Omega',real=True)
la=1+O**2*r**2;om=2*O*T
h=s.diag(-la,la,r**2);hinv,C,Ric=geometry(h,[T,r,x])
S=s.Matrix(3,3,lambda a,b:(s.diff(la,[T,r,x][a])*s.diff(la,[T,r,x][b])+s.diff(om,[T,r,x][a])*s.diff(om,[T,r,x][b]))/la**2)
for a in range(3):
 for b in range(3):equal(f'helical_Ricci_{a}{b}',Ric[a,b]-S[a,b]/2)
dot=lambda f,g:s.simplify(sum(hinv[a,b]*s.diff(f,[T,r,x][a])*s.diff(g,[T,r,x][b]) for a in range(3) for b in range(3)))
box=lambda f:s.simplify(sum(s.diff(la*r*hinv[a,b]*s.diff(f,[T,r,x][b]),[T,r,x][a]) for a in range(3) for b in range(3))/(la*r))
equal('helical_lambda_wave_map',box(la)-(dot(la,la)-dot(om,om))/la)
equal('helical_omega_wave_map',box(om)-2*dot(la,om)/la)
A=O*r**2/la
equal('helical_twist',la**2*la*r*hinv[1,1]*hinv[2,2]*s.diff(A,r)-s.diff(om,T))
# Flat lift and ALL independent tensor components, not scalar curvature alone.
g=s.zeros(4)
for a in range(3):
 for b in range(3):g[a,b]=h[a,b]/la
avec=s.Matrix([0,0,A,1]);g += la*avec*avec.T
g_expected=s.Matrix([[-1,0,0,0],[0,1,0,0],[0,0,r*r,O*r*r],[0,0,O*r*r,la]])
for a in range(4):
 for b in range(4):equal(f'flat_lift_component_{a}{b}',g[a,b]-g_expected[a,b])
g=s.simplify(g);ginv,C4,Ric4=geometry(g,[T,r,x,y]);coords=[T,r,x,y]
for a in range(4):
 for b in range(4):
  for c in range(4):
   for d in range(4):
    riem=s.diff(C4[a][d][b],coords[c])-s.diff(C4[a][c][b],coords[d])+sum(C4[a][c][e]*C4[e][d][b]-C4[a][d][e]*C4[e][c][b] for e in range(4))
    equal(f'flat_Riemann_{a}{b}{c}{d}',riem)
# Full class with +V convention; all scalar equations already zero on chart.
f,w,V=s.symbols('f w V',real=True)
RicSc=s.simplify(s.trace(hinv*Ric));X=s.simplify(s.trace(hinv*S));Ein=s.simplify(Ric-h*RicSc/2);stress=s.simplify(S-h*X/2)
E=s.simplify(f*Ein-w*stress/2-V*h/2)
equal('metric_tt_response',E[0,0]-(O**2*(f-w)/la+V*la/2))
equal('metric_rr_response',E[1,1]-(O**2*(f-w)/la-V*la/2))
equal('invert_relative_weight',la*(E[0,0]+E[1,1])/(2*O**2)-(f-w))
equal('invert_potential',(E[0,0]-E[1,1])/la-V)
for a in range(3):
 for b in range(3):equal(f'selected_full_metric_{a}{b}',E[a,b].subs({w:f,V:0}))
equal('zero_pitch_blindness_weight',E[0,0].subs({O:0,V:0}))
# Quantum target dictionary: reinterpret upper-half-plane coords, no claim original M is unchanged.
l=s.symbols('lambda',positive=True);z=s.symbols('chi',real=True)
M=s.Matrix([[1,z],[z,z*z+l*l]])/l
equal('target_det',M.det()-1)
for a,p in enumerate([l,z]):
 for b,q in enumerate([l,z]):equal(f'new_target_metric_{a}{b}',s.trace(M.inv()*s.diff(M,p)*M.inv()*s.diff(M,q))/2-(1/l**2 if a==b else 0))
# Further cylindrical reduction, with generic functions, checks original equations.
R=s.symbols('R',positive=True)
psi=s.Function('psi')(T,R);chi=s.Function('chi')(T,R);gam=s.Function('gamma')(T,R)
hc=s.diag(-s.exp(gam),s.exp(gam),R**2)
hi,cc,rc=geometry(hc,[T,R,x])
src=s.Matrix(3,3,lambda a,b:s.diff(psi,[T,R,x][a])*s.diff(psi,[T,R,x][b])+s.exp(-2*psi)*s.diff(chi,[T,R,x][a])*s.diff(chi,[T,R,x][b]))
equal('cylindrical_gamma_T_constraint',2*R*(rc[0,1]-src[0,1]/2)-(s.diff(gam,T)-R*(s.diff(psi,T)*s.diff(psi,R)+s.exp(-2*psi)*s.diff(chi,T)*s.diff(chi,R))))
equal('cylindrical_gamma_R_constraint',R*((rc[0,0]-src[0,0]/2)+(rc[1,1]-src[1,1]/2))-(s.diff(gam,R)-R*(s.diff(psi,T)**2+s.diff(psi,R)**2+s.exp(-2*psi)*(s.diff(chi,T)**2+s.diff(chi,R)**2))/2))
boxc=lambda F:s.simplify(sum(s.diff(s.exp(gam)*R*hi[a,b]*s.diff(F,[T,R,x][b]),[T,R,x][a]) for a in range(3) for b in range(3))/(s.exp(gam)*R))
dotc=lambda F,G:s.simplify(sum(hi[a,b]*s.diff(F,[T,R,x][a])*s.diff(G,[T,R,x][b]) for a in range(3) for b in range(3)))
lc=s.exp(psi)
wave_l=boxc(lc)-(dotc(lc,lc)-dotc(chi,chi))/lc
wave_ch=boxc(chi)-2*dotc(lc,chi)/lc
expected_psi=s.diff(psi,T,2)-s.diff(psi,R,2)-s.diff(psi,R)/R+s.exp(-2*psi)*(s.diff(chi,T)**2-s.diff(chi,R)**2)
expected_chi=s.diff(chi,T,2)-s.diff(chi,R,2)-s.diff(chi,R)/R-2*(s.diff(psi,T)*s.diff(chi,T)-s.diff(psi,R)*s.diff(chi,R))
equal('cylindrical_psi_PDE',-s.exp(gam-psi)*wave_l-expected_psi)
equal('cylindrical_chi_PDE',-s.exp(gam)*wave_ch-expected_chi)
# Hodge component formula gives omega_T=e2psi A_R/R, omega_R=e2psi A_T/R.
AT,AR=s.symbols('A_T A_R')
equal('sector_twist_T',lc**2*s.exp(gam)*R*hi[1,1]*hi[2,2]*AR-s.exp(2*psi)*AR/R)
equal('sector_twist_R',-lc**2*s.exp(gam)*R*hi[0,0]*hi[2,2]*AT-s.exp(2*psi)*AT/R)
receipt={'status':'PASS','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'check_count':len(checks),'checks':checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact tensor/algebra checks for helical calibration and further cylindrical reduction. Written classification, dualization, and theorem arguments separate; no all-solution existence or quantum continuum claim.','parameters':'real Omega!=0,r>0 for nondegenerate calibration; all components checked symbolically before specialization','source_independence':'No original project verifier imported.'}
Path(__file__).with_name('one_killing_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'Ricci':str(Ric),'Ett':str(E[0,0]),'Err':str(E[1,1])},indent=2))
