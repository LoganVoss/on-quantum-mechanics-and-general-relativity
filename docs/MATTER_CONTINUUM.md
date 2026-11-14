# A controlled matter continuum with reciprocal shape response

A material continuum can be derived with quantitative error control **while a finite geometric field basis is retained**. The limit contains transported positions, internal quantum states, number current, stress, and reciprocal response of the retained shape coefficients. It is a stronger statement than sampling probes in a prescribed shape trajectory.

The microscopic family must include those transported parcels. Refining the shipped single-cell target grid or oscillator cutoff alone cannot create a spacetime current. The collective construction also scales the geometric coefficient and population extensively, $f_N=Nf$ and population $Nn_0$, and divides action and energy by $N$. This is a specified large-population, weak-gravity scaling, not a fixed $\hbar$, fixed-Newton-constant ultraviolet limit.

The fully nonlinear removal of the **geometric spatial cutoff** remains open. A separate [linearized spatial theorem](LINEARIZED_SPATIAL_LIMIT.md) removes that cutoff in a controlled tangent sector.

## 1. Material trajectories and the covariant action

Let $a$ label a compact material domain with smooth positive weight $w(a)$. On a prescribed smooth Lorentzian background $h_{ab}$, consider future-timelike trajectories
```math
X^a(t,a)=(t,X(t,a)),\qquad
b(t,a)=\sqrt{-h_{ab}(X)\dot X^a\dot X^b}>0.
```

Work before caustics: $X_t$ is a diffeomorphism, its Jacobian $\mathcal J_X=\det D_aX$ is bounded below, and the proper-clock factor $b$ has a positive lower bound. Each parcel carries a normalized internal state $\psi(t,a)$ with the [selected probe Hamiltonian](DYNAMICAL_COUPLING.md). Its material action is
```math
S_{\mathrm{mat}}
=\int dt\,da\,w(a)
\left[
i\hbar\langle\psi|\dot\psi\rangle
-b\left(m_0+\langle\widehat H_q(X)\rangle\right)
\right],
\qquad m_0>0.
```

A symmetrized real Berry term gives the same normalized-state variation. Define Eulerian fields through the inverse material map:
```math
j^0(t,X)=\frac{w}{\mathcal J_X},\qquad
j^i=j^0\dot X^i,\qquad
n=\frac{j^0b}{\sqrt{-h}},\qquad
u^a=\frac{\dot X^a}{b},\qquad
\Psi(t,X)=\psi(t,a).
```

Changing variables $d^2x=\mathcal J_X\,da$ gives exactly
```math
S_{\mathrm{mat}}
=\int d^3x
\left[
j^a i\hbar\langle\Psi|\partial_a\Psi\rangle
-\sqrt{-h}\,n\left(m_0+\langle\widehat H_q\rangle\right)
\right].
```

