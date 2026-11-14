# A controlled quantum-to-parcel limit

The selected interaction can be connected to a relativistic state-carrying parcel by a quantitative large-population limit. The quantum internal state keeps its proper-time Schrödinger dynamics, while the collective geometric and transport variables concentrate around classical trajectories.

This is a theorem for an **explicitly augmented, localized regulator family**. The earlier one-probe cell has neither particle positions nor a spacetime number current, and spatial refinement alone does not suppress its entanglement. The construction here adds those variables and scales the population and geometric inertia together. It is a collective weak-coupling family, not an ultraviolet limit with every physical constant held fixed.

The result in this note is the microscopic-to-parcel stage. The material-label continuum, strong-current reconstruction, and gravitational constraints have separate obligations. In particular, this theorem does not quantize the Einstein constraint algebra.

## 1. The regulator and its scaling

At fixed spatial, oscillator, Fourier, and phase-space cutoffs, use bounded canonical clock/shift observables together with symmetric identical internal probes. The selected local oscillator interaction is the one derived in [Dynamical coupling](DYNAMICAL_COUPLING.md).

Let $N$ denote a common large-population parameter. For a physical cell of volume $v$ and normalized occupied density $n$, the actual number of probes scales as $K\simeq Nnv$, and the geometric inertia scales as $Nfv$. The local small parameter is therefore controlled by $1/(Nv)$, with density factors retained. The occupied-patch statement assumes density bounded away from zero; empty cells require separate treatment.

For the algebraic theorem below, the fixed cutoff and density factors are absorbed into explicit coefficients. Total Hamiltonian and action are normalized per population. This scaling keeps the normalized reciprocal force finite and leaves each internal probe's calibrated quantum frequency intact.

## 2. Bounded observables give an explicit dynamical estimate

Let $Y_1^{(N)},\ldots,Y_m^{(N)}$ be bounded self-adjoint operators with $\|Y_j^{(N)}\|\le1$. Their real classical coordinates $y_j$ lie in a compact embedded Poisson phase space and obey $|y_j|\le1$. Use the Heisenberg sign convention

```math
\Pi_{ij}(y)=\{y_j,y_i\}.
```

Assume the finite algebra satisfies

```math
\frac{iN}{\hbar}[Y_i,Y_j]
=\Pi_{ij}(Y)+R_{ij,N},
\qquad \|R_{ij,N}\|\le\frac{r_0}{N},
\qquad \|[Y_i,Y_j]\|\le\frac{\kappa_0}{N},
```

where every $\Pi_{ij}$ is an explicitly ordered polynomial. The polynomial substitution need not itself be Hermitian; the exact scaled commutator $(iN/\hbar)[Y_i,Y_j]$ is Hermitian, and the remainder includes the ordering discrepancy.

For an ordered polynomial $P=\sum_a c_a y_{a_1}\cdots y_{a_{k_a}}$, define the finite coefficient bounds

```math
M_P=\sum_a|c_a|,
\qquad L_P=\sum_a|c_a|k_a.
```

For a normalized state $\Psi$, set

```math
D_N=\sum_j\|(Y_j-y_j)\Psi\|^2.
```

The exact telescoping identity gives

```math
\|(P(Y)-P(y))\Psi\|\le L_P\sqrt{D_N}.
```

To see why no factorization assumption is hidden here, write a monomial difference as a sum of an operator prefix, one factor $Y_{a_r}-y_{a_r}$, and a scalar suffix. The error factor acts directly on $\Psi$; all prefix factors have norm at most one.

Leibniz expansion gives an explicit polynomial $G_{Pj}$ such that

```math
\frac{iN}{\hbar}[P(Y),Y_j]
=G_{Pj}(Y)+R_{Pj,N},
\qquad \|R_{Pj,N}\|\le\frac{r_0L_P}{N}.
```

Its scalar value is the classical Hamiltonian generator $G_{Pj}(y)=\{y_j,P\}$. A second product-commutator expansion yields

