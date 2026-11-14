# Independent review of the proposed controlled matter bridge

This bounded review is complete before public continuum writing. No proposed verifier was imported and no public repository file was edited. The review examined the actual finite-algebra proof, curved-kinetic alternative, material quadrature theorem, strong current estimate, oscillator cutoff argument, linearized covariant spatial theorem, and the combined parameter construction.

## Reviewed endpoint

The defensible main endpoint is a nonlinear **matter continuum at fixed finite geometric Galerkin dimension and finite internal cutoff**, on a prescribed smooth 2+1 metric, before caustics. It is obtained from an explicitly augmented, localized, large-population quantum family with physical parcel positions/momenta and collective internal masses. It is not the direct spatial refinement of the earlier one-cell Hamiltonian.

An ordered full-oscillator corollary is conditional on a common regular time interval, strict compact/precaustic margins, and the required uniform higher number moments and label derivatives. A separate result removes the physical spatial lattice in the linearized reciprocal sector on the specified Einstein-dust background. Neither theorem removes the full nonlinear geometric cutoff or quantizes Einstein constraints.

Within these precise contracts, I found no unresolved essential algebraic or estimate discrepancy after the corrections below.

## Main proof checks

1. **Bounded noncommutative algebra.** The ordered telescoping identity is valid: every deviation is placed immediately before the state, with operator prefixes and scalar suffixes. It therefore does not assume commutativity or an unproved factorization. The coefficient constants require both operator norms and classical coordinate magnitudes at most one; the revised statement says so. The Hamiltonian is explicitly self-adjoint with a real classical symbol.

2. **Positive square-root commutator and source.** I checked the resolvent expansion, ordering identity and constants1/(2m0),1/(8m0^3). The extra commutator term is necessary and is included. The same integral represents the Fréchet variation of the actual matrix square root. Polynomial source variations are therefore controlled by the same concentration estimates. Positivity of the root argument is maintained by the stated positive factorization/mass gap. The complete Hamiltonian is manifestly nonnegative in the zero-shift positive construction; an ADM shift is a self-adjoint polynomial contribution, and positivity should not be inferred for an arbitrary coordinate-time vector without an extra condition.

3. **Dynamical deviation inequality.** Exact Schrödinger differentiation gives D'≤2√D(a√D+b/N), hence D'≤(2a+1)D+b²/N² and the stated finite-time Gronwall estimate. Constants can depend on every fixed cutoff and must remain in the diagonal. The proof concerns actual unitary many-body evolution, not only expectation closure assigned afterward.

4. **Internal reduced states.** The symmetric-sector Casimir identity and S_N=2β_N+(d−1)/N hold. I independently checked them for a qutrit basis and two symmetric copies. The fixed-k reduced-state trace bound follows from commuting projection union bounds. It does not imply whole-state norm closeness to a product, and the synthesis does not claim that.

5. **Canonical preparations.** The clock/shift commutator normalization and real embedding are consistent with the declared Poisson orientation. The periodized-Gaussian preparation has an elementary O(1/N) deviation bound with deliberately loose constants. Physical unwrapped positions and target coordinates still require an interior chart or a consistent periodic-distance interpretation; the final contract states this rather than inferring global canonical position operators on a finite torus.

6. **Relativistic parcel and proper clock.** The Hamiltonian symbol sqrt(p²+[m0+<h>]²) yields the proper-time multiplier ε/sqrt(p²+ε²). The ADM Legendre identity, including the minus-shift convention, checks exactly. This requires the new collective-mass architecture; it does not follow from a one-probe quantum mass operator. The nonlinear parcel benchmark had a coherence orientation error that was corrected and independently checked against full-state partial traces.

7. **Curved Hamilton–Jacobi alternative.** The position, kinetic and internal-deviation inequalities and their coefficients rederive correctly. The revised proof requires a global real HJ phase on the whole regularized quantum configuration domain, with its derivative bounds; a phase valid only near the classical trajectory is not enough because quantum states develop tails. This was a necessary domain correction. The bounded-algebra theorem does not depend on this secondary HJ lemma.

8. **Nonlinear material continuum.** At fixed geometric/internal cutoffs, the coupled coefficient/parcel equations are a smooth reciprocal ODE/integral system. Midpoint quadrature plus the actual Lipschitz constants gives the stated h² Gronwall estimate. The field is not prescribed forcing. Population rounding must also enter the trajectory error, not only the direct current weights; it now does. The exact material-to-Eulerian change of variables yields the Brown-type matter action before caustics, with general local flow represented by the Clebsch-capable form.

