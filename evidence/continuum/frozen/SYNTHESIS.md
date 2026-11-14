# Controlled matter-sector continuum: synthesis for independent review

Research scratch, not public deliverable. The proposed result is a controlled nonlinear matter continuum for an explicitly augmented, localized large-population family at a FIXED finite geometric Galerkin dimension, on a prescribed smooth 2+1 background. It is not a fixed-occupancy refinement of the shipped one-cell regulator, and it does not remove the nonlinear geometric cutoff or quantize Einstein constraints.

## Contract and construction

Fix a finite geometric basis L, a compact physical coordinate patch (or periodic spatial box), a smooth globally hyperbolic prescribed background h with bounded ADM coefficients and positive lapse, a positive rest energy m0, and a finite regular time interval [0,T]. The limiting geometric-mode variables and material trajectories stay inside an interior compact phase-space patch; target lambda and covariance heights remain positive with a fixed margin. Material labels are two dimensional, have smooth density n0 bounded above and below by positive constants, and the Lagrangian flow remains a smooth diffeomorphism with Jacobian bounded away from zero. At fixed L and finite internal cutoff, these hypotheses hold for a nonempty short-time interval by ordinary Banach-space ODE local existence on C^r label maps: the field has finitely many coefficients and the label evolution has no label derivatives on its right-hand side.

The classical comparison is reciprocal: field modes evolve under their Galerkin Hamiltonian plus the integral of parcel energies; parcel centers, momenta and internal states evolve under that same Hamiltonian. The shape is not a prescribed forcing. The background metric is prescribed, and the field equations are Galerkin-projected.

The microscopic architecture adds data absent from the original cell: physical material positions and momenta, transport Hamiltonians, spatial field couplings, and symmetric internal populations. With label mesh h, positive weights mu_j=n0(a_j)h^2, and population N, choose K_j=round(N mu_j) probes in parcel j. Use normalized geometry action N f, parcel action K_j, and total action/energy per N. Thus this is a collective weak-coupling/classical family, not a fixed-hbar, fixed-Newton-constant UV limit. For N h^2 sufficiently large, K_min >= c N h^2.

For each finite regulator, use the positive clock/shift and symmetric-probe construction in MEANFIELD_FINDINGS. The local proper-time probe coupling is the selected oscillator compressed at internal cutoff D. Its finite positive Fourier approximant carries a separately bounded C^r error delta_reg. Positive geometric kinetic approximants and collective mass B >= m0^2 supply a self-adjoint finite quantum Hamiltonian. In a zero-shift ADM chart a positive lapse ordering is sqrt(L B L), whose classical symbol is L sqrt(b); a shift adds its symmetrized polynomial term. This is an explicitly chosen canonical regularization, not a uniqueness theorem for quantization.

The parcel mass is collective:

    H_parcel = K_j sqrt(P_j^2 + [m0 + A_Kj(h_M)]^2).

Its classical limit is sqrt(p^2 + [m0+<h_M>]^2), with the proper-time factor in the internal Schrodinger equation. A single-probe square root has the wrong nonlinear energy closure for generic superpositions; the independent obstruction control records this.

## Stage 1: actual quantum dynamics to reciprocal parcels

For the fixed finite regulator, the bounded-algebra proof gives

    D(t) <= exp(C t)[D(0)+B^2 t/K_min^2].

Explicit coherent/product preparations give D(0)<=Cprep/K_min. Physical bounded observables, source variations, and stress variations have finite cutoff-dependent coefficients Cobs. The square-root Frechet-derivative lemma controls derivatives of the actual microscopic Hamiltonian, rather than assigning a classical source after the limit. It uses the same integral and norm estimate as the commutator lemma, with C=delta B and c=delta b; source and stress variations therefore converge for the declared polynomial external-field variations. Local shear symmetry is recovered only after the cutoff defects vanish; no exact finite-cutoff Ward identity is assumed.

