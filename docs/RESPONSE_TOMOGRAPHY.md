# Reading the gravitational action from its response

Two theories can share a vacuum and still respond differently to the same source. In the constant curvature-squared class, two calibrated curvature-response channels recover both independent deformation coefficients exactly. The calculation also supplies error intervals, a way to infer an unknown gravitational normalization, and a test of the assumed response class.

This is a mathematical source-and-response construction. The bundle contains no measurements of these channels. The related [sourced-calibration theorem](QUADRATIC_SELECTION.md) gives an exact nonlinear selection result using dust and charged reference geometries.

## Contract and linear field equation

Use the same physical metric, curvature convention, minimal matter prescription, and normalized action as in the selection note:

```math
S=\frac1{2\kappa}\int\sqrt{-g}
\left[R+\alpha R^2+\beta R_{ab}R^{ab}+\gamma E_4\right]d^4x
+S_{\mathrm m}.
```

The coefficients are constants, $\kappa>0$, the background is Minkowski spacetime, and the perturbative source satisfies $\partial^aT_{ab}=0$. No Killing-symmetry restriction is imposed. A Green-function or boundary prescription selects the particular sourced response; arbitrary added homogeneous waves are excluded from the transfer measurement.

Linearizing the exact equations gives

```math
\boxed{
(1+\beta\Box)G^L_{ab}
+(2\alpha+\beta)(\eta_{ab}\Box-\partial_a\partial_b)R^L
=\kappa T_{ab}.}
```

Its trace is

```math
-R^L+(6\alpha+2\beta)\Box R^L=\kappa T.
```

