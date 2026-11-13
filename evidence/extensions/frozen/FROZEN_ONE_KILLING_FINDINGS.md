# Scratch findings: one-Killing selection and current-corrected twist

All derivations in this record are research scratch work, completed before public appendices or manuscript changes. Public statements must preserve the precise assumptions below. Existing one-Killing Einstein reduction is established literature; the contribution newly derived here is the explicit flat helical inverse calibration and its compatibility analysis with the independently selected quantum probe coupling. Worldwide priority is not established.

## 1. The exact enlarged field space

Let h be an arbitrary 2+1-dimensional Lorentzian metric, lambda>0 and chi real scalar fields. On a local patch take a spacelike symmetry coordinate y and a connection A with F=dA. The four-metric dictionary is

    g4=lambda^(-1) h_ab dx^a dx^b + lambda (dy+A_a dx^a)^2.

Only y-independence is imposed. In particular h,lambda,chi may depend on both spatial quotient coordinates. This is genuinely a one-Killing theory class, not the original two-Killing block ansatz. The Einstein-frame metric h is lambda times the literal quotient metric. That factor and the normalization of y are explicit parts of the new calibrated dictionary.

With orientation epsilon_Trx=+sqrt(-h), Lorentzian Hodge star obeys star^2=-1 on one- and two-forms. In vacuum the twist convention is

    dchi=lambda^2 star_h F,       F=-lambda^(-2) star_h dchi.

The local reconstruction requires the right side for F to be closed. Global bundle periods and topology are additional data.

## 2. Action classification

Assume locality, base-diffeomorphism invariance, no additional fields, polynomial total derivative order at most two, and constant full SL(2,R) action on the upper-half-plane target (u,v)=(chi,lambda). The invariant target metric is

    G=(dlambda^2+dchi^2)/lambda^2.

Target transitivity makes any invariant coefficient of R[h] or potential a constant. Target isotropy has no invariant one-form and has a unique invariant symmetric bilinear form up to scale. Consequently, modulo divergences, the complete action in this class is

    S[f,w,V]=integral sqrt(-h)[f R[h] - w G_AB(q) nabla q^A.nabla q^B/2 + V] d^3x,

where f,w,V are constants. No parity assumption is needed at this derivative order: an orientation-odd base scalar would need a three-form/three derivatives, and target dimension two supplies no target three-form. Gravitational Chern-Simons terms are above the stipulated order.

This class is stronger than all conceivable one-Killing reductions. Full target SL(2,R), the Einstein frame and fixed field content are inputs. In particular a four-dimensional cosmological term reduces to a nonconstant norm-dependent potential, outside full target invariance. Do not claim a solution to the cosmological-constant problem.

## 3. A flat helical calibration selects the relative coefficient

Begin with Minkowski cylindrical coordinates (T,r,phi,z), and let phi=x+Omega y, z=y, with fixed real Omega !=0. Then

    g4=-dT^2+dr^2+r^2(dx+Omega dy)^2+dy^2.

Its designated Killing field is K=partial_y=partial_z+Omega partial_phi, which is spacelike. On a local patch r>0,

    lambda=1+Omega^2 r^2,
    A=(Omega r^2/lambda) dx,
    h= -lambda dT^2 + lambda dr^2 + r^2 dx^2,
    chi=2 Omega T.

Direct calculation gives dchi=lambda^2 star_h dA. The lifted metric is flat by its displayed coordinate transformation; all 256 Riemann components were also independently checked to vanish.

Put S_ab=(lambda_a lambda_b+chi_a chi_b)/lambda^2 and X=h^ab S_ab. Exact quotient curvature is

    Ric_TT=2 Omega^2/lambda^2,
    Ric_rr=2 Omega^4 r^2/lambda^2,
    Ric_xx=0,
    Ric_ab=S_ab/2.

Both target equations vanish:

    Box lambda -[(dlambda)^2-(dchi)^2]/lambda=0,
    Box chi -2 dlambda.dchi/lambda=0.

For the action above the inverse-metric Euler expression is

    E_ab=f Einstein_ab -w(S_ab-h_ab X/2)/2 -V h_ab/2.

In particular,

    E_TT=Omega^2(f-w)/lambda +V lambda/2,
    E_rr=Omega^2(f-w)/lambda -V lambda/2.

Therefore, at any one regular calibration point, E_TT=E_rr=0 is equivalent to

    w=f,       V=0.

For these values every metric and target equation vanishes on the calibration. This proves an all-field stationarity equivalence over the full one-Killing theory class. Positive nondegenerate target kinetic energy adds f=w>0. Overall normalization remains free.

