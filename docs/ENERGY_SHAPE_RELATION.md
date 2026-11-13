# A compact equation for energy, shape, and quantum overlap

The model's most useful compact relation is

```math
\boxed{\Delta E=\hbar\omega\left(\mathcal F^{-2}-1\right).}
```

It says that a calibrated quantum probe's excitation energy is fixed by its overlap with the ground state selected by the geometry. Here $\mathcal F$ is **squared fidelity**, not an amplitude, and $\hbar\omega$ is the calibrated oscillator energy gap.

This is an exact relation inside the model, with concrete uses. It is not a proposed replacement for $E=mc^2$, and it does not identify the gap with a universal gravitational constant.

## 1. What the symbols mean

Let $M$ be the positive symmetric determinant-one shape matrix, and let an independently prepared centered saturated Gaussian state have covariance $N/2$. The common calibrated frame representation and centered quadratic propagation select

```math
\widehat H_M^{\mathrm{ex}}
=\frac{\hbar\omega}{2}\widehat R^T M^{-1}\widehat R
-\frac{\hbar\omega}{2}I.
```

Its zero-energy ground ray is $\psi_M$. The probe is $\psi_N$, and

```math
\mathcal F=\left|\langle\psi_M\mid\psi_N\rangle\right|^2,
\qquad
\Delta E=\langle\psi_N|\widehat H_M^{\mathrm{ex}}|\psi_N\rangle.
```

The coupling selection, its extra assumptions, and the reciprocal dynamics are proved in [Dynamical coupling](DYNAMICAL_COUPLING.md). In particular, the frequency is calibrated and the quadratic class matters. An arbitrary nonquadratic interaction does not obey this relation.

## 2. Derivation

Taking the expectation of the quadratic Hamiltonian gives

```math
\Delta E=\frac{\hbar\omega}{4}
\left[\mathrm{Tr}(M^{-1}N)-2\right].
```

For the curvature-minus-one target metric $G$, the intrinsic shape distance obeys

```math
\cosh d_G(M,N)=\frac12\mathrm{Tr}(M^{-1}N).
```

The exact Gaussian overlap formula is $\mathcal F=\mathrm{sech}(d_G/2)$. Consequently,

```math
\boxed{
\Delta E
=\frac{\hbar\omega}{2}(\cosh d_G-1)
=\hbar\omega\sinh^2\left(\frac{d_G}{2}\right)
=\hbar\omega(\mathcal F^{-2}-1).}
```

Equivalently, the mean excitation number is $\bar n=\mathcal F^{-2}-1$. The identity uses the full finite separation; it is not a small-distance approximation. Near matching, $\Delta E=(\hbar\omega/4)d_G^2+O(d_G^4)$.

Gaussian covariance, fidelity, and squeezed-state excitation energy are established structures. This result makes their exact relation to the model's selected interaction explicit. [Banchi, Braunstein and Pirandola](https://arxiv.org/abs/1507.01941v1), [Hackl and Bianchi](https://arxiv.org/abs/2010.15518v4).

## 3. It also fixes the magnitude of the shape source

Define the reciprocal source $\mathcal S=-\nabla_M\Delta E$ in the target metric. Differentiating the distance formula gives

```math
\boxed{\|\mathcal S\|_G^2
=\Delta E(\Delta E+\hbar\omega).}
```

The identity extends continuously to the matching point, where both energy and source vanish. It is a relation between an internal excitation energy and a source per dimensionless shape coordinate; a conversion to a force on a physical detector requires the additional spacetime observation map.

If $E_{\mathrm{int}}=\Delta E+\hbar\omega/2$ includes the oscillator zero-point offset, the same statement is

```math
E_{\mathrm{int}}^2-\|\mathcal S\|_G^2
=\left(\frac{\hbar\omega}{2}\right)^2.
```

This is a hyperbolic energy–shape identity. Its resemblance to a relativistic mass-shell equation does not make the target coordinates spacetime momentum or derive a new mass–energy law.

For any centered finite-covariance state, set $N=2\Sigma$, without assuming saturation. Direct differentiation gives the more general relation

