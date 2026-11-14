"""Independent bounded controls for the proposed controlled matter bridge.
No proposed verifier is imported; analytic proof review is recorded separately.
"""
from pathlib import Path
import hashlib,json,math,platform
import sympy as s
import numpy as np
from scipy.linalg import expm
from scipy.special import comb

OUT=Path(__file__).resolve().parent
checks=[]
def eq(name,expr):
    if isinstance(expr,s.MatrixBase):
        residual=expr.applyfunc(s.simplify)
        assert residual==s.zeros(*expr.shape),(name,residual)
    else:
        residual=s.simplify(expr)
        assert residual==0,(name,residual)
    checks.append({'name':name,'residual':'0'})

# Ordered telescoping identity; the deviation is adjacent to the state.
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
a,b,c=s.symbols('a b c',real=True)
eq('ordered_noncommuting_telescoping',X*Y*Z-a*b*c*s.eye(2)-X*Y*(Z-c*s.eye(2))-X*(Y-b*s.eye(2))*c-(X-a*s.eye(2))*b*c)

# Square-root constants via t=m²u; independent beta-integral evaluation.
m=s.symbols('m',positive=True)
eq('resolvent_integral_second_power',s.gamma(s.Rational(3,2))*s.gamma(s.Rational(1,2))/(s.pi*m*s.gamma(2))-1/(2*m))
eq('resolvent_integral_third_power',s.gamma(s.Rational(3,2))**2/(s.pi*m**3*s.gamma(3))-1/(8*m**3))

# Internal propagation-of-chaos Casimir in dimension3, rather than dimension2.
d=3;Id=s.eye(d);basis=[Id/s.sqrt(d)]
for i in range(d):
 for j in range(i+1,d):
  E=s.zeros(d);E[i,j]=1;Et=E.T
  basis.extend([(E+Et)/s.sqrt(2),-s.I*(E-Et)/s.sqrt(2)])
basis.extend([s.diag(1,-1,0)/s.sqrt(2),s.diag(1,1,-2)/s.sqrt(6)])
gram=s.Matrix(len(basis),len(basis),lambda i,j:s.trace(basis[i]*basis[j]))
eq('qutrit_HS_basis',gram-s.eye(9))
swap=s.zeros(9)
for i in range(3):
 for j in range(3):swap[3*i+j,3*j+i]=1
eq('qutrit_swap_completeness',sum((s.kronecker_product(B,B)for B in basis),s.zeros(9))-swap)
embed=s.zeros(9,6);col=0
for i in range(3):
 for j in range(i,3):
  if i==j:embed[3*i+j,col]=1
  else:embed[3*i+j,col]=embed[3*j+i,col]=1/s.sqrt(2)
  col+=1
As=[(s.kronecker_product(B,Id)+s.kronecker_product(Id,B))/2 for B in basis]
eq('qutrit_two_copy_Casimir',embed.H*sum((A*A for A in As),s.zeros(9))*embed-2*s.eye(6))
rho=s.diag(1,0,0);bs=[s.trace(rho*B)for B in basis]
variance=sum(((A-bi*s.eye(9))**2 for A,bi in zip(As,bs)),s.zeros(9))
bad=s.eye(9)-(s.kronecker_product(rho,Id)+s.kronecker_product(Id,rho))/2
eq('qutrit_variance_bad_particle_identity',embed.H*(variance-2*bad)*embed-s.eye(6))

# Proper time and the ADM shift have a fixed orientation.
L,e,p1,p2,b1,b2,g11,g12,g22=s.symbols('L e p1 p2 b1 b2 g11 g12 g22',real=True)
momentum=s.Matrix([p1,p2]);metric=s.Matrix([[g11,g12],[g12,g22]]);shift=s.Matrix([b1,b2])
energy=s.sqrt((momentum.T*metric*momentum)[0]+e*e)
H=L*energy-(shift.T*momentum)[0]
vel=s.Matrix([s.diff(H,p1),s.diff(H,p2)])
eq('ADM_clock_derivative',s.diff(H,e)-L*e/energy)
eq('ADM_worldline_Legendre_identity',(momentum.T*vel)[0]-H+e*L*e/energy)

# Independent full energy differentiation of the moving reciprocal parcel.
cg,pg,xx,yy,px,py,uu=s.symbols('cg pg xx yy px py uu',real=True)
vv,mass,weight=s.symbols('vv mass weight',positive=True)
chig=cg*s.sin(xx)
internal=((chig-uu)**2+(1-vv)**2)/(4*vv)
epsp=mass+internal
parcel=s.sqrt(px*px+py*py+epsp*epsp)
total=(cg*cg+pg*pg)/2+weight*parcel
clock=epsp/parcel
vars=[cg,pg,xx,yy,px,py,uu,vv]
flow=[pg,-cg-weight*clock*s.diff(internal,cg),px/parcel,py/parcel,
      -clock*s.diff(internal,xx),0,
      clock*(vv*vv-1-(uu-chig)**2),2*clock*vv*(chig-uu)]
eq('moving_reciprocal_parcel_energy_identity',sum(s.diff(total,q)*dq for q,dq in zip(vars,flow)))

