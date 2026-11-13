# Selecting against the full constant curvature-squared class

Flat and Ricci-flat geometries leave an important ambiguity: many curvature-squared theories admit the same vacuum solutions. Two concrete **sourced** calibrations remove that ambiguity in a declared four-dimensional action class. A dust cosmology tests the scalar-curvature combination; a charged electrovacuum tests the remaining Ricci-curvature combination.

The resulting theorem allows unrestricted four-dimensional metric variations. Its source calibrations are additional physical premises, stated below. They are not deductions from the original flat-vacuum selection theorem, and the calculation supplies no new observational data.

## The action class and physical frame

Use signature $(-,+,+,+)$ and the curvature convention

```math
R_{ab}=\partial_c\Gamma^c_{ab}-\partial_b\Gamma^c_{ac}
+\Gamma^c_{cd}\Gamma^d_{ab}-\Gamma^c_{bd}\Gamma^d_{ac}.
```

Fix a positive gravitational normalization $\kappa$ and a physical metric $g$ to which the specified matter couples minimally. Consider

```math
S=\frac1{2\kappa}\int \sqrt{-g}
\left[R+\alpha R^2+\beta R_{ab}R^{ab}+\gamma E_4\right]d^4x
+S_{\mathrm m}[g,\mathrm{matter}],
```

```math
E_4=R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2.
```

The coefficients $\alpha,\beta,\gamma$ are constants. The Einstein term and the vanishing cosmological constant are already fixed. The two deformation coefficients $\alpha,\beta$ have dimensions of length squared in this normalization; they are distinct from the original theorem's overall coefficient $a$.

This covers the parity-even constant-coefficient quadratic-curvature bulk class in four dimensions, modulo the Euler density and boundary terms. For example, an unnormalized addition $A R^2+B R_{ab}R^{ab}$ corresponds to $\alpha=2\kappa A$, $\beta=2\kappa B$. A constant $\Box R$ term is also a boundary contribution. Compactly supported variations, or a declared compatible boundary completion, are understood.

No Killing ansatz is imposed on the action or its variations. The informative reference solutions themselves have symmetries; that does not restrict the metric variations used to obtain the field equations.

## Exact equations

Define the curvature Euler tensors

```math
\begin{aligned}
H^{(1)}_{ab}
&=2RR_{ab}-\frac12g_{ab}R^2
+2(g_{ab}\Box-\nabla_a\nabla_b)R,\\
H^{(2)}_{ab}
&=\Box R_{ab}+\frac12g_{ab}\Box R-\nabla_a\nabla_bR\\
&\quad+2R_{acbd}R^{cd}-\frac12g_{ab}R_{cd}R^{cd}.
\end{aligned}
```

The field equation and its trace are

```math
G_{ab}+\alpha H^{(1)}_{ab}+\beta H^{(2)}_{ab}=\kappa T_{ab},
```

```math
\boxed{-R+(6\alpha+2\beta)\Box R=\kappa T.}
```

