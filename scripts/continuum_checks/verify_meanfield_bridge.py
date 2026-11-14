"""Scratch exact and bounded controls for a declared large-population bridge.

No supplied verifier is imported. Analytic inequalities are proved separately;
the finite controls check their algebra and a solvable nonlinear parcel.
"""
from pathlib import Path
import sympy as s
import numpy as np
from scipy.special import gammaln
import scipy
import json,hashlib,platform,datetime

checks=[]
def eq(name,expression):
    if isinstance(expression,s.MatrixBase):
        for i in range(expression.rows):
            for j in range(expression.cols):eq(f'{name}_{i}{j}',expression[i,j])
        return
    r=s.simplify(s.expand(expression))
    assert r==0,(name,r)
    checks.append({'name':name,'residual':'0'})

# General two-dimensional variable-metric kinetic/transport commutator.
x,y=s.symbols('x y',real=True);eps,I=s.symbols('eps I',positive=True)
q=[x,y];g11=s.Function('g11')(x,y);g12=s.Function('g12')(x,y);g22=s.Function('g22')(x,y)
g=s.Matrix([[g11,g12],[g12,g22]])
U=s.Matrix([s.Function('U1')(x,y),s.Function('U2')(x,y)])
f=s.Function('f')(x,y)
divU=sum(s.diff(U[a],q[a])for a in range(2))
def T(z):return -eps**2/(2*I)*sum(s.diff(g[a,b]*s.diff(z,q[b]),q[a])for a in range(2)for b in range(2))
def L(z):return -s.I*eps*(sum(U[a]*s.diff(z,q[a])for a in range(2))+divU*z/2)
C=s.Matrix(2,2,lambda a,b:sum(U[c]*s.diff(g[a,b],q[c])-g[c,b]*s.diff(U[a],q[c])-g[a,c]*s.diff(U[b],q[c])for c in range(2)))
candidate=-eps**2/(2*I)*sum(s.diff(C[a,b]*s.diff(f,q[b]),q[a])for a in range(2)for b in range(2))+eps**2/(4*I)*sum(s.diff(g[a,b]*s.diff(divU,q[b]),q[a])for a in range(2)for b in range(2))*f
eq('variable_metric_transport_commutator',s.I/eps*(L(T(f))-T(L(f)))-candidate)
# Unitary flattening of hyperbolic L²(du dv/v²) gives divergence-form kinetic.
v=s.symbols('v',positive=True);u=s.symbols('u',real=True);z=s.Function('z')(u,v)
eq('hyperbolic_measure_flattening',-v*(s.diff(v*z,u,2)+s.diff(v*z,v,2))+v*v*s.diff(z,u,2)+s.diff(v*v*s.diff(z,v),v))

# Resolvent constants for the positive square-root generator lemma.
t,m=s.symbols('t m',positive=True)
eq('sqrt_resolvent_constant_2',s.integrate(s.sqrt(t)/(m*m+t)**2,(t,0,s.oo))/s.pi-1/(2*m))
eq('sqrt_resolvent_constant_3',s.integrate(s.sqrt(t)/(m*m+t)**3,(t,0,s.oo))/s.pi-1/(8*m**3))

# HS-orthonormal Hermitian basis: completeness, antisymmetry, symmetric Casimir.
Id=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
basis=[A/s.sqrt(2)for A in [Id,X,Y,Z]]
for a,A in enumerate(basis):
 for b,B in enumerate(basis):eq(f'HS_basis_{a}{b}',s.trace(A*B)-(1 if a==b else 0))
swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
eq('swap_completeness',sum((s.kronecker_product(A,A)for A in basis),s.zeros(4))-swap)
h0,h1,h2,h3=s.symbols('h0:4',real=True);H=h0*Id+h1*X+h2*Y+h3*Z
Gamma=s.Matrix(4,4,lambda a,b:s.I*s.trace(basis[b]*(H*basis[a]-basis[a]*H)))
eq('internal_rotation_antisymmetric',Gamma+Gamma.T)

for N in range(1,5):
 def at(A,j):
  ops=[Id]*N;ops[j]=A
  out=ops[0]
  for op in ops[1:]:out=s.kronecker_product(out,op)
  return out
 As=[sum((at(A,j)for j in range(N)),s.zeros(2**N))/N for A in basis]
 # Symmetric Dicke embedding, verified exactly.
 embed=s.zeros(2**N,N+1)
 for integer in range(2**N):
  k=integer.bit_count();embed[integer,k]=1/s.sqrt(s.binomial(N,k))
 casimir=sum((A*A for A in As),s.zeros(2**N))
 eq(f'symmetric_Casimir_N{N}',embed.T*casimir*embed-(1+s.Rational(1,N))*s.eye(N+1))
 P=s.Matrix([[1,0],[0,0]])
 b=[s.trace(P*A)for A in basis]
 V=sum(((A-bi*s.eye(2**N))**2 for A,bi in zip(As,b)),s.zeros(2**N))
 beta=s.eye(2**N)-sum((at(P,j)for j in range(N)),s.zeros(2**N))/N
 eq(f'variance_counting_identity_N{N}',embed.T*(V-2*beta)*embed-s.eye(N+1)/N)