The exact inverse and sharp two-channel error bounds are

    f-w=lambda(E_TT+E_rr)/(2 Omega^2),
    V=(E_TT-E_rr)/lambda,

and if both residual magnitudes are <=epsilon,

    |f-w| <=lambda epsilon/Omega^2,
    |V| <=2epsilon/lambda.

They are individually sharp for the two-response algebraic problem. Omega=0 is an explicit negative control: the target is constant and the relative coefficient becomes invisible.

The calibration itself has additional isometries because it is flat. The theorem does NOT restrict the action's general configurations to those isometries: h,lambda,chi remain arbitrary fields of three coordinates. We do not claim here an explicit generic nonlinear solution with exactly one isometry, nor a global existence/stability theorem. The action-selection statement, not discovery of the familiar reduction, is the mathematical enlargement.

## 4. Exact off-shell gravitational identity

For the general dictionary, before any field equation,

    sqrt(-g4) R[g4]
    =sqrt(-h)[R[h] -(dlambda)^2/(2lambda^2) -lambda^2 F_ab F^ab/4]
      +partial_a(sqrt(-h) nabla^a log(lambda)).

A derivation uses q=lambda^(-1)h and the standard one-fiber curvature contraction

    R[g4]=R[q] -lambda F_q^2/4 -lambda^(-1)Box_q lambda
                        +(dlambda)^2_q/(2lambda^2).

The 3D conformal transformation q=lambda^(-1)h gives

    R[g4]=lambda R[h]+Box_h lambda
                -3(dlambda)^2_h/(2lambda)-lambda^3 F_h^2/4,

which yields the density identity. It was additionally checked at fully independent normal-coordinate/gauge jets: h=diag(-1,1,1), dh=0, A=0 at an arbitrary point, with independent second metric jets and arbitrary first/second lambda and A jets. These are coordinate/gauge choices, not on-shell restrictions.

Legendre dualization of F, not simple substitution into its kinetic term, gives

    S=f integral sqrt(-h)[R -(dlambda^2+dchi^2)/(2lambda^2)].

The first-order dualization term must be retained to obtain the correct minus sign for the chi kinetic term.

## 5. Exact recovery of the original cylindrical sector

The original nonlinear cylindrical metric is

    g4=e^(gamma-psi)(-dT^2+dR^2)
          +e^psi(dz+A dphi)^2 +R^2 e^(-psi)dphi^2.

Reduce only K=partial_z. Then

    lambda=e^psi,
    h3=e^gamma(-dT^2+dR^2)+R^2dphi^2,
    chi_T=e^(2psi) A_R/R,
    chi_R=e^(2psi) A_T/R.

The last two relations are precisely the original dual-twist relations. The target metric becomes dpsi^2+e^(-2psi)dchi^2. The 3D Einstein/wave-map equations give exactly

    psi_TT-psi_RR-psi_R/R+e^(-2psi)(chi_T^2-chi_R^2)=0,
    chi_TT-chi_RR-chi_R/R-2(psi_T chi_T-psi_R chi_R)=0,
    gamma_R=R[psi_T^2+psi_R^2+e^(-2psi)(chi_T^2+chi_R^2)]/2,
    gamma_T=R[psi_T psi_R+e^(-2psi)chi_T chi_R].

All four reductions and both Hodge component identities were symbolically verified for arbitrary functions psi,chi,gamma of T,R. Thus the original nonlinear system is a further symmetry-restricted sector of the selected one-Killing action.

## 6. Quantum dictionary and its changed interpretation

Set

    M(lambda,chi)=lambda^(-1)[[1,chi],[chi,chi^2+lambda^2]].

Then det M=1 and (1/2)Tr[(M^-1 dM)^2]=G. The existing centered saturated Gaussian dictionary applies with (u,v)=(chi,lambda). This now encodes a Killing norm and twist. It is NOT the identical two-orbit shape matrix of the previous formulation. The calibrated common SL(2,R) representation remains a premise.

There is no independent area scalar rho in this field space. A zeroth-derivative algebraic target-equivariant probe gap therefore cannot be an arbitrary function of rho or of target position. A constant scale remains. Explicit base-dependent backgrounds, derivative/curvature-dependent probe terms, and additional fields would enlarge that class and require new selection conditions.

## 7. The naive coupling obstruction

A generic independent probe interaction E(M,N) sources the chi equation. If one kept the vacuum reconstruction F_vac=-lambda^-2 star dchi, it would obey

    dF_vac=-(n/f)(partial E/partial chi) vol_h,

which is generally nonzero. It then cannot equal dA. Hence the unchanged vacuum twist dictionary cannot be carried into the sourced model silently.

