# The quantum geometry of shape

A quantum state has a shape: the relative sizes and correlations of its position and momentum uncertainties. In this model, that shape is described by exactly the same matrix as the shape of a gravitational symmetry orbit. The correspondence goes beyond a shared diagram. It fixes a metric, a finite overlap probability, and a geometric phase, with all normalization factors intact.

The results here apply to **centered, uncertainty-saturating states of one canonical degree of freedom**, with the calibrated representation used in the [physical-premises derivation](../source/v2.4/notes/PHYSICAL_PREMISES_PROOF.md). They describe the geometry of this family of quantum states and its identification with the model's orbit-shape field. The spacetime interpretation still uses the stated geometric dictionary.

## 1. From a Gaussian ray to an orbit shape

Take dimensionless canonical operators $\widehat Q=x$ and $\widehat P=-i\partial_x$, with $[\widehat Q,\widehat P]=i$. The centered normalized state is

```math
\psi_{u,v}(x)=\left(\frac v\pi\right)^{1/4}
\exp\left[\frac{iu-v}{2}x^2\right],
\qquad u\in\mathbb R,\quad v>0.
```

Its covariance and normalized shape are

```math
\Sigma=\frac1{2v}
\begin{pmatrix}
1&u\\
u&u^2+v^2
\end{pmatrix},
\qquad
M=2\Sigma,
\qquad
\det\Sigma=\frac14,
\qquad
\det M=1.
```

Every positive symmetric determinant-one $2\times2$ matrix occurs exactly once: recover $v=1/M_{11}$ and $u=M_{12}/M_{11}$. The overall phase of $\psi$ is irrelevant to this correspondence.

The source also proves why Gaussianity follows from canonical uncertainty saturation. With centered covariance entries $q,c,p$, set

```math
z=\frac{c+i/2}{q},\qquad B=\widehat P-z\widehat Q.
```

For a positive trace-one density operator $\widehat\varrho$ with finite second moments,

```math
\mathrm{Tr}(\widehat\varrho B^*B)
=\frac{qp-c^2-1/4}{q}.
```

At saturation this vanishes. Positivity places every vector in the support of $\widehat\varrho$ in the kernel of $B$. That kernel is the one-dimensional square-integrable solution space of $-i\psi'-zx\psi=0$. The state is therefore a pure Gaussian ray.

The model uses a common calibrated $SL(2,\mathbb R)$ congruence action on covariance shapes and orbit shapes. Under that representation, equivariance and the isotropic calibration fix their identification. This representation is part of the physical input; the covariance matrix by itself does not determine a Lorentzian spacetime.

## 2. One tensor supplies both distance and phase

For coordinates $\theta=(u,v)$, define the quantum geometric tensor

```math
\mathcal Q_{ij}
=\langle\partial_i\psi\mid\partial_j\psi\rangle
-\langle\partial_i\psi\mid\psi\rangle
 \langle\psi\mid\partial_j\psi\rangle.
```

The logarithmic derivatives and Gaussian moments are

```math
\partial_u\log\psi=\frac{i x^2}{2},
\qquad
\partial_v\log\psi=\frac1{4v}-\frac{x^2}{2},
```

```math
\langle x^2\rangle=\frac1{2v},
\qquad
\langle x^4\rangle=\frac3{4v^2}.
```

Substitution gives the complete tensor:

```math
\boxed{
\mathcal Q=\frac1{8v^2}
\begin{pmatrix}
1&i\\
-i&1
\end{pmatrix}.}
```

Its real part is the Fubini–Study metric restricted to this Gaussian family. With the pure-state quantum Fisher information convention $g_{\mathrm{QFI}}=4\mathrm{Re}\mathcal Q$,

```math
ds^2_{\mathrm{FS}}=\frac{du^2+dv^2}{8v^2},
\qquad
ds^2_{\mathrm{QFI}}=\frac{du^2+dv^2}{2v^2}.
```

Direct matrix differentiation gives the gravitational model's normalized shape metric:

```math
\boxed{
G=\frac12\mathrm{Tr}\left[(M^{-1}dM)^2\right]
=\frac{du^2+dv^2}{v^2}
=8g_{\mathrm{FS}}=2g_{\mathrm{QFI}}.}
```

These factors matter. Rescaling the target metric changes the normalization of its coupling in the action.

For the phase convention

```math
\mathcal A=i\langle\psi\mid d\psi\rangle,
\qquad
\mathcal F_{\mathrm B}=d\mathcal A,
```

one obtains

```math
\mathcal A=-\frac{du}{4v},
\qquad
\boxed{\mathcal F_{\mathrm B}=-\frac{du\wedge dv}{4v^2}.}
```