```math
\|[P(Y),Q(Y)]\|\le\frac{\kappa_0L_PL_Q}{N}.
```

The constants may be conservative and large. They are computed from the actual finite polynomials, rather than assumed uniform as the cutoffs grow.

## 3. The nonlinear square root is controlled

The relativistic mass Hamiltonian is not polynomial. The following resolvent lemma handles it, including noncommuting momentum and mass operators.

Let $B=B(Y)$ be self-adjoint with $B\ge m_0^2I$, and suppose its scalar value $b=B(y)\ge m_0^2$, where $m_0>0$. For one observable define

```math
C_N=\frac{iN}{\hbar}[B,Y_j],
\qquad c=G_{Bj}(y).
```

Then

```math
\begin{aligned}
\left\|\left(\frac{iN}{\hbar}[\sqrt B,Y_j]
-\frac{c}{2\sqrt b}\right)\Psi\right\|
\le{}&\frac{\|(C_N-c)\Psi\|}{2m_0}
+\frac{|c|\|(B-b)\Psi\|}{4m_0^3}\\
&+\frac{\|[C_N,B]\|}{8m_0^3}.
\end{aligned}
```

### Proof

Positive functional calculus gives

```math
[\sqrt B,Y_j]
=\frac1\pi\int_0^\infty
t^{1/2}(B+t)^{-1}[B,Y_j]\,(B+t)^{-1}\,dt.
```

Put $R=(B+t)^{-1}$ and $r=(b+t)^{-1}$. The difference of integrands is exactly

```math
RC_NR-cr^2
=R^2(C_N-c)+R[C_N,R]+c(R^2-r^2).
```

Use $[C_N,R]=-R[C_N,B]R$ and $R-r=-rR(B-b)$. The three terms are bounded by the corresponding errors times $(m_0^2+t)^{-2}$, $(m_0^2+t)^{-3}$, and $2(m_0^2+t)^{-3}$. Finally,

```math
\frac1\pi\int_0^\infty\frac{t^{1/2}}{(m_0^2+t)^2}\,dt
=\frac1{2m_0},
\qquad
\frac1\pi\int_0^\infty\frac{t^{1/2}}{(m_0^2+t)^3}\,dt
=\frac1{8m_0^3}.
```

This proves the estimate directly. Finite-dimensional regulators have no unresolved operator-domain issue in this step.

### Explicit constants

Writing $G=G_{Bj}$, one admissible bound for the generator error is $a_j\sqrt{D_N}+b_j/N$, where

```math
a_j=\frac{L_G}{2m_0}+\frac{M_GL_B}{4m_0^3},
```

```math
b_j=\frac{r_0L_B}{2m_0}
+\frac{\kappa_0L_GL_B+2M_Br_0L_B}{8m_0^3}.
```

The last numerator bounds $[C_N,B]$ after splitting $C_N=G(Y)+R_{Bj,N}$.

### Actual source and stress variations

The same resolvent integral gives the Fréchet derivative $D\sqrt B[C]$. Consequently the same bound applies with $C=\delta B$ and $c=\delta b$. If $\delta B$ satisfies the polynomial bounds, derivatives of the **actual normalized quantum Hamiltonian** converge to derivatives of the limiting Hamiltonian. This controls its scalar sources and metric/stress variations; the limiting observables are not assigned independently after choosing a desired classical equation.

In a matrix eigenbasis of $B$, the exact derivative is $C_{ij}/(\sqrt{b_i}+\sqrt{b_j})$, providing an independent finite-matrix check.

## 4. Quantitative quantum-to-classical and pure-state convergence

Let

```math
K_N=P_0(Y)+\sum_\ell w_\ell\sqrt{B_\ell(Y)},
\qquad B_\ell(Y)\ge m_\ell^2I,
\qquad B_\ell(y)\ge m_\ell^2>0.
```

Assume $K_N$ is self-adjoint, the weights are real, and the classical symbol $k(y)$ is real. The concrete regulator uses symmetrically ordered kinetic terms and positive roots. The physical quantum dynamics is