# Exact functional derivatives of the Brown parcel Hamiltonian.
p,e=s.symbols('p e',real=True);mass=s.symbols('mass',positive=True)
F=s.sqrt(p*p+e*e)
eq('proper_time_factor',s.diff(F,e)-e/F)
eq('coordinate_velocity',s.diff(F,p)-p/F)
eq('mass_convexity',s.diff(F,e,2)-p*p/F**3)
eq('Brown_Legendre_identity',p*(p/F)-F+e*(e/F))

# Nonlinear collective-mass quantum dynamics: exact symmetric amplitudes.
m0=1.0;momentum=0.7;time=0.8
Fnum=lambda a:np.sqrt(momentum**2+(m0+a)**2)
freq=(m0+0.5)/Fnum(0.5)
M2=momentum**2/(momentum**2+m0**2)**1.5
rows=[]
for N in [1,2,4,8,16,32,64,128,256,512]:
 k=np.arange(N,dtype=float)
 probs=np.exp(gammaln(N)-gammaln(k+1)-gammaln(N-k)-(N-1)*np.log(2.0))
 probs/=probs.sum()
 increments=N*(Fnum((k+1)/N)-Fnum(k/N))
 coherence=0.5*np.sum(probs*np.exp(-1j*time*increments))
 limit=0.5*np.exp(-1j*time*freq)
 trace_error=float(2*abs(coherence-limit))
 bound=float(abs(time)*M2*(np.sqrt(N-1)/(2*N)+1/N))
 assert trace_error<=bound+2e-13,(N,trace_error,bound)
 kk=np.arange(N+1,dtype=float)
 pp=np.exp(gammaln(N+1)-gammaln(kk+1)-gammaln(N-kk+1)-N*np.log(2.0));pp/=pp.sum()
 energy=float(np.sum(pp*Fnum(kk/N)))
 closure=energy-float(Fnum(0.5));energy_bound=M2/(8*N)
 assert -2e-14<=closure<=energy_bound+2e-14,(N,closure,energy_bound)
 # Positivity of the exact one-probe reduced density.
 # coherence is rho_10 for i*dpsi/dt=H*psi, not rho_01.
 rho=np.array([[0.5,coherence.conjugate()],[coherence,0.5]])
 assert np.linalg.eigvalsh(rho).min()>=-2e-14
 rows.append({'population':N,'trace_norm_error':trace_error,'analytic_trace_bound':bound,'energy_per_probe':energy,'closure_error':closure,'analytic_energy_bound':energy_bound,'coherence_real':float(coherence.real),'coherence_imag':float(coherence.imag)})

# Independently construct the full 2^N state and trace N-1 probes.
# This tests the time-phase and matrix-index convention, not only eigenvalues.
partial_trace_rows=[]
for N in range(1,6):
 counts=np.array([integer.bit_count()for integer in range(2**N)],dtype=float)
 state=np.exp(-1j*time*N*Fnum(counts/N))/np.sqrt(2**N)
 amplitudes=state.reshape(2,-1)
 reduced=amplitudes@amplitudes.conj().T
 k=np.arange(N,dtype=float)
 probs=np.exp(gammaln(N)-gammaln(k+1)-gammaln(N-k)-(N-1)*np.log(2.0));probs/=probs.sum()
 c10=0.5*np.sum(probs*np.exp(-1j*time*N*(Fnum((k+1)/N)-Fnum(k/N))))
 predicted=np.array([[0.5,c10.conjugate()],[c10,0.5]])
 error=float(np.linalg.norm(reduced-predicted,ord='fro'))
 assert error<2e-14,(N,error)
 assert abs(reduced[1,0]-c10)<2e-14
 partial_trace_rows.append({'population':N,'full_Hilbert_dimension':2**N,'reduced_density_error':error,'coherence_convention':'rho_10'})

# Finite canonical clock/shift realizes the abstract commutator assumptions.
# UV=exp(-2pi i/N)VU corresponds to positive physical {q,p}=1.
clock_rows=[]
for N in [4,8,16,32]:
 Un=np.diag(np.exp(2j*np.pi*np.arange(N)/N))
 Vn=np.roll(np.eye(N,dtype=complex),-1,axis=0)
 assert np.linalg.norm(Un@Vn-np.exp(-2j*np.pi/N)*Vn@Un)<1e-12
 obs=[(Un+Un.conj().T)/2,(Un-Un.conj().T)/(2j),(Vn+Vn.conj().T)/2,(Vn-Vn.conj().T)/(2j)]
 zero=np.zeros((N,N),complex)
 dq=[-obs[1],obs[0],zero,zero];dp=[zero,zero,-obs[3],obs[2]]
 max_res=max_comm=0.0
 for a in range(4):
  for b in range(4):
   comm=obs[a]@obs[b]-obs[b]@obs[a]
   pi=2*np.pi*(dq[b]@dp[a]-dp[b]@dq[a])
   residue=np.linalg.norm(1j*N*comm-pi,2)
   cnorm=np.linalg.norm(comm,2)
   assert residue<=2*np.pi**2/N+1e-12,(N,a,b,residue)
   assert cnorm<=2*np.pi/N+1e-12
   max_res=max(max_res,residue);max_comm=max(max_comm,cnorm)
 clock_rows.append({'dimension':N,'max_generator_remainder':float(max_res),'generator_bound':float(2*np.pi**2/N),'max_commutator_norm':float(max_comm),'commutator_bound':float(2*np.pi/N)})

