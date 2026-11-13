# Bounded independent review of extension proposals

This is a research review record, written before public extension authoring. Proposed claims were treated as questions, and supplied PASS labels were not used as mathematical premises. No public repository files were changed and no further reviewer was commissioned.

## Independent execution

`review.py` imports no proposed verifier. It completes **31 exact symbolic checks** in Python 3.12.13 / SymPy 1.14.0. The accompanying `receipt.json` records every residual, the reviewer-source hash, and SHA-256 hashes for the inspected proposal scripts and working proofs.

The check uses different derivation routes where consequential:

- Quadratic coupling is recovered from rotation isotropy and an explicit positive Cholesky frame.
- Ground-band compression is reconstructed from logarithmic-derivative moments rather than differentiating the proposed full product expression.
- Helical quotient curvature is recovered from the warped-product curvature of a conformal two-dimensional base and a circular fiber.
- The sourced curvature-squared witness is obtained by directly varying the four-dimensional metric, connection and Ricci tensor in the original Ricci-squared action. No supplied H2 field equation, lapse-variation implementation, or proposed curvature routine is imported.
- The current-corrected dual action is checked both as a Legendre elimination and by its derivative with respect to the matter current. This explicitly detects the missing contact term.

The independent calculations support the stated exact identities. They do not reproduce every supplied check, the full finite-regulator evolution, or a continuum limit.

## 1. Selected positive quadratic coupling: supported in the stated class

For a centered instantaneous target-only Weyl-ordered quadratic Hamiltonian, positivity and

    K(A M A^T)=A^(-T) K(M) A^(-1)

force K(I) to be scalar by rotational isotropy. Writing M=A A^T then gives K(M)=k M^(-1). Calibrating the oscillator energy gap fixes k=hbar omega>0. A target-invariant scalar offset is constant; subtracting hbar omega/2 fixes the ground-energy reference.

The proof uses no derivative dependence, extra target invariants, background dependence, or spectator fields. In the original two-Killing class a separate area rho allows a gap omega(rho). In the one-Killing target-only class, full target transitivity removes that freedom. This distinction must remain explicit.

The nonquadratic perturbation zeta n_M(n_M-1), zeta>=0, preserves equivariance, the vacuum and first gap, so it is a direct counterexample to uniqueness without quadraticity. The proposal includes this correct limitation. Ordinary Gaussian oscillator dynamics is established structure, not a universal new gravitational interaction.

The script's K=omega M^(-1) is a frequency matrix in its covariance equation, while the physical Hamiltonian's K=hbar omega M^(-1) is an energy matrix. These conventions agree, but public notation should avoid silently interchanging them.

## 2. Exact ground-band compression and leakage: supported as an instantaneous law

For H=kappa(-Delta_G)+Hprobe, kappa=hbar^2/(2I), and normalized initial state chi(M)psi_M(x) with chi smooth compactly supported,

    P H P chi = kappa[-v^2(chi_uu+chi_vv)-i v chi_u/2+5chi/16].

The Berry convention A=-du/(4v) makes this kappa(-Delta_A+1/4). With measure du dv/v^2,

    D=v(partial_v-i partial_u)+1/4,
    Ddagger=-v partial_v-i v partial_u+5/4,
    P H P=kappa Ddagger D.

The independent calculation recovers

    Q H(chi psi)=kappa v Dchi (x^2-1/(2v))psi,
    ||Q H(chi psi)||^2=kappa^2 ||Dchi||^2/2=kappa E/2,

where E=<chi psi,H chi psi>. Strong differentiability of the unitary on D(H) then gives

    ||Q exp(-itH/hbar)(chi psi)||^2=E t^2/(4I)+o(t^2).

This is an exact small-time coefficient. It is not an all-time equality, a claimed finite-time bound, or a uniform limit as omega tends to infinity. The pointwise projection P is bounded; compact-support Gaussian packets lie in the required operator domain because the differential expression applied to them is square integrable and the form integration-by-parts identity identifies that operator action.

The condition Dchi=0 makes v^(1/4)chi holomorphic. Compact support then forces chi=0. Thus no nonzero packet in this class is an exactly invariant ground-band state. Treating P H P as the exact autonomous joint evolution would contradict this off-band term.

## 3. Continuum directional-response observable: precision repair resolved

The matched full-energy spectral-measure argument is valid: a jointly acting target isometry and metaplectic unitary commute with the positive form-defined Hamiltonian, and the radial initial shape packet is invariant. The two initial joint states therefore have identical energy spectral measures, not merely equal energy means.

