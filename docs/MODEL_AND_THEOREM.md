# The model and the selection theorem

The theorem selects an action within a specified class. It is an equivalence about first variations, not an assumption that the action is a minimum.

## Contract

Take an oriented two-dimensional Lorentzian base with signature $(-,+)$, an area field $\rho>0$, and a smooth symmetric positive matrix $M$ with determinant one. Set $J_a=M^{-1}\partial_aM$, $T_{ab}=\operatorname{Tr}(J_aJ_b)$, $\tau=h^{ab}T_{ab}$, and $X=h^{ab}\rho_a\rho_b$. All fields vary independently, with compact support, before the reference chart is inserted.

Assume locality, base diffeomorphism invariance, constant target $SL(2,\mathbb R)$ congruence invariance, no additional fields, and polynomial dependence on derivatives of **total order at most two**. Modulo divergences, the action is

$$
S=\int_B\sqrt{-h}\left[F(\rho)R[h]+U(\rho)X-\frac{W(\rho)}4\tau+V(\rho)\right]d^2x+S_{\mathrm{odd}},
$$

$$
S_{\mathrm{odd}}=2\int_B k(\rho)e^P(P_tQ_r-P_rQ_t)\,dt\,dr,
\qquad
M=\begin{pmatrix}e^P&e^PQ\\e^PQ&e^{-P}+e^PQ^2\end{pmatrix}.
$$

Here $F\in C^2(0,\infty)$ and $U,W,V,k\in C^1(0,\infty)$. The invariant target metric and area form are

$$
G=dP^2+e^{2P}dQ^2,\qquad \Omega=e^P dP\wedge dQ.
$$

The classification follows from the target isotropy representation: there is no invariant covector, one symmetric invariant bilinear form up to scale, and one alternating form up to scale. Target scalar invariants are constant; coefficient functions may therefore depend on $\rho$. A term $C(\rho)\Box\rho$ integrates into $U$. The [original proof](../source/v2.4/notes/PHYSICAL_PREMISES_PROOF.md) gives the details.

## Exact equivalence

The following configuration, over the full positive quadrant, is stationary for every allowed compactly supported variation if and only if the coefficients below hold on the same connected positive domain:

$$
h=-dt^2+dr^2,\quad \rho=tr,\quad P=\log(t/r),\quad Q=0;
$$

$$
F=a\rho+b,\quad U=\frac a{2\rho},\quad W=a\rho,\quad V=0,\quad k=k_0.
$$

Strictly positive nondegenerate radiative energy adds $a>0$. It does not determine its magnitude. The associated four-metric is flat:

$$
g=-dt^2+dr^2+t^2dz^2+r^2d\phi^2,
$$

as follows from $X^0=t\cosh z$, $X^3=t\sinh z$, $X^1=r\cos\phi$, $X^2=r\sin\phi$.

## The proof in a few steps

Independent inverse-metric variation gives

$$
E_{ab}=(h_{ab}\Box-\nabla_a\nabla_b)F
+U\left(\rho_a\rho_b-\frac12h_{ab}X\right)
-\frac W4\left(T_{ab}-\frac12h_{ab}\tau\right)-\frac12h_{ab}V.
$$

The even part of the area equation is

$$
E_\rho=F'R-U'X-2U\Box\rho-\frac14W'\tau+V',
$$

and the even shape equations are

$$
E_P=\nabla_a(W\nabla^aP)-We^{2P}(\nabla Q)^2,
\qquad E_Q=\nabla_a(We^{2P}\nabla^aQ).
$$

On the chart, putting $s=t^2+r^2$, the metric residuals become

$$
E_{tt}=-F''t^2+\frac{Us}{2}-\frac{Ws}{4\rho^2}+\frac V2,
\qquad
E_{rr}=-F''r^2+\frac{Us}{2}-\frac{Ws}{4\rho^2}-\frac V2,
$$