```math
\|\mathcal S\|_G^2
=\Delta E(\Delta E+\hbar\omega)
-\frac{(\hbar\omega)^2}{4}(\det N-1).
```

The uncertainty relation gives $\det N\ge1$, hence

```math
\|\mathcal S\|_G^2\le\Delta E(\Delta E+\hbar\omega).
```

Equality is the covariance-saturation condition. Under the original canonical reconstruction hypotheses, it identifies the centered pure Gaussian family. An isotropic thermal covariance gives positive excitation energy and zero directional source. Thus equal energy need not imply equal source.

## 4. Three practical calculations

### Infer mismatch energy from a measured overlap

Suppose the probe is known to be in the centered saturated Gaussian family, its frame and gap are independently calibrated, and its measured squared overlap with $\psi_M$ is $\mathcal F=4/5$. Then

```math
\frac{\Delta E}{\hbar\omega}
=\left(\frac54\right)^2-1=\frac9{16},
\qquad d_G=2\log2,
\qquad\frac{\|\mathcal S\|_G}{\hbar\omega}=\frac{15}{16}.
```

These are exact model predictions for that preparation. State-family errors, displacement, mixedness, and calibration uncertainty must be treated separately; the overlap formula is not valid for arbitrary states sharing a normalized covariance shape.

### Translate an energy budget into a geometry bound

If $\Delta E\le E_{\max}$ within the same state family, then

```math
d_G\le2 \mathrm{arsinh}
\sqrt{\frac{E_{\max}}{\hbar\omega}},
\qquad
\mathcal F\ge\frac1{\sqrt{1+E_{\max}/(\hbar\omega)}}.
```

This converts a preparation-energy constraint into an allowed target-distance interval and minimum overlap. It can be used to choose a permitted mismatch before a numerical evolution or controlled probe experiment.

### Separate energy from response direction

At the isotropic geometry $M=I$, prepare

```math
N_+=\begin{pmatrix}4&0\\0&1/4\end{pmatrix},\qquad
N_-=\begin{pmatrix}1/4&0\\0&4\end{pmatrix}.
```

Both have $\Delta E=9\hbar\omega/16$ and $\mathcal F=4/5$. They are related by a canonical quarter-turn and have the same entire oscillator energy distribution. Nevertheless, their shape sources point in opposite directions. In the target coordinates $M=M(x,y)$,

```math
\mathcal S_x\big|_{M=I}=\frac{\hbar\omega}{2}N_{12},
\qquad
\mathcal S_y\big|_{M=I}
=-\frac{\hbar\omega}{4}(N_{11}-N_{22}).
```

The two preparations therefore have $\mathcal S_x=0$ and $\mathcal S_y=\mp15\hbar\omega/16$. A classical shape cell initially at rest has the corresponding opposite accelerations after division by its calibrated inertia.

The [fully quantum construction](DYNAMICAL_COUPLING.md#4-equal-full-energy-distributions-opposite-shape-responses) strengthens the comparison: with a common radial shape packet, the two joint preparations have identical full joint-energy spectral measures and opposite initial responses of a bounded directional observable. Its significance is that quantum orientation information affects the selected source. It is not a claim that energy conservation fails or that all alternative gravitational models are excluded.

## 5. What this equation does and does not summarize

The relation combines three parts of the research: a calibrated quantum-state dictionary, the hyperbolic shape metric, and the newly selected quadratic interaction. It turns a correspondence into a specified energy and source law.

It does not summarize every theorem in the bundle. The action-selection argument, curvature-squared discriminators, one-Killing extension, and quantum constraint problem have their own equations and assumptions. It also does not fix $\omega$, the gravitational normalization, or the shape inertia from first principles.

The [dynamical checker](../scripts/extension_checks/verify_dynamical_extension.py) verifies the exact energy and source identities, general covariance slack, symmetry relations, and declared controls. [Executed evidence](../evidence/extensions/dynamics/dynamical_extension_receipt.json). The earlier [quantum-geometry proof](QUANTUM_GEOMETRY.md) establishes the finite-fidelity relation and its domain counterexample. All numbers above are mathematical consequences or synthetic checks, not measured new gravitational effects.