However, the initially stated continuum observable X1=sinh(r) cos(theta) is unbounded. A compactly supported initial state makes the formal double commutator finite, but that alone does not prove that <X1> exists for the evolved state on an interval, or justify differentiating an unbounded expectation. No exponential-moment propagation argument was supplied. This is a proof-domain gap, not a demonstrated counterexample to the coefficient.

There is a direct exact repair. Choose a smooth radial cutoff zeta equal to one on a neighborhood of the initial packet support and zero outside a larger finite target ball. Use the bounded observable

    O=zeta(r) X1.

It remains odd under the quarter-turn symmetry. On the initial support it and its derivatives equal X1, so its initial acceleration is exactly the proposed

    +/- hbar omega (1+kappa_packet) sinh(r_probe)/(2I).

For bounded O and initial vector in D(H^2), the second expectation derivative follows directly from the strong unitary Taylor expansion. The cutoff therefore preserves the claimed measurable initial-response coefficient while removing the unproved unbounded-observable assumption. All-time opposite responses also follow for this bounded O from symmetry. The finite-grid observable is already bounded and is unaffected.

The need to control unbounded-observable domains is standard; see the primary result of Friesecke and Schmidt, *A sharp version of Ehrenfest's theorem for general self-adjoint operators*, https://arxiv.org/abs/1003.3372v1, theorem 1 in https://arxiv.org/html/1003.3372. The cutoff repair here follows directly from locality and the strong Taylor expansion. The proposing agent has now applied this bounded-observable formulation to the final scratch proof and verification metadata; the reviewer confirmed that update. No later-time unbounded X1 expectation is claimed.

## 4. One-Killing helical calibration: supported with changed dictionary

The independent warped-product calculation reproduces, for lambda=1+Omega^2 r^2 and chi=2Omega T,

    Ric_TT=2Omega^2/lambda^2,
    Ric_rr=2Omega^4 r^2/lambda^2,
    Ric_xx=0,

and the target equations and twist relation for A=Omega r^2 dx/lambda. The two metric residuals invert to

    f-w=lambda(E_TT+E_rr)/(2Omega^2),
    V=(E_TT-E_rr)/lambda.

For Omega!=0 and r>0, full chart stationarity therefore selects w=f and V=0 within the proposed invariant constant-coefficient class. Positive nondegenerate target energy selects f>0. Omega=0 genuinely loses sensitivity to the relative weight.

The action permits arbitrary fields of all three quotient coordinates even though the particular calibration is highly symmetric. This is a genuine enlargement of the action's field space beyond the two-Killing sector, not an example of a generic solution with exactly one symmetry. Full SL(2,R) target invariance, total derivative order <=2, no extra fields, and the Einstein-frame dictionary remain assumptions.

The new target matrix represents Killing norm and twist. It is not the old two-orbit shape matrix. The old cylindrical dynamics are recovered only after the explicitly stated further symmetry reduction and dualization.

The off-shell reduction identity is consistent with the independent conformal calculation: q=lambda^(-1)h, followed by a one-fiber reduction, gives

    R4=lambda R3+Box_h lambda-3(dlambda)^2/(2lambda)-lambda^3 F^2/4.

Multiplying by sqrt(-g4)=sqrt(-h)/lambda produces exactly the proposed Einstein-frame bulk density plus div(grad log(lambda)). Correct scalar dualization requires its first-order term; direct substitution into the gauge kinetic density would give the wrong sign.

## 5. Sourced twist: repair and contact term are necessary and consistent

A generic chi-dependent oscillator expectation sources the twist equation. Consequently the vacuum formula F=-lambda^(-2) star dchi is not closed in general. The proposal's explicit positive unimodular probe example with nonzero partial_chi E correctly demonstrates the obstruction.

The shear dressing Psi=exp(i chi Q^2/2) psi_tilde removes chi from the oscillator Hamiltonian and contributes -hbar<Q^2/2>dchi to the state Berry action. For the specified smooth state fluid, J is independent of the auxiliary one-form v during algebraic elimination. It can depend on h,j,psi_tilde and must be varied with those dependencies afterward.

The master density

    -f v^2/(2lambda^2)-J.v+f v.star F

gives v=lambda^2(star F-J/f), and its elimination yields

    -f lambda^2 F^2/4-lambda^2 J.star F+lambda^2 J^2/(2f).

