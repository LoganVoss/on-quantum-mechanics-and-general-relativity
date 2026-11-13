# Selection with one spacetime symmetry

The calibration argument extends to a theory with **one designated spacelike Killing field**. Its quotient has two spatial coordinates and one time coordinate. General configurations may depend on all three quotient coordinates; no second Killing symmetry is imposed.

The result is a conditional selection theorem in this larger field space. The underlying one-Killing Einstein–hyperbolic-wave-map reduction is established mathematics. The contribution developed here is an explicit flat helical calibration that selects its relative action coefficient, together with a direct recovery of the original nonlinear cylindrical sector. The [Geroch reduction literature](https://arxiv.org/html/1403.6511v2) and [Moncrief's account](https://maths.anu.edu.au/files/CMAProcVol19-Moncrief.pdf) supply the relevant precedent.

## The enlarged geometric dictionary

Let $h$ be a three-dimensional Lorentzian metric of signature $(-,+,+)$, let $\lambda>0$, and let $A$ be a one-form. The four-dimensional metric is

```math
g_4=\lambda^{-1}h_{ab}(x) dx^a dx^b
+\lambda(x)\bigl(dy+A_a(x)dx^a\bigr)^2.
```

The fields are independent of $y$. The designated Killing field is $K=\partial_y$, with norm $g_4(K,K)=\lambda$. The connection $A$ restores base–orbit mixing. Its curvature is $F=dA$.

Here $h$ is the **Einstein-frame quotient metric**: it is $\lambda$ times the literal metric on the planes orthogonal to $K$. Its normalization and the normalization of $y$ are explicit parts of the dictionary. This differs from the literal two-dimensional quotient convention of the original theorem.

On a regular oriented patch, take the volume form with positive component $\epsilon_{Trx}=\sqrt{-h}$. The Lorentzian Hodge star obeys $*^2=-1$ on one-forms and two-forms. In the vacuum theory, define the twist potential $\chi$ by

```math
d\chi=\lambda^2 *_hF,
\qquad
F=-\lambda^{-2}*_h d\chi.
```

The scalar twist description is local. Reconstruction of $A$ requires the displayed two-form to be closed; global periods and bundle topology require additional information. The sourced case needs a modified relation, derived in [Current and reconstruction](CURRENT_AND_RECONSTRUCTION.md).

The target metric is

```math
G=\frac{d\lambda^2+d\chi^2}{\lambda^2}.
```

This is the same normalized hyperbolic geometry as before, now built from a Killing norm and twist rather than the shape of a two-dimensional symmetry orbit.

## The action class

Assume:

- Locality and base diffeomorphism invariance.
- An arbitrary three-dimensional Lorentzian metric and only the two target fields $(\lambda,\chi)$.
- Invariance under constant $SL(2,\mathbb R)$ transformations of the upper half-plane.
- Polynomial dependence on derivatives of total order at most two.
- Smooth fields and compactly supported independent variations on regular local patches.

Target transitivity makes every invariant scalar coefficient a constant. At a target point, the isotropy representation has no invariant one-form and has one invariant symmetric bilinear form up to scale. Modulo divergences, the action therefore has the form

```math
S[f,w,V]
=\int \sqrt{-h}\left[
fR[h]-\frac{w}{2\lambda^2}
\bigl((\nabla\lambda)^2+(\nabla\chi)^2\bigr)+V
\right]d^3x,
```

where $f,w,V$ are constants. A target-dependent coefficient of $R[h]$ is excluded by transitivity. There is no independent mixed term built from an invariant target covector. Terms linear in target second derivatives reduce by integration by parts to the kinetic term.

No parity assumption is needed at this order. A base orientation tensor has three indices, while a parity-odd target pullback scalar would require three derivatives and a target three-form. Gravitational Chern–Simons terms also exceed the stipulated derivative order.

The assumptions define the comparison class. In particular, full target symmetry is an input. A four-dimensional cosmological term reduces to a nonconstant norm-dependent potential and is outside this invariant class. The theorem below does not solve the cosmological-constant problem or classify every possible one-Killing matter theory.

## A flat helical calibration

Start with Minkowski space in cylindrical coordinates and change coordinates by

```math
\phi=x+\Omega y,\qquad z=y,
\qquad \Omega\ne0.
```

The metric becomes

```math
g_4=-dT^2+dr^2+r^2(dx+\Omega dy)^2+dy^2.
```

The designated Killing field is the spacelike helix

```math
K=\partial_y=\partial_z+\Omega\partial_\phi.
```

On a patch with $r>0$, the reduced fields are

```math
\boxed{
\lambda=1+\Omega^2r^2,\qquad
\chi=2\Omega T,\qquad
h=-\lambda dT^2+\lambda dr^2+r^2dx^2,
\qquad
A=\frac{\Omega r^2}{\lambda}\,dx.}
```

Direct differentiation gives $d\chi=\lambda^2 *_h dA$. The four-metric is flat by its displayed coordinate transformation. The independent checker also verifies all 256 components of its Riemann tensor.

Define

```math
S_{ab}=\frac{\partial_a\lambda\partial_b\lambda
+\partial_a\chi\partial_b\chi}{\lambda^2},
\qquad X=h^{ab}S_{ab}.
```

The quotient curvature is nontrivial:

```math
\mathrm{Ric}_{TT}=\frac{2\Omega^2}{\lambda^2},
\qquad
\mathrm{Ric}_{rr}=\frac{2\Omega^4r^2}{\lambda^2},
\qquad
\mathrm{Ric}_{xx}=0,
\qquad
\mathrm{Ric}_{ab}=\frac12S_{ab}.
```

Both target wave-map expressions vanish:

```math
\tau^\lambda
=\Box_h\lambda-\frac{(\nabla\lambda)^2-(\nabla\chi)^2}{\lambda}=0,
```

```math
\tau^\chi
=\Box_h\chi-\frac{2\nabla\lambda\cdot\nabla\chi}{\lambda}=0.
```

### Selection theorem

**Within the stated action class, the helical configuration is stationary under every independent compactly supported field variation if and only if**

```math
\boxed{w=f,\qquad V=0.}
```

Positive nondegenerate target kinetic energy further selects $f=w>0$. The overall normalization remains free.

**Proof.** Varying the unrestricted inverse metric gives

```math
E_{ab}
=f\left(\mathrm{Ric}_{ab}-\frac12h_{ab}R\right)
-\frac w2\left(S_{ab}-\frac12h_{ab}X\right)
-\frac V2h_{ab}.
```

On the calibration,

```math
E_{TT}=\frac{\Omega^2}{\lambda}(f-w)+\frac{V\lambda}{2},
\qquad
E_{rr}=\frac{\Omega^2}{\lambda}(f-w)-\frac{V\lambda}{2}.
```

The sum and difference isolate the coefficients:

```math
\boxed{
f-w=\frac{\lambda}{2\Omega^2}(E_{TT}+E_{rr}),
\qquad
V=\frac{E_{TT}-E_{rr}}{\lambda}.}
```

Since $\lambda>0$ and $\Omega\ne0$, vanishing of these two components forces $w=f$ and $V=0$. For those coefficients, $\mathrm{Ric}_{ab}=S_{ab}/2$ makes every metric equation vanish. The two target expressions already vanish, so every scalar variation vanishes as well. This proves the full converse. Strict positivity of the nondegenerate target kinetic term requires $w>0$ and hence $f>0$.

The calibration can be evaluated at any one regular point because this action class has only constant coefficients. This is different from inferring unrestricted functions from finitely sampled area values in the original theorem.

For $|E_{TT}|,|E_{rr}|\le\epsilon$, the same inverse gives

```math
|f-w|\le\frac{\lambda\epsilon}{\Omega^2},
\qquad |V|\le\frac{2\epsilon}{\lambda}.
```

The two constants are individually sharp in this two-response algebraic problem. At $\Omega=0$, the target is constant and the relative kinetic coefficient becomes invisible. That is a useful negative control.

The flat calibration has extra isometries. The theorem's **field space does not** impose those extra isometries: its fields remain arbitrary functions of three quotient coordinates. This extends action selection to the one-Killing class. It does not supply a new explicit generic nonlinear solution with exactly one isometry or a global existence theorem.

## Why the selected theory is the one-Killing Einstein reduction

For the general metric dictionary, a geometric identity valid before imposing field equations is

```math
\sqrt{-g_4}R[g_4]
=\sqrt{-h}\left[
R[h]-\frac{(\nabla\lambda)^2}{2\lambda^2}
-\frac{\lambda^2}{4}F_{ab}F^{ab}
\right]
+\partial_a\left(\sqrt{-h}\nabla^a\log\lambda\right).
```

To derive it, first set $q=\lambda^{-1}h$. Contraction of the one-fiber connection gives

```math
R[g_4]=R[q]-\frac\lambda4F_{ab}F_q^{ab}
-\lambda^{-1}\Box_q\lambda
+\frac{(\nabla\lambda)^2_q}{2\lambda^2}.
```

The three-dimensional conformal transformation then yields

```math
R[g_4]
=\lambda R[h]+\Box_h\lambda
-\frac{3}{2\lambda}(\nabla\lambda)^2_h
-\frac{\lambda^3}{4}F_{ab}F_h^{ab}.
```

Using $\sqrt{-g_4}=\lambda^{-1}\sqrt{-h}$ proves the density identity. A first-order Legendre dualization of $F$ gives the scalar action

```math
S=f\int\sqrt{-h}\left[
R[h]-\frac{(\nabla\lambda)^2+(\nabla\chi)^2}{2\lambda^2}
\right]d^3x.
```

Simple substitution of the vacuum duality relation into the Maxwell kinetic term would give the wrong scalar sign; the first-order dualization term is essential. The [current note](CURRENT_AND_RECONSTRUCTION.md) derives that step in a form that also handles the coupled probe.

The off-shell identity was independently checked at an arbitrary regular point using normal coordinates for $h$ and a local gauge with $A=0$. Independent second metric derivatives and arbitrary first and second derivatives of $\lambda$ and $A$ were retained. These are coordinate and gauge choices, not field-equation restrictions.

## The original nonlinear system is recovered exactly

Write the original cylindrical metric as

```math
g_4=e^{\gamma-\psi}(-dT^2+dR^2)
+e^\psi(dz+\mathcal A\,d\phi)^2
+R^2e^{-\psi}d\phi^2.
```

Reducing only $K=\partial_z$ gives

```math
\lambda=e^\psi,
\qquad
h=e^\gamma(-dT^2+dR^2)+R^2d\phi^2,
```

```math
\chi_T=\frac{e^{2\psi}}R\mathcal A_R,
\qquad
\chi_R=\frac{e^{2\psi}}R\mathcal A_T.
```

These are exactly the original dual-twist relations. The target metric becomes

```math
G=d\psi^2+e^{-2\psi}d\chi^2.
```

When the fields are further restricted to be $\phi$-independent, the full three-dimensional equations reproduce

```math
\psi_{TT}-\psi_{RR}-\frac{\psi_R}{R}
+e^{-2\psi}(\chi_T^2-\chi_R^2)=0,
```

```math
\chi_{TT}-\chi_{RR}-\frac{\chi_R}{R}
-2(\psi_T\chi_T-\psi_R\chi_R)=0,
```

```math
\gamma_R=\frac R2\left[
\psi_T^2+\psi_R^2+e^{-2\psi}(\chi_T^2+\chi_R^2)
\right],
\qquad
\gamma_T=R\left[\psi_T\psi_R+e^{-2\psi}\chi_T\chi_R\right].
```

All four relations were symbolically checked for arbitrary functions $\psi,\chi,\gamma$ of $T,R$. The original coupled evolution is therefore a further symmetry-restricted sector of the selected one-Killing action.

## The quantum interpretation changes in a precise way

Define

```math
M(\lambda,\chi)
=\frac1\lambda
\begin{pmatrix}1&\chi\\\chi&\chi^2+\lambda^2\end{pmatrix}.
```

Then $\det M=1$ and

```math
\frac12\mathrm{Tr}\left[(M^{-1}dM)^2\right]
=\frac{d\lambda^2+d\chi^2}{\lambda^2}.
```

The centered saturated Gaussian dictionary applies with $(u,v)=(\chi,\lambda)$. The matrix now encodes **norm and twist**. It is not the identical two-orbit shape matrix of the original formulation. Its identification with probe covariance still requires the calibrated common frame representation.

There is no independent area scalar $\rho$ in this field space. Within a zeroth-derivative algebraic target-equivariant probe class, target transitivity therefore excludes an arbitrary position-dependent gap. A constant gap scale remains. Derivative couplings, explicit base-dependent backgrounds, and additional fields would enlarge that class. The [dynamical coupling theorem](DYNAMICAL_COUPLING.md) and [energy–shape relation](ENERGY_SHAPE_RELATION.md) state the probe assumptions.

## Evidence and boundaries

The independent [one-Killing checker](../scripts/extension_checks/verify_one_killing.py) passed **309 exact checks**. The [generic reduction and current-duality checker](../scripts/extension_checks/verify_generic_reduction.py) passed **15 exact checks**. Their receipts are [here](../evidence/extensions/one_killing/one_killing_receipt.json) and [here](../evidence/extensions/one_killing/generic_reduction_receipt.json). The counts include tensor components and controls, not independent physical discoveries. No original project verifier is imported.

The action-selection theorem is a written proof supported by these exact calculations. The local reduction and its hyperbolic target have substantial prior literature. The helical inverse calibration and the explicit consistency chain are additions to this project; a bounded comparison does not establish worldwide priority.

The result concerns one Killing symmetry, the declared derivative class, and a fixed frame. Generic symmetry-free gravity, global evolution, a fully quantized continuum, and experimental applicability remain additional questions. Adding quantum probe sources also changes the reconstruction law; the [current correction](CURRENT_AND_RECONSTRUCTION.md) is required before interpreting the sourced theory as a connection-based geometry.
