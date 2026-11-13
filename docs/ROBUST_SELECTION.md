# How close to Einstein form when the equations are almost satisfied?

The exact selection theorem identifies one coefficient family from vanishing calibration equations. A useful next question is quantitative: if the equations have a small residual, how far can the coefficients move?

The answer is explicit. Five residuals at two points determine bounds for all four coefficient functions. Across a connected area interval, those bounds control the distance from one common affine family. This is **stability of coefficient inference in the fixed calibration**, rather than a theorem about the time evolution of perturbations.

The original [`ThmA.lean`](../source/v2.4/lean/ThmA.lean) already contains `robust_V` and `robust_F2`, sharp partial estimates for denominator-cleared metric residuals. The extension here gives the complete inversion in the original Euler-component normalization, adds sharp $U$ and $W$ bounds, and integrates the result into a quantitative near-affine theorem.

## 1. Fix the equations and their normalization

Let $I\subset(0,\infty)$ be a connected interval. Take $F\in C^2(I)$ and the coefficient functions $U,W,V$ of the [selected two-derivative action](../source/v2.4/notes/VARIATIONAL_DERIVATION.md). Write $F'=dF/d\rho$ and $F''=d^2F/d\rho^2$.

On the flat calibration

$$
h=-dt^2+dr^2,
\qquad
\rho=tr,
\qquad
M=\begin{pmatrix}t/r&0\\0&r/t\end{pmatrix},
\qquad t,r>0,
$$

the unrestricted metric variation gives

$$
\begin{aligned}
E_{tt}
&=-F''t^2+\frac U2(t^2+r^2)
-\frac W{4\rho^2}(t^2+r^2)+\frac V2,\\
E_{rr}
&=-F''r^2+\frac U2(t^2+r^2)
-\frac W{4\rho^2}(t^2+r^2)-\frac V2,\\
E_{tr}
&=-\rho F''-F'+\rho U+\frac W{2\rho}.
\end{aligned}
$$

Every coefficient on the right is evaluated at the same $\rho=tr$. These are the unscaled Euler components. An error tolerance for equations multiplied by $4\rho^2$, or for a different coordinate normalization, is a different tolerance and must be converted before using the bounds below.

## 2. Five residuals and an exact inversion

For any fixed $\rho\in I$, choose the swapped calibration points

$$
A_\rho=\left(2\sqrt\rho,\frac{\sqrt\rho}{2}\right),
\qquad
B_\rho=\left(\frac{\sqrt\rho}{2},2\sqrt\rho\right).
$$

Both have area $\rho$. Define

$$
\begin{aligned}
e_1&=E_{tt}(A_\rho),& e_2&=E_{rr}(A_\rho),\\
e_3&=E_{tt}(B_\rho),& e_4&=E_{rr}(B_\rho),\\
e_5&=E_{tr}(A_\rho)=E_{tr}(B_\rho).
\end{aligned}
$$

With $f_1=F'(\rho)$ and $f_2=F''(\rho)$, substitution gives

$$
\begin{aligned}
e_1&=-4\rho f_2+\frac{17\rho U}{8}-\frac{17W}{16\rho}+\frac V2,\\
e_2&=-\frac{\rho f_2}{4}+\frac{17\rho U}{8}-\frac{17W}{16\rho}-\frac V2,\\
e_3&=-\frac{\rho f_2}{4}+\frac{17\rho U}{8}-\frac{17W}{16\rho}+\frac V2,\\
e_4&=-4\rho f_2+\frac{17\rho U}{8}-\frac{17W}{16\rho}-\frac V2,\\
e_5&=-\rho f_2-f_1+\rho U+\frac W{2\rho}.
\end{aligned}
$$

They satisfy $e_1+e_2=e_3+e_4$. Elementary linear combinations produce four exact recovery identities:

$$
\boxed{V=\frac{e_1-e_2+e_3-e_4}{2},}
$$

$$
\boxed{\rho F''=\frac2{15}(-e_1+e_2+e_3-e_4),}
$$

$$
\boxed{\frac W\rho-F'
=e_5-\frac2{17}(e_1+e_2+e_3+e_4),}
$$

$$
\boxed{2\rho U-F'
=e_5+\frac{-38e_1+98e_2+98e_3-38e_4}{255}.}
$$

No fit or limiting approximation enters these identities. They hold at each positive area value.

## 3. Sharp pointwise bounds

Suppose the five residuals obey $|e_j|\le\epsilon$ for a common $\epsilon\ge0$. Apply the triangle inequality to each exact recovery formula:

$$
\boxed{
|V|\le2\epsilon,
\qquad
|F''|\le\frac{8\epsilon}{15\rho}.}
$$

