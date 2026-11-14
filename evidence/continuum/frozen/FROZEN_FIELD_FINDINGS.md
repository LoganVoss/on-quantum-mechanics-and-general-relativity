# Frozen spatial/material continuum findings

Scratch research record, not a public deliverable. All calculations in this note were completed before public authoring. The branch establishes a nonlinear reciprocal **material continuum at fixed geometric Galerkin cutoff**, strong current/contact convergence, internal Gaussian-cutoff control, and a full smooth **linearized spatial continuum** on an exact covariant dust background. It does not establish nonlinear removal of the geometric cutoff or the full constrained quantum-gravity continuum.

## 1. What cannot be obtained from the shipped cell by refinement alone

The existing 4-by-8 grid discretizes the configuration target H² of a single quantum shape degree of freedom. It is not a lattice in physical space. Refining that grid and the oscillator cutoff approximates the single-cell operator on L²(H²)⊗L²(R). The number-current, worldline position, velocity, and neighboring spatial-gradient variables required by the state-fluid model are absent.

Even tensoring independent cells does not supply the missing dynamics. For H=Σ_i H_i and operators O_i,B_j supported at distinct sites, [O_i(t),B_j]=0 exactly for every regulator size and every t. A limit preserving these local-response observables cannot acquire a nonzero off-site retarded response. The selected wave-map action has a spatial principal part and does have such responses. A spatially coupled family and transported matter variables must therefore be specified as additional microscopic structure.

The large-population construction used by the parent is also a new controlled scaling: f_N=Nf, extensive parcel populations Nn0, and normalized energy/action divided by N. It is a collective classical/weak-gravity scaling, not a fixed-hbar, fixed-Newton-constant ultraviolet continuum.

## 2. Material trajectories give the covariant state-fluid action exactly

Let a range over a compact two-dimensional material domain A with positive smooth weight w(a). Let X^a(t,a)=(t,X(t,a)) be smooth future timelike worldlines. Before caustics assume each X_t is a diffeomorphism, with det D_aX≥j_*>0, and b(t,a)=sqrt(-h_ab(X) dotX^a dotX^b)≥b_*>0. The metric h is a prescribed smooth Lorentzian 2+1 background in this theorem.

Introduce a normalized internal state psi(t,a) with selected Hamiltonian h_q. The material action is

 S_mat=∫dt∫_A da w(a)[i hbar<psi|dotpsi> - b(m0+<h_q(X)>)]

plus the particle-number phase boundary term. A symmetrized real Berry term may be used. Define Eulerian fields through the inverse material map:

 j^0(t,X)=w/det D_aX,
 j^i=j^0 dotX^i,
 n=j^0 b/sqrt(-h),
 u^a=dotX^a/b,
 Psi(t,X)=psi(t,a).

Changing variables dx=(det D_aX)da gives exactly

 S_mat=∫d³x[j^a i hbar<Psi|partial_aPsi> - sqrt(-h)n(m0+<h_q>)]

with ∂_a j^a=0 identically. Adding the usual velocity-potential/Clebsch representation gives the Brown-type action already stated in the repository. General material trajectories correspond locally to the Clebsch-capable version; a single potential alone is a restricted subclass. The state equation is i hbar dpsi/dtau=h_q psi. The matter stress is n epsilon u_a u_b and its source/force law is the existing variational one. This is an exact pre-caustic coordinate/variational equivalence, not yet a quantum limit.

In ADM coordinates h=-L²dt²+gamma_ij(dx^i+beta^i dt)(dx^j+beta^j dt), a parcel has canonical Hamiltonian

 H_par=L sqrt(gamma^ij P_iP_j+[m0+<h_q(X)>]²)-beta^iP_i.

The internal equation has multiplier L epsilon/sqrt(gamma^ijP_iP_j+epsilon²)=d tau/dt. The separate large-N composite-parcel analysis is needed to derive this expectation-inside-square-root mass law: a single quantized rest-mass operator does not produce it for arbitrary internal superpositions.

## 3. A nonlinear reciprocal material continuum with a fixed geometric cutoff

