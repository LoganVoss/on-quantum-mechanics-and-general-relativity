# Controlled large-population quantum bridge — research derivation

Scratch mathematical record; no public repository files were edited. This result concerns an explicitly augmented, localized regulator family. It is not a spatial-refinement theorem for the previous fixed one-probe quantum cell, and it does not quantize the gravitational metric constraints.

## 1. Why a new scaling family is necessary

The previous model has one quantum shape degree of freedom and one probe. Its finite-grid refinement does not introduce a conserved spacetime number current or worldline positions, and it does not suppress shape–probe entanglement. A deterministic pure-state fluid cannot be inferred from those operations alone.

A controlled family can nevertheless use the same selected local interaction. Introduce a large population scale N, symmetric identical internal probes per material parcel, and semiclassically quantized canonical geometric/parcel variables. Scale total geometric inertia and action with the population so that the normalized force stays finite. For a spatial cell of physical volume v and normalized number density n, the actual probe count is K≈N n v, and the geometric inertia is N f v. Thus the local small parameter is proportional to 1/(N v), not simply 1/N. Empty/vacuum cells require separate treatment; the occupied-patch theorem assumes positive density bounded away from zero.

The auxiliary finite phase-space, Fourier, oscillator, and spatial cutoffs below are part of the declared regulator. Every estimate first fixes them. A later diagonal choice may remove them provided the separate classical consistency/stability estimates and oscillator-domain estimates are supplied. There is no claimed uniform-in-cutoff quantum-field estimate.

## 2. A self-contained bounded-algebra theorem

Let Y_1^(N),…,Y_m^(N) be bounded self-adjoint operators, with ||Y_j||≤1. Their real classical coordinates y lie in a compact embedded Poisson phase space, with |y_j|≤1 for every component. Set the Heisenberg sign convention Π_ij(y)={y_j,y_i}. Assume

    (iN/ℏ)[Y_i,Y_j]=Π_ij(Y)+R_ij,N,
    ||R_ij,N||≤r0/N,
    ||[Y_i,Y_j]||≤κ0/N.

Every Π_ij is a fixed ordered polynomial. The substitution Π_ij(Y) need not be separately Hermitian; the exact commutator is, and the stated remainder covers ordering differences. Coefficients may depend smoothly on time, with uniform bounds on the time interval.

For an ordered polynomial P(y)=Σ_a c_a y_(a1)…y_(ak), define

    M_P=Σ_a |c_a|,
    L_P=Σ_a |c_a| deg(a).

These are conservative finite coefficient bounds, not optimal constants. For normalized Ψ and D=Σ_j||(Y_j−y_j)Ψ||², exact telescoping gives

    ||[P(Y)−P(y)]Ψ||≤L_P sqrt(D).

Indeed, a monomial minus its scalar value equals Σ_r(prefix of operators)(Y_ar−y_ar)(scalar suffix). The error always acts directly on Ψ, so no unjustified commuting or state-factorization step occurs.

Leibniz expansion gives

    (iN/ℏ)[P(Y),Y_j]=G_Pj(Y)+R_Pj,N,
    ||R_Pj,N||≤r0 L_P/N,

where G_Pj is the explicit polynomial obtained by replacing each monomial factor in turn by Π_(ar,j). Its scalar symbol is the Hamiltonian generator X_P y_j={y_j,P}. Furthermore,

    ||[P(Y),Q(Y)]||≤κ0 L_P L_Q/N.

Both statements follow by finite product commutator identities. All constants are obtained from the actual finite polynomial coefficients.

### Positive square-root lemma

Let B=B(Y) be self-adjoint and B≥m0²I, with m0>0, and let its scalar value b=B(y)≥m0². For one basic observable Y_j, define

    C_N=(iN/ℏ)[B,Y_j],    c=G_Bj(y).

For a normalized Ψ,

    ||[(iN/ℏ)[sqrt(B),Y_j]−c/(2sqrt(b))]Ψ||
    ≤ ||(C_N−c)Ψ||/(2m0)
      + |c| ||(B−b)Ψ||/(4m0³)
      + ||[C_N,B]||/(8m0³).

Proof. The positive square-root functional calculus gives

    [sqrt(B),Y_j]=(1/π)∫_0^∞ t^(1/2)(B+t)^−1[B,Y_j](B+t)^−1 dt.

