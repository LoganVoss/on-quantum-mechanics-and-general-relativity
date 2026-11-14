# What a controlled continuum limit must preserve

A smaller numerical grid is not automatically a more complete physical theory. The continuum construction needs to identify which degrees of freedom are being refined, which observables converge, and which fluctuations remain.

The results below identify concrete conditions for the positive construction in [Quantum to parcels](QUANTUM_TO_PARCELS.md), [Matter continuum](MATTER_CONTINUUM.md), and the [continuum contract](CONTINUUM_CONTRACT.md). They rule out several shortcuts. They do not rule out the explicitly augmented, prepared, large-population limit proved there.

## 1. The original grid is a grid of shapes

The earlier quantum control uses four radial and eight angular cells on the hyperbolic **configuration space** of shape matrices, with an outer target radius of 1.2. Its other factor is the oscillator Fock space. Refining those two cutoffs approximates the single-cell operator on

```math
L^2(\mathbb H^2,d\mathrm{vol}_G)\otimes L^2(\mathbb R).
```

It does not create a lattice of physical spatial positions. Particle positions, transport momenta, material labels, number density, and a spacetime current are absent from that original operator family.

This is a statement about the specified observables and dynamics, rather than an abstract count of Hilbert-space dimensions. A matter continuum must add the physical transport architecture and specify its scaling. The current extension does so explicitly; it does not relabel the old shape grid as physical space.

## 2. Fixed-occupancy spatial refinement has an energy obstruction

The hyperbolic target metric is $G=v^{-2}(du^2+dv^2)$. Its kinetic form on smooth compactly supported functions is

```math
q_G[\phi]=\int du\,dv\left(|\partial_u\phi|^2+|\partial_v\phi|^2\right),
\qquad
\|\phi\|_G^2=\int du\,dv\frac{|\phi|^2}{v^2}.
```

The identity

```math
\left|f'-\frac{f}{2v}\right|^2
=|f'|^2-\frac{|f|^2}{4v^2}
-\frac12\partial_v\left(\frac{|f|^2}{v}\right)
```

gives, after integration and removal of the compact-support boundary term,

```math
\boxed{-\Delta_G\ge\frac14.}
```

