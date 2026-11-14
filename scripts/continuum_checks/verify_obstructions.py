#!/usr/bin/env python3
"""Independent bounded controls on proposed quantum-cell/fluid limits.

No repository verifier is imported. Results are scratch research evidence.
"""
from pathlib import Path
import hashlib,json,math,platform,time
import sympy as s
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.stats import binom

OUT=Path(__file__).resolve().parent
started=time.monotonic();checks=[]
def exact(name,e):
    z=s.simplify(s.expand(e))
    assert z==0,(name,z)
    checks.append({'name':name,'residual':'0'})

# Conditional Gaussian evolution under the actual selected positive quadratic.
R=s.symbols('R',positive=True)
c,z=s.symbols('c z',real=True)
J=s.Matrix([[0,1],[-1,0]])
Mp=s.diag(R,1/R);Mm=s.diag(1/R,R)
Sp=c*s.eye(2)+z*J*Mp.inv();Sm=c*s.eye(2)+z*J*Mm.inv()
Np=Sp*Sp.T;Nm=Sm*Sm.T
avg=s.simplify((Np+Nm)/2)
v=c*c+z*z*(R*R+1/(R*R))/2
for i in range(2):
 for j in range(2):exact(f'conditional_mean_covariance_{i}{j}',avg[i,j]-(v if i==j else 0))
exact('conditional_covariance_determinant_plus',Np.det()-(c*c+z*z)**2)
exact('conditional_covariance_determinant_minus',Nm.det()-(c*c+z*z)**2)
exact('average_covariance_determinant',avg.det()-v*v)
# On c²+z²=1: squared fidelity =1/[1+2 sinh²(r) sin²(theta)].
exact('conditional_overlap_denominator',v.subs(c*c,1-z*z)-(1+(R-1/R)**2*z*z/2))
F=s.Rational(8,17)
purity=(1+F)/2
exact('quarter_period_exact_purity',purity-s.Rational(25,34))
exact('quarter_period_exact_linear_entropy',1-purity-s.Rational(9,34))
rr,tt,om=s.symbols('r t omega',real=True)
linear_entropy=s.sinh(rr)**2*s.sin(om*tt)**2/(1+2*s.sinh(rr)**2*s.sin(om*tt)**2)
exact('initial_purity_loss_coefficient',s.diff(linear_entropy,tt,2).subs(tt,0)/2-om**2*s.sinh(rr)**2)

# Direct finite-Fock unitary computation; Q²/P² are projected exactly, not formed
# by squaring truncated Q/P matrices.
def branch_hamiltonian(cutoff,positive):
    n=np.arange(cutoff,dtype=float)
    a2=np.diag(np.sqrt(np.arange(1,cutoff-1)*np.arange(2,cutoff)),2)
    kq,kp=(.5,2.) if positive else (2.,.5)
    return (kq+kp)*np.diag(2*n+1)/4+(kq-kp)*(a2+a2.T)/4-np.eye(cutoff)/2
numeric=[]
for cutoff in (32,48,64):
    Hplus=branch_hamiltonian(cutoff,True);Hminus=branch_hamiltonian(cutoff,False)
    assert np.linalg.eigvalsh(Hplus).min()>-1e-12
    vacuum=np.eye(cutoff,dtype=complex)[:,0]
    states=[expm(-1j*H*math.pi/2)@vacuum for H in (Hplus,Hminus)]
    rho=(np.outer(states[0],states[0].conj())+np.outer(states[1],states[1].conj()))/2
    observed=float(np.trace(rho@rho).real)
    overlap=float(abs(np.vdot(states[0],states[1]))**2)
    error=abs(observed-25/34)
    numeric.append({'Fock_cutoff':cutoff,'time':math.pi/2,'purity':observed,
                    'branch_squared_overlap':overlap,'absolute_purity_error':error,
                    'trace_error':abs(float(np.trace(rho).real)-1),
                    'distance_to_nearest_pure_state':float(1-np.linalg.eigvalsh(rho).max())})
