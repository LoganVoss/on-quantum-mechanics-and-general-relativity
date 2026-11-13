"""Scratch exact independent verification of the Gaussian-band kinetic operator."""
from pathlib import Path
import sympy as s
import json,hashlib,datetime

u=s.symbols('u', real=True)
v=s.symbols('v', positive=True)
x=s.symbols('x',real=True)
chi=s.Function('chi')(u,v)
psi=(v/s.pi)**s.Rational(1,4)*s.exp((s.I*u-v)*x*x/2)
prob=s.sqrt(v/s.pi)*s.exp(-v*x*x)
mom={n:s.integrate(x**n*prob,(x,-s.oo,s.oo)) for n in (0,2,4)}
checks=[]
def eq(name,expr):
 r=s.simplify(s.expand(expr))
 assert r==0,(name,r)
 checks.append({'name':name,'residual':str(r)})
def mean(expr):
 p=s.Poly(s.expand(expr),x)
 return s.simplify(sum(c*mom[power[0]] for power,c in p.terms()))

eq('gaussian_normalization',mom[0]-1)
full=s.simplify(-v*v*(s.diff(chi*psi,u,2)+s.diff(chi*psi,v,2))/psi)
projected=mean(full)
target=-v*v*(s.diff(chi,u,2)+s.diff(chi,v,2))-s.I*v*s.diff(chi,u)/2+s.Rational(5,16)*chi
eq('exact_projected_kinetic_operator',projected-target)
Au=-1/(4*v)
def Du(c):return s.diff(c,u)-s.I*Au*c
magnetic=-v*v*(Du(Du(chi))+s.diff(chi,v,2))
eq('Berry_covariant_kinetic_plus_Born_Huang',projected-magnetic-chi/4)
D=v*(s.diff(chi,v)-s.I*s.diff(chi,u))+chi/4
off=s.simplify(full-projected)
eq('exact_offband_second_excitation',off-v*D*(x*x-1/(2*v)))
eq('offband_orthogonal_to_vacuum',mean(off))
eq('centered_x_squared_variance',mean((x*x-1/(2*v))**2)-1/(2*v*v))
DdagD=-v*s.diff(D,v)-s.I*v*s.diff(D,u)+s.Rational(5,4)*D
eq('projected_factorization_Ddagger_D',projected-DdagD)

# Formal compact support integration by parts gives <Dχ,Dχ>=<χ,D†Dχ>.
# Thus ||Q H Pχ||² = kappa²/2 ||Dχ||² = kappa/2 <Pχ,H Pχ>.
# At one point, this norm coefficient is checked independently here.
z=s.symbols('z',complex=True)
eq('leakage_norm_coefficient',mean(s.conjugate(v*z*(x*x-1/(2*v)))*v*z*(x*x-1/(2*v)))-s.conjugate(z)*z/2)

# A compactly supported nonzero χ cannot make the band invariant:
# Dχ=0 iff f=v^(1/4)χ satisfies ∂v f−i∂u f=0 (holomorphic f).
eq('holomorphic_zero_leakage_condition',s.diff(v**s.Rational(1,4)*chi,v)-s.I*s.diff(v**s.Rational(1,4)*chi,u)-v**s.Rational(-3,4)*D)

# A concrete normalized packet permits a separate exact integral check.
# This packet is not compactly supported, but all integrations by parts converge.
packet=2/s.pi**s.Rational(1,4)*v*v*s.exp(-v-u*u/2)
measure=packet*packet/(v*v)
def integ(expr):
 return s.simplify(s.integrate(s.integrate(s.expand(expr),(u,-s.oo,s.oo)),(v,0,s.oo)))
eq('explicit_packet_normalization',integ(measure)-1)
Dp=v*(s.diff(packet,v)-s.I*s.diff(packet,u))+packet/4
packet_Dnorm=integ(s.conjugate(Dp)*Dp/(v*v))
eq('explicit_packet_kinetic_energy_in_kappa_units',packet_Dnorm-s.Rational(45,16))
packet_projected=-v*v*(s.diff(packet,u,2)+s.diff(packet,v,2))-s.I*v*s.diff(packet,u)/2+s.Rational(5,16)*packet
eq('explicit_packet_independent_projected_energy',integ(packet*packet_projected/(v*v))-packet_Dnorm)
eq('explicit_packet_offband_norm_in_kappa_squared_units',packet_Dnorm/2-s.Rational(45,32))

out=Path(__file__).resolve().parent
receipt={'status':'PASS','date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy':s.__version__,
 'checks':checks,'check_count':len(checks),
 'projected_operator':str(projected),'offband_coefficient_D':str(D),
 'domain':'chi in C_c^infty(H²); Gaussian psi_M; full H=kappa(-Δ_G)+Hprobe(M), ground energy subtracted',
 'analytic_steps':['Friedrichs positive operator extension','compact-support integration by parts','holomorphic compact-support uniqueness','strong unitary Taylor expansion on D(H)'],
 'claim':'exact band compression and instantaneous leakage law, not an exact invariant ground-band evolution',
 'concrete_packet':{'chi':'2*pi^(-1/4)*v^2*exp(-v-u^2/2)','energy_over_kappa':'45/16','leakage_norm_squared_over_kappa_squared':'45/32','initial_excitation_probability_coefficient':'45*hbar^2/(128*I^2)'}}
(out/'projection_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'projected':str(projected)},indent=2))