coherent_rows=[]
for N in [4,8,16,32,64,128,256,512]:
 j=np.arange(-N//2,N//2,dtype=float)
 vec=sum(np.exp(-np.pi*(j+ell*N)**2/N)for ell in range(-4,5));vec/=np.linalg.norm(vec)
 expU=np.sum(abs(vec)**2*np.exp(2j*np.pi*j/N))
 expV=np.vdot(vec,np.roll(vec,1))
 D0=float(2*(1-expU.real)+2*(1-expV.real))
 assert D0<=400*np.pi**2/N+1e-12
 assert abs(expU-expV)<1e-12
 coherent_rows.append({'dimension':N,'initial_squared_deviation':D0,'N_times_deviation':N*D0,'proved_conservative_bound':400*np.pi**2/N})

# Independent finite-matrix checks of the noncommuting square-root bound.
rng=np.random.default_rng(237)
sqrt_rows=[]
frechet_rows=[]
for trial in range(6):
 A=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
 Bmat=np.eye(3)+A@A.conj().T/8
 O=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));O=(O+O.conj().T)/2;O/=np.linalg.norm(O,2)
 vec=rng.normal(size=3)+1j*rng.normal(size=3);vec/=np.linalg.norm(vec)
 NN=7;Cmat=1j*NN*(Bmat@O-O@Bmat)
 bscalar=float(np.vdot(vec,Bmat@vec).real);cscalar=0.7
 ev,W=np.linalg.eigh(Bmat);sqrtB=(W*np.sqrt(ev))@W.conj().T
 lhs=np.linalg.norm((1j*NN*(sqrtB@O-O@sqrtB)-cscalar/(2*np.sqrt(bscalar))*np.eye(3))@vec)
 rhs=np.linalg.norm((Cmat-cscalar*np.eye(3))@vec)/2+abs(cscalar)*np.linalg.norm((Bmat-bscalar*np.eye(3))@vec)/4+np.linalg.norm(Cmat@Bmat-Bmat@Cmat,2)/8
 assert lhs<=rhs+1e-12,(trial,lhs,rhs)
 sqrt_rows.append({'trial':trial,'lhs':float(lhs),'proved_rhs':float(rhs),'min_B_eigenvalue':float(ev.min())})
 # The actual Hamiltonian-variation derivative uses the same resolvent lemma.
 variation=O;cvar=0.2
 vt=W.conj().T@variation@W
 derivative=W@(vt/(np.sqrt(ev)[:,None]+np.sqrt(ev)[None,:]))@W.conj().T
 flhs=np.linalg.norm((derivative-cvar/(2*np.sqrt(bscalar))*np.eye(3))@vec)
 frhs=np.linalg.norm((variation-cvar*np.eye(3))@vec)/2+abs(cvar)*np.linalg.norm((Bmat-bscalar*np.eye(3))@vec)/4+np.linalg.norm(variation@Bmat-Bmat@variation,2)/8
 assert flhs<=frhs+1e-12,(trial,flhs,frhs)
 # A positive lapse sandwich gives a positive root even without commutation.
 raw=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
 lapse=0.8*np.eye(3)+raw@raw.conj().T/20
 min_lapse=float(np.linalg.eigvalsh(lapse).min())
 min_sandwich=float(np.linalg.eigvalsh(lapse@Bmat@lapse).min())
 assert min_sandwich>=min_lapse**2-2e-13
 frechet_rows.append({'trial':trial,'derivative_error_lhs':float(flhs),'proved_rhs':float(frhs),'lapse_minimum':min_lapse,'sandwich_minimum':min_sandwich,'proved_sandwich_lower_bound':min_lapse**2})

out=Path(__file__).resolve().parent
report={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'scipy':scipy.__version__,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_check_count':len(checks),'checks':checks,'parcel_parameters':{'m0':m0,'momentum':momentum,'time':time,'limiting_internal_frequency':float(freq),'max_second_derivative':float(M2),'coherence_convention':'rho_10; rho_01 is its conjugate'},'parcel_rows':rows,'direct_partial_trace_controls':partial_trace_rows,'canonical_clock_controls':clock_rows,'coherent_preparation_controls':coherent_rows,'noncommuting_square_root_controls':sqrt_rows,'frechet_source_and_lapse_controls':frechet_rows,'scope':'Algebraic controls and a solvable finite-internal-cutoff nonlinear collective parcel. Not a full field simulation or proof of unregularized quantum gravity.'}
(out/'meanfield_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'parcel_N512_error':rows[-1]['trace_norm_error'],'parcel_N512_bound':rows[-1]['analytic_trace_bound']},indent=2))
