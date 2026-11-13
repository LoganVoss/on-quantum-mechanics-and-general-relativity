"""Independent radial action variation of Ricci-squared on charged electrovac.

No imported geometry or variation code from the proposed calibration checker.
The lapse and radial metric are independent before the variation.
"""
import sympy as s
from pathlib import Path
import json,hashlib
r=s.symbols('r',positive=True)
A,B=s.symbols('A B',positive=True)
Ap,App,Bp=s.symbols('Ap App Bp',real=True)
Rtt=App/(2*B)-Ap*Bp/(4*B*B)-Ap*Ap/(4*A*B)+Ap/(r*B)
Rrr=-App/(2*A)+Ap*Ap/(4*A*A)+Ap*Bp/(4*A*B)+Bp/(r*B)
Rth=1-1/B+r*Bp/(2*B*B)-r*Ap/(2*A*B)
Ric2=Rtt**2/A**2+Rrr**2/B**2+2*Rth**2/r**4
L=r*r*s.sqrt(A*B)*Ric2
f=1-2/r+1/(4*r*r)
sub={A:f,B:1/f,Ap:s.diff(f,r),App:s.diff(f,r,2),Bp:s.diff(1/f,r)}
# sqrt(A B) is one on the exterior branch; simplify before radial derivatives.
def at(expr):
 # Every coefficient contains sqrt(A B); on the exterior RN branch A B=1.
 rational=s.cancel(expr/s.sqrt(A*B))
 return s.factor(rational.subs(sub))
p0=at(s.diff(L,A));p1=at(s.diff(L,Ap));p2=at(s.diff(L,App))
EL=s.factor(p0-s.diff(p1,r)+s.diff(p2,r,2))
mixed=s.factor(-f*EL/r**2)
expected=-3*(4*r*r-8*r+1)/(4*r**8)
assert s.simplify(mixed-expected)==0,(mixed,expected)
point=s.simplify(mixed.subs(r,3))
assert point==-s.Rational(13,8748)
report={'status':'PASS','method':'Independent Euler variation of the static spherical Ricci-squared density with lapse/radial metric kept independent, then RN evaluation.',
 'H_mixed_tt':str(mixed),'point_r3':str(point),'sympy':s.__version__,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'limits':'Checks the lapse equation at a regular exterior point. Full tensor checks are separate.'}
Path(__file__).with_name('independent_rn_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