$$
E_{tr}=-(\rho F''+F')+\rho U+\frac{W}{2\rho}.
$$

Subtracting the diagonal equations gives $V=F''(t^2-r^2)$. At fixed $\rho$, evaluating at $(\sqrt\rho,\sqrt\rho)$ gives $V=0$; evaluating at $(2\sqrt\rho,\sqrt\rho/2)$ then gives $F''=0$. The remaining two relations give $2\rho^2U=W$ and $W=\rho F'$. The mean-value theorem on each compact segment of the connected domain makes $F'=a$ and then $F=a\rho+b$.

The odd contribution to the $Q$ equation is $-4(t/r)k'(tr)$, so $k'=0$ throughout the domain. A constant $k$ multiplies $\Omega=d(e^PdQ)$ and is a boundary term. Substituting the selected functions makes the area and both shape equations vanish as well, proving the full converse. The [complete first variation](../source/v2.4/notes/VARIATIONAL_DERIVATION.md) retains its boundary current.

## Why the selected action is gravitational

For the literal block dictionary $g=h+\rho M$, a geometric identity valid **off shell**, before any field equation, is

$$
\sqrt{-g}R[g]=\sqrt{-h}\left[\rho R[h]+\frac{(\nabla\rho)^2}{2\rho}
-\frac\rho4\operatorname{Tr}(J_aJ^a)\right]
-2\partial_a\!\left(\sqrt{-h}\nabla^a\rho\right).
$$

Thus the selected bulk action is the two-Killing reduction of Einstein–Hilbert gravity up to normalization and boundary terms. The reduction itself has established precedent; the result here is the conditional selection route, its explicit assumptions, and its verification. A constant $b$ gives no local bulk equation; interpreting it globally as an Euler term requires the appropriate boundary and corner completion.

## A second route to the area weight

For $\partial_\pm=\partial_T\pm\partial_R$ and $J_\pm=M^{-1}\partial_\pm M$, define

$$
\mathsf{MC}=\partial_+J_--\partial_-J_++[J_+,J_-],\qquad
\mathcal E=\frac{\partial_+(WJ_-)+\partial_-(WJ_+)}W.
$$

For the regular scalar-current Lax family $L_+=J_+/(1-s)$, $L_-=J_-/(1+s)$, the spectral field must obey

$$
\partial_+s=\frac{s(1+s)}{1-s}\frac{\partial_+W}{W},\qquad
\partial_-s=\frac{s(1-s)}{1+s}\frac{\partial_-W}{W}.
$$

With these transport equations, the exact identities are

$$
\mathcal F=\frac{\mathsf{MC}-s\mathcal E}{1-s^2},\qquad
\partial_-\partial_+s-\partial_+\partial_-s
=\frac{4s^2}{1-s^2}\frac{W_{+-}}W.
$$

For positive $C^2$ weight, generic admissible current jets, a current-independent spectral construction, and $s\ne0,\pm1$, the local family exists exactly when $W_{+-}=0$. If $W=W(\rho)$, $\rho_{+-}=0$, and every area value has a non-null representative, this gives affine $W$. A shrinking-axis limit $W(0^+)=0$ and positivity then select $W=c\rho$, $c>0$. Null area gradients, constant currents, and the trivial spectral branch must be kept separate. The [complete Lax proof](../source/v2.4/notes/INTEGRABILITY_COMPLETE_PROOF.md) constructs the spectral family and states every condition.

## Necessary distinctions

The quantum-state/shape identification is kinematic. The canonical representation and uncertainty saturation do not derive spacetime dimension or Lorentzian signature. Full stationarity selects the bulk coefficients within the stipulated derivative class; it does not exclude all higher-derivative theories. Ricci-flat backgrounds also solve broad curvature-squared modifications. The supplied [deformation analysis](../source/v2.4/notes/DEFORMATION_FRAME_TWIST_ADDENDUM.md) gives a sharper discriminator for one specified reduced deformation.

The literal metric frame is also an input. Its operational identification requires a calibrated minimal massive or nonzero-orbit-momentum probe. Those mathematical probe constructions are not laboratory observations.