Put R=(B+t)^−1 and r=(b+t)^−1. Move C_N through the second resolvent:

    R C_N R − c r²
      =R²(C_N−c)+R[C_N,R]+c(R²−r²).

Use [C_N,R]=−R[C_N,B]R and R−r=−rR(B−b). The three norm bounds are respectively (m0²+t)^−2||(C_N−c)Ψ||, (m0²+t)^−3||[C_N,B]||, and 2|c|(m0²+t)^−3||(B−b)Ψ||. The exact integrals are

    (1/π)∫t^(1/2)/(m0²+t)² dt=1/(2m0),
    (1/π)∫t^(1/2)/(m0²+t)³ dt=1/(8m0³).

This proves the bound without invoking an unproved semiclassical functional-calculus approximation. Finite-dimensional regulators have no domain difficulty in this step.

The same integral is the Fréchet derivative Dsqrt(B)[C] for an arbitrary bounded self-adjoint variation C. Therefore the identical bound applies to the actual Hamiltonian source variation, with C=δB and c=δb. When δB is a polynomial with the stated coefficient bounds, its concentration and commutator errors are controlled by the same telescoping algebra. The normalized quantum Hamiltonian's scalar-source and stress variations thus converge to the variations of the limiting Hamiltonian; they are not merely independently assigned observables. In finite matrices the derivative can also be checked directly in B's eigenbasis, where its entries are C_ij/(sqrt(b_i)+sqrt(b_j)).

Write G=G_Bj. The polynomial estimates then give a generator error of the form a_j sqrt(D)+b_j/N, where one explicit choice is

    a_j=L_G/(2m0)+M_G L_B/(4m0³),
    b_j=r0 L_B/(2m0)
        +(κ0 L_G L_B+2M_B r0 L_B)/(8m0³).

The last numerator bounds [C_N,B] by splitting C_N=G(Y)+R and using the polynomial commutator bound plus ||[R,B]||≤2||R||||B||.

### Quantitative dynamical conclusion

Let the normalized Hamiltonian be a fixed finite sum of polynomial terms and positive square roots:

    K_N=P0(Y)+Σ_l w_l sqrt(B_l(Y)),
    B_l(Y)≥m_l²I, B_l(y)≥m_l², m_l>0.

Assume K_N is self-adjoint, the weights w_l are real, and the classical symbol k(y) is real. In the concrete construction the polynomial kinetic terms are symmetrically ordered and the square-root terms are positive, so these conditions hold. The physical Schrödinger evolution is iℏ∂tΨ_N=N K_NΨ_N. The limiting coordinates solve the classical Hamilton equations generated by k(y)=P0(y)+Σ_l w_l sqrt(B_l(y)). For polynomial terms use a_j=L_(G_P0j), b_j=r0 L_P0. For roots use the constants above, multiplied by |w_l|. Sum per j, then define a=(Σ_j a_j²)^(1/2), b=(Σ_j b_j²)^(1/2).

For the squared deviation functional

    D_N(t)=Σ_j ⟨(Y_j−y_j(t))²⟩,

exact Schrödinger differentiation and Cauchy–Schwarz yield

    D_N'≤2sqrt(D_N)(a sqrt(D_N)+b/N)
         ≤(2a+1)D_N+b²/N².

Consequently, for 0≤t≤T,

    D_N(t)≤exp(Ct)[D_N(0)+b²t/N²],   C=2a+1.

This is a complete finite-cutoff quantum-to-classical/mean-field estimate. The constants are independent of N for a fixed regulator specification, and depend explicitly on its finite polynomial coefficients, the number of observables, and positive mass gaps. The theorem is not uniform as those regulator parameters are enlarged unless a further bound is proved.

## 3. Concrete algebra realizing the assumptions

### Symmetric internal probes

For a finite internal dimension d, use an HS-orthonormal Hermitian basis B_α, including I/sqrt(d), with ||B_α||≤1, and

    A_N(B_α)=N^−1 Σ_{j=1}^N B_α^(j).

Commutators are exact Lie-algebra relations of size 1/N. A pure product initial state remains in Sym^N(C^d). The identity Σ_α B_α⊗B_α=Swap implies, on this symmetric sector,

    Σ_α A_N(B_α)²=1+(d−1)/N.