Define A_h,D,reg(T) to include Cprep, exp(CT), B, the finite number of parcels/basis observables, all physical-observable polynomial constants, and the positive-density constant in K_min>=c N h^2. Then, for N h^2>=1,

    delta_quantum <= A_h,D,reg(T)/sqrt(N h^2).

A can be very large and need not be uniform as h,D,reg change. It is obtained from the stated finite coefficient norms, not guessed independent of cutoffs. Taking a supremum over the bounded rounding ratios makes the constant independent of N at fixed h,D,reg.

Internal propagation of chaos follows from the exact symmetric-sector identity

    S_K = 2 beta_K+(D-1)/K,
    ||rho_K^(k)-rho^tensor k||_1 <= sqrt(2k S_K).

Only fixed-k marginals are claimed close to products. No closeness of the entire entangled many-body state to a product is asserted.

## Stage 2: reciprocal parcel quadrature to covariant matter

At fixed geometric L and internal D, the classical common Hamiltonian on field modes and label trajectories is smooth and locally Lipschitz on the declared compact set. Material midpoint quadrature produces

    e_h(t) <= exp(C_T t)e_h(0) + Q_T h^2 [exp(C_T t)-1]/C_T,

with the continuous C_T=0 interpretation. Population rounding contributes an additional O(1/(N h^2)) error to the common field force and hence to paths; it is not merely a direct current-weight error. Finite Fourier/positive approximation contributes O(delta_reg). Constants depend on L,D and the declared smooth interval; no uniform nonlinear L->infinity estimate is claimed.

Before caustics, the label integral of the proper-time worldline/state action is exactly the Brown-type state-fluid action, by change of variables and constrained current variations. It yields the same quantum proper-flow equation, dust stress, and reciprocal target source as CURRENT_AND_RECONSTRUCTION. This proves the matter-action identity and its finite-L reciprocal approximation, not the unprojected Einstein/shape PDE.

## Stage 3: strong quantum current and the contact term

Use a smooth even mollifier of width eta. The quantum current uses the COLLECTIVE internal charge A_K(Q^2/2), not a single-probe operator whose intrinsic quantum variance remains nonzero. Symmetrize the bounded current amplitude with the position kernel: Jhat(x)=sum_j mu_j {K_eta(x-Xhat_j),Bhat_j}/2, where Bhat is the symmetrized collective charge times the Hamiltonian transport velocity, with the prescribed metric-volume factor. This is a declared coarse observable; exact microscopic local current conservation is not asserted at finite cutoffs. Symmetrize the bounded current amplitude with the position kernel. The operator L2 bound uses joint spectral calculus of commuting position operators and does not assume independence of different parcels. For d=2,

    delta_J <= C_T [ eta^2 + h^2 eta^-3
        + delta_path eta^-2 + delta_amp eta^-1
        + (N h^2)^-1 eta^-1 ].

Here delta_path and delta_amp include the quantum RMS error, the positive-polynomial approximation error, the reciprocal classical-grid error where relevant, and the rounding-induced trajectory error. At finite D the observable constants must be absorbed before choosing N. Weak convergence alone is insufficient: the separate oscillatory-current example retains a J^2 defect.

For the symmetrized quadratic current observable,

    |<Jhat^2>-J^2|_L1 <= delta_J (2||J||_L2+delta_J)

componentwise in the bounded prescribed metric. For the lambda-weighted product use the definite order Re< (lambdahat Jhat_a)Psi,(lambdahat Jhat_b)Psi > and the bounded prescribed inverse-metric contraction. Its error is controlled by bounded lambda and its RMS concentration; another noncommuting order is not silently substituted. This proves contact-functional convergence. It does not assert exact finite-N quantum scalar/connection dualization.

Finite oscillator projection does not preserve the full metaplectic shear identity. Its boundary defect must vanish in the ordered internal-cutoff limit; it cannot be silently set to zero at finite D. At fixed geometric L, even after internal removal, the total twist current is conserved only in the retained test space. A full pointwise F=dA reconstruction requires the remaining geometric PDE limit. The strong matter-current result does not remove that obligation.