```math
i\hbar\partial_t\Psi_N=NK_N\Psi_N.
```

The limiting coordinates solve the Hamilton equations generated by $k(y)$. Sum the constants above over all Hamiltonian terms, with factors $|w_\ell|$. For polynomial terms use $a_j=L_{G_{P_0j}}$ and $b_j=r_0L_{P_0}$. Define

```math
a=\left(\sum_j a_j^2\right)^{1/2},
\qquad b=\left(\sum_j b_j^2\right)^{1/2},
\qquad C=2a+1.
```

Exact Schrödinger differentiation and Cauchy–Schwarz give

```math
\frac{dD_N}{dt}
\le2\sqrt{D_N}\left(a\sqrt{D_N}+\frac bN\right)
\le CD_N+\frac{b^2}{N^2}.
```

Therefore, for $0\le t\le T$,

```math
\boxed{D_N(t)\le e^{Ct}
\left[D_N(0)+\frac{b^2t}{N^2}\right].}
```

At fixed cutoffs these constants are independent of $N$. Time-dependent smooth backgrounds are permitted when the coefficient bounds hold uniformly over the interval.

### Internal states converge, not only their averages

For internal dimension $d$, choose an HS-orthonormal Hermitian basis $B_\alpha$, including $I/\sqrt d$, and use collective operators

```math
A_N(B_\alpha)=\frac1N\sum_{j=1}^N B_\alpha^{(j)}.
```

A pure product preparation remains in the symmetric probe sector. The completeness identity $\sum_\alpha B_\alpha\otimes B_\alpha=\mathrm{Swap}$ gives

```math
\sum_\alpha A_N(B_\alpha)^2
=1+\frac{d-1}{N}
```

on that sector. For a pure target $\rho=|\psi\rangle\langle\psi|$, define

```math
S_N=\sum_\alpha
\left\langle\left(A_N(B_\alpha)-\mathrm{Tr}(\rho B_\alpha)\right)^2\right\rangle,
\qquad
\beta_N=1-\mathrm{Tr}(\rho\rho_N^{(1)}).
```

Then exactly

```math
S_N=2\beta_N+\frac{d-1}{N},
\qquad
\boxed{\|\rho_N^{(k)}-\rho^{\otimes k}\|_1
\le2\sqrt{k\beta_N}\le\sqrt{2kS_N}.}
```

For $1\le k\le N$, the first inequality follows from the union bound for the commuting one-particle projectors and the pure-state trace-distance estimate. The second follows from the Casimir relation and $\beta_N\le S_N/2$. This is propagation of chaos for each fixed $k$ in the specified symmetric family. Initially $S_N=(d-1)/N$. Thus the estimate controls the internal pure-state closure used by the state-fluid action.

## 5. A concrete canonical regulator and preparation

Finite clock/shift matrices satisfy

```math
UV=e^{-2\pi i/n}VU.
```

The negative phase corresponds to positive physical $\{q,p\}=1$ with the Heisenberg convention above. Their real and imaginary parts are bounded self-adjoint observables. Exact Weyl multiplication supplies the polynomial commutator relations. For $n=cN$, fixed integer $c>0$, conservative bounds are

```math
\kappa_0=\max(2\pi/c,2),\qquad
r_0=\frac{2\pi^2}{c^2\hbar},
```

with the associated canonical-area normalization. The internal Lie-algebra commutators are exact. Physical coordinates are represented only inside a declared phase-space patch containing the classical trajectory; this is a new canonical regularization of the selected interaction, not an assertion that the old fixed grid already had a continuum limit.

A nonempty preparation class is supplied by the periodized Gaussian

```math
\phi_n(j)=Z_n^{-1/2}\sum_{\ell\in\mathbb Z}
\exp\left[-\frac{\pi(j+\ell n)^2}{n}\right].
```

Poisson summation makes it invariant under the unitary discrete Fourier transform. For the four real clock/shift coordinates centered at $(1,0,1,0)$, its squared deviation is $4(1-\mathrm{Re}\langle U\rangle)$. The bounds $1-\cos\theta\le\theta^2/2$ and $\langle j^2\rangle\le50n$ give

