# A controlled linearized spatial continuum

A complete spatial-cutoff estimate is available for the reciprocal **linearized** shape–matter system on an exact three-dimensional Einstein-dust background. The quantum quadratic regulator has the same first-moment equations, and its centered fluctuation energy can be controlled separately.

This theorem is stronger than refining one Fourier mode, but it remains a tangent-sector result. It does not establish the nonlinear geometric cutoff limit discussed in [Matter continuum](MATTER_CONTINUUM.md).

## 1. An exact covariant background

Use the three-dimensional Einstein-frame metric and material density
```math
h_3=-dt^2+t^2(dx^2+dy^2),
\qquad
n(t)=\frac{n_0}{t^2},
\qquad
n_0m_0=2f,
\qquad t\ge t_0>0.
```

Set the background target to $(\chi,\lambda)=(0,1)$ and the probe to its matched ground state, with excitation energy subtracted. The matter is comoving. Direct curvature calculation gives
```math
\mathrm{Einstein}_{00}=\frac1{t^2},
\qquad
\mathrm{Einstein}_{ij}=0,
```
so the Einstein equation holds:

```math
2f\mathrm{Einstein}_{ab}=T^{\mathrm m}_{ab}.
```

Let
```math
q=(\chi,\delta\lambda),\qquad
z=(u,\delta v),\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
```

Probe excitation energy, shape stress, and the force that changes matter velocity are quadratic in perturbation amplitude. Hence first-order density, velocity, and metric perturbations may remain zero while the shape and internal perturbations interact.

The resulting first-order equations are
```math
\boxed{
q_{tt}+\frac2tq_t-\frac1{t^2}\Delta_xq
=-\frac{g_0}{t^2}(q-z),
\qquad
z_t=2\omega J(q-z),
\qquad
g_0=\frac{n_0\hbar\omega}{2f}.}
```

In components, $u_t=2\omega(\delta v-\delta\lambda)$ and
$\delta v_t=2\omega(\chi-u)$, fixing the symplectic orientation.

These equations are the exact linearization of the declared covariant model on this background. They are not obtained by inserting a chosen shape trajectory into the quantum equation.

## 2. The quadratic action and energy

The tangent action is
```math
L_2=\int d^2x\left[
\frac{ft^2}{2}|q_t|^2
-\frac f2|\nabla q|^2
+\frac{n_0\hbar}{4}z_2\dot z_1
-\frac{n_0\hbar\omega}{4}|q-z|^2
\right].
```

With $p=ft^2q_t$ and $c=n_0\hbar\omega/2$, a Fourier mode has positive Hamiltonian
```math
\boxed{
H_k(t)=\frac{|p|^2}{2ft^2}
+\frac{f|k|^2}{2}|q|^2
+\frac c2|q-z|^2.}
```

The canonical geometric bracket and internal bracket
$\{z_1,z_2\}=4/(n_0\hbar)$ reproduce both equations. At collective scale $N$, the corresponding commutators are
```math
[\widehat q,\widehat p]=\frac{i\hbar}{N},
\qquad
[\widehat z_1,\widehat z_2]=\frac{4i}{Nn_0},
```
with normalized action multiplied by $N$. The physical Schrödinger evolution is $i\hbar\partial_t\Psi=N\widehat H_k\Psi$, where $H_k$ is the displayed normalized Hamiltonian.

A quadratic quantum Hamiltonian evolves first moments by these same linear equations exactly. This is the quantization of the quadratic tangent theory; its identification with the full finite-amplitude microscopic dynamics would require a separate error estimate.

The energy has a useful work identity:
```math
\boxed{\frac{dH_k}{dt}=-\frac{|p|^2}{ft^3}\le0.}
```

The decrease reflects the time-dependent cosmological background. The quantum centered fluctuation energy obeys the same nonincrease law. No false time-translation conservation is imposed on this expanding background.

## 3. Spatial lattice and exact mode error

On a periodic spatial domain, centered lattice differences replace $|k|^2$ by
```math
|k_h|^2=\sum_i
\left[\frac2h\sin\left(\frac{k_i h}{2}\right)\right]^2.
```

For resolved modes,
```math
0\le |k|^2-|k_h|^2
\le\frac{h^2}{12}\sum_i k_i^4,
\qquad
|k_h|\ge\frac2\pi|k|.
```

The lattice preserves the same reciprocal internal coupling. Initialize it with the spectral projection of the continuum initial data, rather than silently identifying point sampling with spectral projection.

For one resolved mode, subtract the continuum and lattice systems. The difference in the momentum equation is the forcing
$-f(|k_h|^2-|k|^2)q_h$. Let $H_{e,k}$ denote the **continuum** energy of the mean-solution error. Since lattice energy is nonincreasing,
```math
\frac{d}{dt}\sqrt{H_{e,k}(t)}
\le
\frac{\big||k_h|^2-|k|^2\big|}
{t|k_h|}
\sqrt{H_{h,k}(t_0)}.
```

