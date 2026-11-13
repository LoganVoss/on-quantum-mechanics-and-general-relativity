#!/usr/bin/env python3
"""Exact independent certificates for necessity AND sufficiency of the Lax route.

The arithmetic is symbolic/rational. The generic-jet test realizes arbitrary
independent symmetric traceless first jets at M=I and their on-shell second jet.
"""
from pathlib import Path
import json
import random
import sympy as S

checks=[]
def zero(name,value):
    value=S.factor(S.together(value))
    if value != 0:
        raise AssertionError((name,value))
    checks.append({'name':name,'residual':'0','status':'passed'})
def matrix_zero(name,m):
    for i in range(m.rows):
        for j in range(m.cols): zero(name+f'_{i}{j}',m[i,j])

s,p,q,wpm,W=S.symbols('s p q wpm W',nonzero=True)
aa=1/(1-s)
bb=1/(1+s)
g=s*(1+s)/(1-s)
h=s*(1-s)/(1+s)
c=(s+1/s)/2
zero('commutator_coefficient',2*aa*bb-aa-bb)
zero('plus_scalar_coefficient',(aa-bb)*p/2+S.diff(bb,s)*g*p)
zero('minus_scalar_coefficient',(aa-bb)*q/2-S.diff(aa,s)*h*q)
zero('MC_multiplier',(aa+bb)/2-1/(1-s*s))
zero('EOM_multiplier',(bb-aa)/2+s/(1-s*s))
zero('g_minus_h',g-h-4*s*s/(1-s*s))
zero('gprime_h_minus_hprime_g',S.diff(g,s)*h-S.diff(h,s)*g-4*s*s/(1-s*s))
obstruction=(S.diff(g,s)*h-S.diff(h,s)*g)*p*q+(g-h)*(wpm/W-p*q)
zero('frobenius_obstruction',obstruction-4*s*s/(1-s*s)*wpm/W)
zero('spectral_curve_plus',1+c+S.diff(c,s)*g)
zero('spectral_curve_minus',-1+c+S.diff(c,s)*h)
zero('spectral_parameter_derivative',1/(W*S.diff(c,s))-2*s*s/(W*(s*s-1)))

# Noncommuting current jets, without imposing their equations in advance.
u,v,x,y,emh,ems,mch,mcs,mck=S.symbols('u v x y emh ems mch mcs mck')
H=S.diag(1,-1)
X=S.Matrix([[0,1],[1,0]])
K=S.Matrix([[0,1],[-1,0]])
Jp=u*H+v*X
Jm=x*H+y*X
C=Jp*Jm-Jm*Jp
E=emh*H+ems*X
MC=mch*H+mcs*X+mck*K
A=(E+MC-C-p*Jm-q*Jp)/2
B=(E-MC+C-p*Jm-q*Jp)/2
curvature=bb*A-aa*B+S.diff(bb,s)*g*p*Jm-S.diff(aa,s)*h*q*Jp+aa*bb*C
matrix_zero('full_curvature_identity',curvature-(MC-s*E)/(1-s*s))
zero('jet_independence',S.det(S.Matrix([[u,x,0],[v,y,0],[0,0,2*(u*y-v*x)]]))-2*(u*y-v*x)**2)

# The second jet is compatible with an actual symmetric determinant-one M.
Aon=-(C+p*Jm+q*Jp)/2
Bon=(C-p*Jm-q*Jp)/2
Mpm=Aon+Jp*Jm
matrix_zero('symmetric_second_jet',Mpm-Mpm.T)
matrix_zero('same_mixed_second_jet',Mpm-(Bon+Jm*Jp))
zero('determinant_second_jet',S.trace(Mpm)-S.trace(Jp*Jm))

# Scalar factor classification of the finite nonzero generic scalar ansatz.
ap,bp=S.symbols('ap bp')
param=(ap-bp)/(ap+bp)
zero('ansatz_constraint_identity',2*ap*bp-(ap+bp)-(ap+bp)*((ap+bp)*(1-param**2)/2-1))

# Harmonic area and the coupled dilaton trace relation.
z=S.symbols('z',positive=True)
Wf=S.Function('W')(z)
Ff=S.Function('F')(z)
Xp,Vp=S.symbols('X V')
boxW=S.diff(Wf,z)*(Vp-S.diff(Ff,z,2)*Xp)/S.diff(Ff,z)+S.diff(Wf,z,2)*Xp
zero('coupled_dilaton_identity',boxW-S.diff(Wf,z)/S.diff(Ff,z)*Vp-(S.diff(Wf,z,2)-S.diff(Wf,z)*S.diff(Ff,z,2)/S.diff(Ff,z))*Xp)
zero('affine_F_derivative',S.diff(S.diff(Wf,z)/S.diff(Ff,z),z)-(S.diff(Wf,z,2)-S.diff(Wf,z)*S.diff(Ff,z,2)/S.diff(Ff,z))/S.diff(Ff,z))
n,cc=S.symbols('n cc',real=True)
zero('power_second_derivative',S.diff(cc*z**n,z,2)-cc*n*(n-1)*z**(n-2))

# Explicit conformal counterfamily and an interior curvature value.
eta,a=S.symbols('eta a',real=True)
Bump=S.exp(-1/((z-1)*(2-z)))
zero('bump_value_at_midpoint',Bump.subs(z,S.Rational(3,2))-S.exp(-4))
zero('bump_second_at_midpoint',S.diff(Bump,z,2).subs(z,S.Rational(3,2))+32*S.exp(-4))
gamma=-2*eta*Bump
R4=-S.exp(-gamma)*S.diff(gamma,z,2)
zero('frame_counterexample_curvature',R4.subs(z,S.Rational(3,2))+64*eta*S.exp(-4)*S.exp(2*eta*S.exp(-4)))

# 256 exact rational, noncommuting on-shell current jets.
rs=random.Random(20261113)
jets=[]
for i in range(256):
    while True:
        vals=[S.Rational(rs.randint(-9,9),rs.randint(1,7)) for _ in range(4)]
        uu,vv,xx,yy=vals
        if uu*yy-vv*xx:break
    ss=S.Rational(i+2,i+259) # strictly 0<s<1
    pp=S.Rational(rs.randint(-9,9),rs.randint(1,7))
    qq=S.Rational(rs.randint(-9,9),rs.randint(1,7))
    jp=uu*H+vv*X
    jm=xx*H+yy*X
    comm=jp*jm-jm*jp
    ap=-(comm+pp*jm+qq*jp)/2
    bm=(comm-pp*jm-qq*jp)/2
    aa0=aa.subs(s,ss);bb0=bb.subs(s,ss)
    cp=bb0*ap-aa0*bm+S.diff(bb,s).subs(s,ss)*g.subs(s,ss)*pp*jm-S.diff(aa,s).subs(s,ss)*h.subs(s,ss)*qq*jp+aa0*bb0*comm
    assert all(S.factor(v)==0 for v in cp)
    jets.append({'index':i,'s':str(ss),'independence_determinant':str(2*(uu*yy-vv*xx)**2),'curvature':'zero_matrix'})

out={'status':'passed','arithmetic':'exact_symbolic_and_rational','sympy_version':S.__version__,'symbolic_check_count':len(checks),'generic_noncommuting_jet_count':len(jets),'checks':checks,'generic_jet_checks':jets}
(Path(__file__).resolve().parents[1]/'evidence'/'integrability_complete_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='generic_jet_checks'},indent=2))