This is the established hyperbolic spectral floor; the displayed Hardy completion supplies the lower bound used here. [Berchio, Ganguly and Grillo, *Sharp Poincaré-Hardy and Poincaré-Rellich inequalities on the hyperbolic space*](https://arxiv.org/abs/1507.02550v4).

Suppose physical cells of volume $v_{\mathrm c}=h^d$ cover a region of volume $V$, with inertia $I_{\mathrm c}=f v_{\mathrm c}$, $f>0$. Retain the nonnegative oscillator excitation and any nonnegative intercell gradient terms. Then even correlated states satisfy

```math
\boxed{H_{\mathrm{total}}
\ge\frac{\hbar^2V}{8f v_{\mathrm c}^2}
=\frac{\hbar^2V}{8f h^{2d}}.}
```

In two physical spatial dimensions this grows as $h^{-4}$. The unsubtracted model at fixed $\hbar$ and $f$ therefore has no uniformly bounded total-energy family under this raw refinement.

Vacuum subtraction, counterterms, or a different scaling could change that conclusion. They are not excluded by the inequality. With a dynamical metric, a subtraction must be included consistently in the action and stress prescription, rather than silently removed from the calculation.

### A scaling that avoids this particular obstruction

The controlled family uses geometry inertia $Nf v_{\mathrm c}$, approximately $Nn_jv_{\mathrm c}$ internal probes in an occupied parcel, and total action and energy normalized by $N$. Its kinetic floor becomes

```math
\frac{H_{\mathrm{total}}}{N}
\ge\frac{\hbar^2V}{8fN^2v_{\mathrm c}^2}.
```

The scale $Nv_{\mathrm c}\to\infty$ suppresses this floor and gives many probes per occupied cell. It preserves the individual internal probe clock while the normalized density remains finite. It is a collective classical/weak-coupling scaling, not a fixed-Newton-constant ultraviolet limit.

For a simple product preparation with target width $\sigma$, the local initial error scales are

```math
\text{kinetic fluctuation}=O\!\left((Nh^d\sigma)^{-2}\right),
\qquad
\text{gradient fluctuation}=O(\sigma^2/h^2).
```

Thus $\sigma=o(h)$ and $Nh^d\sigma\to\infty$ are a sufficient preparation pattern for these two terms. Dynamical growth and all cutoff-dependent constants still have to be controlled; these initial estimates alone are not a continuum theorem.

## 3. A heavy shape can still leave a mixed probe

A large inertia does not suppress a macroscopic superposition of shapes by itself. Consider two frozen branches of the selected coupling,

```math
M_+=\mathrm{diag}(e^r,e^{-r}),\qquad
M_-=\mathrm{diag}(e^{-r},e^r),
```

with an equal coherent shape superposition and the oscillator vacuum as the initial probe. The frozen-branch test is the zero-shape-kinetic, infinite-inertia case. It uses the selected quadratic Hamiltonians, not an independently chosen decoherence channel.

For $\theta=\omega t$, the conditional symplectic matrices are

```math
S_\pm(t)=\cos\theta\,I+\sin\theta\,J M_\pm^{-1},
\qquad N_\pm(t)=S_\pm S_\pm^T.
```

Their average is

```math
\frac{N_++N_-}{2}
=\left[1+2\sinh^2r\sin^2(\omega t)\right]I.
```

The exact Gaussian overlap and reduced-probe purity are therefore

```math
\mathcal F(t)=\frac1{1+2\sinh^2r\sin^2(\omega t)},
\qquad
\mathrm{Tr}\,\rho_{\mathrm p}(t)^2=\frac{1+\mathcal F(t)}2.
```

At $r=\log2$ and $t=\pi/(2\omega)$,

```math
\boxed{\mathrm{Tr}\,\rho_{\mathrm p}^2=\frac{25}{34}<1.}
```

The closest pure state remains at trace distance

```math
\frac12\left(1-\sqrt{\frac8{17}}\right)
\simeq0.1570028297,
```

where trace distance means one half of the trace norm. Independent unitary computations at Fock cutoffs 32, 48, and 64 approach the exact purity with absolute errors $1.95\times10^{-8}$, $1.63\times10^{-11}$, and $1.40\times10^{-14}$.

The full joint state is still pure and evolves unitarily. The reduced probe becomes mixed because it is correlated with the shape branch. A deterministic pure-state fluid therefore needs concentrated, well-prepared data and a reduced-state convergence theorem. The positive large-population result provides such a theorem for fixed-order marginals; it does not claim that the entire entangled many-body state becomes a product.

## 4. A kinetic continuum need not be pressureless dust

Two equal relativistic streams with proper densities $n/2$, rest energy $m$, and velocities $u_\pm=\gamma(1,\pm b)$, $0<|b|<1$, have

```math
T^{ab}=mn\gamma^2
\begin{pmatrix}1&0\\0&b^2\end{pmatrix},
\qquad
\det T=\frac{m^2n^2b^2}{(1-b^2)^2}>0.
```

Every pressureless one-velocity tensor $n\varepsilon u^a u^b$ has rank one. It cannot reproduce this two-stream stress, even when its scalar internal energy is adjusted to match the energy density.

Monokinetic preparation and a single-valued material flow before caustics are therefore substantive assumptions. The explicit free flow

```math
x(t,a)=a-tb\tanh a,
\qquad
\partial_a x=1-tb\,\mathrm{sech}^2a
```

first loses its spatial Jacobian at $a=0$, $t=1/b$. The transported density is divided by this Jacobian. Smooth pressureless closure cannot simply be continued through that event. This is a fixed-background kinematic control, not a self-gravitating solution.

Semiclassical measures naturally give Liouville or Vlasov transport in their stated settings; obtaining a single velocity and pure local internal state requires additional preparation and regularity. [Lions and Paul, *Sur les mesures de Wigner*](https://ems.press/journals/rmi/articles/5283).

## 5. Weak currents do not determine the required contact term

The repaired twist action contains $J_aJ^a$. On a periodic coordinate choose the future timelike currents

```math
J_n^0=j_0+a\sin(nx),\qquad J_n^i=0,
\qquad j_0>|a|.
```

They converge weakly to $(j_0,0)$, but

```math
J_n\cdot J_n\rightharpoonup-j_0^2-\frac{a^2}{2},
```

rather than $-j_0^2$. Integration by parts removes the oscillating terms against smooth test functions, while the quadratic defect survives.

Strong $L^2$ control is sufficient. In a bounded prescribed metric, Euclidean component norms give

```math
\|J_n^2-J^2\|_{L^1}
\le C_h\|J_n-J\|_{L^2}
\left(\|J_n\|_{L^2}+\|J\|_{L^2}\right).
```

For a normalized two-dimensional Gaussian mollifier,

```math
K_\eta(x)=\frac1{2\pi\eta^2}e^{-|x|^2/(2\eta^2)},
\qquad \|K_\eta\|_{L^2}^2=\frac1{4\pi\eta^2}.
```

Independent weighted samples therefore have the fluctuation bound

```math
\mathbb E\|J_{N,\eta}-\mathbb E J_{N,\eta}\|_{L^2}^2
\le\frac{\mathbb E|a|^2}{4\pi N\eta^2}.
```

This suggests the scale $N\eta^2\to\infty$, together with $\eta\to0$ and a controlled smoothing bias. The proved matter bridge uses a stronger operator-valued estimate that does not assume independent parcels. Its current uses a collective internal charge and an explicit ordering for the quadratic contact observable. It does not square an unregulated point-current distribution or assert an exact finite-cutoff quantum duality.

## 6. Relativistic mass averaging is an additional issue

At fixed classical momentum and geometry, define $F(e)=\sqrt{p^2+e^2}$. A single quantum mass operator gives $\mathbb E F(m_0+\widehat h)$, whereas the desired mean-energy parcel law uses $F(m_0+\mathbb E\widehat h)$. These expressions generally differ.

For internal energies $0,2$ with equal probabilities and $m_0=|p|=1$,

```math
\frac{\sqrt2+\sqrt{10}}2>\sqrt5.
```

Center-of-mass semiclassical motion alone does not remove this nonlinear averaging difference.

For $N$ independent internal copies in product preparation, let $A_N=N^{-1}\sum_j\widehat h_j$, with nonnegative $\widehat h_j$, mean $\mu$, and variance $\sigma_h^2<\infty$. With $m_0>0$,

```math
0\le F''(e)=\frac{p^2}{(p^2+e^2)^{3/2}}\le\frac1{m_0},
\qquad e\ge m_0.
```

Taylor's remainder and Jensen's inequality then give

```math
\boxed{0\le\mathbb E F(m_0+A_N)-F(m_0+\mu)
\le\frac{\sigma_h^2}{2m_0N}.}
```

The proper-clock factor $F'(e)=e/\sqrt{p^2+e^2}$ also satisfies

```math
\mathbb E|F'(m_0+A_N)-F'(m_0+\mu)|
\le\frac{\sigma_h}{m_0\sqrt N},
```

and, using concavity and $|F'''|\le3/m_0^2$,

```math
0\le F'(m_0+\mu)-\mathbb E F'(m_0+A_N)
\le\frac{3\sigma_h^2}{2m_0^2N}.
```

These are conditional expectation bounds. The [quantum-to-parcel theorem](QUANTUM_TO_PARCELS.md) supplies the separate commutator and concentration argument needed for actual dynamics of the collective-mass regulator. An energy calculation alone would not prove that dynamical limit.

## What the positive result must retain

The controlled construction adds physical transport variables, scales the population and geometry together, uses well-prepared states, works on a smooth precaustic interval, and controls currents strongly enough for the contact functional. Fixed-cutoff estimates retain their actual constants when parameters are changed.

The established mean-field literature supplies relevant methods, not an automatic theorem for the unbounded hyperbolic/oscillator model. For example, the quantitative result of [Golse, Mouhot and Paul](https://arxiv.org/abs/1502.06143v4) has its own interaction hypotheses. Strong-resolvent convergence at each fixed population does not by itself justify interchanging all cutoffs and limits.

At fixed geometric Galerkin dimension, the limit supplies the matter action and projected reciprocal shape equations. It does not automatically give pointwise twist closure, unrestricted Einstein equations, or a fixed-coupling quantum-field continuum. Those remaining obligations are identified in the [continuum contract](CONTINUUM_CONTRACT.md).

## Executed evidence and independent review

The [obstruction checker](../scripts/continuum_checks/verify_obstructions.py) passed **28 exact checks**, three Fock controls, and five collective-mass controls. Its [receipt](../evidence/continuum/obstructions/obstruction_receipt.json) separates the exact formulas from finite numerical observations.

The separate [positive-chain review](../evidence/continuum/review/REVIEW.md) checked the proposed estimates and identified corrections to clock orientation, the Hamilton–Jacobi domain, fluctuation-energy normalization, current ordering, and limit bookkeeping. Its [independent checker](../scripts/continuum_checks/review_positive_bridge.py) passed **12 exact identities and 12 bounded controls**; the [receipt](../evidence/continuum/review/review_receipt.json) records the reviewed source hashes. This was separately tasked AI-assisted checking, not external human peer review.

The calculations and review were completed before public authoring. They establish the stated mathematical controls, not experimental observations.