The estimate follows directly from
$|p_e|\le\sqrt{2f}\,t\sqrt{H_{e,k}}$ and
$|q_h|\le\sqrt{2H_{h,k}/(f|k_h|^2)}$.
Also $H_{h,k}(t_0)\le H_k(t_0)$. Integrating gives
```math
\boxed{
\sqrt{H_{e,k}(T)}
\le
\frac{\pi}{24}h^2
\log\left(\frac T{t_0}\right)
|k|^3\sqrt{H_k(t_0)}.}
```

The zero mode has no spatial-symbol error and its mean equations are treated exactly.

## 4. A full smooth-field bound

Assume the weighted initial energy is finite:
```math
Q^2=\sum_k |k|^6H_k(t_0)<\infty.
```

Summing the resolved-mode estimate and bounding the omitted Fourier tail yields
```math
\boxed{
\sqrt{E_{\mathrm{mean}}(T)}
\le
\frac{\pi}{24}h^2
\log\left(\frac T{t_0}\right)Q
+\left(\frac h\pi\right)^3Q.}
```

The second term follows because every omitted mode has $|k|\ge\pi/h$ and each mode’s energy is nonincreasing. This is a whole-field estimate with an explicit smoothness requirement, not an extrapolation from one successful numerical mode.

Suppose the initial quantum centered fluctuation energy measured with the **lattice** Hamiltonian is at most $\delta_{\mathrm{initial}}^2$. On resolved modes,
```math
H_k\le\frac{\pi^2}{4}H_{h,k}.
```

Therefore the continuum-energy RMS error is bounded by
```math
\boxed{
\sqrt{E_{\mathrm{RMS}}(T)}
\le
\frac\pi2\,\delta_{\mathrm{initial}}
+\frac{\pi}{24}h^2
\log\left(\frac T{t_0}\right)Q
+\left(\frac h\pi\right)^3Q.}
```

The factor $\pi/2$ converts lattice fluctuation energy to continuum energy; omitting it would mix two different norms. Refining the spatial mesh does not itself make $\delta_{\mathrm{initial}}$ small. The collective preparation and scaling must ensure that separately.

### The zero-mode qualification

The energy is a seminorm on a common constant configuration $q=z$, $p=0$. It does not control that configuration’s absolute variance. Claims about all shape-coordinate observables additionally require initial localization of the common zero mode and its separate finite-dimensional covariance propagation.

The displayed bound is an energy-norm convergence theorem. It must not be relabeled a uniform pointwise bound without the additional regularity and zero-mode conditions.

## 5. Repaired current closure and background flux

Even the matched oscillator ground state carries the shear charge
$\langle\widehat Q^2/2\rangle=1/4$. Its background current is
```math
J^0=\frac{\hbar n_0}{4t^2}.
```

The [current-corrected reconstruction](CURRENT_AND_RECONSTRUCTION.md) gives the local background curvature
```math
F_{12}=-\frac{\hbar n_0}{4f}.
```

It is closed and nonzero. The shifted curvature $F+*J/f$ vanishes when $\chi$ is constant, as required by the scalar description. Setting this background connection curvature to zero would discard the current correction.

At first order,
```math
\delta J^0=-\frac{\hbar n_0}{4t^2}z_2.
```

The coupled $\chi$ and $z_2$ equations cancel in
$\partial_a(\sqrt{-h}\,C^a)$, with
$C=f\lambda^{-2}d\chi+J$. Thus the linearized system preserves the repaired total-current identity.

A constant flux on a spatial torus need not be globally exact. A global four-dimensional bundle, its flux quantization, and its boundary sector require additional data. This theorem supplies a covariant three-dimensional background and local reconstruction; it does not assert a global zero-twist uplift.

## 6. Executed controls

The [field-continuum checker](../scripts/continuum_checks/verify_field_continuum.py) and [receipt](../evidence/continuum/field/field_continuum_receipt.json) retain the exact background, Hamiltonian, energy-work, and current-closure calculations.

For Fourier mode $(1,2)$ on $t\in[1,2]$, grids of 16, 32, 64, and 128 points per direction give observed endpoint convergence orders
**2.0105, 2.0028, and 2.0007**. Every computed energy error is below the explicit analytic estimate. These bounded tests check coefficients and implementation; the global theorem is the mode-energy proof above.

The same script separately tests nonlinear reciprocal material quadrature, strong current/contact convergence, and Gaussian internal-cutoff control. Those tests have the distinct scopes stated in [Matter continuum](MATTER_CONTINUUM.md).

This establishes a controlled spatial continuum for the reciprocal linearized covariant sector. A nonlinear geometric-cutoff theorem, full nonlinear Einstein-constraint limit, and a fixed-parameter quantum-gravity continuum remain separate obligations.

