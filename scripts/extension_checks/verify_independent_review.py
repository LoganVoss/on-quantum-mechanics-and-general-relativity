"""Bounded independent checks of extension proposals; no proposed verifier imported."""
from pathlib import Path
import hashlib,json,platform
import sympy as s
OUT=Path(__file__).resolve().parent
checks=[]
def ck(name,expression):
 value=s.simplify(expression)
 assert value==0,(name,value)
 checks.append({'name':name,'exact_residual':str(value)})

# 1. Quadratic selection: solve isotropy, then one positive Cholesky frame.
a,b,c=s.symbols('a b c',real=True)
J=s.Matrix([[0,1],[-1,0]])
K0=s.Matrix([[a,b],[b,c]])
iso=J.T*K0*J-K0
sol=s.solve(list(iso),[b,c],dict=True)[0]
ck('isotropy_offdiagonal',sol[b]);ck('isotropy_common_diagonal',sol[c]-a)
u=s.symbols('u',real=True);v=s.symbols('v',positive=True)
A=s.Matrix([[1/s.sqrt(v),0],[u/s.sqrt(v),s.sqrt(v)]])
M=A*A.T
ck('calibration_frame_det',A.det()-1)
K=A.inv().T*(a*s.eye(2))*A.inv()
for i in range(2):
 for j in range(2):ck(f'selected_quadratic_{i}{j}',K[i,j]-a*M.inv()[i,j])
ck('gap_determinant',K.det()-a*a)

# 2. Ground-band compression via moments of logarithmic wavefunction derivatives.
# No differentiation of a full chi*psi wavefunction is used here.
x=s.symbols('x',real=True)
cu,cv,cuu,cvv,C=s.symbols('cu cv cuu cvv C',complex=True)
lu=s.I*x*x/2;lv=1/(4*v)-x*x/2
moments={0:s.Integer(1),2:1/(2*v),4:3/(4*v*v)}
def mean(poly):
 return s.simplify(sum(coef*moments[power[0]] for power,coef in s.Poly(s.expand(poly),x).terms()))
lap=-v*v*(cuu+cvv+2*cu*lu+2*cv*lv+C*(lu*lu+lv*lv+s.diff(lv,v)))
projected=mean(lap)
expected=-v*v*(cuu+cvv)-s.I*v*cu/2+5*C/16
ck('projected_operator_independent_moments',projected-expected)
D=v*(cv-s.I*cu)+C/4
off=lap-projected
ck('offband_coefficient',off-v*D*(x*x-1/(2*v)))
ck('offband_mean_zero',mean(off))
ck('offband_norm_prefactor',mean(v*v*(x*x-1/(2*v))**2)-s.Rational(1,2))
# Formal adjoint derived with density v^-2: (v ∂v)†=−v∂v+1.
chi=s.Function('chi')(u,v)
Dchi=v*(s.diff(chi,v)-s.I*s.diff(chi,u))+chi/4
DD=-v*s.diff(Dchi,v)-s.I*v*s.diff(Dchi,u)+5*Dchi/4
ck('projected_operator_factorization',DD-expected.subs({C:chi,cu:s.diff(chi,u),cv:s.diff(chi,v),cuu:s.diff(chi,u,2),cvv:s.diff(chi,v,2)}))
hbar,I,E,t=s.symbols('hbar I E t',positive=True)
kappa=hbar*hbar/(2*I)
ck('leakage_Taylor_coefficient',t*t/(hbar*hbar)*(kappa*E/2)-E*t*t/(4*I))

# 3. Helical quotient using warped-product curvature of 2D conformal base + circle.
r,O=s.symbols('r Omega',positive=True)
lam=1+O*O*r*r
phi=s.log(lam)/2
Rbase=-2*s.diff(phi,r,2)/lam
Rtt=-lam*Rbase/2+s.diff(phi,r)/r
Rrr=lam*Rbase/2+s.diff(phi,r)/r
ck('helical_Rtt_warped_derivation',Rtt-2*O*O/lam**2)
ck('helical_Rrr_warped_derivation',Rrr-2*O**4*r*r/lam**2)
# Hessian contribution in R_xx is -r Box_base(r)=0.
boxlam=s.diff(r*s.diff(lam,r),r)/(lam*r)
lambda_grad=s.diff(lam,r)**2/lam;twist_grad=-(2*O)**2/lam
ck('helical_target_norm_equation',boxlam-(lambda_grad-twist_grad)/lam)
connection=O*r*r/lam
ck('helical_twist_from_connection',lam**2*s.diff(connection,r)/r-2*O)
f,w,pot=s.symbols('f w pot',real=True)
X=(-4*O*O+4*O**4*r*r)/lam**3
R3=(-Rtt+Rrr)/lam
Ett=f*(Rtt+lam*R3/2)-w*(4*O*O/lam**2+lam*X/2)/2+pot*lam/2
Err=f*(Rrr-lam*R3/2)-w*(4*O**4*r*r/lam**2-lam*X/2)/2-pot*lam/2
ck('helical_weight_inverse',lam*(Ett+Err)/(2*O*O)-(f-w))
ck('helical_potential_inverse',(Ett-Err)/lam-pot)

