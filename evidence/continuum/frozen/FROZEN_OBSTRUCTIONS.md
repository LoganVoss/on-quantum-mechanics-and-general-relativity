# Independent continuum audit: frozen constraints and controls

This is a scratch mathematical review, completed before public continuum writing. It imports no proposed verifier. The inspected baseline is the existing quantum shape/probe cell in research edition2.0 (package2.0.1). The independent program `verify_obstructions.py` passed28 exact checks, three finite-Fock unitary controls, and five collective-mass expectation controls. This pass does not purport to prove the desired full continuum limit.

## 1. What the existing regulator actually discretizes

The code's `nr=4`, `nt=8`, radius1.2 are polar coordinates on the **target/configuration manifold H²**. Each block is conditioned on a shape matrix M; its other factor is the oscillator Fock space. Increasing these grid sizes or the oscillator cutoff approximates the same single-cell quantum operator on L²(H²) tensor L²(R). These parameters are not physical spatial lattice spacings.

There are no physical particle positions, particle momenta, material labels, number-density variables, or transport currents in that regulator. The declared operator/observable identification therefore does not itself supply the local number current required by the state-fluid model. This is not an abstract Hilbert-space dimension argument (infinite separable Hilbert spaces can be isomorphic); it is a statement about the actual operators, observables, and scaling supplied by this model.

A field/matter continuum construction must explicitly add a physical spatial discretization and transport/material architecture. Introducing those is a model extension, not merely removal of the current two cutoffs.

## 2. An exact raw-refinement energy obstruction

For χ in C_c^infty(H²), with G=v^(-2)(du²+dv²),

 q_G[χ]=∫du dv (|χ_u|²+|χ_v|²),
 ||χ||²_G=∫du dv |χ|²/v².

The one-dimensional Hardy completion is

 |f'−f/(2v)|²=|f'|²−|f|²/(4v²)−(1/2)∂v(|f|²/v)

for real f, and extends by real/imaginary decomposition. Compact support removes the boundary term. Therefore

 −Δ_G >=1/4.

This is also the established bottom of the hyperbolic-plane Laplacian spectrum; the elementary proof gives the lower bound needed here.

Now add K=V/v_cell physical cells covering a volumeV, use the inertia prescribed by a local target kinetic density, I_cell=f v_cell, and retain the nonnegative oscillator excitation term. Even for correlated states across cells,

 H_total >= K hbar²/(8 f v_cell)
          = hbar² V/(8 f v_cell²).

For v_cell=h^d this is O(h^(−2d)); in two quotient spatial dimensions it grows as h^(−4). Positive intercell gradient terms cannot cancel it. Thus the **unsubtracted, fixed-hbar, fixed-f physical-cell refinement has no uniformly bounded total-energy family**. This conclusion does not rule out renormalization, vacuum subtraction, changed scalings, correlated preparations, or another continuum construction. A subtraction coupled to a dynamical metric must itself be included in the action/stress prescription rather than silently discarded.

### Compatible large-N scaling

A natural declared alternative uses geometry inertia N f v_cell and physical probe occupation K_j approximately N n_j v_cell in cellj, with total energy/action divided byN. This preserves each internal probe's proper frequency while keeping normalized matter densityn finite. The normalized kinetic lower bound is then

 E_total/N >= hbar² V/(8 f N² v_cell²).

The scale N v_cell→infinity makes this floor vanish and supplies many probes per populated cell. This is not a dynamical convergence proof.

For independent localized target packets of widthσ around a smooth classical field, the usual local-coordinate initial error estimates are

 normalized kinetic fluctuation = O((N h^d σ)^(-2)),
 spatial gradient fluctuation = O(σ²/h²),

with constants on a fixed compact target patch. Thus a simple sufficient preparation scaling is σ=o(h) and N h^d σ→infinity. For example σ=h^(1+δ), N=h^(−d−1−2δ), δ>0, makes both errors tend to zero. This estimate describes a product-packet preparation, not every correlated quantum field. The constants and dynamical growth must still be controlled in the positive-limit theorem.

UsingN probes in every cell while independently multiplying each probe Hamiltonian by cellvolume is not equivalent: it changes the physical probe frequency. Density, geometry normalization, and the clock must be scaled together.

## 3. Heavy shape alone does not yield a pure-state fluid

Consider the selected quadratic interaction with two frozen shape branches

 M_+=diag(e^r,e^(−r)), M_−=diag(e^(−r),e^r),