For the selected oscillator H_M=hbar nu Rhat^T M^-1 Rhat/2 and independent covariance N=2Sigma,

    E_ex=hbar nu[Tr(M^-1 N)-2]/4,
    partial_chi E_ex=hbar nu(chi N11-N12)/(2lambda).

At M=I and N=[[1,1],[1,2]], the covariance is positive unimodular but the source is -hbar nu/2. This is an exact negative control of naive reconstruction, not a numerical instability.

## 8. Current-corrected duality repairs closure

Use the metaplectic shear U_chi=exp(i chi Qhat^2/2) and Psi=U_chi psi_tilde. With

    H0(lambda)=hbar nu[P_hat^2+lambda^2 Q_hat^2]/(2lambda),
    H_M=U_chi H0 U_chi^dagger,

its expectation in Psi is the expectation of H0 in psi_tilde. The Berry derivative is

    i hbar<Psi|partial_a Psi>
     =i hbar<psi_tilde|partial_a psi_tilde>
       -hbar<Q_hat^2/2> partial_a chi.

For a smooth conserved probe number current n u^a, define J^a=hbar n u^a<Q_hat^2/2>. The chi action is

    L_chi= -f (dchi)^2/(2lambda^2) -J.dchi.

Its equation conserves C=f lambda^-2 dchi+J. Accordingly

    F=-star C/f,       dF=0,
    dchi=lambda^2(star F-J/f).

On a contractible patch F=dA now exists. This is a modified reconstruction law.

The full local Legendre equivalence is supplied by the master density

    L_master=-f v^2/(2lambda^2)-J.v+f v.star F,  F=dA,

with independent one-form v. Variation of A gives dv=0, locally v=dchi. Variation of v gives v=lambda^2(star F-J/f). Eliminating v gives exactly

    L_dual= -f lambda^2 F^2/4 -lambda^2 J.star F
                   +lambda^2 J^2/(2f)
           =-f lambda^2 (F+star J/f)^2/4.

The cross term and the current-squared contact term are compulsory. All component signs, the algebraic variation, and the completed square were independently checked in a local (-,+,+) Lorentz frame. Metric variations must also retain J's metric dependence; equality of the master actions then preserves the stress equations.

For point-worldline delta currents, J^2 is undefined without a regulator. This derivation therefore uses a specified smooth current or finite regulator; it does not assert an unregulated point-particle completion.

## 9. A covariant smooth-current realization

One possible explicitly enlarged matter class uses a timelike vector density j^a, n=sqrt(-h_ab j^a j^b)/sqrt(-h), and u^a=j^a/(sqrt(-h)n), together with a scalar velocity potential theta. A normalized quantum state field Psi lives in a fixed calibrated oscillator Hilbert space on each local fluid element. Consider

    S_m=integral [j^a(partial_a theta+i hbar<Psi|partial_a Psi>)
                   -sqrt(-h)n(m0+<H_M>)] d^3x,

with normalization enforced by a multiplier. Variation of theta gives partial_a j^a=0; variation of Psi gives the Schrödinger equation along u, up to the physically irrelevant phase multiplier; variation of j gives the velocity equation. Varying the same action with respect to h,lambda,chi gives reciprocal geometric sources. This is a deterministic variational state-fluid model, not a quantized continuum theory. Local smoothness is assumed and caustics are not solved here.

A single theta gives a restricted velocity-potential subclass. Add Clebsch terms beta_A partial_a alpha^A to admit general local fluid vorticity, as in established relativistic fluid actions. Norm/phase gauge is compensated by a theta shift. This example supplies a consistent covariant smooth current for the duality calculation; selecting this matter architecture itself is an additional assumption.

The exact chi-shift symmetry yields, on a mechanical cell,

    p_chi -hbar<Q_hat^2>/2 = constant.

Indeed, Heisenberg evolution gives partial_chi<E>=-hbar d<Q_hat^2/2>/dt, while p_chi_dot=-partial_chi<E>. This is a useful backreaction diagnostic.

The reconstructed four-metric with a probe is generally not vacuum. The reduced action is a consistent local Einstein-matter extension with a current-corrected connection sector. Calling it ordinary four-dimensional minimally coupled matter, or a generic four-dimensional quantum-gravity theory, would require an explicit corresponding matter uplift and further analysis; neither follows automatically from the scalar duality.

## 10. Exact verification and primary precedents