9. **Strong quantum current.** The operator-valued L² kernel estimate is sound even when position and current amplitude do not commute. It uses the collective internal charge and the actual Hamiltonian velocity/proper-clock observable. A single probe charge would retain O(1) quantum fluctuations and would not satisfy the claimed RMS concentration. The definite lambda/current ordering in the synthesis is retained; no alternate noncommuting contact ordering is silently substituted.

10. **Contact functional.** Strong L² current concentration gives L¹ control of the quadratic current functional by Cauchy–Schwarz. The independent oscillatory-current counterexample explains why weak convergence is insufficient. The claim is convergence of the specified ordered observables; it is not exact scalar/connection duality of the finite quantum regulator.

11. **Internal cutoff removal.** The bandwidth-two commutator estimate for oscillator-number moments is uniform in the cutoff on the compact classical interval. Weighted Duhamel and coupled ODE stability then support the stated conditional classical-Galerkin consistency estimate. Higher label derivatives need corresponding higher weighted number moments. The full metaplectic shear identity fails at finite cutoff; its boundary defect has norm O(D²), supported on the last two levels, and expectation bounded by C D^(2−2s)||A^sψ_D||². Thus s>1 with the uniform moment bound removes it in the ordered limit. This does not make the finite-D Ward identity exact.

12. **Full linearized spatial sector.** The Einstein-dust background and reciprocal tangent Hamiltonian are consistent. The classical mean-energy error estimate rederives with coefficientπ/24 and tail(h/π)^3. Quantum fluctuation energy is nonincreasing in the lattice energy, so conversion to the continuum energy needs the factorπ/2. The statement and receipt were corrected accordingly. The common constant zero mode is only a seminorm direction; separate localization is correctly required for absolute configuration observables. Nonlinear Einstein/geometric-cutoff removal is not inferred from this tangent theorem.

## Combined-limit bookkeeping

The fixed-cutoff diagonal h=s^5, eta=s^2, N≥A²s^(−26), with the actual cutoff-dependent observable/preparation constants inside A, has the stated exponents. Quantum position error≤s^8 produces current error≤s^4; midpoint and mollifier errors are also s^4. Rounding-induced trajectory and direct weight errors are smaller at this scale.

The final tolerance-based order is essential. First choose eta from the true smooth-current bias; choose D with the fixed kernel factors and uniform moment/label margins; choose h from the actual finite-D quadrature constants; then choose positive-polynomial accuracy small enough after h,eta are fixed; choose N last using all resulting finite constants. This avoids multiplying a fixed regulator approximation error by a subsequently diverging eta^−2 factor. No D-uniform h^(4/5) rate follows without additional uniform estimates.

At fixed geometric cutoff, the local shape/twist residual only vanishes in the retained test space. Strong convergence of the matter current and contact term does not by itself prove pointwise total-current closure or reconstruct F=dA. The synthesis explicitly leaves that to the remaining geometric PDE limit.

## Independent executed checks

`review_positive_bridge.py` passes **12 exact identities/matrix identities** and three bounded computational families:

- Six full-state partial traces, N=1,…,6, checking the sign and placement of rho10. Maximum discrepancy1.57e−16; the incorrectly conjugated density differs by a visible O(1) amount.
- Five independent noncommuting positive-square-root generator controls in dimension4.
- One genuinely noncommuting position/amplitude current control, with actual L² error0.7133405653 below bound0.9540151417.

The exact checks include a different internal dimension from the proposed verifier, the ADM proper-time/Legendre identities, a direct total-energy differentiation of the moving reciprocal parcel, and the lattice/continuum energy comparison behind theπ/2 correction.

These finite checks support algebraic implementation. They do not replace the analytic inequalities, prove a full quantum-field continuum by sampling, or constitute external human peer review. The earlier obstruction pass separately records28 exact checks, the purity counterexample, refinement energy floor, multistream and contact controls, and conditional collective-mass bounds.

## Corrections resolved before freeze

- Explicit |y_j|≤1 and Hamiltonian self-adjointness/real-symbol hypotheses.
- The nonlinear parcel's lower-left coherence convention rho10, verified by direct partial trace.
- Global HJ-domain qualification for the exact quantum gauge argument.
- Theπ/2 lattice-to-continuum fluctuation-energy factor and zero-mode qualification.
- Collective, rather than single-probe, current charge and an explicit contact ordering.
- Rounding-induced path errors, finite-D shear defects, and regulator/mollifier tolerance ordering.

No public repository files were modified by this review.
