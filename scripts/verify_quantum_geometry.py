#!/usr/bin/env python3
"""Independent, bounded exact and quadrature checks of Gaussian target corollaries.
Only trusted dependencies are imported. The original verification scripts are not
imported. Outputs are scratch evidence, with no empirical or novelty claim.
"""
from pathlib import Path
import argparse, hashlib, json, platform, math
import sympy as s
import scipy
from scipy.integrate import quad

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent, help='Directory for the JSON execution receipt')
args = parser.parse_args()
OUT = args.output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
checks=[]
def eq(name, expr):
    residual=s.simplify(expr)
    if residual != 0:
        raise AssertionError((name, residual))
    checks.append({'name':name,'status':'pass','exact_residual':'0'})

u,U=s.symbols('u U', real=True)
v,V=s.symbols('v V', positive=True)
x=s.symbols('x', real=True)
I=s.I
psi=(v/s.pi)**s.Rational(1,4)*s.exp((I*u-v)*x*x/2)
prob=s.sqrt(v/s.pi)*s.exp(-v*x*x)
moments={j:s.integrate(x**j*prob,(x,-s.oo,s.oo)) for j in [0,2,4]}
eq('normalization',moments[0]-1)
eq('second_moment',moments[2]-1/(2*v))
eq('fourth_moment',moments[4]-3/(4*v*v))
def expectation(poly):
    poly=s.Poly(s.expand(poly), x)
    return s.simplify(sum(c*moments[int(p[0])] for p,c in poly.terms()))
logd=[s.simplify(s.diff(psi,p)/psi) for p in (u,v)]
mean=[expectation(d) for d in logd]
Q=s.Matrix(2,2,lambda a,b:expectation(s.conjugate(logd[a])*logd[b])-s.conjugate(mean[a])*mean[b])
Qtarget=s.Matrix([[1,I],[-I,1]])/(8*v*v)
for a in range(2):
 for b in range(2): eq(f'QGT_{a}{b}',Q[a,b]-Qtarget[a,b])
A=s.Matrix([I*m for m in mean])
eq('Berry_connection_u',A[0]+1/(4*v))
eq('Berry_connection_v',A[1])
B=s.diff(A[1],u)-s.diff(A[0],v)
eq('Berry_curvature_is_minus_quarter_area',B+1/(4*v*v))
M=s.Matrix([[1,u],[u,u*u+v*v]])/v
N=s.Matrix([[1,U],[U,U*U+V*V]])/V
eq('shape_determinant',M.det()-1)
metric=s.Matrix(2,2,lambda a,b:s.trace(M.inv()*s.diff(M,(u,v)[a])*M.inv()*s.diff(M,(u,v)[b]))/2)
for a in range(2):
 for b in range(2): eq(f'shape_metric_twice_QFI_{a}{b}',metric[a,b]-8*s.re(Q[a,b]))
coshd=1+((u-U)**2+(v-V)**2)/(2*v*V)
eq('relative_trace_distance',s.trace(M.inv()*N)/2-coshd)
# The Gaussian integral gives |overlap|^4 = 4vV/((v+V)^2+(u-U)^2).
fidelity_squared=4*v*V/((v+V)**2+(u-U)**2)
eq('finite_fidelity_hyperbolic_identity',fidelity_squared-2/(coshd+1))
eq('finite_fidelity_covariance_identity',fidelity_squared-1/((M+N)/2).det())
# Target coordinate change: P=-log(v), Q=u; Ω=e^P dP∧dQ = du∧dv/v².
eq('odd_action_Berry_coefficient',2/(v*v)+8*B)
# Hyperbolic rectangle [u0,u1] x [v0,v1] fixes orientation and Berry sign.
u0,u1=s.symbols('u0 u1',real=True)
v0,v1=s.symbols('v0 v1',positive=True)
phase_bottom_top=-(u1-u0)/(4*v0)+(u1-u0)/(4*v1)
area=(u1-u0)*(1/v0-1/v1)
eq('Berry_Stokes_rectangle',phase_bottom_top+area/4)
# Fundamental bounds are finite algebra, separate from analytic integration.
rho=s.symbols('rho',positive=True)
f2,f1,uc,wc,vc=s.symbols('f2 f1 uc wc vc',real=True)
t,r=s.symbols('t r',positive=True)
Ett=-f2*t*t+uc*(t*t+r*r)/2-wc*(t*t+r*r)/(4*rho*rho)+vc/2
Err=-f2*r*r+uc*(t*t+r*r)/2-wc*(t*t+r*r)/(4*rho*rho)-vc/2
Etr=-rho*f2-f1+rho*uc+wc/(2*rho)
Aplus=s.simplify((Ett-Err).subs({t:2*s.sqrt(rho),r:s.sqrt(rho)/2}))
Aminus=s.simplify((Ett-Err).subs({t:s.sqrt(rho)/2,r:2*s.sqrt(rho)}))
eq('near_selector_V_recovery',(Aplus+Aminus)/2-vc)
eq('near_selector_F2_recovery',(Aminus-Aplus)*s.Rational(2,15)/rho-f2)
D0=s.simplify(((Ett+Err)/2).subs({t:s.sqrt(rho),r:s.sqrt(rho)}))
eq('near_selector_W_recovery',Etr-D0-(wc/rho-f1))
eq('near_selector_U_recovery',Etr+D0+2*rho*f2-(2*rho*uc-f1))
sample1={t:2*s.sqrt(rho),r:s.sqrt(rho)/2}
sample2={t:s.sqrt(rho)/2,r:2*s.sqrt(rho)}
e=[s.simplify(Ett.subs(sample1)),s.simplify(Err.subs(sample1)),s.simplify(Ett.subs(sample2)),s.simplify(Err.subs(sample2))]
eq('boost_pair_average_identity',s.Rational(2,17)*sum(e)-D0)
eq('five_residual_W_recovery',Etr-s.Rational(2,17)*sum(e)-(wc/rho-f1))
eq('five_residual_U_recovery',Etr+(-38*e[0]+98*e[1]+98*e[2]-38*e[3])/255-(2*rho*uc-f1))
# Each sharp pointwise algebraic constant has an exact feasible witness.
eps=s.symbols('eps',positive=True)
for name, signs, cross, expected in [
 ('V',(1,-1,1,-1),0,2*eps),
 ('rho_F2',(-1,1,1,-1),0,8*eps/15),
 ('W_over_rho_minus_F1',(1,1,1,1),-1,-25*eps/17),
 ('2rho_U_minus_F1',(-1,1,1,-1),1,31*eps/15)]:
 vals=[sign*eps for sign in signs]
 dd=s.Rational(2,17)*sum(vals)
 ff=s.Rational(2,15)*(-vals[0]+vals[1]+vals[2]-vals[3])/rho
 vv=(vals[0]-vals[1]+vals[2]-vals[3])/2
 ww=rho*(cross*eps-dd)
 uu=(cross*eps+dd+2*rho*ff)/(2*rho)
 witness={f1:0,f2:ff,uc:uu,wc:ww,vc:vv}
 for j in range(4): eq(f'sharp_{name}_diagonal_{j}',e[j].subs(witness)-vals[j])
 eq(f'sharp_{name}_cross',Etr.subs(witness)-cross*eps)
 target={'V':vc,'rho_F2':rho*f2,'W_over_rho_minus_F1':wc/rho-f1,'2rho_U_minus_F1':2*rho*uc-f1}[name]
 eq(f'sharp_{name}_bound',target.subs(witness)-expected)