an equal coherent shape superposition, and oscillator vacuum in the probe. This is an exact two-branch regulator with vanishing shape kinetic term, the relevant infinite-inertia test. For θ=ωt, the conditional symplectic evolution is

 S_±=cosθ I+sinθ J M_±^(−1),
 N_±(t)=S_± S_±^T.

The average covariance is

 (N_++N_−)/2=[1+2sinh²r sin²θ] I.

Hence the squared overlap of conditional probe states is

 F(t)=1/[1+2sinh²r sin²(ωt)],

and after tracing the shape,

 Trρ_probe(t)²=(1+F(t))/2.

For r=log2 and t=π/(2ω), this purity is exactly25/34, rather than1. The trace distance to the closest pure state is (1−sqrt(8/17))/2≈0.1570028297. The small-time purity loss is ω²sinh²r t²+O(t⁴).

Independent matrix evolution at Fock cutoffs32,48,64 converges to the exact purity with errors1.95e−8,1.63e−11,1.40e−14, respectively. Exact projected quadratic matrix elements are used; truncated Q/P squares are not passed off as exact canonical operators.

This control is a failure of **unprepared deterministic pure-state closure**, not a no-go result for a concentrated semiclassical/mean-field limit. A large inertia alone does not remove a macroscopic superposition of shapes or its conditional probe mixing. Well-prepared concentration and a propagation-of-chaos/state-closure hypothesis are necessary ingredients in a claimed pure-state-fluid route. Smooth narrowly concentrated shape branches can approximate the frozen branch preparation; the control does not rely on assigning a physical position to those shape labels.

## 4. Kinetic limits need not be pressureless one-velocity limits

For two equal relativistic streams of proper densitiesn/2, rest energym and velocitiesu_±=γ(1,±b), 0<|b|<1, their stress in1+1 coordinates is

 T^{ab}=mnγ² diag(1,b²),
 detT=m²n²b²/(1−b²)²>0.

Every pressureless one-velocity stressnε u^a u^b has rankone. It cannot reproduce that tensor, even if its scalar internal energy is adjusted to match the energy component. Thus local density/current convergence alone does not identify the pressureless state-fluid stress.

Monokinetic preparation and a smooth single-valued flow before caustics are essential. The explicit free flow

 x(t,a)=a−t b tanh a,
 ∂_a x=1−tb sech²a

remains a local diffeomorphism for t<1/b and first loses its Jacobian at a=0,t=1/b. A material density is divided by this Jacobian; a smooth pressureless closure cannot simply be continued through that event. This is a kinematic fixed-background control, not a claimed self-gravitating solution.

Primary semiclassical results naturally produce Liouville/Vlasov measures. Additional preparation and regularity are needed to collapse such a measure to a single current and pure internal state. That distinction remains even when the quantum evolution itself is perfectly unitary.

## 5. The current-squared reconstruction term requires strong control

The repaired twist action contains J_aJ^a. Weak current convergence does not determine it. On a periodic spatial coordinate, choose a future timelike current

 J_n^0=j0+a sin(nx), J_n^i=0, j0>|a|.

Then J_n converges weakly to(j0,0), but

 J_n.J_n converges weakly to −j0²−a²/2,

rather than −j0². For smooth test functions the oscillating terms vanish by integration by parts with a1/n bound. The nonzero quadratic defect remains. This is a direct control against passing the contact action or its stress through weak convergence alone.

StrongL² convergence, plus suitable bounded/strong coefficient convergence, suffices:

 ||J_n²−J²||_L1 <= ||J_n−J||_L2 (||J_n||_L2+||J||_L2)

for Euclidean component norms controlling a bounded background metric. The Lorentz contraction is then handled by the metric coefficients.

For independent smoothed particles,

 J_{N,η}(x)=N^(−1) Σ a_j K_η(x−X_j),

the Hilbert-space variance identity gives

 E||J_{N,η}−EJ_{N,η}||²_L2
 =N^(−1)[E||aK_η||²_L2−||E(aK_η)||²_L2]
 <= E|a|² ||K_η||²_L2/N.

In two dimensions, K_η=(2πη²)^(−1) exp(−|x|²/(2η²)) has squared norm1/(4πη²). Thus Nη²→infinity removes this fluctuation term, while η→0 controls smoothing bias for a regular underlying current. This is a sufficient scaling and the generic fluctuation scale; degenerate deterministic preparations need not saturate it. Uniform quantum source moments and dynamical concentration remain additional obligations. Unsmeared delta currents cannot be squared at finiteN.