# Direct full state partial trace fixes the sign of the lower-left coherence.
coherence_rows=[]
time=.8;momentum0=.7
F=lambda x:np.sqrt(momentum0**2+(1+x)**2)
for N in range(1,7):
    amplitudes=np.array([np.exp(-1j*time*N*F(k.bit_count()/N))/np.sqrt(2**N)for k in range(2**N)])
    state=amplitudes.reshape(2,-1)
    reduced=state@state.conj().T
    ks=np.arange(N)
    probabilities=comb(N-1,ks)/2**(N-1)
    c10=.5*np.dot(probabilities,np.exp(-1j*time*N*(F((ks+1)/N)-F(ks/N))))
    candidate=np.array([[.5,np.conjugate(c10)],[c10,.5]])
    error=float(np.max(abs(reduced-candidate)))
    wrong=float(np.max(abs(reduced-candidate.conj())))
    assert error<2e-14 and wrong>.1
    coherence_rows.append({'population':N,'correct_density_error':error,'conjugated_orientation_error':wrong})

# Check the noncommuting root-generator estimate with independent fixed data.
rng=np.random.default_rng(42681);root_rows=[]
for trial in range(5):
    A=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    B=np.eye(4)*1.44+A@A.conj().T/9
    Zm=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));O=(Zm+Zm.conj().T)/2;O/=np.linalg.norm(O,2)
    vec=rng.normal(size=4)+1j*rng.normal(size=4);vec/=np.linalg.norm(vec)
    N=9;m0=1.2;bscalar=float(np.vdot(vec,B@vec).real);cscalar=-.4
    C=1j*N*(B@O-O@B)
    eig,W=np.linalg.eigh(B);sqrtB=(W*np.sqrt(eig))@W.conj().T
    lhs=np.linalg.norm((1j*N*(sqrtB@O-O@sqrtB)-cscalar/(2*np.sqrt(bscalar))*np.eye(4))@vec)
    rhs=np.linalg.norm((C-cscalar*np.eye(4))@vec)/(2*m0)+abs(cscalar)*np.linalg.norm((B-bscalar*np.eye(4))@vec)/(4*m0**3)+np.linalg.norm(C@B-B@C,2)/(8*m0**3)
    assert lhs<=rhs+1e-12
    root_rows.append({'trial':trial,'lhs':float(lhs),'bound':float(rhs)})

# The quantum current bound remains valid when position and amplitude do not commute.
position=np.diag([-.25,.45]);amplitude=np.array([[.2,1j],[-1j,-.1]],complex)
vec=np.array([np.sqrt(.7),np.sqrt(.3)*np.exp(.4j)])
Xcl=.1;bcl=.3;eta=.6
projectors=[np.diag([1,0]),np.diag([0,1])]
coeff=[(P@amplitude+amplitude@P)@vec/2 for P in projectors]+[-bcl*vec]
centers=[-.25,.45,Xcl]
normK2=1/(2*np.sqrt(np.pi)*eta)
integrated=sum(np.vdot(coeff[i],coeff[j])*normK2*np.exp(-(centers[i]-centers[j])**2/(4*eta**2))for i in range(3)for j in range(3))
lhs=float(np.sqrt(max(0,integrated.real)))
deltaB=np.linalg.norm((amplitude-bcl*np.eye(2))@vec)
deltaX=np.linalg.norm((position-Xcl*np.eye(2))@vec)
rhs=np.sqrt(normK2)*deltaB+(np.linalg.norm(amplitude,2)+abs(bcl))*np.sqrt(normK2/(2*eta*eta))*deltaX/2
assert lhs<=rhs+1e-13

# Resolved lattice/continuum energy comparison and necessity of the norm factor.
kh2,k2,f,t,coupling=s.symbols('kh2 k2 f t coupling',positive=True)
q1,q2,p1,p2,z1,z2=s.symbols('q1 q2 p1 p2 z1 z2',real=True)
qnorm=q1*q1+q2*q2;pnorm=p1*p1+p2*p2;rel=(q1-z1)**2+(q2-z2)**2
Hh=pnorm/(2*f*t*t)+f*kh2*qnorm/2+coupling*rel/2
Hc=pnorm/(2*f*t*t)+f*k2*qnorm/2+coupling*rel/2
eq('continuum_minus_lattice_energy',Hc-Hh-f*(k2-kh2)*qnorm/2)
eq('energy_equivalence_remainder',(s.pi**2/4)*Hh-Hc-(s.pi**2/4-1)*(pnorm/(2*f*t*t)+coupling*rel/2)-f*(s.pi**2*kh2/4-k2)*qnorm/2)

report={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'exact_check_count':len(checks),'checks':checks,
 'proper_clock_orientation_controls':coherence_rows,'square_root_controls':root_rows,
 'noncommuting_current_control':{'lhs':lhs,'bound':float(rhs),'commutator_norm':float(np.linalg.norm(position@amplitude-amplitude@position))},
 'scope':'Independent selected algebra and finite controls; analytic proof/domain review is separate. No proposed verifier imported.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'review_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'coherence_max_error':max(r['correct_density_error']for r in coherence_rows),'current_bound_check':[lhs,float(rhs)]},indent=2))