Choose a fixed finite smooth spatial basis for the shape field q_c(x), including a constant twist-shift mode. Restrict the selected shape action to this basis on fixed h. On a compact regular region of coefficient/particle/internal-state phase space its positive finite mass matrix is invertible, and the resulting Hamiltonian vector field is smooth. Use either finite internal dimension D or the exact centered Gaussian state coordinates (u,v), with v bounded away from zero on the declared interval. The latter remain an invariant internal family under a classical quadratic Hamiltonian.

After canonical reduction, write the common reciprocal equations as

 dot z=F(z,t)+∫_A w(a)G(z,xi(t,a),t) da,
 dot xi(t,a)=V(z,xi(t,a),t),

where z contains all retained shape coefficients/momenta and xi contains parcel position/momentum/internal state. G is the derivative of the same parcel Hamiltonian that generates V; thus q is not a prescribed external shape. The metric h remains prescribed. Smooth cutoffs outside a compact regular neighborhood may be used to obtain global Lipschitz extensions; they are inactive for the sufficiently close trajectories under consideration.

Partition A=[0,1]^d into midpoint cells of width h, a_j their centers, and m_j=h^d w(a_j). The discrete reciprocal equations replace the integral by Σ_j m_jG and use the same V for each parcel. Let xi(t,a_j) be the continuum-label solution sampled at the nodes. Assume

 |F(z)-F(z')|≤L_F|z-z'|,
 |G(z,xi)-G(z',xi')|≤L_G(|z-z'|+|xi-xi'|),
 |V(z,xi)-V(z',xi')|≤L_V(|z-z'|+|xi-xi'|),

throughout the regular region, and W_h=Σm_j≤W_*. Define

 Q_T=(1/24)Σ_l sup_[0,T]×A ||partial_a_l²[w(a)G(z(t),xi(t,a),t)]||,
 C=L_F+W_*L_G+L_V.

With E_h=|z_h-z|+max_j|xi_j-xi(t,a_j)|, the upper Dini derivative satisfies

 D⁺E_h≤C E_h+Q_T h².

Therefore

 E_h(t)≤exp(Ct)E_h(0)+Q_T h² [exp(Ct)-1]/C,

with the obvious t limit for C=0. This is a genuine nonlinear feedback convergence theorem at fixed geometric basis/cutoffs. It is not the assumption of a desired response trajectory.

Proof: subtract the coefficient equations, add/subtract the sampled continuum integrand, apply the midpoint-rule remainder and the stated Lipschitz constants. The node ODE difference is bounded by L_V times the joint error; the two inequalities sum to the displayed one. The quadrature constant is explicit. If A1=sup|partial_a xi| and A2=sup|partial_a²xi|, each second derivative of wG is bounded by

 ||w''|| G0 +2||w'||G1 A1+||w||(G2 A1²+G1 A2).

The material ODE gives A1(t)≤A1(0)exp(L_Vt) and the usual inhomogeneous Gronwall bound for A2 from bounded D²V. The same differentiated ODE controls the C¹ difference of the continuous flow extension generated by z_h, so a strict pre-caustic Jacobian margin persists for small h. The constants can depend on the retained geometric cutoff, internal cutoff, localization and time; no cutoff-uniform nonlinear field estimate is asserted.

The limit action is exactly the Brown state-fluid action coupled to the **Galerkin-projected** shape equations. Its matter Ward identity is exact. The full local wave-map residual need not vanish outside the retained test space. In particular, full local d(*C)=0 and F=dA reconstruction do not follow merely from a fixed-basis limit; global/retained-mode shift conservation is weaker. Removing the geometric cutoff remains a separate PDE stability problem.

## 4. Strong current and current-squared control

Weak empirical convergence alone is insufficient for the J² contact term. Let K_eta(x)=eta^-d K(x/eta) be a smooth even normalized mollifier, with finite second moment and square-integrable derivatives through order two. For a smooth limiting current J and a pre-caustic C² material flow, form the componentwise smoothed empirical current from the same material weights and current amplitudes. Fold all h_ab, sqrt(-h), proper-clock, velocity, and internal expectation factors into the smooth amplitude. On a fixed regular coordinate patch the physical and coordinate L² norms are equivalent.

Let delta_path bound the parcel position error and delta_amp bound all current-amplitude errors (including velocity, number weight, metric factors and internal state, not only psi). Midpoint quadrature in the Banach space L²_x gives

 ||J_h,eta-J||_2 ≤ C[eta²+h² eta^(-d/2-2)
                         +delta_path eta^(-d/2-1)+delta_amp eta^(-d/2)].

The first term is the symmetric-mollifier bias. Two material derivatives bring at most two spatial derivatives of K_eta, whose L² norm scales eta^(-d/2-2). Translation is L²-Lipschitz with ||grad K_eta||_2, giving the path term. The amplitude term uses ||K_eta||_2. Exact constants are products of the declared kernel norms and the uniform C² material/metric bounds.

For d=2, eta=h^(2/5) and classical reciprocal parcel error O(h²) give

 ||J_h,eta-J||_2=O(h^(4/5)).

Consequently

 ||J_h,eta²-J²||_1 ≤ (||J_h,eta||_2+||J||_2)||J_h,eta-J||_2

(up to the bounded inverse-metric contraction factor). Thus the necessary contact functional converges strongly enough. This controls the limiting contact expression; it does not declare an unregulated square of a point current meaningful or an exact finite-particle quantum dual action.

### Quantum RMS version, including ordering

Let Xhat_j have jointly commuting position components, let Bhat_j be a bounded self-adjoint current amplitude, and compare with classical X_j,b_j. Define the symmetrized current

 Jhat_eta(x)=Σ_j m_j {K_eta(x-Xhat_j),Bhat_j}/2.

For the state Psi suppose RMS position and amplitude deviations are delta_X,j and delta_B,j. Spectral calculus gives exactly

 ∫||K_eta(x-Xhat_j) phi||² dx=||K_eta||_2² ||phi||²,

 ∫||(K_eta(x-Xhat_j)-K_eta(x-X_j))Psi||² dx
       ≤||grad K_eta||_2² <|Xhat_j-X_j|²>.

Use K(B-b)+b(K-K_cl) for the first operator order and B(K-K_cl)+K_cl(B-b) for the second. The triangle inequality then yields

 ||(Jhat_eta-J_classical,eta)Psi||_[L²_x H]
 ≤Σ_j m_j[||K_eta||_2 delta_B,j
       +(||Bhat_j||+|b_j|)||grad K_eta||_2 delta_X,j/2].

No statistical independence or commutation of B with X is needed. A bounded symmetrized velocity/charge product has the required RMS bound by telescoping its factors. This theorem requires the full RMS controls, not merely agreement of means.

For bounded lambda_hat and controlled RMS lambda error, the same argument bounds the ordered field lambda_hat Jhat-lambda J. If that L²_xH error is delta_F, then the difference between the symmetrically contracted quantum quadratic-current expectation and its classical value is at most

 ||h^-1||_infinity delta_F(2||lambda J||_2+delta_F).

This is convergence of declared ordered observables, not a claim that classical scalar/vector dualization is an exact identity of the finite-N quantum theory.

In d=2, eta=h^(2/5), requiring RMS errors delta_X,delta_B≤A_h/sqrt(N h²) and choosing

 N≥A_h² h^(-26/5)

makes the path term O(h^(4/5)); amplitude errors are smaller. Integer parcel-count rounding has TWO effects. Its total weight discrepancy is O(1/(N h^d)); this directly contributes C/[N h^d eta^(d/2)] to the current, and it perturbs the reciprocal coefficient/parcel ODE, producing path and amplitude errors O(B_T/(N h^d)) through the same classical Gronwall estimate. Those dynamical errors must also be inserted into the eta^(-d/2-1) and eta^(-d/2) terms. For d=2 and the stated N scaling, the path-rounding contribution is O(h^(12/5)) and the direct weight term is O(h^(14/5)), provided A_h also dominates the relevant classical amplification constants; both are smaller than h^(4/5). A_h must retain its actual time/cutoff dependence; this is not an efficient or uniform fixed-parameter quantum-field limit.

## 5. Removing the internal cutoff on Gaussian classical paths

For a compact classical target path and bounded proper-clock factor, the quadratic Schrödinger dynamics preserve centered pure Gaussianity. Write their squeezing magnitude r(t). The symplectic flow bounds r(t)≤r0+∫||omega dot_tau J M^-1||dt. On a fixed finite interval this gives a finite r_* and theta=tanh(r_*)<1. In the reference Fock basis, odd coefficients vanish and |c_n(t)|≤theta^(n/2). Therefore

 ||(1-P_D)psi(t)||≤theta^(D/2)/sqrt(1-theta).

The quadratic operator connects only n to n,n±2. If its off-diagonal a² coefficient has magnitude at most B, then

 ||P_D H(1-P_D)psi||≤B(D+2) theta^(D/2)/sqrt(1-theta).

Duhamel's formula for the Galerkin evolution, including normalized projected initial data, gives the safe norm bound

 ||psi_D-psi||≤[3+B T(D+2)/hbar] theta^(D/2)/sqrt(1-theta).

The same estimate holds for rays if a different Gaussian gauge is used. For vacuum initial data the initial tail vanishes and the leading 3 can be replaced by 1. The numerical control uses this tighter special case.

For quadratic source/current observables A, decompose into P_D/Q_D blocks. A_D has norm O(D), its boundary blocks have norm O(D), and Gaussian weighted tails sum explicitly. A safe bound has the form

 |<A>_D-<A>|≤32 C_A(D+2)[3+B T(D+2)/hbar]
                    theta^(D/2)/(1-theta)^(5/2),

where C_A bounds the diagonal, pair-creation/annihilation and scalar coefficients of A. No finite-dimensional exact CCR is asserted.

For reciprocal finite-Galerkin classical feedback this can be extended by weighted state error. Let Nop=a†a+1. Since H_D connects n↔n±2 with coefficients O(n+1),

 d<Nop^(2s)>_D/dt ≤C_s <Nop^(2s)>_D

with C_s independent of D for compact target coefficients; this follows by bounding the polynomial differences of neighboring diagonal powers and 2|ab|≤|a|²+|b|². For e_D=psi_D-P_Dpsi_true, commutator estimates and Duhamel give

 d||Nop e_D||/dt ≤C||Nop e_D||+C|delta classical variables|
                         +C D² theta^(D/2).

The quadratic-source error is bounded by the same weighted norm plus Gaussian tails. Coupling this to the finite-dimensional geometry/parcel ODE and using compact-region bootstrap yields C_T D²theta^(D/2) convergence. Uniform label regularity requires the analogous finite weighted derivatives of the initial states; smooth Gaussian label data supply them. This is an ordered classical-limit/internal-cutoff result at fixed geometric cutoff. It is not uniform control of arbitrary entangled finite-N states as D→infinity; the large-N step must retain its D-dependent constants.

### Hard Fock cutoffs do not preserve exact shear covariance

At finite D, h_D=P_D h_M P_D is generally not exactly conjugated by exp(i chi P_D Q² P_D/2). The compressed commutator identity contains boundary terms:

 [P h P,P G P]-P[h,G]P = -P h(1-P)G P+P G(1-P)h P, G=Q²/2.

For quadratic h,G these terms are supported on the last two retained Fock levels and have norm O(D²). They need not vanish in operator norm as D increases. Their expectation on states with a uniform weighted number moment obeys a bound C D^(2-2s)||Nop^s psi_D||² for s>1, and the Gaussian tail controls are stronger. Thus the full selected Gaussian shear/current Noether identity is recovered in the ordered D→infinity limit, not exactly in every finite-D regulator. The finite-D current is a defined bounded observable; it is not automatically an exactly conserved Noether current. At a fixed geometric Galerkin cutoff, even after D removal, only projected twist closure is available until the geometric field cutoff is removed.

The checker includes an explicit D=6, chi=1/3, lambda=2 nonzero compressed-shear defect with vanishing lower retained block. This is a negative control, retained rather than hidden by describing every cutoff as exactly equivariant.

## 6. Full smooth linearized spatial continuum on an exact covariant background

There is a stronger full-spatial result in the tangent sector. Use the exact 2+1 Einstein-dust background

 h3=-dt²+t²(dx²+dy²),  n=n0/t²,  q0=(chi=0,lambda=1),
 probe ground ray,  n0 m0=2f, t≥t0>0.

With ground excitation energy subtracted, Einstein_00=1/t² and Einstein_ij=0, so 2f Einstein=T_m. At first order, excitation energy, shape stress, and matter force are quadratic in perturbation amplitude. Density, velocity and metric perturbations can therefore remain zero consistently while the coupled shape/internal perturbations evolve.

Let q=(chi,delta lambda), z=(u,delta v), J=[[0,-1],[1,0]]. The exact first-order equations are

 q_tt+(2/t)q_t-t^-2 Delta_x q=-(g0/t²)(q-z),
 z_t=2omega J(q-z),  g0=n0 hbar omega/(2f).

The quadratic action is

 L2=∫[f t²|q_t|²/2-f|grad q|²/2
          +n0 hbar z2 dot z1/4-n0 hbar omega |q-z|²/4]dx.

For p=f t²q_t, each Fourier mode has positive Hamiltonian

 H_k(t)=|p|²/(2f t²)+f|k|²|q|²/2+c|q-z|²/2,
 c=n0 hbar omega/2.

Its quantum Heisenberg first moments satisfy the same linear equations exactly under the corresponding canonical commutators. At collective scale N, [q,p]=i hbar/N and [z1,z2]=4i/(Nn0) for normalized action multiplied by N. This is the quantization of the quadratic tangent theory, not an unproved exact finite-amplitude identification with the nonlinear microscopic Hamiltonian.

The work identity is H'_k=-|p|²/(f t³)≤0. Quantum centered fluctuation energy obeys the same nonincrease law. On a periodic spatial domain, centered lattice differences replace |k|² by

 k_h²=Σ_i [2 sin(k_i h/2)/h]²,
 0≤|k|²-k_h²≤h²Σ_i k_i⁴/12.

On resolved modes, |k_h|≥2|k|/pi. With spectrally projected initial data, let H_e,k be the continuum energy of the mean-solution difference. Its forcing is delta p'=-f(k_h²-|k|²)q_h, hence

 d sqrt(H_e,k)/dt ≤ |k_h²-|k|²| sqrt(H_h,k(t0))/(t |k_h|).

Since H_h,k(t0)≤H_k(t0),

 sqrt(H_e,k(T))≤(pi/24)h² log(T/t0)|k|³ sqrt(H_k(t0)).

Zero modes have zero symbol error and are treated exactly at the level of their mean equations. The energy is a seminorm on the common constant configuration q=z,p=0. A claim about all configuration observables also requires initial localization of that zero mode and its separate finite-dimensional covariance propagation; the energy estimate alone does not control its absolute configuration variance. If

 Q²=Σ_k |k|⁶ H_k(t0)<infinity,

summing the resolved bound and using the spectral tail gives the full-field energy bound

 sqrt(E_mean_error(T))≤(pi/24)h²log(T/t0)Q+(h/pi)³Q.

If initial quantum centered fluctuation energy measured in the LATTICE energy H_h is at most delta_initial², positivity and exact quadratic evolution make that lattice fluctuation energy nonincreasing. On resolved modes H_k≤(pi²/4)H_h, since |k_h|≥2|k|/pi and the remaining positive kinetic/coupling terms are common. Therefore the CONTINUUM-energy RMS estimate is

 sqrt(E_quantum_RMS_error(T))
 ≤(pi/2)delta_initial+(pi/24)h²log(T/t0)Q+(h/pi)³Q.

The pi/2 conversion is essential unless delta_initial was already defined with that inflation. The same conservative factor is valid if an initial continuum-energy envelope is supplied. The zero-mode energy remains a seminorm; separate initial zero-mode localization and finite-dimensional covariance propagation are required for absolute configuration-observable convergence.

This is a controlled full smooth **linearized** spatial continuum, including mutual shape/internal response, on an actual Einstein-dust background. Nonlinear geometric-cutoff removal is not inferred from it. The collective preparation must make delta_initial→0; refining a fixed-hbar independent-cell state does not do so automatically.

### Background and linear twist closure

The matched probe ground state still has <Qhat²/2>=1/4. Thus J^0=hbar n0/(4t²), and the corrected local connection has F12=-hbar n0/(4f), a closed nonzero background flux. The shifted curvature F+*J/f vanishes when chi is constant. On a torus the flux need not be globally exact; global bundle/quantization input is not supplied. The statement is a 3D covariant background plus local reconstruction, not a global 4D zero-twist claim.

At first order delta J^0=-hbar n0 z2/(4t²). The coupled chi and z2 equations make partial_a(sqrt(-h)C^a)=0 exactly. Thus the tangent dynamics retain the repaired-current consistency, rather than quietly reverting to the vacuum twist map.

## 7. Executed bounded verification

`verify_field_continuum.py` passes 92 exact symbolic identities plus five finite computational families:

1. All nine 2+1 Einstein-dust components, the reciprocal quadratic Hamiltonian generator/work identity, linear total-current closure, scaling identities, and a hard-Fock shear-boundary negative control.
2. Spatial grids16,32,64,128 for Fouriermode(1,2) on t∈[1,2]: observed endpoint orders2.01054,2.00282,2.00072; actual energy errors lie below the analytic energy estimate. This checks the scheme/coefficients, not the proof of an infinite-dimensional theorem by sampling.
3. Nonlinear reciprocal label evolution with one homogeneous retained shape mode, material midpoint grids4,8,16,32, compared with independent16/24 Gauss quadratures: errors1.59047e-4,3.97947e-5,9.95074e-6,2.48781e-6, orders1.99881,1.99970,1.99993. Geometry is dynamically driven by all probes. The h3 background is prescribed; this finite-amplitude example is not a new full Einstein solution.
4. Strong mollified current/contact Fourier-aliasing control for J0=2+0.3cosxcosy on the torus; decreasing L² current errors at eta=h^.4. The theory provides the rate, while this finite control exercises smoothing and the quadratic functional.
5. Independent Fock Galerkin control along an exact constant-M Gaussian path, cutoffs8,12,16,24,32. At24 the covariance error is7.65814e-11; at32 it is9.99201e-15. All ray errors satisfy the stated tail-Duhamel bound. The printed ray error at32 is numerical zero from floating-point cancellation, not an exact identity.

All computations use Python3.12.13, SymPy1.14.0, NumPy2.3.5, SciPy1.17.0. The script imports none of the earlier research verifiers. No public repository files were changed by this branch.

## 8. What remains unresolved

The controlled results above do not prove nonlinear removal of the physical geometric Galerkin cutoff, uniform ultraviolet estimates for the full quantum field, full Einstein-constraint propagation under that removal, a continuum microscopic measurement theory, or a minimally coupled four-dimensional matter uplift. The exact matter-action equivalence does not create degrees of freedom absent from the starting regulator. The prescribed additions and collective scaling must be named in any final claim.

Primary precedents checked: Brown's relativistic fluid action, https://arxiv.org/abs/gr-qc/9304026v1; Dobrushin, Vlasov equations (1979), DOI10.1007/BF01077243, and Iacobelli's primary analysis of Wasserstein stability https://doi.org/10.1007/s00205-021-01705-9; Carles–Nouri, monokinetic limits before caustics, https://arxiv.org/abs/1506.07339. These establish broader frameworks, not the complete specific quantum-gravity limit requested here. All finite-mode estimates and the particular coupled tangent equations above are explicitly derived; worldwide priority is not asserted.