The number-current identity $\partial_a j^a=0$ follows from the transported material measure. The velocity-potential and Clebsch representation supplies the covariant state-fluid action in [Current and reconstruction](CURRENT_AND_RECONSTRUCTION.md). General material trajectories correspond locally to the Clebsch-capable formulation; one velocity potential alone describes a restricted subclass. This action structure has established precedent in [Brown’s relativistic-fluid formulation](https://arxiv.org/abs/gr-qc/9304026v1).

The change of variables is an exact pre-caustic equivalence. It does not itself prove that a quantum regulator approaches these trajectories.

### The relativistic parcel generator and its clock

For
```math
h=-L^2dt^2+\gamma_{ij}(dx^i+\beta^i dt)(dx^j+\beta^jdt),
```
the corresponding canonical parcel Hamiltonian is
```math
H_{\mathrm{par}}
=L\sqrt{\gamma^{ij}P_iP_j+
\left(m_0+\langle\widehat H_q(X)\rangle\right)^2}
-\beta^iP_i.
```

Writing $\varepsilon=m_0+\langle\widehat H_q\rangle$, its internal evolution has multiplier
```math
\frac{L\varepsilon}
{\sqrt{\gamma^{ij}P_iP_j+\varepsilon^2}}
=\frac{d\tau}{dt}.
```

Thus the quantum equation uses the proper flow clock:
$i\hbar\,d\psi/d\tau=\widehat H_q\psi$.

The expectation inside the square root is consequential. For a single quantum parcel, $\langle\sqrt{P^2+(m_0+\widehat H)^2}\rangle$ generally differs from $\sqrt{P^2+(m_0+\langle\widehat H\rangle)^2}$. The collective composite-parcel construction is an additional microscopic assumption needed to obtain the latter mass law; it is not implied by the old single-cell Hamiltonian.

## 2. A nonlinear reciprocal limit at a fixed geometric basis

Choose a fixed finite smooth spatial basis for the shape field $q_c(x)$, including a constant twist-shift mode. Restrict the selected shape action to that basis. On a compact regular region, the finite positive kinetic matrix is invertible and the resulting Hamiltonian vector field is smooth.

The internal sector may use a fixed Fock cutoff, or the exact Gaussian coordinates $(u,v)$ in a region with $v>0$ bounded away from zero. Under a classical quadratic Hamiltonian the centered Gaussian family is invariant. The background metric is prescribed; the shape coefficients are dynamical.

Write the common reciprocal equations as
```math
\dot z=F(z,t)+\int_A w(a)G(z,\xi(t,a),t)\,da,\qquad
\dot\xi(t,a)=V(z,\xi(t,a),t).
```

Here $z$ contains the retained shape coefficients and momenta, and $\xi$ contains the parcel position, momentum, and internal variables. The force $G$ and parcel evolution $V$ come from the **same** Hamiltonian. This retains both directions of influence.

Partition $A=[0,1]^d$ into midpoint cells of width $h$, with centers $a_j$ and weights $m_j=h^d w(a_j)$. Replace the integral by $\sum_jm_jG$ and evolve every parcel with the same $V$.

Suppose the regular region has Lipschitz bounds
```math
\begin{aligned}
|F(z)-F(z')|&\le L_F|z-z'|,\\
|G(z,\xi)-G(z',\xi')|&\le L_G(|z-z'|+|\xi-\xi'|),\\
|V(z,\xi)-V(z',\xi')|&\le L_V(|z-z'|+|\xi-\xi'|),
\end{aligned}
```
and $\sum_jm_j\le W_*$. Define
```math
Q_T=\frac1{24}\sum_{\ell=1}^d
\sup_{[0,T]\times A}
\left\|
\partial_{a_\ell}^2
\left[w(a)G(z(t),\xi(t,a),t)\right]
\right\|,
\qquad
C=L_F+W_*L_G+L_V.
```

For
```math
E_h(t)=|z_h(t)-z(t)|
+\max_j|\xi_j(t)-\xi(t,a_j)|,
```
the error satisfies
```math
\boxed{
E_h(t)\le e^{Ct}E_h(0)
+Q_T h^2\frac{e^{Ct}-1}{C}.}
```
The last factor is $t$ when $C=0$.

**Proof.** Subtract the coefficient equations and add/subtract the midpoint samples of the continuum integrand. The midpoint remainder is at most $Q_T h^2$. The remaining terms are bounded by the three Lipschitz constants. The upper Dini derivative of $E_h$ is at most $CE_h+Q_T h^2$; integration gives the result.

The constant is inspectable. If $A_1$ and $A_2$ bound the first and second material derivatives of $\xi$, a second derivative of $wG$ is bounded by
```math
\|w''\|G_0+2\|w'\|G_1A_1+
\|w\|(G_2A_1^2+G_1A_2).
```

The differentiated parcel ODE bounds $A_1,A_2$ on the common time interval. It also controls the $C^1$ difference of the continuous flow extension generated by $z_h$, so a strict Jacobian margin persists for sufficiently small $h$. Smooth cutoffs outside the regular neighborhood can be used in the proof; they are inactive on these trajectories.

This is a nonlinear feedback theorem, not an assumption that the desired trajectory is already known. Its constants can depend on the retained geometric basis, internal cutoff, localization, and time.

### What survives the fixed-basis limit

The material-label continuum gives the Brown state-fluid action coupled to the **projected** shape equations. The matter transport and its Ward identity are exact. The geometric equation is tested only against the retained basis.

Consequently, the full local twist equation need not vanish outside that space. Global or retained-mode shift conservation is weaker than pointwise $d(*C)=0$. A fixed-basis limit alone does not establish unrestricted local $F=dA$ reconstruction or the full Einstein equations.

## 3. Strong currents are needed for the contact interaction

Weak empirical convergence does not justify the current-squared term. Use an even normalized smooth kernel
```math
K_\eta(x)=\eta^{-d}K(x/\eta)
```
with finite second moment and square-integrable derivatives through order two.

The $O(\eta^2)$ even-kernel bias assumes a periodic domain or interior observations with a smooth extension and the required $H^2$ current regularity; it does not cover an abrupt vacuum boundary.

Fold proper-clock, velocity, metric-volume, number-weight, and internal-expectation factors into the material current amplitude. On a regular coordinate patch, the coordinate and physical $L^2$ norms are equivalent. Let $\delta_{\mathrm{path}}$ bound parcel position errors and $\delta_{\mathrm{amp}}$ bound **all** amplitude errors, including velocity and internal state. Then
```math
\boxed{
\|J_{h,\eta}-J\|_2
\le C_T\left[
\eta^2+h^2\eta^{-d/2-2}
+\delta_{\mathrm{path}}\eta^{-d/2-1}
+\delta_{\mathrm{amp}}\eta^{-d/2}
\right].}
```

The four terms are the symmetric-kernel bias, the $L^2_x$ midpoint remainder, translation error, and amplitude error. Two material derivatives bring at most two derivatives of the kernel; $\|\nabla^rK_\eta\|_2=\eta^{-d/2-r}\|\nabla^rK\|_2$ gives the displayed powers.

For two spatial dimensions, choose $\eta=h^{2/5}$. Classical reciprocal parcel errors of order $h^2$ then give
```math
\|J_{h,\eta}-J\|_2=O(h^{4/5}).
```

The contact term follows by Cauchy–Schwarz:
```math
\|J_{h,\eta}^2-J^2\|_1
\le(\|J_{h,\eta}\|_2+\|J\|_2)
\|J_{h,\eta}-J\|_2,
```
with the bounded inverse-metric factor included for Lorentzian contraction.

This constructs a meaningful limiting contact functional. It does not define an unregulated square of a point current.

## 4. Quantum current fluctuations and operator ordering

The same estimate can control the quantum current itself, not just its mean. Let $\widehat X_j$ have jointly commuting position components, and let $\widehat B_j$ be a bounded self-adjoint current amplitude. Its internal charge must be the appropriate **collective charge per probe** when the classicalization uses a populated parcel.

Define
```math
\widehat J_\eta(x)
=\sum_jm_j\frac{
K_\eta(x-\widehat X_j)\widehat B_j+
\widehat B_jK_\eta(x-\widehat X_j)}2.
```

Compare with classical $X_j,b_j$. Let $\delta_{X,j}$ and $\delta_{B,j}$ be the RMS deviations in the common quantum state. Spectral calculus gives
```math
\int\|K_\eta(x-\widehat X_j)\phi\|^2\,dx
=\|K_\eta\|_2^2\|\phi\|^2,
```
and
```math
\int\|
[K_\eta(x-\widehat X_j)-K_\eta(x-X_j)]\Psi
\|^2\,dx
\le\|\nabla K_\eta\|_2^2
\langle|\widehat X_j-X_j|^2\rangle.
```

For the first operator order, use $K(B-b)+b(K-K_{\mathrm{cl}})$. For the second, use $B(K-K_{\mathrm{cl}})+K_{\mathrm{cl}}(B-b)$. Therefore
```math
\begin{aligned}
\|(\widehat J_\eta-J_{\mathrm{cl},\eta})\Psi\|_{L^2_x\mathcal H}
\le\sum_jm_j\bigg[
&\|K_\eta\|_2\delta_{B,j}\\
&+\frac{\|\widehat B_j\|+|b_j|}{2}
\|\nabla K_\eta\|_2\delta_{X,j}
\bigg].
\end{aligned}
```

No statistical independence, or commutation of $\widehat B_j$ with $\widehat X_j$, is assumed. A bounded symmetrized velocity/charge product is handled by telescoping its factors. The operator norms and their cutoff dependence must remain in the constants.

For the contact expression, specify an ordering. Set
```math
\widehat A_a(x)=\widehat\lambda(x)\widehat J_a(x),
\qquad
\widehat{\mathcal Q}(x)
=h^{ab}(x)\widehat A_a(x)^\dagger\widehat A_b(x).
```

If $\widehat\lambda$ is bounded and its RMS error is controlled, the same product estimate bounds $\|(\widehat A-A)\Psi\|_{L^2_x\mathcal H}=\delta_A$, where $A_a=\lambda J_a$. Then
```math
\int\left|
\langle\widehat{\mathcal Q}\rangle
-\lambda^2h^{ab}J_aJ_b
\right|dx
\le
\|h^{-1}\|_\infty
\delta_A(2\|\lambda J\|_2+\delta_A).
```

This is convergence of a declared ordered quantum observable. It does not claim that scalar–connection dualization is an exact identity of the finite-population quantum theory.

### A sufficient diagonal scaling

In two dimensions, suppose the relevant RMS errors are bounded by
$\delta\le A_h/\sqrt{Nh^2}$, with all time, occupied-density, preparation, localization, and cutoff factors retained in $A_h$. This constant is independent of the subsequently chosen global population $N$; rounding-ratio bounds are taken uniformly in $N$. With $\eta=h^{2/5}$, the sufficient choice
```math
N\ge A_h^2h^{-26/5}
```
makes the dominant quantum path term no larger than order $h^{4/5}$.

Integer count rounding has two effects. Its total weight discrepancy is $O((Nh^2)^{-1})$, giving a direct current contribution $O((Nh^2\eta)^{-1})$. It also changes the reciprocal trajectories through the classical equations; the resulting path and amplitude errors must enter their respective kernel terms. With the displayed scaling, and $A_h$ large enough to include their Grönwall constants, these contributions are of orders $h^{12/5}$ and $h^{14/5}$, below the leading $h^{4/5}$ error.

This is a sufficient controlled scaling, not a claim of an efficient or cutoff-uniform quantum field limit.

## 5. Ordered removal of the internal Fock cutoff

On a compact classical target path with bounded proper-clock factor, a quadratic Hamiltonian preserves centered Gaussianity. If the squeezing magnitude obeys $r(t)\le r_{\ast}<\infty$, put $\theta=\tanh r_{\ast}<1$. In the reference Fock basis,
```math
|c_n(t)|\le\theta^{n/2},
\qquad
\|(1-P_D)\psi(t)\|
\le\frac{\theta^{D/2}}{\sqrt{1-\theta}}.
```

Quadratic evolution connects only $n$ to $n,n\pm2$. If the off-diagonal pair coefficient has magnitude at most $B$, the omitted boundary coupling is bounded by
```math
\|P_DH(1-P_D)\psi\|
\le B(D+2)\frac{\theta^{D/2}}{\sqrt{1-\theta}}.
```

For the following explicit bound, both states use the same prescribed time-dependent quadratic generator, including the same proper-clock multiplier: $\psi_D$ evolves under $P_DH(t)P_D$. Duhamel’s formula, including normalized projected initial data, gives the safe bound
```math
\boxed{
\|\psi_D-\psi\|
\le
\left[3+\frac{BT(D+2)}{\hbar}\right]
\frac{\theta^{D/2}}{\sqrt{1-\theta}}.}
```

For vacuum initial data, the initial projection error is zero and the leading 3 can be replaced by 1. Quadratic source and current expectations have a corresponding polynomial in $D$ times exponential-tail bound.

For reciprocal finite-basis feedback, use the weighted error with
$\widehat{\mathcal N}=a^\dagger a+1$. Neighboring Fock-level differences yield
```math
\frac{d}{dt}
\langle\widehat{\mathcal N}^{2s}\rangle_D
\le C_s\langle\widehat{\mathcal N}^{2s}\rangle_D,
```
uniformly in $D$ on the compact coefficient region. The weighted state error is bounded by its current size, the classical-variable error, and a forcing of order $D^2\theta^{D/2}$. Quadratic-source errors obey the same weighted estimate. Coupled Grönwall and regular-region bootstrap therefore control ordered internal-cutoff removal at fixed geometric basis. Smooth label derivatives require the analogous finite weighted regularity of the initial states; smooth Gaussian label data satisfy it.

All limits use the same regular time interval, with uniform target, clock, and Jacobian margins. This does not supply cutoff-uniform estimates for arbitrary entangled finite-population states; the population limit must retain its actual $D$-dependent constants.

### A retained shear boundary defect

Hard Fock projection is not exactly shear covariant. For $P=P_D$ and $G=\widehat Q^2/2$,
```math
[PhP,PGP]-P[h,G]P
=-Ph(1-P)GP+PG(1-P)hP.
```

These boundary terms are supported on the last two retained levels and can have operator norm of order $D^2$. At $D=6,\chi=1/3,\lambda=2$, the checked Noether residual has diagonal
```math
(0,0,0,0,5/4,7/4)
```
and squared Frobenius norm $37/8$.

Their expectation is bounded by
$C D^{2-2s}\|\widehat{\mathcal N}^{s}\psi_D\|^2$, which tends to zero for a uniform moment bound with $s>1$. Thus the full shear/current identity is recovered in the ordered $D\to\infty$ limit. A finite $D$ current observable is not automatically an exactly conserved Noether current. Even after this removal, a fixed geometric basis supplies only projected twist closure.

## Verification and remaining obligation

The [unchanged field checker](../scripts/continuum_checks/verify_field_continuum.py) and [executed receipt](../evidence/continuum/field/field_continuum_receipt.json) include **92 exact checks**, nonlinear reciprocal material-grid convergence, strong current/contact controls, the linearized spatial checks, and an independent Fock-cutoff comparison.

The nonlinear numerical control retains one homogeneous shape mode and evolves the shape together with a continuum of Gaussian probes on a prescribed background. Material-grid errors decrease from $1.59\times10^{-4}$ to $2.49\times10^{-6}$ with orders approaching 2. This exercises reciprocal feedback; it is not a full finite-amplitude Einstein solution.

The internal-cutoff control retains the insufficient 24-level result, with covariance error $7.66\times10^{-11}$, and reaches $9.99\times10^{-15}$ at 32 levels. A numerically printed zero ray error at the largest cutoff means floating-point resolution, not an exact identity.

The remaining nonlinear task is geometric spatial-cutoff removal with estimates strong enough for the full field equations, constraints, and reconstruction. The finite-basis theorem does not assume that missing result. The classical particle/continuum stability framework has established precedents, including [Dobrushin’s Vlasov analysis](https://doi.org/10.1007/BF01077243) and [Iacobelli’s Wasserstein stability work](https://doi.org/10.1007/s00205-021-01705-9); no worldwide-priority claim is made here.