In the conventional Bach-tensor normalization, $H^{(2)}=2B+H^{(1)}/3$. These equations agree with the established Weyl-squared/$R^2$ formulation after changing basis. They also explain why Ricci-flat vacuum references leave both coefficients undetermined. [Pravda et al., *Exact solutions to quadratic gravity*, equations (1)–(5)](https://arxiv.org/html/1606.02646v3).

## The sourced-calibration theorem

**Theorem.** In the stated action class, with the same fixed metric interpretation, gravitational normalization, dust stress, and minimal Maxwell coupling, the two configurations below satisfy the full field equations if and only if

```math
\boxed{\alpha=\beta=0.}
```

The constant Euler coefficient $\gamma$ remains free in the local bulk equations.

### Calibration 1: a pressureless cosmology

On a regular patch $t>0$, take

```math
ds^2=-dt^2+t^{4/3}(dx^2+dy^2+dz^2),
\qquad \kappa\rho_{\mathrm d}=\frac4{3t^2},
\qquad p_{\mathrm d}=0.
```

The dust four-velocity is $u^a=(1,0,0,0)$, and $T_{ab}=\rho_{\mathrm d}u_a u_b$. Direct curvature calculation gives

```math
R=\frac4{3t^2},
\qquad \Box R=-\frac8{3t^4},
\qquad
G_{ab}=\mathrm{diag}\left(\frac4{3t^2},0,0,0\right).
```

The dust equations are consistent: the comoving flow is geodesic and $\dot\rho_{\mathrm d}+3H\rho_{\mathrm d}=0$ with $H=2/(3t)$. The specified stress gives $-R=\kappa T$. Substituting it into the exact quadratic trace equation leaves

```math
(6\alpha+2\beta)\Box R=0.
```

Since $\Box R$ is nonzero throughout the patch,

```math
3\alpha+\beta=0.
```

This is one independent coefficient condition. Homogeneous and isotropic geometries are insensitive to the Weyl-squared sector, so this calibration alone cannot determine both coefficients. That property also appears in the established quadratic-gravity dust literature. [Buoninfante et al., *Dust collapse and horizon formation in Quadratic Gravity*](https://arxiv.org/abs/2410.05941v2).

### Calibration 2: a charged electrovacuum

Choose a reference length as the unit and use the Reissner–Nordström parameters $M=1$, $Q=1/2$:

```math
f(r)=1-\frac2r+\frac1{4r^2},
```

```math
ds^2=-f\,dt^2+f^{-1}dr^2
+r^2\left(d\theta^2+\sin^2\theta\,d\phi^2\right).
```

For the Maxwell action

```math
S_{\mathrm{EM}}=-\frac14\int\sqrt{-g}\,F_{ab}F^{ab}\,d^4x,
```

the calibrated electric field is $F_{tr}=\sqrt{2/\kappa}\,Q/r^2$. The executed exact check uses $\kappa=2$, for which $F_{tr}=1/(2r^2)$. This is a fixed source normalization, not a fit of the source to the deformation coefficients. A different fixed $\kappa$ changes the electric-field normalization while retaining the same geometric $Q$.

All Maxwell equations and all sixteen Einstein–Maxwell component equations hold for this configuration. Its scalar curvature is zero, so $H^{(1)}=0$. The remaining tensor is

```math
H^{(2)a}{}_{b}
=\frac{4r^2-8r+1}{4r^8}\,\mathrm{diag}(-3,-1,2,2).
```

At $r=3$, the lapse is $13/36>0$ and

```math
H^{(2)t}{}_{t}=-\frac{13}{8748}\ne0.
```

The point lies in a regular exterior patch. The specified Maxwell stress already equals $G/\kappa$, so the added field equation is $\beta H^{(2)}=0$. Its nonzero component forces $\beta=0$. The dust relation then gives $\alpha=0$.

Conversely, $\alpha=\beta=0$ returns the two original Einstein-matter configurations, and the constant Euler term supplies no local bulk equation. This proves both directions. Neither the singular center nor a coordinate-degenerate horizon is used.

## An exact inverse, with sharp error bounds

The same two configurations provide quantitative inference when their required equations have nonzero residuals. Let

```math
\mathcal R_{ab}
=G_{ab}+\alpha H^{(1)}_{ab}+\beta H^{(2)}_{ab}-\kappa T_{ab}.
```

In the displayed dimensionless calibration units, define $y_{\mathrm D}$ as its trace on the dust configuration at $t=1$, and $y_{\mathrm R}$ as its mixed $t$–$t$ component on the charged configuration at $r=3$. Then

```math
\begin{pmatrix}y_{\mathrm D}\\y_{\mathrm R}\end{pmatrix}
=
\begin{pmatrix}
-16&-16/3\\
0&-13/8748
\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\end{pmatrix},
\qquad \det=\frac{52}{2187}\ne0.
```

Thus

```math
\boxed{
\beta=-\frac{8748}{13}y_{\mathrm R},
\qquad
\alpha=-\frac{y_{\mathrm D}}{16}+\frac{2916}{13}y_{\mathrm R}.}
```

If $|y_{\mathrm D}|\le\epsilon_{\mathrm D}$ and $|y_{\mathrm R}|\le\epsilon_{\mathrm R}$, the bounds are

```math
\boxed{
|\beta|\le\frac{8748}{13}\epsilon_{\mathrm R},
\qquad
|\alpha|\le\frac{\epsilon_{\mathrm D}}{16}
+\frac{2916}{13}\epsilon_{\mathrm R}.}
```

Each bound is individually sharp in this two-residual norm. The affine map is invertible, so the extremizing corners of the residual rectangle correspond to actual constant coefficient pairs. The checker reconstructs those pairs and verifies both residuals exactly. Extra sign or physical constraints can restrict the feasible corners; sharpness is asserted for the declared real coefficient class.

To restore a reference length $L_0$, use $\bar\alpha=\alpha/L_0^2$, $\bar\beta=\beta/L_0^2$, and $\bar y=L_0^2y$ in the displayed numerical matrix. The bounds depend on that calibration and residual normalization. Their large charged-background coefficient reflects the sensitivity of this particular sampling point; it is not a universal precision claim.

## Verification and relation to the existing research

The [sourced-calibration checker](../scripts/extension_checks/verify_sourced_calibrations.py) passes **73 exact symbolic checks**. These include the dust curvature and Einstein components, the charged curvature and Maxwell equations, the complete Einstein–Maxwell component comparison, the nonzero deformation tensor, its covariant conservation, and the residual inverse and sharpness corners. The [receipt](../evidence/extensions/curvature/sourced_calibration_receipt.json) records the script hash and environment.

The decisive charged component was also obtained independently by varying the radial curvature-squared action with two independent metric functions **before** imposing the reference relation between them. That route agrees with the direct covariant-tensor calculation. See the [independent radial-action checker](../scripts/extension_checks/verify_rn_variation_independent.py) and its [receipt](../evidence/extensions/independent_rn/independent_rn_receipt.json).

The supplied November 13 novelty review identified the broader strategy of using curvature response to expose coefficients invisible to Ricci-flat vacuum stationarity, and gave two linear Hessian probes. The present result adds exact sourced reference solutions, a full constant-coefficient selector, and a sharp finite residual inverse. This is part of the AI-assisted verification lineage, not external human peer review or a certification of historical priority.

The theorem strengthens theoretical specificity within a larger action class. It requires new sourced-calibration premises and fixed matter couplings. It does not show that the original quantum–shape dictionary alone demands those responses. Variable curvature coefficients, extra fields, higher operators, nonlocal terms, and quantum effective corrections require their own analysis. [Response tomography](RESPONSE_TOMOGRAPHY.md) gives distinguishing observables and explains these boundaries in operational terms.