For a pure target ρ=|ψ><ψ|, b_α=Tr(ρB_α), define S_N=Σ_α⟨(A_N(B_α)−b_α)²⟩. Then exactly

    S_N=2β_N+(d−1)/N,
    β_N=1−Tr(ρ ρ_N^(1)).

For any fixed k≤N, the union bound on commuting projectors and the pure-state trace-distance bound give

    ||ρ_N^(k)−ρ^⊗k||_1≤2sqrt(kβ_N)≤sqrt(2k S_N).

Thus D_N=O(1/N) controls actual reduced quantum states, not only mean observables. A pure initial product has S_N(0)=(d−1)/N. This is a propagation-of-chaos statement in the declared symmetric setting.

The limiting internal Poisson dynamics is the usual projective-Hilbert Schrödinger dynamics. For a Hamiltonian depending on ρ only through e=Tr(ρh), it gives iℏ ψdot=(∂k/∂e)hψ up to a phase multiplier. Purity and trace are preserved.

### Localized canonical coordinates

Finite clock/shift matrices U,V with UV=e^(−2πi/n)V U realize a compact canonical phase space. Take their real and imaginary parts as bounded basic observables. For Fourier monomials the exact Weyl multiplication and sine commutator identities supply the assumed 1/N commutators and remainders. For clock dimension n=cN with fixed positive integer c, one may use conservative constants κ0=max(2π/c,2) and r0=2π²/(c²ℏ), with the corresponding classical angular Poisson scaling. Physical coordinate scales are chosen so the embedded compact phase space has the desired canonical area; c records that area choice.

The construction uses **finite-degree positive Fourier/polynomial approximants only**, not an unqualified passage to a smooth infinite series. Fix an interior physical phase-space patch containing the limiting trajectory with a positive margin. Choose a smooth periodic positive matrix extension h_D^R equal to the actual projected oscillator P_D h_M P_D on a neighborhood of that patch, for example by a convex cutoff interpolation with a constant positive reference Hamiltonian outside. For finite degree L, let p_(D,L) be a Hermitian Fourier polynomial with C^r error at most δ_reg. Then

    h_(D,L)=p_(D,L)+δ_reg I≥0,

with value error at most2δ_reg and derivative error at mostδ_reg. The uniformly elliptic metric coefficient has the analogous positive approximation; Σ_ab P_a g_poly^ab(q)P_b is then positive even though momenta and configuration coefficients do not commute. Momentum coordinate functions are also smoothly periodicized and approximated on the chosen interior patch. Thus B_l=P_l²+(m0+A_N(h_l))²≥m0² exactly, even when P_l and the mass operator do not commute.

At fixed spatial, oscillator and localization parameters, the finite-degree classical vector field differs from the intended smooth regularized field by at most C_reg δ_reg. Ordinary ODE stability gives a trajectory error at most C_T δ_reg before patch departure; a strict patch margin permits the usual bootstrap. This approximation error must be added to the quantum, oscillator and spatial errors. Choose δ_reg(h) small enough for the desired physical observable tolerance first, and then choose N(h) using the **actual finite-degree** M_P,L_P coefficients. Expanding Fourier monomials into Hermitian cos/sin generators may produce very large (even exponential-in-degree) coefficient bounds; they are retained in the diagonal. No degree-uniform or efficient-computation claim is made.

A periodic Gaussian coherent packet gives canonical-coordinate deviation O(1/N). One explicit construction at a clock dimension n≥4 is

    φ_n(j)=Z_n^−1/2 Σ_(l∈Z) exp[−π(j+ln)²/n],
    j=−floor(n/2),…,ceil(n/2)−1.

Poisson summation makes this vector an eigenvector of the unitary discrete Fourier transform, so its U and V expectations coincide. For basic cos/sin coordinates centered at (1,0,1,0), its squared deviation is 4(1−Re<U>). Using 1−cosθ≤θ²/2 gives D0≤8π²<E j²>/n². A conservative elementary bound is <j²>≤50n: the periodized amplitude is at most sqrt5 times its central Gaussian on the fundamental interval; Z_n≥(sqrt(n)/2)e^(−π/2); and Σ_(j∈Z)j²e^(−2πj²/n)≤n^(3/2). Hence

    D0,canonical≤400π²/n.