assert numeric[-1]['absolute_purity_error']<1e-9,numeric
assert numeric[-1]['branch_squared_overlap']<.5

# Hardy identity proving −Δ_H² >=1/4 on C_c^∞(H²).
vv=s.symbols('v',positive=True);f=s.Function('f')(vv)
hardy_remainder=(s.diff(f,vv)-f/(2*vv))**2-s.diff(f,vv)**2+f*f/(4*vv*vv)+s.diff(f*f/vv,vv)/2
exact('Hardy_identity_with_total_derivative',hardy_remainder)
hbar,grav,V,cell,N=s.symbols('hbar grav V cell N',positive=True)
raw=(V/cell)*hbar*hbar/(8*grav*cell)
scaled=(V/cell)*hbar*hbar/(8*N*grav*cell)/N
exact('raw_spatial_refinement_energy_floor',raw-hbar*hbar*V/(8*grav*cell**2))
exact('large_N_per_copy_energy_floor',scaled-hbar*hbar*V/(8*grav*N*N*cell**2))
hx=s.symbols('h',positive=True)
exact('two_spatial_dimensions_raw_h_minus_four',raw.subs(cell,hx**2)-hbar*hbar*V/(8*grav*hx**4))

# A relativistic two-stream stress cannot equal pressureless one-velocity stress.
speed=s.symbols('b',real=True);mass,density=s.symbols('mass density',positive=True)
gamma2=1/(1-speed*speed)
T=mass*density*gamma2*s.diag(1,speed*speed)
exact('two_stream_stress_determinant',T.det()-mass**2*density**2*speed**2/(1-speed*speed)**2)
u0,u1=s.symbols('u0 u1',real=True)
ud=s.Matrix([u0,u1]);Td=mass*density*ud*ud.T
exact('single_stream_dust_rank_one',Td.det())
exact('two_stream_finite_example_determinant',T.det().subs({speed:s.Rational(1,2),mass:1,density:1})-s.Rational(4,9))

# Exact smooth transport flow and its first caustic, on a flat test background.
label,t,b=s.symbols('label t b',real=True)
flow=label-t*b*s.tanh(label)
jac=s.diff(flow,label)
exact('transport_Jacobian',jac-(1-t*b/s.cosh(label)**2))
exact('first_caustic_at_label_zero',jac.subs({label:0,t:1/b}))

# Weak current convergence does not determine the quadratic contact interaction.
angle=s.symbols('angle',real=True)
j0,amp=s.symbols('j0 amp',real=True)
current=j0+amp*s.sin(angle)
exact('oscillatory_current_mean',s.integrate(current,(angle,0,2*s.pi))/(2*s.pi)-j0)
exact('oscillatory_current_contact_defect',s.integrate(current*current,(angle,0,2*s.pi))/(2*s.pi)-j0*j0-amp*amp/2)
eta,x1,x2=s.symbols('eta x1 x2',positive=True)
kernel=s.exp(-(x1*x1+x2*x2)/(2*eta*eta))/(2*s.pi*eta*eta)
kernel_norm=s.integrate(s.integrate(kernel*kernel,(x1,-s.oo,s.oo)),(x2,-s.oo,s.oo))
exact('two_dimensional_mollifier_squared_norm',kernel_norm-1/(4*s.pi*eta*eta))

