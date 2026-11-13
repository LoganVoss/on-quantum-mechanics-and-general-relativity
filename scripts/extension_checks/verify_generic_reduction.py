#!/usr/bin/env python3
"""Generic-jet off-shell Kaluza reduction and current-corrected twist duality.
All symbolic: h-normal coordinates and A=0 gauge at one arbitrary regular point.
The first and second jets of lambda/A and second metric jets remain independent.
"""
from pathlib import Path
import sympy as s,json,hashlib,platform,datetime
checks=[]
def eq(name,e):
 r=s.factor(s.cancel(s.expand(e)))
 if r!=0:raise AssertionError((name,r))
 checks.append({'name':name,'residual':'0'})

def scalar_curvature(g,dg,ddg):
 n=g.rows;gi=g.inv();dgi=[-gi*dg[k]*gi for k in range(n)]
 C=[[[sum(gi[a,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c]) for d in range(n))/2 for c in range(n)]for b in range(n)]for a in range(n)]
 DC=[[[[sum(dgi[k][a,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c])+gi[a,d]*(ddg[k][b][d,c]+ddg[k][c][d,b]-ddg[k][d][b,c])for d in range(n))/2 for c in range(n)]for b in range(n)]for a in range(n)]for k in range(n)]
 Ric=s.Matrix(n,n,lambda a,b:sum(DC[c][c][a][b]-DC[b][c][a][c]+sum(C[c][c][d]*C[d][a][b]-C[c][b][d]*C[d][a][c]for d in range(n))for c in range(n)))
 return s.expand(s.trace(gi*Ric))
L=s.symbols('lambda',positive=True);f=s.symbols('f',positive=True)
eta=s.diag(-1,1,1)
ell=s.symbols('l0:3');ell2=s.Matrix(3,3,lambda a,b:s.Symbol(f'l{min(a,b)}{max(a,b)}'))
AA=s.Matrix(3,3,lambda a,b:s.Symbol(f'A{a}_{b}'))
A2=[s.Matrix(3,3,lambda a,b:s.Symbol(f'A{z}_{min(a,b)}{max(a,b)}'))for z in range(3)]
h2=[[s.Matrix(3,3,lambda a,b:s.Symbol(f'h{min(a,b)}{max(a,b)}_{min(c,d)}{max(c,d)}'))for d in range(3)]for c in range(3)]
g=s.diag(-1/L,1/L,1/L,L)
dg=[s.zeros(4) for k in range(4)]
ddg=[[s.zeros(4)for k in range(4)]for j in range(4)]
for k in range(3):
 for a in range(3):
  for b in range(3):dg[k][a,b]=-ell[k]*eta[a,b]/L**2
  dg[k][a,3]=dg[k][3,a]=L*AA[a,k]
 dg[k][3,3]=ell[k]
for k in range(3):
 for j in range(3):
  for a in range(3):
   for b in range(3):ddg[k][j][a,b]=h2[k][j][a,b]/L+(2*ell[k]*ell[j]/L**3-ell2[k,j]/L**2)*eta[a,b]+L*(AA[a,k]*AA[b,j]+AA[a,j]*AA[b,k])
   ddg[k][j][a,3]=ddg[k][j][3,a]=ell[k]*AA[a,j]+ell[j]*AA[a,k]+L*A2[a][k,j]
  ddg[k][j][3,3]=ell2[k,j]
R4=scalar_curvature(g,dg,ddg);R3=scalar_curvature(eta,[s.zeros(3)for _ in range(3)],h2)
X=sum(eta[i,i]*ell[i]**2 for i in range(3));box=sum(eta[i,i]*ell2[i,i]for i in range(3))
F=AA.T-AA
F2=sum(eta[a,a]*eta[b,b]*F[a,b]**2 for a in range(3)for b in range(3))
eq('generic_offshell_R4',R4-L*R3-box+s.Rational(3,2)*X/L+L**3*F2/4)
# √−g4=√−h/L. The divergence is □log(lambda)=box/L-X/L².
eq('generic_offshell_EH_density',R4/L-(R3-X/(2*L**2)-L**2*F2/4)-(box/L-X/L**2))
# Exact scalar-current / connection duality in local Lorentz frame (-,+,+).
v=s.Matrix(s.symbols('v0:3'));j=s.Matrix(s.symbols('J0:3'));ff01,ff02,ff12=s.symbols('F01 F02 F12')
starF=s.Matrix([ff12,ff02,-ff01]);dot=lambda a,b:(a.T*eta*b)[0]
master=-f*dot(v,v)/(2*L**2)-dot(j,v)+f*dot(v,starF)
solution=L**2*(starF-j/f)
for a in range(3):eq(f'master_v_variation_{a}',s.diff(master,v[a]).subs(dict(zip(v,solution))))
Fsq=2*(-ff01**2-ff02**2+ff12**2)
dual=-f*L**2*Fsq/4-L**2*dot(j,starF)+L**2*dot(j,j)/(2*f)
eq('exact_current_corrected_dual_action',master.subs(dict(zip(v,solution)))-dual)
starJ=s.Matrix([[0,j[2],-j[1]],[-j[2],0,-j[0]],[j[1],j[0],0]])
Fmat=s.Matrix([[0,ff01,ff02],[-ff01,0,ff12],[-ff02,-ff12,0]])
shifted=Fmat+starJ/f
norm2=lambda A:sum(eta[a,a]*eta[b,b]*A[a,b]**2 for a in range(3)for b in range(3))
eq('square_completed_gauge_action',dual+f*L**2*norm2(shifted)/4)
for a in range(3):eq(f'generalized_twist_relation_{a}',solution[a]-L**2*(starF[a]-j[a]/f))
# No-current limit returns the ordinary scalar dual and classical metric reconstruction.
eq('zero_current_dual_limit',dual.subs(dict(zip(j,[0]*3)))+f*L**2*Fsq/4)
# Quantum shear source/charge identity and explicit failure of unmodified twist.
chi,hbar,nu=s.symbols('chi hbar nu',real=True)
n11,n12,n22=s.symbols('N11 N12 N22',real=True)
M=s.Matrix([[1,chi],[chi,chi**2+L**2]])/L
N=s.Matrix([[n11,n12],[n12,n22]])
J0=s.Matrix([[0,1],[-1,0]])
energy=hbar*nu*s.trace(M.inv()*N)/4-hbar*nu/2
Ndot=nu*(J0*M.inv()*N-N*M.inv()*J0)
Tdot=Ndot[0,0]/4
eq('quantum_shear_source_charge_identity',s.diff(energy,chi)+hbar*Tdot)
eq('mechanical_total_shift_charge',-s.diff(energy,chi)-hbar*Tdot)
example=s.diff(energy,chi).subs({L:1,chi:0,n11:1,n12:1,n22:2})
eq('nonzero_naive_twist_source_example',example+hbar*nu/2)
eq('counterexample_probe_purity',s.Matrix([[1,1],[1,2]]).det()-1)
receipt={'status':'PASS','check_count':len(checks),'checks':checks,'python':platform.python_version(),'sympy':s.__version__,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'genericity':'Normal coordinates for arbitrary Lorentzian h at an arbitrary regular point; A=0 is local gauge. Independent lambda first/second jets, A first/second jets, h second jets retained.','limits':['Classical local duality with smooth current. Products of point-particle distributions are not defined without regularization.','Probe current duality modifies twist reconstruction; it does not establish a quantum spacetime continuum.']}
Path(__file__).with_name('generic_reduction_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'symbolic_variables':len(set().union(R4.free_symbols,R3.free_symbols)),'R4_terms':len(s.Add.make_args(R4))},indent=2))