```math
D_{0,\mathrm{canonical}}\le\frac{400\pi^2}{n},\qquad n\ge4.
```

For completeness, the latter moment bound follows by bounding the periodized amplitude by $\sqrt5$ times the central Gaussian, using $Z_n\ge(\sqrt n/2)e^{-\pi/2}$, and bounding $\sum_jj^2e^{-2\pi j^2/n}$ by $n^{3/2}$. The constants are intentionally conservative. Nearest-grid translations add only $O(n^{-2})$ center error. With $m$ canonical pairs and pure product probes,

```math
D_N(0)\le\frac{400\pi^2m+d-1}{N}+O(N^{-2}),
```

with the appropriate $cN$ denominators if different canonical areas are used.

### Finite positive coefficient approximation

The theorem uses finite polynomials. It does not silently extend coefficient-sum bounds to an arbitrary smooth infinite Fourier series.

Choose a smooth periodic positive matrix extension $h_D^R$ equal to the projected selected oscillator $P_Dh_MP_D$ near the physical trajectory patch. A convex cutoff interpolation with a positive reference operator supplies one such extension. Let a Hermitian finite Fourier polynomial $p_{D,L}$ approximate it in $C^r$ with error at most $\delta_{\mathrm{reg}}$. Then

```math
h_{D,L}=p_{D,L}+\delta_{\mathrm{reg}}I\ge0.
```

Its value error is at most $2\delta_{\mathrm{reg}}$, and derivative error at most $\delta_{\mathrm{reg}}$. The metric coefficients admit the analogous positive approximation, so $\sum_{ab}P_ag_{\mathrm{poly}}^{ab}(q)P_b$ is positive. These constructions preserve the mass gap required by the square-root lemma.

At fixed spatial, oscillator, and localization cutoffs, the classical vector-field error is bounded by $C_{\mathrm{reg}}\delta_{\mathrm{reg}}$. ODE stability gives a corresponding $C_T\delta_{\mathrm{reg}}$ trajectory error before patch departure. A strict patch margin permits a bootstrap. This error is included separately in the final diagonal limit.

Expanding finite Fourier monomials into Hermitian generators can produce large coefficient sums. Their actual values enter $M_P,L_P$ and hence $C,b$. No degree-uniform estimate or computational efficiency is asserted.

## 6. The collective relativistic mass produces the proper quantum clock

For one augmented material parcel take

```math
\widehat H_N^{\mathrm{parcel}}
=N\sqrt{P_N^2+\left(m_0+A_N(h(q(X_N)))\right)^2},
\qquad m_0>0.
```

The relativistic formulas use units $c=1$. The square-root argument is at least $m_0^2I$ when the selected internal Hamiltonian is positive. Momentum and mass need not commute. Its classical symbol is

```math
E(X,p,\rho)=\sqrt{p^2+\varepsilon^2},
\qquad \varepsilon=m_0+\mathrm{Tr}(\rho h(q(X))).
```

The limit equations are

```math
\dot X=\frac pE,
\qquad
\dot p=-\frac\varepsilon E\mathrm{Tr}(\rho\,\partial_Xh),
\qquad
i\hbar\dot\psi=\frac\varepsilon E h\psi
```

up to the physically irrelevant phase multiplier. Since

```math
\frac{d\tau}{dt}=\frac\varepsilon E
=\sqrt{1-|\dot X|^2},
```

the internal equation is exactly $i\hbar d\psi/d\tau=h\psi$. The Legendre identity

```math
p\cdot\dot X-E=-\varepsilon\frac{d\tau}{dt}
```

turns the canonical action into

```math
\int\left[i\hbar\langle\psi|d\psi\rangle
-\left(m_0+\langle h\rangle\right)d\tau\right].
```

This is the internal-state worldline integrand used in the precaustic material-label construction of the [covariant state-fluid action](CURRENT_AND_RECONSTRUCTION.md). Introducing the parcel center and collective mass is additional microscopic structure; it is not selected by the earlier one-probe Hamiltonian alone.