The independent review confirms both the action and its J derivative: delta Ldual/delta J_a reproduces -v^a. If the contact term is omitted, the current equation differs by a nonzero lambda^2 J/f contribution. The cross term and contact term are therefore compulsory, not optional interpretive additions.

The generalized conserved current f lambda^(-2)dchi+J gives a closed F locally; global periods/bundles remain separate. Delta-supported worldline J makes J^2 undefined without a regularization. The smooth-current/finite-regulator qualification is necessary.

The state-fluid stress and Ward identities are consistent with direct metric/current variation: T_ab=n epsilon u_a u_b, with reciprocal scalar-force exchange. They establish a local covariant variational model, not global absence of caustics.

## 6. Clock and quantization boundaries must not be merged

Three levels are currently distinct:

1. A fully quantum positive shape/probe cell, and its tested finite-volume/Fock regulator.
2. A classical geometry coupled reciprocally to a variational quantum state, including the finite-cell semiquantum ODE and smooth state-fluid source action.
3. A reconstructed four-dimensional metric with generalized twist/current coupling.

No derivation of level 2 as a controlled continuum or mean-field limit of level 1 has been provided. No ordinary minimally coupled four-dimensional matter action whose reduction yields level 2 has been proved. The one-Killing field theory also does not quantize all gravitational constraints.

The clock issue independently prevents silently identifying the source with a minimal 4D oscillator: for a horizontal curve, d tau4=lambda^(-1/2) ds3. A fixed 4D proper-time gap therefore becomes lambda-dependent in the Einstein-frame 3D clock. The selected constant gap is a declared 3D calibration, as the revised scratch proof now states.

These are scope boundaries, not contradictions within the individual models. Public integration should present a compatible family of explicitly related constructions with open limit/uplift obligations, rather than assert one derived fully quantum spacetime theory.

## 7. Full-4D curvature-squared sourced selector: independently supported

Use the normalized action (2kappa)^(-1) integral sqrt(-g)[R+alpha R^2+beta Ricci^2+gamma Euler4]+S_m, with the same physical metric, fixed minimal matter actions and fixed calibrated source configurations.

An independent Weyl variation gives trace(H_R^2)=6Box R and trace(H_Ricci^2)=2Box R. The dust scale factor a=t^(2/3) gives R=4/(3t^2), Box R=-8/(3t^4), so retaining the same Einstein-dust solution requires 3alpha+beta=0.

For the charged electrovac f=1-2/r+1/(4r^2), the independent review directly perturbs the lapse in the raw Ricci-squared action while retaining the radial metric independently. It recovers

    H_Ricci^2 mixed(t,t)=-3(4r^2-8r+1)/(4r^8),
    H_Ricci^2 mixed(t,t)|r=3=-13/8748.

The scalar curvature vanishes, so the R^2 contribution is zero. Retaining the same calibrated Maxwell source then forces beta=0, and the dust condition forces alpha=0. The two-response determinant is 52/2187, nonzero. The constant Euler coefficient remains bulk-invisible.

This strengthens discrimination in a finite specified action class using extra sourced calibration premises. It does not derive those source assumptions from the original vacuum selector, exclude arbitrary higher operators/nonlocal terms, or constitute an empirical bound on measured Wilson coefficients. The fixed metric/source prescription is essential because field redefinitions can move curvature terms into matter interactions. The chosen calibrations happen to be symmetric, but variation of the action is unrestricted four-dimensional; a nonzero lapse variation alone suffices to demonstrate failure of stationarity.

## Verdict and remaining obligations

The reviewed exact identities and conditional selectors are supported by independent calculations. The local-observable repair in section 3 has been incorporated and independently confirmed before public authoring. No unresolved algebraic failure was found in the reviewed integration points. The scope obligations below remain explicit limits, not completed bridges.

The strongest defensible combined claim is: a calibrated target-equivariant quadratic interaction and a one-Killing inverse calibration admit explicit reciprocal quantum/variational constructions, exact band compression and initial leakage, a consistent current-corrected twist duality, and a separately conditioned full-4D curvature-squared discriminator. This is a set of precise model-level extensions. It is not yet a controlled interacting quantum-gravity continuum, a derived minimal four-dimensional quantum matter theory, or experimental evidence.

The reviewer has not re-executed the supplied regulator evolution or all reported source checks. Those remain separately labeled executions by their owning verifiers. No worldwide novelty assessment or external peer review is claimed.