The sign also follows from $\mathcal F_{ij}=-2\mathrm{Im}\mathcal Q_{ij}$ in this convention. Gaussian geometric phases have an established literature; these formulas make that geometry explicit in the coordinates and normalization of this model. [Garcia-Chung, *On the geometric phase for Gaussian states* (2020)](https://arxiv.org/abs/2004.14204v1).

## 3. The permitted odd term is a Berry-curvature boundary term

In the source's target coordinates $P=-\log v$ and $Q=u$,

```math
G=dP^2+e^{2P}dQ^2,
\qquad
\Omega=e^P dP\wedge dQ
=\frac{du\wedge dv}{v^2}.
```

Consequently,

```math
\boxed{\mathcal F_{\mathrm B}=-\frac14\Omega.}
```

Let $\varphi:B\to\mathbb H^2$ be the shape field on an oriented base patch. The coefficient-selection theorem makes the allowed parity-odd coupling $k$ constant. Its action is therefore

```math
\begin{aligned}
S_{\mathrm{odd}}
&=2k\int_B\varphi^*\Omega\\
&=-8k\int_B\varphi^*\mathcal F_{\mathrm B}\\
&=-8k\oint_{\partial B}\varphi^*\mathcal A.
\end{aligned}
```

The target metric and the permitted odd density are thus the real and imaginary geometric data of the same Gaussian state family. The odd term contributes through the boundary and has no bulk Euler derivative when $k$ is constant.

For a closed state path $C=\partial\Sigma$ with the induced orientation, the geometric phase is

```math
\gamma_{\mathrm B}
=\oint_C\mathcal A
=-\frac14\int_\Sigma\Omega
\pmod{2\pi}.
```

The global Gaussian formula above fixes a smooth gauge over the entire upper half-plane. That space is contractible and $\mathcal F_{\mathrm B}$ is exact, so this result introduces no quantization of area or of $k$. It provides a precise geometric-phase interpretation of the boundary term. Under $\psi\mapsto e^{i\alpha}\psi$, $\mathcal A\mapsto\mathcal A-d\alpha$ and the curvature is unchanged.

An orientation check is useful. For the counterclockwise rectangle $[u_0,u_1]\times[v_0,v_1]$, with $u_1>u_0$ and $v_1>v_0>0$,

```math
\oint\mathcal A
=-\frac{u_1-u_0}{4}
\left(\frac1{v_0}-\frac1{v_1}\right)
=-\frac14\mathrm{Area}_G(\Sigma).
```

Reversing orientation, or adopting the opposite convention for the Berry connection, reverses the corresponding sign.

## 4. Finite quantum overlap is an exact distance formula

The metric measures nearby changes. The same geometry also determines the overlap between states separated by a finite distance.

For $z=u+iv$ and $z'=u'+iv'$, Gaussian integration gives

```math
\langle\psi_z\mid\psi_{z'}\rangle
=\frac{\sqrt2 (vv')^{1/4}}
{\sqrt{v+v'-i(u'-u)}}.
```

The square root uses the branch with positive real part. Define **squared fidelity**, or transition probability, by

```math
\mathcal F=\left|\langle\psi_z\mid\psi_{z'}\rangle\right|^2.
```

Then

```math
\mathcal F
=\frac{2\sqrt{vv'}}
{\sqrt{(v+v')^2+(u-u')^2}}
=\frac1{\sqrt{\det\left((M+M')/2\right)}}.
```

This is a pure one-mode specialization of Gaussian-state fidelity, for which more general covariance formulas are already known. [Banchi, Braunstein and Pirandola, *Quantum fidelity for arbitrary Gaussian states*, Physical Review Letters **115**, 260501 (2015)](https://doi.org/10.1103/PhysRevLett.115.260501); [primary preprint](https://arxiv.org/abs/1507.01941v1).

The intrinsic geodesic distance $d_G$ of the curvature-minus-one metric $G$ obeys

```math
\cosh d_G
=1+\frac{(u-u')^2+(v-v')^2}{2vv'}
=\frac12\mathrm{Tr}(M^{-1}M').
```

Combining the two expressions gives

```math
\boxed{
\mathcal F=\mathrm{sech}\left(\frac{d_G}{2}\right),
\qquad
d_G=2\mathrm{arcosh}\left(\frac1{\mathcal F}\right).}
```

This translates finite shape separation into a quantum transition probability. Its small-distance expansion,

```math
\mathcal F=1-\frac{d_G^2}{8}+O(d_G^4),
```

recovers $g_{\mathrm{FS}}=G/8$.

The distance $d_G$ is intrinsic to the Gaussian shape manifold. It differs from the ambient projective Hilbert-space distance $\arccos\sqrt{\mathcal F}$. Calling both simply “quantum distance” would conceal this distinction.

## 5. A decisive check of the domain

Consider the oscillator vacuum and first excited state:

```math
\psi_0(x)=\pi^{-1/4}e^{-x^2/2},
\qquad
\psi_1(x)=\sqrt2 x\psi_0(x).
```

They are normalized and orthogonal, and their covariances are

```math
\Sigma_0=\frac12 I,
\qquad
\Sigma_1=\frac32 I.
```

If one normalizes an arbitrary covariance by $M=\Sigma/\sqrt{\det\Sigma}$, both states have $M=I$. Their overlap is nevertheless zero. The first excited state lies outside the uncertainty-saturating family: $\det\Sigma_1=9/4$.

This exact counterexample identifies the boundary of the result. Normalized covariance shape determines the ray and fidelity in the stated saturated centered family; it cannot encode arbitrary quantum states. Displacements, mixedness, and non-Gaussian information require additional data.

## Verification and provenance

These corollaries were derived before the public research notes were written. The [independent checker](../scripts/verify_quantum_geometry.py) imports no supplied verification implementation. It verifies the quantum tensor, metric and Berry identities, finite-fidelity identities, and the oscillator negative control. The same script checks the [quantitative selection extension](ROBUST_SELECTION.md).

The combined run passes **58 exact symbolic checks and five independent adaptive quadratures of the wavefunctions**. The largest observed absolute discrepancy between quadrature and the finite-distance fidelity formula is $2.22\times10^{-16}$. Quadratures use absolute and relative tolerances $10^{-12}$ and a comparison threshold $2\times10^{-11}$. [Executed receipt](../evidence/quantum_geometry/quantum_geometry_receipt.json).

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_quantum_geometry.py --output-dir work/quantum_geometry
```

The Gaussian integrals and geometric arguments above are analytic proofs. Symbolic identities and finite numerical quadratures provide distinct verification evidence. This quantum-geometric section is not a Lean formalization or a report of a laboratory measurement. Its contribution to this bundle is the explicit, consistently normalized connection to the selected gravitational model.