### Positive ADM ordering and actual variations

On a prescribed smooth ADM background, the classical Hamiltonian is

```math
L\sqrt{\gamma^{ij}p_ip_j+\varepsilon^2}-\beta^ip_i.
```

A variable lapse is not a constant weight in the abstract theorem. A covered positive quantum ordering is $\sqrt{L_{\mathrm{poly}}BL_{\mathrm{poly}}}$, with $L_{\mathrm{poly}}\ge L_{\min}>0$. Then

```math
L_{\mathrm{poly}}BL_{\mathrm{poly}}
\ge m_0^2L_{\min}^2I,
```

and its exact scalar symbol is $L_{\mathrm{poly}}(y)\sqrt b$. Its difference from the original $L\sqrt b$ is part of the declared approximation error. The shift is a symmetrically ordered polynomial term. The abstract theorem requires self-adjoint evolution, not a nonnegative Hamiltonian for every polynomial or signed weight. The physical kinetic and mass pieces give a positive realization in a zero-shift background; a generic ADM shift need not preserve total positivity. This ordering is specified rather than claimed unique. The Fréchet estimate controls variations of these actual operators with respect to target and background fields, giving their limiting force and stress sources. It does not quantize the background constraint algebra.

### Why the single-probe substitute fails

In general,

```math
\mathrm{Tr}\left[\rho\sqrt{p^2+(m_0+h)^2}\right]
\ne\sqrt{p^2+\left(m_0+\mathrm{Tr}(\rho h)\right)^2}.
```

The discrepancy persists at fixed one-probe occupancy. Replacing the operator by its mean without the collective limit would be an uncontrolled closure. The large-population preparation and estimate above supply the missing argument.

## 7. An exactly solvable quantum check of the nonlinear clock

Take $h=\mathrm{diag}(0,1)$, $m_0=1$, $p=0.7$, $\hbar=1$, and the initial state $(|0\rangle+|1\rangle)/\sqrt2$ in every probe. The exact symmetric-sector energies are

```math
E_N(k)=NF(k/N),\qquad F(a)=\sqrt{p^2+(m_0+a)^2}.
```

Define the reduced coherence as $c_N=(\rho_N^{(1)})_{10}$, so the upper-right entry is its conjugate. It is exactly

```math
c_N(t)=\frac12\mathbb E_{K\sim\mathrm{Bin}(N-1,1/2)}
\exp\left[-itN\left(F\left(\frac{K+1}{N}\right)-F\left(\frac KN\right)\right)\right].
```