r0=s.symbols('r0',positive=True)
H=rho*s.log(rho/r0)-rho+r0
eq('integrated_robustness_kernel_second_derivative',s.diff(H,rho,2)-1/rho)
eq('integrated_robustness_kernel_basepoint',H.subs(rho,r0))
eq('integrated_robustness_kernel_base_derivative',s.diff(H,rho).subs(rho,r0))

# Adversarial nonsaturating state: |1> and vacuum have the same normalized
# covariance shape, but are orthogonal. This prevents a universal-state claim.
vac=s.pi**s.Rational(-1,4)*s.exp(-x*x/2)
exc=s.sqrt(2)*x*vac
eq('negative_control_excited_normalization',s.integrate(exc*exc,(x,-s.oo,s.oo))-1)
eq('negative_control_excited_overlap',s.integrate(vac*exc,(x,-s.oo,s.oo)))
eq('negative_control_excited_Q_variance',s.integrate(x*x*exc*exc,(x,-s.oo,s.oo))-s.Rational(3,2))
eq('negative_control_excited_P_variance',s.integrate(s.diff(exc,x)**2,(x,-s.oo,s.oo))-s.Rational(3,2))

# Independent adaptive quadrature of actual wavefunctions, finite list, no sweep.
cases=[((0.,1.),(0.,1.)),((0.,1.),(0.,4.)),((-1.,.7),(1.3,2.1)),((3.,.4),(-2.,1.6)),((.3,2.),(.3001,2.0002))]
numerics=[]
for first,second in cases:
 a,b=first;c,d=second
 norm=(b*d)**.25/math.sqrt(math.pi)
 decay=(b+d)/2; osc=(c-a)/2
 re,er=quad(lambda xx:norm*math.exp(-decay*xx*xx)*math.cos(osc*xx*xx),-math.inf,math.inf,epsabs=1e-12,epsrel=1e-12,limit=200)
 im,ei=quad(lambda xx:norm*math.exp(-decay*xx*xx)*math.sin(osc*xx*xx),-math.inf,math.inf,epsabs=1e-12,epsrel=1e-12,limit=200)
 observed=re*re+im*im
 dh=math.acosh(max(1.,1+((a-c)**2+(b-d)**2)/(2*b*d)))
 prediction=1/math.cosh(dh/2)
 error=abs(observed-prediction)
 assert error<2e-11,(first,second,error)
 numerics.append({'first':first,'second':second,'squared_fidelity_quadrature':observed,'sech_distance_prediction':prediction,'absolute_error':error,'quad_reported_integral_error':er+ei})

receipt={'schema':'independent-quantum-geometry-checks-v1','status':'pass','python':platform.python_version(),'sympy':s.__version__,'scipy':scipy.__version__,'scope':'Exact symbolic checks plus five independent wavefunction quadratures; analytic derivations separate; not Lean proof or empirical observation.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_checks':checks,'quadrature_checks':numerics,'QGT':str(Q),'Berry_A':str(A),'Berry_F_uv':str(B),'exact_check_count':len(checks),'quadrature_case_count':len(cases),'mixed_state_negative_control':{'states':'thermal states νI and μI with ν!=μ and ν,μ>1/2','normalized_shape':'I for both','conclusion':'shape map loses purity: fidelity-distance formula cannot cover mixed states'}}
(OUT/'quantum_geometry_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'pass','exact_checks':len(checks),'quadrature_cases':len(cases),'max_error':max(n['absolute_error'] for n in numerics)},indent=2))