Here $L$ denotes linearization, not a length. The independent verifier obtains the quadratic contribution by differentiating the curvature-squared action in all ten symmetric metric-amplitude variables. It checks all ten resulting symbol components, the Bianchi identities, and the vanishing curvature of pure gauge perturbations. The field equation and its extra spin sectors belong to established quadratic gravity. [Pravda et al., equations (1)–(5)](https://arxiv.org/html/1606.02646v3), [Salvio, *Quadratic Gravity*](https://arxiv.org/abs/1804.09944v2).

## Two channels determine two coefficients

For a Fourier mode $e^{ik\cdot x}$, take a nonzero spacelike covector and set $z=k^ak_a>0$, so $\Box\mapsto-z$. Decompose the conserved source into its transverse traceless and transverse scalar sectors. One convenient transverse projector is

```math
\theta_{ab}=\eta_{ab}-\frac{k_a k_b}{z}.
```

The tensor channel uses a nonzero transverse traceless source amplitude. The scalar channel uses a nonzero trace, for example a source proportional to $\theta_{ab}$. These are calibrated operator probes; physically realizing their source profiles is an additional task.

Normalize the two curvature responses to their Einstein values:

```math
\begin{aligned}
r_2(z)&=\frac{G^L_{\mathrm{TT}}}{\kappa T_{\mathrm{TT}}}
=\frac1{1-\beta z},\\
r_0(z)&=\frac{R^L}{-\kappa T}
=\frac1{1+(6\alpha+2\beta)z}.
\end{aligned}
```

The quotient in the tensor channel refers to amplitudes in the same chosen nonzero polarization. Both curvature observables are gauge invariant at linear order about flat space. Choose a scale where the transfer functions are finite and nonzero.

Define the inverse-response deviations

```math
y_2=\frac{r_2^{-1}-1}{z},
\qquad y_0=\frac{r_0^{-1}-1}{z}.
```

Their coefficient map and inverse are

```math
\begin{pmatrix}y_2\\y_0\end{pmatrix}
=
\begin{pmatrix}0&-1\\6&2\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\end{pmatrix},
\qquad \det=6,
```

```math
\boxed{\beta=-y_2,\qquad\alpha=\frac{y_0+2y_2}{6}.}
```

Therefore $r_0=r_2=1$ at one known nonzero spacelike scale selects $\alpha=\beta=0$ **within this fixed constant-coefficient class**. The Euler coefficient remains invisible to local bulk response. The conclusion is not available from Ricci-flat vacuum survival or from testing only perturbations with $\delta R_{ab}=0$.

## Exact uncertainty intervals

If estimated inverse-response deviations have independent error bounds $|\delta y_0|\le\epsilon_0$ and $|\delta y_2|\le\epsilon_2$, the coefficient errors obey

```math
\boxed{|\delta\alpha|\le\frac{\epsilon_0+2\epsilon_2}{6},
\qquad|\delta\beta|\le\epsilon_2.}
```

The bounds are individually sharp in this rectangular error model: the affine inverse maps its extremizing corners to feasible coefficient pairs.

For direct positive-response estimates $\widehat r_i$ with an absolute uncertainty $\epsilon_i<\widehat r_i$, monotonicity of the reciprocal gives the exact interval

```math
y_i\in\left[
\frac{(\widehat r_i+\epsilon_i)^{-1}-1}{z},
\frac{(\widehat r_i-\epsilon_i)^{-1}-1}{z}
\right].
```

Apply the affine coefficient inverse to these intervals. In particular, a bound $|r_i-1|\le\delta_i<1$ gives

```math
|y_i|\le\frac{\delta_i}{z(1-\delta_i)}.
```

These are parameter-identification bounds for specified source and response errors. They do not include unknown source calibration, nonlinear corrections, or omitted operators unless those effects are included in the error model.

## Inferring the leading normalization as well

If $\kappa$ is unknown, use the unnormalized responses

```math
P_2=\frac{G^L_{\mathrm{TT}}}{T_{\mathrm{TT}}},
\qquad P_0=-\frac{R^L}{T}.
```

Their inverses are affine functions of scale, with the **same intercept**:

```math
X_2(z)=P_2(z)^{-1}=\frac{1-\beta z}{\kappa},
\qquad
X_0(z)=P_0(z)^{-1}=\frac{1+(6\alpha+2\beta)z}{\kappa}.
```

Measure the tensor channel at two distinct positive scales $z_1,z_2$ and the scalar channel at $z_1$. Set

```math
\begin{aligned}
q&=\frac{z_2X_2(z_1)-z_1X_2(z_2)}{z_2-z_1},\\
s_2&=\frac{X_2(z_2)-X_2(z_1)}{z_2-z_1},\\
s_0&=\frac{X_0(z_1)-q}{z_1}.
\end{aligned}
```

Then

```math
\boxed{\kappa=\frac1q,\qquad
\beta=-\frac{s_2}{q},\qquad
\alpha=\frac{s_0+2s_2}{6q}.}
```

The design matrix for $(q,s_2,s_0)$ is

```math
\begin{pmatrix}1&z_1&0\\1&z_2&0\\1&0&z_1\end{pmatrix},
\qquad \det=z_1(z_2-z_1)\ne0.
```

A positive inferred $q$ is required by $\kappa>0$. A fourth observation, $X_0(z_2)$, provides an exact consistency test:

```math
\boxed{
z_2X_0(z_1)-z_1X_0(z_2)
-z_2X_2(z_1)+z_1X_2(z_2)=0.}
```

This fourth relation tests the shared-intercept model instead of merely fitting all the available data. Its satisfaction at finitely many points does not prove that the assumed operator class holds at every scale.

## Application: separating two exterior gravitational potentials

In the parameter range $\beta<0$ and $c=6\alpha+2\beta>0$, define

```math
m_2^2=-\frac1\beta,\qquad m_0^2=\frac1c.
```

The masses are real in this range. This does not remove the massive spin-two mode's negative-residue issue in the ordinary local quadratic theory.

For a calibrated static point mass, choose the decaying, asymptotically flat linearized solution in isotropic/Newtonian gauge,

```math
ds^2=-(1+2\Phi)dt^2+(1-2\Psi)d\mathbf{x}^2.
```

The established quadratic-gravity potentials are

```math
\begin{aligned}
\Phi(r)&=-\frac{GM}{r}\left[
1+\frac13e^{-m_0r}-\frac43e^{-m_2r}\right],\\
\Psi(r)&=-\frac{GM}{r}\left[
1-\frac13e^{-m_0r}-\frac23e^{-m_2r}\right].
\end{aligned}
```

These Yukawa corrections and their mode interpretation are prior physics, originating in the higher-derivative gravity literature. The current checker independently solves the linearized source equations in Fourier space and checks all ten components against the stated potentials. [Salvio, sections 2.3 and 5](https://arxiv.org/html/1804.09944v2).

The useful inverse is especially simple. At a known radius, set $U=-r\Phi/(GM)$ and $V=-r\Psi/(GM)$. Then

```math
\boxed{e^{-m_0r}=U-2V+1,\qquad
e^{-m_2r}=\frac{2-U-V}{2}.}
```

If both reconstructed quantities lie strictly between zero and one, their logarithms give the two masses; these determine $\beta$ and $\alpha$. Vanishing reconstructed exponentials represent absent-mode limits rather than finite masses.

This is an application within the linearized point-source model. Extracting both potentials from observations requires a defined source size, radial coordinate, boundary prescription, and independent clock/lensing or other suitable probe data. A single force measurement is not automatically a measurement of both local potentials.

## Two controls against overinterpreting the inverse

### A higher-derivative term can hide at one scale

Replace the scalar inverse response by

```math
1+(c-dz_*)z+dz^2,\qquad c=6\alpha+2\beta.
```

At the chosen scale $z=z_*$, this agrees with $1+cz$ for every $d$. Away from that scale its difference is

```math
dz(z-z_*).
```

The checker verifies this exact negative control. One-scale tomography identifies the two coefficients in its declared quadratic class; it does not exclude arbitrary higher operators.

### “No additional poles” is an additional structural requirement

Within the exact finite polynomial class, $\beta\ne0$ produces an additional tensor response pole and $c\ne0$ an additional scalar response pole. Requiring both to be absent forces $\beta=c=0$, hence $\alpha=0$ modulo Euler. For the real-mass tensor branch,

```math
\frac1{z(1+z/m_2^2)}=\frac1z-\frac1{z+m_2^2}.
```

The opposite residues expose the extra spin-two mode. This is an established feature of quadratic gravity, not a new consequence of the quantum–shape dictionary. If the polynomial action is only a low-energy effective expansion, a pole outside its validity range cannot establish that its coefficient must vanish. Higher and nonlocal theories need a separate analysis. [Salvio](https://arxiv.org/abs/1804.09944v2), [Donoghue, *General relativity as an effective field theory*](https://arxiv.org/abs/gr-qc/9405057).

## Why the physical metric and matter coupling must remain fixed

At first order in a perturbative local redefinition $\delta g_{ab}=uR_{ab}+vRg_{ab}$,

```math
\delta S_{\mathrm{EH}}
=\frac1{2\kappa}\int\sqrt{-g}
\left[-uR_{ab}R^{ab}+(u/2+v)R^2\right]d^4x,
```

while the matter action changes by

```math
\delta S_{\mathrm m}
=\frac12\int\sqrt{-g}
\left[uT^{ab}R_{ab}+vTR\right]d^4x.
```

Changing the gravitational operator basis can therefore change the displayed source interactions as well. The inverse above identifies coefficients with a fixed physical metric and matter prescription. It is not a basis-independent assertion that every occurrence of a curvature-squared term can be measured separately. Equivalent descriptions must carry their sources and probes through the same redefinition.

## Evidence and credit

The [response checker](../scripts/extension_checks/verify_curvature_response.py) passes **88 exact symbolic identities** and five finite rational inverse examples. Its [receipt](../evidence/extensions/curvature/curvature_response_receipt.json) records the executable hash, conventions, calculations, and limits. The checks cover the full linear symbol, gauge and Bianchi identities, response inversion, sharp inverse-error corners, potential reconstruction, unknown-$\kappa$ identification, and the higher-derivative negative control.

The supplied November 13 novelty review proposed two flat curvature-Hessian probes with contractions $(0,1/2)$ and $(36,12)$ and determinant $-18$. Those reviewer calculations are independently reproduced and credited in the checker. The additions here are the complete sourced-response map, its uncertainty treatment, the shared-normalization inverse, and the explicit applications and failure controls. Their ingredients have substantial prior literature; the package does not certify worldwide novelty or an observed deviation from Einstein gravity.
