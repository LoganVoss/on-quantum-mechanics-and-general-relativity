# A controlled matter-sector continuum

The result is a finite-time connection from an **explicitly augmented quantum regulator** to the covariant state-fluid matter action, with reciprocal shape response through a **fixed finite geometric basis**. The unrestricted nonlinear geometric continuum is not established.

The additions to the microscopic model are explicit: physical parcel positions, transport Hamiltonians, symmetric populations of internal probes, spatial shape couplings, and a collective scaling. Refining the previous one-cell target grid alone cannot supply these variables.

## What is being taken to a limit?

| Parameter | Meaning | Result |
|---|---|---|
| $N$ | Collective population and extensive geometric-action scale | Quantum concentration and pure internal-state closure |
| $\ell$ | Mesh of physical material labels | Nonlinear matter continuum before caustics |
| $\eta$ | Width of the current mollifier | Strong current and contact-functional convergence |
| $d$ | Internal oscillator cutoff | Separate ordered removal under moment and regularity hypotheses |
| Fourier/phase regularization | Positive canonical approximants and localization | Explicit approximation error included before selecting $N$ |
| $L$ | Number of geometric modes | **Fixed in the nonlinear theorem** |
| $a$ in the separate linear theorem | Physical spatial lattice spacing | Full smooth linearized spatial limit on the specified Einstein-dust background |

The old radial/angular grid instead resolves possible values of one shape matrix. It is not a physical spatial mesh. [Obstructions and controls](CONTINUUM_OBSTRUCTIONS.md).

## Main theorem: the declared regime

Fix a finite geometric basis $L$, a finite internal cutoff $d$, a positive rest energy $m_0$, and a prescribed smooth $2+1$ background metric. Use a regular finite interval on which the limiting phase-space trajectories stay inside a compact physical patch, the target heights remain positive, and the material flow is a smooth diffeomorphism with a positive Jacobian margin. The occupied label region has smooth number density bounded away from zero. For the strong current estimate, use a periodic domain or interior observations with a smooth extension, and require the limiting current to have the stated $H^2$ regularity. An abrupt vacuum boundary does not satisfy that bias premise.

The field modes, parcel centers and momenta, and internal states evolve under one common Hamiltonian. Shape responds to matter; it is not prescribed as an external forcing. The background spacetime metric remains prescribed, and the shape equations are projected onto the retained modes.

At fixed cutoffs, these conditions hold on a nonempty short-time interval for regular data. In material coordinates the system is a smooth ODE on the finite mode variables and regular label maps. Its right-hand side has no label derivatives; local existence and stability therefore follow before the position map reaches a caustic or the trajectory exits the physical patch.

For this regime there is a family of finite self-adjoint quantum regulators and well-prepared states whose phase-space observables, fixed-probe marginals, matter sources, and mollified currents converge to the corresponding state-fluid quantities. The zero-shift realization has nonnegative kinetic and mass terms; generic self-adjointness does not by itself imply positivity.

The proof has three quantitative stages.

## 1. Quantum dynamics to reciprocal parcels

For a regulator with local population parameter $n$, the [bounded-algebra theorem](QUANTUM_TO_PARCELS.md) gives

```math
\mathfrak D_n(t)
\le e^{Ct}\left[\mathfrak D_n(0)+\frac{B^2t}{n^2}\right],
\qquad \mathfrak D_n(0)\le\frac{C_{\mathrm{prep}}}{n}.
```

Here $\mathfrak D_n$ is a sum of squared deviations of bounded canonical and collective internal observables. The constants come from the actual finite polynomial coefficients, positive mass gaps, and observable norms. They are independent of population for that regulator specification, but need not remain bounded when other cutoffs change.

The exact symmetric-sector identity gives a corresponding statement for reduced quantum states:

```math
S_n=2\beta_n+\frac{d-1}{n},
\qquad
\|\rho_n^{(k)}-\rho^{\otimes k}\|_1
\le\sqrt{2kS_n},\qquad k\le n.
```

Thus the internal state remains quantum while collective geometry and transport concentrate around their classical values. This is not convergence of the entire many-body state to a product in norm.

The relativistic parcel uses a collective mass,