$$
\boxed{
|W-\rho F'|\le\frac{25}{17}\rho\epsilon,
\qquad
\left|U-\frac{F'}{2\rho}\right|
\le\frac{31\epsilon}{30\rho}.}
$$

For example, the sum of the absolute coefficients in the last recovery formula is

$$
1+\frac{38+98+98+38}{255}
=1+\frac{16}{15}=\frac{31}{15}.
$$

Division by $2\rho>0$ gives the stated $U$ bound.

Each pointwise constant is attained in the algebraic inference problem. For $\epsilon>0$, the following normalized residual patterns are feasible:

| Quantity attaining its bound | $(e_1,e_2,e_3,e_4)/\epsilon$ | $e_5/\epsilon$ |
| --- | --- | ---: |
| $V$ | $(1,-1,1,-1)$ | $0$ |
| $\rho F''$ | $(-1,1,1,-1)$ | $0$ |
| $W/\rho-F'$ | $(1,1,1,1)$ | $-1$ |
| $2\rho U-F'$ | $(-1,1,1,-1)$ | $1$ |

To see that these are actual coefficient witnesses, rather than arbitrary residual assignments, take any compatible $e_1,\ldots,e_4$ and set

$$
D=\frac2{17}(e_1+e_2+e_3+e_4),
\qquad f_1=0,
$$

$$
f_2=\frac2{15\rho}(-e_1+e_2+e_3-e_4),
\qquad
V=\frac{e_1-e_2+e_3-e_4}{2},
$$

$$
W=\rho(e_5-D),
\qquad
U=\frac{e_5+D+2\rho f_2}{2\rho}.
$$

Substitution recovers all five residuals. Each table row obeys the required compatibility condition. The checker verifies every substituted residual and the attained bound exactly.

Sharpness here concerns pointwise coefficient jets with these residual constraints. Extra global conditions, positivity requirements, or a restricted family of coefficient functions could change the optimum.

## 4. One affine family across an interval

Assume the same residual envelope holds at every $\rho\in I$. Fix a reference area $\rho_0\in I$ and define

$$
a=F'(\rho_0),
\qquad
b=F(\rho_0)-a\rho_0,
$$

$$
L(\rho,\rho_0)=\left|\log\frac\rho{\rho_0}\right|,
\qquad
H(\rho,\rho_0)=\rho\log\frac\rho{\rho_0}-\rho+\rho_0.
$$

The function $H$ is nonnegative: it and its first derivative vanish at $\rho_0$, while $\partial_\rho^2H=1/\rho>0$.

Integrating $|F''(s)|\le8\epsilon/(15s)$ along the segment between $\rho_0$ and $\rho$ gives

$$
\boxed{|F'(\rho)-a|
\le\frac{8\epsilon}{15}L(\rho,\rho_0).}
$$

Taylor's integral remainder yields

$$
F(\rho)-(a\rho+b)
=\int_{\rho_0}^{\rho}(\rho-s)F''(s)\,ds.
$$

For $\rho\ge\rho_0$, the error is bounded by $(8\epsilon/15)\int_{\rho_0}^{\rho}(\rho-s)/s\,ds$. For $\rho\le\rho_0$, it is bounded by $(8\epsilon/15)\int_{\rho}^{\rho_0}(s-\rho)/s\,ds$. Both integrals equal $H(\rho,\rho_0)$, so

$$
\boxed{|F(\rho)-(a\rho+b)|
\le\frac{8\epsilon}{15}H(\rho,\rho_0).}
$$

Combining this common slope with the pointwise $W$ and $U$ estimates gives

$$
\boxed{
|W(\rho)-a\rho|
\le\rho\epsilon
\left[\frac{25}{17}+\frac8{15}L(\rho,\rho_0)\right],}
$$

$$
\boxed{
\left|U(\rho)-\frac a{2\rho}\right|
\le\frac\epsilon\rho
\left[\frac{31}{30}+\frac4{15}L(\rho,\rho_0)\right].}
$$

Along with $|V|\le2\epsilon$, these estimates control the distance from one common selected coefficient family. At $\epsilon=0$, they recover

$$
F=a\rho+b,
\qquad
U=\frac a{2\rho},
\qquad
W=a\rho,
\qquad
V=0
$$

throughout the connected interval.

## 5. What this establishes

Small calibration residuals force the coefficients close to Einstein form, with a known dependence on area and reference scale. The result supplies an explicit error certificate for approximate symbolic calculations or measured residuals, provided the same calibrated equations and error envelope apply.

The theorem uses genuine derivatives, the fixed theory class, and residual control at every area value in the interval. A finite sample of area values alone does not establish the uniform premise. For nonzero $\epsilon$, the logarithm and inverse-area factors also prevent an automatic uniform conclusion at a shrinking axis.

Positive radiative energy remains a separate condition. The equations above do not determine Newton's constant, eliminate the separate odd coupling, or prove dynamical stability. The exact all-field theorem supplies the parity-odd selection and the appropriate physical interpretation.

## Verification

The independent [checker](../scripts/verify_quantum_geometry.py) verifies all four inversion identities, the complete sharpness witnesses, and the derivative identities of the integrated remainder kernel. The integrations and triangle inequalities are proved explicitly above. The combined run with [quantum geometry](QUANTUM_GEOMETRY.md) has **58 exact symbolic checks and five wavefunction quadratures**, all passing. [Executed receipt](../evidence/quantum_geometry/quantum_geometry_receipt.json).

Run from the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_quantum_geometry.py --output-dir work/quantum_geometry
```

The symbolic receipt records the source hash and dependency versions. It is an execution record, distinct from the analytic proof and from any Lean certificates shipped elsewhere in the bundle.