Nearest-grid phase-space translations add only O(n^−2) error for a prescribed center. For m canonical pairs and d-dimensional pure product probes, D_N(0)≤[400π²m+d−1]/N plus the stated centering term (or the corresponding cN clock denominators). The constants are deliberately conservative. This supplies nonempty explicit preparations for the theorem. More general squeezed preparation gives an error proportional to σ²+(ℏ/(Nσ))². The earlier fixed 4×8 shape grid is not such a scaling sequence.

This is a declared positive compact regulator family, locally approximating the same selected interaction and target kinetic energy. It is not claimed identical to the old finite-volume regulator at every finite cutoff. Fourier/localization removal is a further consistency step, and the limiting trajectory must stay in the physical chart where the approximation applies.

## 4. The relativistic collective parcel gives the Brown clock

The correct normalized parcel Hamiltonian is

    k(X,p,ρ)=sqrt(p²+[m0+Tr(ρh(q(X)))]²).

It arises from the explicitly selected large-population quantum regulator

    H_N^parcel=N sqrt[P_N²+(m0+A_N(h(q(X_N))))²],

under the bounded/localized quantization assumptions above. The positive mass m0 removes the singularity in the square-root estimates. The actual microscopic architecture uses a collective internal energy; it is added structure, not forced by the previous one-probe cell.

Write ε=m0+Trρh, E=sqrt(p²+ε²). The limit equations are

    Xdot=p/E,
    pdot=−(ε/E) Tr(ρ ∂_X h),
    iℏ ψdot=(ε/E)hψ  (up to phase),
    dτ/dt=ε/E=sqrt(1−|Xdot|²).

Thus iℏ dψ/dτ=hψ. The canonical action reduces by the exact Legendre identity p·Xdot−E=−ε dτ/dt to

    ∫[iℏ<ψ|dψ>−(m0+<h>)dτ].

This is exactly the internal-state worldline integrand whose precaustic material-label continuum yields the Brown state-fluid action. In a prescribed ADM background, the classical Hamiltonian becomes lapse·sqrt(gamma^ij p_i p_j+ε²)−shift·p, with the internal proper-time factor lapse·ε/sqrt(gamma^ij p_i p_j+ε²). A configuration-dependent lapse is not a constant weight in the abstract theorem. An explicit positive quantum ordering is instead sqrt(L_poly B L_poly), where L_poly≥Lmin>0 and B is the positive polynomial mass/kinetic operator. Since L_poly B L_poly≥m0² Lmin², this is a covered square-root term; its classical symbol is L_poly sqrt(b). The shift contribution is a symmetrically ordered polynomial term. This is a declared ordering choice, not a uniqueness theorem for quantized covariant matter. These background coefficients must satisfy the regularity/localization bounds of the theorem. No quantization of their gravitational constraint algebra is inferred.

A naive single-particle operator sqrt[p²+(m0+h)²] has expectation Trρ sqrt[p²+(m0+h)²], which generally differs from sqrt[p²+(m0+Trρh)²]. The discrepancy persists at fixed one-probe occupancy. It is the collective large-population construction, together with its stated preparation, that removes this nonlinear-mass obstruction.

## 5. A solvable nonlinear quantum parcel control

Take h=diag(0,1), m0=1, p=0.7, ℏ=1, and initial state (|0>+|1>)/sqrt2 in every probe. In the symmetric N-probe basis, the exact Hamiltonian is diagonal with energies

    E_N(k)=N F(k/N),   F(a)=sqrt[p²+(m0+a)²].

With the Schrödinger convention iℏψdot=Hψ, define c_N=(ρ_N^(1))_10; the opposite matrix entry is its complex conjugate. This one-probe coherence at time t is exactly

    c_N(t)=½ E_{K~Bin(N−1,½)} exp{−it N[F((K+1)/N)−F(K/N)]}.