- `verify_one_killing.py`: 309 exact checks, including all 256 lifted Riemann components, all nine quotient Ricci equations, target equations, response inversion, zero-pitch negative control, and full cylindrical sector reduction.
- `verify_generic_reduction.py`: 15 exact checks, including arbitrary-jet off-shell reduction, master-action duality and contact term, and source/Noether/naive-reconstruction controls.
- Both import no verifier from the original project. Python 3.12.13, SymPy 1.14.0. Run with `work/numerical_audit/venv/bin/python work/extension_symmetry/<script>`.
- Receipt files record source hashes. Counts are identities/components, not counts of independent physical discoveries.

Primary literature inspected:

1. Vincent Moncrief, *The Reduction Problem for Einstein's Equations*, pp.168-174, https://maths.anu.edu.au/files/CMAProcVol19-Moncrief.pdf . One-Killing 2+1 Einstein/hyperbolic-wave-map reduction and global twist/bundle qualifications are established here. Do not treat the reduction itself as new.
2. R.G. Leigh, A.C. Petkou, P.M. Petropoulos, P.K. Tripathy, *The Geroch group in Einstein spaces*, arXiv:1403.6511v2, https://arxiv.org/html/1403.6511v2 . Sections2-3 explicitly distinguish quotient and conformally rescaled metrics and norm/twist variables; its displayed example uses timelike Killing conventions, so our spacelike signs were derived directly rather than copied.
3. J.D. Brown, *Action functionals for relativistic perfect fluids*, Class.Quant.Grav.10(1993)1579-1606, https://arxiv.org/abs/gr-qc/9304026v1 and https://arxiv.org/html/gr-qc/9304026v1 . Precedent for dynamical current, number conservation, velocity potentials and Clebsch fields.

Strongest supported conclusion: an explicit inverse flat-calibration theorem selects the standard one-Killing Einstein-wave-map action within the declared invariant class; the original nonlinear cylindrical sector is recovered exactly. Coupling an independent quantum probe requires a generalized twist/current relation, whose local master-action equivalence is derived and checked. No experimental observation, global existence claim, fully quantized continuum, or worldwide priority claim is established by these calculations.

## 11. Explicit sourced equations, dust stress, and the clock boundary

Let epsilon=m0+<H_M>, H_A=partial H_M/partial q^A, q=(lambda,chi), and use the covariant smooth-current action in section9. Holding the densitized j^a fixed during inverse-metric variation,

    delta(sqrt(-h)n)=sqrt(-h)n u_a u_b delta h^ab/2,
    T^matter_ab=n epsilon u_a u_b.

The current and state equations are

    nabla_a(nu^a)=0,
    i hbar u^a partial_a Psi=H_M Psi  (up to the normalization/phase multiplier),
    partial_a theta+i hbar<Psi|partial_a Psi>+epsilon u_a=0

for the single-velocity-potential subclass. Clebsch terms extend the final canonical-velocity relation without changing the displayed stress tensor.

The field equations of the common action are

    2f Einstein_ab = f(S_ab-h_ab X/2)+T^matter_ab,
    f tau^A(q)= n G^AB <H_B>,

where tau^lambda=Box lambda-[(dlambda)^2-(dchi)^2]/lambda and tau^chi=Box chi-2 dlambda.dchi/lambda. In particular

    f nabla_a(lambda^-2 nabla^a chi)=n<H_chi>.

On the state/current equations, the diffeomorphism Ward identity gives

    nabla_a T^matter[a]_b = -n<H_A> partial_b q^A.

The scalar stress has the opposite divergence by its sourced equation, so the Einstein Bianchi identity is consistent. The proper-flow energy law is u^a partial_a epsilon=<H_A>u^a partial_a q^A. The projected fluid-force law is epsilon u^a nabla_a u_b=-(delta_b^a+u_bu^a)<H_A>partial_a q^A. These are variational identities for the declared model; they do not prove global evolution or exclude caustics.

The clock convention is consequential. The action uses proper flow time measured by the Einstein-frame h3 metric. For a horizontal four-dimensional trajectory, the geometric dictionary gives

    d tau_4=lambda^(-1/2) ds_3.

Therefore a fixed four-dimensional proper-time oscillator gap would appear lambda^(-1/2)-dependent when its generator is expressed in h3 proper time. The constant target-equivariant gap is a specified three-dimensional clock calibration. It must not be relabeled automatic minimally coupled four-dimensional matter. The missing matter-uplift claim is kept separate for this reason as well as the generalized twist/current term.

## Freeze status

All calculations supporting this scratch record are complete: the one-Killing calibration, generic-jet reduction, old-sector recovery, source obstruction, current-corrected duality and Ward/dust identities have been derived. The two executed scripts pass 309 and15 exact checks respectively. The written fluid Ward/dust derivations are analytic and are not included in those check counts. A separately tasked reviewer is inspecting the raw definitions and scripts. No public repository file has been changed by this task.