# Relativistic mass averaging is nonlinear; the Brown internal-energy closure
# needs a separate collective scaling rather than a one-probe WKB assertion.
pp,ee=s.symbols('p e',positive=True)
energy_symbol=s.sqrt(pp*pp+ee*ee)
clock_symbol=s.diff(energy_symbol,ee)
exact('relativistic_proper_clock_derivative',clock_symbol-ee/s.sqrt(pp*pp+ee*ee))
exact('relativistic_convexity',s.diff(energy_symbol,ee,2)-pp*pp/(pp*pp+ee*ee)**s.Rational(3,2))
exact('relativistic_third_derivative',s.diff(energy_symbol,ee,3)+3*pp*pp*ee/(pp*pp+ee*ee)**s.Rational(5,2))
exact('curvature_bound_first_step',1/s.sqrt(pp*pp+ee*ee)-s.diff(energy_symbol,ee,2)-ee*ee/(pp*pp+ee*ee)**s.Rational(3,2))
exact('one_probe_Jensen_gap_squared',((s.sqrt(2)+s.sqrt(10))/2)**2-5-(s.sqrt(5)-2))
parcel=[]
for copies in (1,4,16,64,256):
    k=np.arange(copies+1)
    probabilities=binom.pmf(k,copies,.5)
    masses=1+2*k/copies
    E=float(np.dot(probabilities,np.sqrt(1+masses*masses)))
    clocks=masses/np.sqrt(1+masses*masses)
    mean_clock=float(np.dot(probabilities,clocks))
    energy_gap=E-math.sqrt(5)
    clock_bias=2/math.sqrt(5)-mean_clock
    clock_abs=float(np.dot(probabilities,abs(clocks-2/math.sqrt(5))))
    assert -1e-13<energy_gap<=1/(2*copies)+1e-13
    assert -1e-13<clock_bias<=3/(2*copies)+1e-13
    assert clock_abs<=1/math.sqrt(copies)+1e-13
    parcel.append({'copies':copies,'energy_Jensen_gap':energy_gap,'energy_bound':1/(2*copies),
                   'proper_clock_bias':clock_bias,'clock_bias_bound':3/(2*copies),
                   'mean_absolute_clock_fluctuation':clock_abs,'clock_fluctuation_bound':1/math.sqrt(copies)})

# Frozen provenance of the inspected regulator; the calculations import no code from it.
INSPECTED_REGULATOR_SHA256='25beeb75cd67f717479d10233637002ab05aad082786c7de8b4e3488e1bec32a'
report={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'scipy':scipy.__version__,
 'exact_check_count':len(checks),'checks':checks,'selected_coupling_purity_control':numeric,
 'relativistic_parcel_controls':parcel,
 'conditional_collective_mass_bounds':{'energy':'0<=E F(m0+A_N)-F(m0+mean h)<=Var(h)/(2 m0 N)',
 'clock_mean_absolute':'E|Fprime(m0+A_N)-Fprime(m0+mean h)|<=sqrt(Var(h))/(m0 sqrtN)',
 'clock_bias':'0<=Fprime(m0+mean h)-E Fprime(m0+A_N)<=3 Var(h)/(2 m0² N)',
 'domain':'Fixed classical momentum and geometry; nonnegative independent identical internal Hamiltonians, product preparation, m0>0 and finite variance. These are expectation bounds, not dynamical convergence.'},
 'continuum_purity':'25/34 at shape branch r=ln2 and t=pi/(2omega)',
 'raw_energy_floor':'hbar² V/(8 f h^(2d)); d=2 gives h^-4',
 'large_N_energy_floor_per_copy':'hbar² V/(8 f N² h^(2d))',
 'current_contact_negative_control':'J_n^0=j0+a sin(nx),j0>|a|, converges weakly but J_n.J_n has defect -a²/2',
 'mollified_current_variance_bound':'For independent weighted particles with finite E|a|²: integrated Euclidean variance <= E|a|²/(4*pi*N*eta²) in two spatial dimensions.',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'inspected_regulator_sha256':INSPECTED_REGULATOR_SHA256,
 'elapsed_seconds':time.monotonic()-started,
 'limits':['The frozen two-branch shape control tests failure of deterministic pure-state closure without concentration; it is not a no-go theorem for well-prepared limits.',
 'The Hardy bound concerns the unsubtracted nonnegative model; renormalization/counterterms are not excluded.',
 'The multistream test shows pressureless closure is extra structure; the original cell contains no particle transport coordinates.',
 'No continuum dynamics or quantum gravitational constraints are proved by these controls.']}
(OUT/'obstruction_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'purity_controls':numeric,'elapsed_seconds':report['elapsed_seconds']},indent=2))