The limiting pure state has coherence ½exp[−itF'(½)], where F'(½) is the required proper-flow clock factor. Let M2=sup_{a∈[0,1]}F''(a)=p²/(p²+m0²)^(3/2). The mean-value theorem, binomial variance, and |e^(ix)−e^(iy)|≤|x−y| give

    ||ρ_N^(1)(t)−ρ(t)||_1
      ≤|t|M2[ sqrt(N−1)/(2N)+1/N ].

Jensen plus the second-derivative bound also gives

    0≤E F(K_N/N)−F(½)≤M2/(8N),
    K_N~Bin(N,½).

The script checks N=1,2,4,8,16,32,64,128,256,512 at t=0.8 against these inequalities, including positivity of each reduced state ρ=[[1/2,conj(c_N)],[c_N,1/2]]. A separate full 2^N-dimensional pure-state construction and partial trace for N=1,…,5 verifies this off-diagonal orientation directly; positivity or trace-error magnitudes alone would not detect a conjugation error. At N=512 the trace-norm discrepancy is 3.467859181458923e−5, below the rigorous bound 0.005178876244007249. This is a genuine finite quantum dynamical test of the nonlinear-mass clock limit, not a trajectory fit or a field-continuum simulation.

## 6. Direct curved-kinetic modulated-energy lemma

A second route verifies the shape-only mean-field mechanism without phase-space compactification. Work on the entire regularized quantum configuration domain R^m, with globally defined smooth bounded coefficients, uniformly elliptic bounded g^ab, and finite internal cutoff. The coefficients agree with the physical hyperbolic model on the chosen interior chart, but the differential estimate is global for this regularized problem. After flattening hyperbolic measure, its exact kinetic operator is P_a g^ab P_b/(2I), P=−iε∂, ε=ℏ/N. For g^ab=v²δ^ab this is unitarily equivalent to the original −ε²Δ_G/(2I).

Let the reference ρ_t,Q_t,P_t solve the Ehrenfest equations. Assume a real phase S is defined and solves the following Hamilton–Jacobi equation on the ENTIRE quantum configuration domain for every t∈[0,T], with all derivatives required below uniformly bounded:

    ∂tS+(∇S)^Tg∇S/(2I)+Tr(ρ_t h(q))=0,
    ∇S(t,Q_t)=P_t,

and set U=g∇S/I. The gauge transformation Ψ=e^(iS/ε)Φ then yields the exact normalized Hamiltonian

    T + ½(U·P+P·U) + [A_N(h(q))−Trρ_t h(q)].

Set A=⟨|q−Q|²⟩, K=⟨T⟩, and S_int=Σ⟨(A_N(Bα)−TrρBα)²⟩. The exact kinetic/transport commutator is

    (i/ε)[L_U,T]=P_a C^ab P_b/(2I)
                  +ε² div[g∇divU]/(4I),
    C^ab=U^c∂c g^ab−g^cb∂cU^a−g^ac∂cU^b.

It is independently checked for a general two-dimensional variable metric. Define

    C_U=sup ||g^−1/2 C g^−1/2||,
    B_U=sup |div(g∇divU)|/(4I),
    B²=sup g^ab Tr(∂a h ∂b h),
    ℓ=2 Lip_op(h)/ℏ,
    gmax=sup||g||.

Then exact differentiation and Cauchy–Schwarz give

    A'≤(2LipU+1)A+(2gmax/I)K,
    K'≤(C_U+1)K+[B²/(2I)]S_int+B_U ε²,
    S_int'≤ℓ(A+S_int).

The last line uses exact antisymmetry of the internal adjoint rotation; it is not a factorization assumption. Consequently D=A+K+S_int obeys

    D'≤C D+B_U ε²,
    C=max(2LipU+1+ℓ, 2gmax/I+C_U+1, B²/(2I)+ℓ).

This provides a direct curved-kinetic proof for the stated globally regularized problem. A phase solving HJ only near the classical trajectory would not justify the exact quantum gauge transformation, because a quantum wavefunction can have tails outside that neighborhood. If only a local phase is available, explicit HJ-residual and localization terms must be included instead; no such stronger local-phase theorem is claimed here.

The global-phase hypothesis has nonempty short-time realizations. Choose g,h globally smooth, uniformly elliptic where appropriate, constant outside a compact physical patch, with bounded derivatives through at least fourth order, and S(0,q)=p0·q. For sufficiently small time the characteristic momenta stay uniformly bounded and the graph projection has derivative I+O(t), uniformly in its initial point. Its perturbation of the identity is then globally bi-Lipschitz. The Hamilton action along those characteristics defines a global real S until the first graph caustic, with the stated derivative bounds. All bounds depend on the fixed regularized coefficient norms and time interval, not N.

Hamilton–Jacobi caustics, coefficient localization, and internal-cutoff removal must not be suppressed. This secondary result does not alone prove the relativistic transport continuum; the primary bounded-algebra theorem handles the additional nonlinear parcel Hamiltonian.

## 7. Cutoff and spatial limits: what must be tracked

For fixed spatial/Fourier/Fock/localization data, the estimates above are uniform in the large-population parameter. If a separate classical approximation has error E_class(h) and the quantum bound is

    D_N,h(T)≤e^(C_h T)[D_N,h(0)+R_h T/Ncell²],

then a declared diagonal sequence is controlled whenever the right-hand side tends to zero and E_class(h)→0. For desired D=O(h4), one sufficient choice is a preparation with σ_h² proportional to e^(−C_hT)h4 and Ncell sufficiently large of order e^(C_hT)h^−4, with all coefficient/preparation constants included. Actual global population is Nglobal=Ncell/v. This also requires σ_h=o(h) and Ncell σ_h→∞ when coupling gradients between neighboring cells.

For a cutoff-dependent observable family, its norms must also enter the diagonal. If Cobs_h bounds its polynomial telescoping constants (including Fock factors and current-reconstruction or mollifier derivatives), source error η_h requires sqrt(D)≤η_h/Cobs_h. For coherent preparation D0≤Cprep_h/Ncell, sufficient explicit population conditions are

    Ncell≥2 exp(C_hT) Cprep_h Cobs_h²/η_h²,
    Ncell≥sqrt(2 exp(C_hT)R_hT) Cobs_h/η_h.

Thus D=O(h4) alone does not imply an O(h²) rate for observables whose norms grow with the cutoff. This qualification is essential for energy/current observables and current-squared reconstruction.

These diagonal choices may be extremely expensive; no computational or physical resource efficiency is claimed. One must explicitly bound C_h,R_h for the chosen finite regulator and state the classical solution's smooth precaustic interval. A formal choice of h→0 at fixed occupancy would fail the stated estimates and the independent quantum kinetic-floor control.

### Classical oscillator-cutoff consistency lemma

There is a separate controlled removal of the internal Galerkin cutoff at the *limiting classical/state-parcel* level. Let A=n_osc+1 and write the selected localized oscillator Hamiltonian

    h(q)=c0(q)I+c1(q)n_osc+c2(q)a²+conj(c2(q))a†²,

with coefficients and their required q derivatives bounded on the declared compact patch. Let P_K project onto levels0,…,K−1. It commutes with A, and h_K=P_K h P_K. The same statements hold when the Hamiltonian is multiplied by the proper-time factor b=e/sqrt(p²+e²)≤1, or by a bounded positive lapse.

For any s≥1/2, the only nonzero matrix elements of [h,A^(2s)] shift oscillator number by two. The mean-value estimate

    |(n+3)^(2s)−(n+1)^(2s)|≤4s(n+3)^(2s−1)

and sqrt[(n+1)(n+2)]≤n+3 give

    ||A^−s[h_K,A^(2s)]A^−s||
       ≤8s 3^s sup|c2|,

uniformly K. Therefore

    ||A^s ψ_K(t)||≤exp[4s3^s sup|c2| t/ℏ] ||A^s ψ_K(0)||.

The full quadratic propagator satisfies the same estimate by its standard finite-core construction, and Gaussian initial data have every such moment. The band estimate also gives ||A^r h A^(−r−1)||≤C_r, with C_r determined directly by the bounded coefficients and the fixed number shifts. Those bounds hold uniformly for P_K h P_K.

Let ψ,q,p solve the full limiting coupled parcel/shape ODE and ψ_K,q_K,p_K its Galerkin version, with the same classical initial coordinates and normalized P_Kψ(0). Work on a fixed smooth localized interval. Define η=||A^1/2(ψ_K−ψ)|| and Z=|q_K−q|+|p_K−p|, including any other finite classical canonical variables. Weighted Duhamel, the s=1/2 propagator bound, and the bandwidth-two boundary support give

    η(t)≤e^(cT)η(0)+C_T∫_0^t[η(s)+Z(s)+(K−2)^(−s0+3/2)]ds,

for any s0>3/2 with finite full-state A^s0 norm. The cutoff forcing estimate is

    ||A^1/2(h_K−h)ψ||
      ≤C ||A^3/2(1−P_(K−2))ψ||
      ≤C (K−2)^(−s0+3/2)||A^s0ψ||.

The Hamiltonian coefficient change is controlled by Z and η. In particular the internal energy/force forms are A-bounded, so their expectation differences are at most C_T(Z+η). The proper-time multiplier is Lipschitz in e,p because e≥m0>0; thus its state dependence also contributes at most C_T(Z+η), not a cutoff-dependent factor. The classical ODE difference satisfies

    Z(t)≤Z(0)+C_T∫_0^t[Z(s)+η(s)]ds.

Gronwall yields the explicit-order estimate

    Z(t)+η(t)≤C_T'[Z(0)+η(0)+(K−2)^(−s0+3/2)],

where C_T' depends on the coefficient/metric derivative bounds, m0, T, and the uniform A^1/2, A^3/2, A^s0 moment bounds, but **not K**. Initial projection and renormalization satisfy η(0)=O(K^(−s0+1/2)). The fully stated constant can be taken from the displayed weighted-propagator exponent and the Gronwall coefficient; no unspecified K dependence is hidden. Uniform classical momentum bounds follow either from the stipulated compact interval or from the positive conserved localized autonomous energy. This is a classical/state-Galerkin consistency estimate, not a claim that the quantum N-body cutoff estimate is itself uniform in K.

For s0=3 one obtains O(K^−3/2). Thus choose K(h) large enough that this bound is below the desired classical spatial error, then choose Ncell(h) from the bounded-algebra theorem with the actual finite-K(h) constants. The order of these estimates and the diagonal dependence are essential. A full interacting quantum continuum at fixed population is not established.

## Verification and literature

`verify_meanfield_bridge.py` passed 164 exact symbolic identities/components plus ten declared quantum parcel controls, four clock/shift commutator controls, eight coherent-preparation controls, six genuinely noncommuting square-root-lemma controls, five direct full-state partial traces, and six Fréchet-source/positive-lapse-sandwich controls. It independently checks the full variable-metric commutator, hyperbolic measure flattening, square-root resolvent integrals, Hermitian-basis/Casimir identities, proper-time derivatives, and exact finite-population density/energy bounds. It imports no project verifier.

The main analytic inequalities are written proofs above, not claimed consequences of a finite test count. Primary context: Golse, Mouhot and Paul, *On the Mean Field and Classical Limits of Quantum Mechanics*, https://arxiv.org/abs/1502.06143 . Their quantitative simultaneous-limit methodology is precedent, not a theorem automatically covering this model. Chen, Shen and Zhang, *On the mean-field and semiclassical limit from quantum N-body dynamics*, https://arxiv.org/abs/2304.03447 , provides a different, substantially harder fluid-limit example; it must not be cited as proving this construction.

Strongest current result: an explicit finite-time quantum-to-classical/pure-internal-state limit for an augmented positive localized regulator, including the nonlinear collective relativistic mass and its proper-flow quantum clock. It supplies a rigorous microscopic-to-parcel stage. The label-to-fluid continuum, metric/source convergence, gravity constraints, and all-cutoff diagonal conditions require their own stated proofs. No empirical or worldwide-priority claim follows.

## Freeze record

The derivations supporting this note are complete at the stated finite-cutoff/diagonal scope. The square-root lemma, collective concentration and chaos estimate, canonical preparation, curved-kinetic alternative, Brown proper-time dynamics, and classical oscillator-Galerkin consistency have been derived. The controls executed successfully. The supplied raw script and this proof record have not been copied into the public repository by this task. A broader unregularized field/constraint claim remains outside the result.

The finite oscillator/phase cutoffs need not preserve exact shear symmetry or local covariant Ward identities. The theorem controls the actual Hamiltonian variations, and the full-state classical endpoint recovers the stated state-fluid current symmetry only after the relevant cutoff removal. An exact finite-cutoff shear Ward identity is not assumed.