## 6. Relativistic internal-energy averaging needs a collective architecture

At fixed classical momentum magnitude|p| and geometry, define F(e)=sqrt(p²+e²), e>=m0>0. A single quantum internal mass operator gives expectation E F(m0+h), whereas the Brown-type mean-energy model uses F(m0+E h). These differ in general.

For a two-level internal observable with energies0,2 and equal probabilities, m0=|p|=1,

 E F(m0+h)=(sqrt2+sqrt10)/2 > sqrt5=F(m0+E h),

since the squared left side exceeds5 bysqrt5−2. Center-of-mass WKB alone therefore does not establish the proposed mean internal-mass closure.

A declared composite parcel withN independent internal copies can repair the conditional energy relation. Let A_N=N^(−1)Σh_j, assume h_j>=0 in identical product preparation, meanμ and finite varianceσ_h². Then Var(A_N)=σ_h²/N. Since

 F''(e)=p²/(p²+e²)^(3/2),   0<=F''<=1/m0,

Taylor's integral remainder and Jensen's inequality give

 0<=E F(m0+A_N)−F(m0+μ)<=σ_h²/(2m0N).

The derivative F'(e)=e/sqrt(p²+e²) is the proper-clock factor. It obeys

 E|F'(m0+A_N)−F'(m0+μ)|<=σ_h/(m0 sqrtN).

Because F'''(e)=−3p²e/(p²+e²)^(5/2), |F'''|<=3/m0² and F' is concave,

 0<=F'(m0+μ)−E F'(m0+A_N)<=3σ_h²/(2m0²N).

The checker evaluates five independent binomial preparationsN=1,4,16,64,256 and confirms all three bounds.

These are conditional expectation bounds at a classical symbol, not a propagation theorem for the full quantum relativistic Hamiltonian. Promoting a composite-parcel Hamiltonian N sqrt(p²+[m0+A_N]²) to a rigorous joint dynamical limit requires its heavy physical-center semiclassical calculus and collective-operator commutator remainders. No such result should be inferred from this energy calculation alone.

## 7. Strongest justified route and remaining proof obligations

A viable route preserves feedback by scaling gravity/shape inertia and many internal copies together, while keeping the individual quantum gap fixed. It must explicitly add physical transport variables or material labels; impose well-prepared concentrated/chaotic and monokinetic data; work before caustics on a declared smooth interval; control the unbounded hyperbolic target and oscillator; and pass the corrected current interaction strongly enough.

A theorem at fixed target localization, finite oscillator cutoff, and fixed finite spatial lattice is useful. Its constants must be tracked as those regularizations are removed. Strong-resolvent convergence at each fixedN alone does not justify exchanging the cutoff, N, and spatial limits. Similarly, a Riemann-sum action consistency estimate alone does not prove convergence of solutions or gravitational constraints.

The original quantum cell contains no quantized quotient metrich or Einstein constraint operators. A controlled matter/shape limit on a prescribed background, or conditional on a smooth self-consistent classical solution, must be named as such. It is not automatically an anomaly-free quantum gravitational continuum.

## Primary literature verified for this pass

- Berchio, Ganguly, Grillo, Sharp Poincaré-Hardy and Poincaré-Rellich inequalities on the hyperbolic space, arXiv:1507.02550v4, https://arxiv.org/abs/1507.02550v4. The hyperbolic spectral floor is established; the elementary Hardy argument above is independently supplied.
- Lions and Paul, Sur les mesures de Wigner, Rev.Math.Iberoam.9(1993),553–618, https://ems.press/journals/rmi/articles/5283, https://doi.org/10.4171/RMI/143. Primary semiclassical measure theory produces Liouville/Vlasov transport in its stated settings.
- Golse, Mouhot, Paul, On the Mean Field and Classical Limits of Quantum Mechanics, Commun.Math.Phys.343(2016),165–205, https://arxiv.org/abs/1502.06143v4. Quantitative mean-field/classical estimates for the paper's C^{1,1} potential class; this does not directly cover the unbounded hyperbolic/oscillator coupling without further work.

No public repository files were changed by this review. The findings are constraints on a valid continuum derivation, not a verdict that every controlled augmented limit is impossible.