# 4. Lorentzian first-order duality. Verify probe-current variation as well as v.
L=s.symbols('lambda',positive=True);f=s.symbols('f',positive=True)
j0,j1,j2,F01,F02,F12=s.symbols('j0 j1 j2 F01 F02 F12',real=True)
j=s.Matrix([j0,j1,j2]);starF=s.Matrix([F12,F02,-F01]);eta=s.diag(-1,1,1)
q=lambda x,y:(x.T*eta*y)[0]
vv=L*L*(starF-j/f)
master_at=-f*q(vv,vv)/(2*L*L)-q(j,vv)+f*q(vv,starF)
F2=2*(-F01*F01-F02*F02+F12*F12)
dual=-f*L*L*F2/4-L*L*q(j,starF)+L*L*q(j,j)/(2*f)
ck('current_dual_action',master_at-dual)
for i in range(3):ck(f'current_response_preserved_{i}',s.diff(dual,j[i])+eta[i,i]*vv[i])
missing=dual-L*L*q(j,j)/(2*f)
# A concrete nonzero J proves dropping contact loses the matter equation.
contact_error=s.diff(missing,j0)+eta[0,0]*vv[0]
ck('contact_omission_error',contact_error-L*L*j0/f)

# 5. Independent raw Ricci-squared action variation in charged electrovac.
# Build background connection plus first variation directly from metric arrays.
r,theta=s.symbols('r theta',positive=True);T,P=s.symbols('T P',real=True)
coords=[T,r,theta,P]
ff=1-2/r+1/(4*r*r)
g=s.diag(-ff,1/ff,r*r,r*r*s.sin(theta)**2);gi=g.inv()
qphi=s.Function('eta')(r)
h=s.diag(-2*ff*qphi,0,0,0);dgi=-gi*h*gi
Gamma=[[[s.simplify(sum(gi[a,d]*(s.diff(g[d,c],coords[b])+s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d])) for d in range(4))/2) for c in range(4)]for b in range(4)]for a in range(4)]
dGamma=[[[s.simplify(sum(dgi[a,d]*(s.diff(g[d,c],coords[b])+s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d]))+gi[a,d]*(s.diff(h[d,c],coords[b])+s.diff(h[d,b],coords[c])-s.diff(h[b,c],coords[d]))for d in range(4))/2)for c in range(4)]for b in range(4)]for a in range(4)]
Ric=s.Matrix(4,4,lambda a,b:s.simplify(sum(s.diff(Gamma[k][a][b],coords[k])-s.diff(Gamma[k][a][k],coords[b])+sum(Gamma[k][k][l]*Gamma[l][a][b]-Gamma[k][b][l]*Gamma[l][a][k]for l in range(4))for k in range(4))))
dRic=s.Matrix(4,4,lambda a,b:s.simplify(sum(s.diff(dGamma[k][a][b],coords[k])-s.diff(dGamma[k][a][k],coords[b])+sum(dGamma[k][k][l]*Gamma[l][a][b]+Gamma[k][k][l]*dGamma[l][a][b]-dGamma[k][b][l]*Gamma[l][a][k]-Gamma[k][b][l]*dGamma[l][a][k]for l in range(4))for k in range(4))))
ck('RN_scalar_curvature',s.trace(gi*Ric))
Ric2=s.trace(gi*Ric*gi*Ric)
dRic2=2*s.trace(gi*dRic*gi*Ric)+2*s.trace(dgi*Ric*gi*Ric)
# Divide out sin(theta); volume variation is eta times volume.
ddensity=s.simplify(r*r*(qphi*Ric2+dRic2))
h0,h1,h2=s.symbols('h0 h1 h2')
ddens=s.expand(ddensity).subs({s.diff(qphi,r,2):h2,s.diff(qphi,r):h1,qphi:h0})
A0=s.diff(ddens,h0);A1=s.diff(ddens,h1);A2=s.diff(ddens,h2)
EL=s.simplify(A0-s.diff(A1,r)+s.diff(A2,r,2))
# δg^{tt}=2 eta/f, so δS=-2∫r² H^t_t eta dr.
Htt=s.factor(-EL/(2*r*r))
ck('RN_independent_action_variation',Htt+3*(4*r*r-8*r+1)/(4*r**8))
ck('RN_regular_point_response',Htt.subs(r,3)+s.Rational(13,8748))
# Dust trace from an independent Weyl variation: traces H_R²=6BoxR,H_Ric²=2BoxR.
t=s.symbols('t',positive=True);scale=t**s.Rational(2,3)
R=6*(s.diff(scale,t,2)/scale+(s.diff(scale,t)/scale)**2)
boxR=-s.diff(R,t,2)-3*s.diff(scale,t)/scale*s.diff(R,t)
ck('dust_R_from_Hubble',R-4/(3*t*t));ck('dust_BoxR_from_Hubble',boxR+8/(3*t**4))
alpha,beta=s.symbols('alpha beta')
response=s.Matrix([[(6*boxR).subs(t,1),(2*boxR).subs(t,1)],[0,Htt.subs(r,3)]])
ck('sourced_two_channel_rank',response.det()-s.Rational(52,2187))

sources=[
 'work/extension_joint/verify_projection.py','work/extension_joint/verify_rn_variation_independent.py',
 'work/extension_symmetry/verify_one_killing.py','work/extension_symmetry/verify_generic_reduction.py',
 'work/extension_symmetry/FROZEN_ONE_KILLING_FINDINGS.md',
 'work/extension_curvature/FROZEN_CURVATURE_FINDINGS.md','work/extension_curvature/verify_sourced_calibrations.py',
 'work/extension_dynamics/verify_dynamical_extension.py','work/extension_dynamics/DYNAMICS_FROZEN.md']
report={'status':'pass','python':platform.python_version(),'sympy':s.__version__,'exact_check_count':len(checks),'checks':checks,'RN_lapse_from_raw_action':str(Htt),'source_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in sources},'reviewer_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Independent exact rederivations of selected integration points only. Does not reproduce the whole proposed verification suite or finite-regulator evolution.'}
(OUT/'receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'pass','exact_checks':len(checks),'RN_Htt':str(Htt)},indent=2))