The limit is $c(t)=\tfrac12e^{-itF'(1/2)}$, with the required proper-flow factor. Put $M_2=p^2/(p^2+m_0^2)^{3/2}$. The mean-value theorem and binomial variance give

```math
\boxed{\|\rho_N^{(1)}(t)-\rho(t)\|_1
\le |t|M_2\left(\frac{\sqrt{N-1}}{2N}+\frac1N\right).}
```

The independent convexity bound is

```math
0\le\mathbb E F(K_N/N)-F(1/2)\le\frac{M_2}{8N},
\qquad K_N\sim\mathrm{Bin}(N,1/2).
```

The checker tests ten populations through $N=512$ at $t=0.8$. At $N=512$, the trace error is approximately $3.47\times10^{-5}$, below the proved bound $0.00518$. Five separate full $2^N$ state constructions and partial traces verify the matrix-index/time-phase convention. These are controlled finite quantum calculations, not a field simulation or experimental measurement.

## 8. How the cutoff-dependent diagonal is chosen

At fixed cutoff specification $h$—including its spatial, oscillator, Fourier, and localization data—write the quantum estimate as

```math
D_{N,h}(T)\le e^{C_hT}
\left[\frac{C_{\mathrm{prep},h}}{N_{\mathrm{cell}}}
+\frac{R_hT}{N_{\mathrm{cell}}^2}\right].
```

Let $C_{\mathrm{obs},h}$ bound the actual source/current observable constants, including Fock and current-reconstruction derivatives. To obtain observable error at most $\eta_h$, sufficient population conditions are

```math
N_{\mathrm{cell}}\ge
\frac{2e^{C_hT}C_{\mathrm{prep},h}C_{\mathrm{obs},h}^2}{\eta_h^2},
```

```math
N_{\mathrm{cell}}\ge
\frac{\sqrt{2e^{C_hT}R_hT}\,C_{\mathrm{obs},h}}{\eta_h}.
```

Thus a bare $D=O(h^4)$ is not enough to claim an $O(h^2)$ current error when observable norms grow. The coefficient-approximation error $\delta_{\mathrm{reg}}$, internal cutoff consistency error, classical material approximation, and strong-current reconstruction error must all be added and balanced separately. The resulting populations may be very large; no efficient resource scaling is claimed.

## Appendix A. Direct curved-kinetic estimate

A complementary proof treats the nonrelativistic shape kinetic term directly. Work on the entire regularized configuration domain $\mathbb R^m$ with globally smooth bounded coefficients and uniformly elliptic $g^{ab}$. Let $P=-i\epsilon\partial$, $\epsilon=\hbar/N$, and $T=P_ag^{ab}P_b/(2I)$. Flattening the hyperbolic measure gives precisely this divergence-form kinetic with $g^{ab}=v^2\delta^{ab}$ on the physical patch.

Assume a real phase $S$ solves HJ on the **entire quantum configuration domain** for $0\le t\le T$, with all derivatives below bounded:

```math
\partial_tS+\frac{(\nabla S)^Tg\nabla S}{2I}
+\mathrm{Tr}(\rho_t h(q))=0,
\qquad U=g\nabla S/I.
```

The reference $(Q_t,P_t,\rho_t)$ must solve the limiting Ehrenfest equations generated by $P^Tg(Q)P/(2I)+\mathrm{Tr}(\rho h(Q))$, with $i\hbar\dot\rho_t=[h(Q_t),\rho_t]$. Require $\nabla S(t,Q_t)=P_t$ throughout the interval. These are part of the lemma hypotheses.

The exact gauge-transformed Hamiltonian is $T+\tfrac12(U\cdot P+P\cdot U)+A_N(h)-\mathrm{Tr}(\rho_t h)$. The following form identities hold first on the common smooth core; the differential estimate assumes the indicated finite moments and solution regularity needed to differentiate those forms. The kinetic/transport commutator is

```math
\frac i\epsilon[L_U,T]
=\frac1{2I}P_aC^{ab}P_b
+\frac{\epsilon^2}{4I}\partial_a(g^{ab}\partial_b\mathrm{div}U),
```

```math
C^{ab}=U^c\partial_cg^{ab}
-g^{cb}\partial_cU^a-g^{ac}\partial_cU^b.
```

For position variance $A$, relative kinetic energy $K$, and collective internal variance $S_{\mathrm{int}}$, exact differentiation gives

```math
\begin{aligned}
A'&\le(2\mathrm{Lip}U+1)A+(2g_{\max}/I)K,\\
K'&\le(C_U+1)K+[B^2/(2I)]S_{\mathrm{int}}+B_U\epsilon^2,\\
S_{\mathrm{int}}'&\le\ell(A+S_{\mathrm{int}}),
\end{aligned}
```

The constants are

```math
\begin{aligned}
C_U&=\sup\|g^{-1/2}Cg^{-1/2}\|,\\
B_U&=\sup|\mathrm{div}(g\nabla\mathrm{div}U)|/(4I),\\
B^2&=\sup g^{ab}\mathrm{Tr}(\partial_ah\partial_bh),\\
\ell&=2\mathrm{Lip}_{\mathrm{op}}(h)/\hbar.
\end{aligned}
```

Internal adjoint rotation is antisymmetric, so its contribution to the derivative of the internal variance cancels exactly.

A phase valid only near the classical trajectory is insufficient because quantum tails can leave that neighborhood. Nonempty short-time global examples follow from globally smooth bounded coefficients with bounded derivatives through fourth order and affine initial phase: the characteristic graph projection remains globally bi-Lipschitz while its derivative is $I+O(t)$. The Hamilton action supplies the global phase until the first graph caustic. Without that hypothesis, explicit HJ-residual/localization terms would be needed.

## Appendix B. Classical oscillator-cutoff consistency

At the limiting classical/state-parcel level, let $A=\widehat n+1$ and write the selected localized oscillator as

```math
h(q)=c_0(q)I+c_1(q)\widehat n+c_2(q)a^2+\overline{c_2(q)}(a^\dagger)^2.
```

Coefficients and required derivatives are bounded on the declared patch. The number projector $P_K$ commutes with $A$, and $h_K=P_KhP_K$. Its bandwidth-two structure gives, for $s\ge1/2$,

```math
\|A^{-s}[h_K,A^{2s}]A^{-s}\|
\le8s3^s\sup|c_2|,
```

uniformly in $K$. Hence number moments grow at most exponentially with constants independent of $K$. The bound also holds with the proper-time multiplier $\varepsilon/E\le1$ or a bounded positive lapse.

Let $\eta=\|A^{1/2}(\psi_K-\psi)\|$, and let $Z$ collect the classical coordinate/momentum differences. Weighted Duhamel estimates and the two-level boundary support give, for $s_0>3/2$,

```math
\eta(t)\le e^{cT}\eta(0)
+C_T\int_0^t\left[\eta(s)+Z(s)+(K-2)^{-s_0+3/2}\right]ds.
```

The forcing estimate is

```math
\|A^{1/2}(h_K-h)\psi\|
\le C\|A^{3/2}(1-P_{K-2})\psi\|
\le C(K-2)^{-s_0+3/2}\|A^{s_0}\psi\|.
```

Energy and force expectations are $A$-bounded forms. The positive rest mass makes the proper-time multiplier Lipschitz in energy and momentum. Thus $Z'\le C_T(Z+\eta)$, and Gronwall gives

```math
Z(t)+\eta(t)\le C_T'
\left[Z(0)+\eta(0)+(K-2)^{-s_0+3/2}\right].
```

The constants depend on coefficient bounds, the smooth time interval, $m_0$, and finite number-moment bounds, but not $K$. Gaussian initial data have all required moments. This is a separate consistency estimate for the limiting state/parcel equations. It does not say the finite $N$ quantum bound is uniform in the oscillator cutoff. The cutoff is chosen first, then its actual constants enter the population diagonal.

## Verification and scientific scope

The [unchanged frozen checker](../scripts/continuum_checks/verify_meanfield_bridge.py) and [receipt](../evidence/continuum/meanfield/meanfield_receipt.json) contain:

- 164 exact symbolic identities/components, including the variable-metric commutator, resolvent integrals, and collective Casimir identities.
- Ten exact-form nonlinear quantum parcel controls, four canonical clock controls, and eight coherent-preparation controls.
- Six noncommuting square-root controls, five independent full-state partial traces, and six Fréchet-source/positive-lapse controls.

The analytical inequalities are proved above; finite test counts are not substitutes for those arguments. Quantitative joint-limit methods have substantial precedent, including [Golse, Mouhot and Paul](https://arxiv.org/abs/1502.06143) and the different fluid-limit setting of [Chen, Shen and Zhang](https://arxiv.org/abs/2304.03447). Neither paper is treated as automatically proving this model's limit.

The positive result is a controlled finite-time microscopic-to-parcel stage with an explicitly retained quantum internal clock and pure-state closure. Finite oscillator and phase cutoffs need not preserve exact shear or covariant Ward identities. The source theorem controls variations of the actual regulator, and the stated current symmetry is recovered at the appropriate classical endpoint after cutoff removal. A fixed-population interacting quantum-field continuum, unrestricted removal of the gravitational geometry cutoff, and quantization of Einstein constraints remain outside this theorem.