```math
H_n^{\mathrm{parcel}}
=n\sqrt{P_n^2+
\left[m_0+A_n(\widehat H_M)\right]^2}.
```

Its limit is

```math
E=\sqrt{p^2+\varepsilon^2},
\qquad
\varepsilon=m_0+\langle\widehat H_M\rangle,
\qquad
i\hbar\dot\psi=\frac{\varepsilon}{E}\widehat H_M\psi.
```

Since $\dot X=p/E$, the multiplier $\varepsilon/E$ is exactly $d\tau/dt$. The internal evolution therefore uses the required proper-flow clock. The exact Legendre transform produces the state-dependent worldline integrand of the covariant matter model.

The same square-root resolvent estimate controls Fréchet derivatives of the **actual regulator Hamiltonian**. Source and stress variations are not assigned after the limit.

### Population and density scaling

For material weights $\mu_j\simeq n_0(a_j)\ell^2$, choose $K_j=\mathrm{round}(N\mu_j)$ probes per parcel. Scale the geometric action by $N$, and normalize action and energy per $N$. In an occupied patch,

```math
K_{\min}\ge c_0N\ell^2
```

once the population is sufficiently large. Rounding changes both weights and subsequent trajectories.

This is a collective, large-population weak-coupling family. It is **not** a fixed $\hbar$, fixed-Newton-constant ultraviolet limit. The kinetic-floor and purity controls show why those operations cannot be interchanged without additional work.

## 2. Parcels to the covariant matter action

The [material-coordinate proof](MATTER_CONTINUUM.md) establishes a reciprocal midpoint-quadrature estimate,

```math
e_\ell(t)
\le e^{C_Tt}e_\ell(0)
+Q_T\ell^2\frac{e^{C_Tt}-1}{C_T},
```

with the continuous interpretation at $C_T=0$. Positive-polynomial approximation adds its declared error, and rounding adds a trajectory/source error of order $1/(N\ell^2)$. These bounds retain the geometric basis and internal cutoff in their constants.

Before caustics, changing variables from material labels to spacetime sends the label-integrated worldline/state action exactly to

```math
S_m=\int\left[
j^\mu\left(\partial_\mu\vartheta
+i\hbar\langle\psi|\partial_\mu\psi\rangle
+\beta_A\partial_\mu\alpha^A\right)
-\sqrt{-h}\,n\left(m_0+\langle\widehat H_M\rangle\right)
\right]d^3x.
```

The Clebsch variables allow general local flow. This is the same state-fluid matter action used in the current-reconstruction model. Its proper-time Schrödinger equation, stress, and reciprocal target sources follow from this common action.

At finite $L$, the geometric equations are still Galerkin equations. Matter convergence does not turn them into the full pointwise Einstein/wave-map system.

## 3. Strong current control preserves the contact term

The quantum current uses the **collective** charge $A_{K_j}(\widehat Q^2/2)$. A single probe retains intrinsic quantum variance and cannot be substituted in the concentration estimate.

Use a smooth even kernel and a definite symmetric order,

```math
\widehat J_{\ell,\eta}(x)
=\sum_j\frac{\mu_j}{2}
\left\{K_\eta(x-\widehat X_j),\widehat B_j\right\}.
```

The amplitude includes the transport velocity, collective internal charge, and prescribed volume factors. This is a specified coarse observable; exact finite-cutoff local conservation is not assumed. The quantum-current proof uses spectral calculus for commuting positions and does not require independence between different parcels.

In two material dimensions,

```math
\delta_J\le C_T\left[
\eta^2+\ell^2\eta^{-3}
+\delta_{\mathrm{path}}\eta^{-2}
+\delta_{\mathrm{amp}}\eta^{-1}
+\frac{1}{N\ell^2\eta}
\right].
```

The path/amplitude terms include quantum RMS deviations, finite positive-approximation error, reciprocal material-grid error, and rounding-induced evolution error. All cutoff-dependent physical observable norms are included before selecting the population.

Strong convergence controls the quadratic contact functional:

```math
\|\langle\widehat J^2\rangle-J^2\|_{L^1}
\le \delta_J\left(2\|J\|_{L^2}+\delta_J\right).
```