## An explicit fixed-cutoff diagonal

For fixed L,D and localization data, let 0<s<=1, h=s^5, eta=s^2. Choose the finite polynomial approximation so its induced physical path/amplitude error is <=s^8. Absorb all quantum physical-observable constants into A>=1 and choose

    N >= A^2 s^-26 = A^2 h^(-26/5).

Then delta_quantum <= A/(sqrt(N) h) <=s^8. The main current terms are

    eta^2=s^4,
    h^2 eta^-3=s^4,
    delta_quantum eta^-2<=s^4,
    (N h^2)^-1 eta^-2<=s^12/A^2,
    (N h^2)^-1 eta^-1<=s^14/A^2.

The deterministic path and amplitude O(h^2)=O(s^10) contributions are smaller. Hence current and contact convergence is O(s^4)=O(h^(4/5)) with fixed-cutoff constants. The population choice may be resource-prohibitive; no efficiency is claimed. It is a constructive sufficient diagonal, not an optimal rate or universal physical scaling.

## Internal oscillator removal and the precise endpoint

The separate weighted-moment/Duhamel theorem controls the limiting classical parcel/state system as D->infinity: for finite A^s0 number moments, s0>3/2,

    error_D(T) <= C_T (D-2)^(-s0+3/2),

with C_T independent of D on the compact smooth fixed-L interval. Gaussian data permit the sharper exponential-tail bound in FROZEN_FIELD_FINDINGS. Label derivatives needed for currents are controlled by differentiating the finite-L flow and using correspondingly higher number moments; Gaussian preparations have all those moments.

The safest claim is an ordered, tolerance-based construction on a COMMON regular time interval with strict compact/precaustic margins and the required uniform higher label-weighted number moments. Fix a target tolerance; first choose a mollifier width eta from the true smooth current bias. Choose the internal cutoff D so the weighted classical path/amplitude and label-regularity errors meet the tolerance after the fixed kernel factors are included. Choose h next from the actual fixed-D quadrature constants and the fixed eta. Choose the positive Fourier approximation accuracy AFTER h and eta, so its induced physical path/amplitude error is at most the tolerance times eta^2 divided by the relevant constants. Finally choose N from the actual population/observable constants of that finite polynomial regulator. No fixed approximation error is multiplied by a subsequently divergent kernel factor. Each choice is finite under the stated estimates; all chosen errors tend to zero along a sequence of tolerances. The fixed-D explicit h^(4/5) diagonal above is a useful concrete special case. Do not quote a D-uniform h^(4/5) rate or uniform nonlinear geometric estimate from this bookkeeping.

The endpoint is the nonlinear covariant matter action with full oscillator internal states, coupled reciprocally to a finite set of geometric modes on a prescribed smooth background, before caustics. The nonlinear geometric L->infinity limit and Einstein constraints are not established by this chain.

## A separate full spatial result in the linearized covariant sector

On the exact 2+1 Einstein-dust background h3=−dt²+t²dx², q0=(0,1), probe ground, n=n0/t² and n0 m0=2f, the first-order matter/shape system is reciprocal while density, velocity and metric perturbations may vanish. The augmented quadratic lattice has exact quantum Heisenberg means equal to its classical linear equations. The positive comoving energy is nonincreasing. For smooth initial data with Q²=Σ|k|^6 H_k(0)<infinity, the continuum-energy RMS bound is

    RMS(T) <= (pi/2) delta_initial
      +(pi/24) h^2 log(T/t0) Q +(h/pi)^3 Q.

The pi/2 converts lattice fluctuation energy to continuum energy. The common constant zero-mode is not controlled by this energy seminorm and needs separate initial localization. This removes physical spatial discretization in the declared linearized sector, not in the full nonlinear system. The background carries a generally nonzero corrected twist flux; only local reconstruction is claimed without global bundle data.