For metric contractions, multiply by the bounded inverse-metric operator norm. The $\lambda$-weighted version uses the definite order
$\mathrm{Re}\langle(\widehat\lambda\widehat J_a)\Psi, (\widehat\lambda\widehat J_b)\Psi\rangle$.
It is controlled by the bounded coefficient and its RMS concentration. Another noncommuting ordering is not silently identified with it.

Weak current convergence would be insufficient: the oscillatory-current counterexample retains a nonzero $J^2$ defect. The strong estimate is what allows the mandatory contact term to survive the matter limit.

## One explicit sufficient diagonal

For fixed geometric/internal cutoffs, absorb all preparation and physical-observable constants into $A_\ell\ge1$, so that

```math
\delta_{\mathrm q}
\le\frac{A_\ell}{\sqrt{N\ell^2}}.
```

Set

```math
\ell=s^5,\qquad \eta=s^2,\qquad
N\ge A_\ell^2s^{-26},\qquad 0<s\le1.
```

Then $\delta_{\mathrm q}\le s^8$. Choose the positive approximation accuracy so its induced physical errors are also at most $s^8$. The leading terms are

```math
\eta^2=s^4,\qquad
\ell^2\eta^{-3}=s^4,\qquad
\delta_{\mathrm q}\eta^{-2}\le s^4.
```

Rounding-induced path and direct-weight terms have normalized powers $s^{12}/A_\ell^2$ and $s^{14}/A_\ell^2$, multiplied by their fixed evolution and weight constants. Those constants are included in the outer $C_T$; the ordinary $O(\ell^2)$ path error is smaller as well. Hence

```math
\boxed{\delta_J=O(\ell^{4/5}),\qquad
\text{contact error}=O(\ell^{4/5})}
```

with the declared fixed-cutoff constants. The population may be extremely large because $A_\ell$ contains the actual finite regulator's coefficients and evolution factors. This is a sufficient controlled construction, not an optimal rate or an efficiency result.

## Ordered internal-cutoff removal

The separate weighted-moment/Duhamel theorem controls the limiting classical parcel/state system as the oscillator cutoff grows. For $A=\widehat n+1$, the quadratic Hamiltonian's bandwidth-two structure gives moment bounds uniform in the internal cutoff. With $s_0>3/2$,

```math
\mathrm{error}_d(T)\le C_T(d-2)^{-s_0+3/2},
```

under the common regular-interval and moment hypotheses. Gaussian data allow exponential-tail estimates. Label derivatives required by current reconstruction need the corresponding higher weighted moments and regularity.

For a combined sequence, use a tolerance-based order: choose a kernel width from the limiting current bias; choose the internal cutoff for the desired weighted path/amplitude accuracy at that width; choose the material mesh; then choose positive Fourier approximation accuracy with its kernel factors included; **choose population last**, using the resulting actual coefficient norms. Never hold a nonzero approximation error fixed while multiplying it by an increasingly singular kernel factor.

Finite Fock projection does not preserve the exact metaplectic shear identity. Its explicit boundary defect vanishes only in the controlled ordered internal limit. The resulting matter current and contact functional converge, but at fixed $L$ total twist conservation still holds only in the retained test space. Full local reconstruction requires the missing geometric PDE limit.

## A separate result without a geometric spatial cutoff

The [linearized spatial theorem](LINEARIZED_SPATIAL_LIMIT.md) removes the physical lattice in the quantized quadratic sector on an exact Einstein-dust background. It proves

```math
\sqrt{\mathcal E_{\mathrm{RMS}}(T)}
\le\frac{\pi}{2}\delta_{\mathrm{initial}}
+\frac{\pi}{24}a^2\log(T/t_0)Q
+(a/\pi)^3Q.
```

Here $a$ is the physical spatial mesh, and $Q$ measures the declared smooth initial Fourier tail. Absolute common-zero-mode variance needs separate localization. This theorem includes reciprocal shape/internal dynamics; it does not upgrade the nonlinear fixed-mode theorem into a nonlinear geometric continuum.

The remaining major obligation is therefore specific: remove the nonlinear geometric cutoff with suitable field and constraint estimates. The present result supplies the quantum-to-matter and strong-current parts of that route.
