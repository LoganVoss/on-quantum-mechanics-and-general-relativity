# Complete local theorem for the independent integrability route

## 1. The exact theorem

Let \(U\) be a connected open subset of a two-dimensional Lorentzian conformal coordinate patch \((T,R)\). Set

\[
\partial_+=\partial_T+\partial_R,\qquad \partial_-=\partial_T-\partial_R.
\]

Let \(W\in C^2(U)\) be strictly positive, and let \(M:U\to\mathrm{Sym}^+_1(2,\mathbb R)\) be a twice-differentiable symmetric positive determinant-one matrix. Define

\[
J_\pm=M^{-1}\partial_\pm M,
\]

\[
\mathcal C=\partial_+J_- -\partial_-J_+ +[J_+,J_-],\qquad
\mathcal E=\frac{\partial_+(WJ_-)+\partial_-(WJ_+)}W.
\tag{1}
\]

The first expression is identically zero for a current obtained from \(M\); the second is the weighted shape equation.

**Theorem 1.** The following are locally equivalent:

1. \(\partial_+\partial_-W=0\).
2. There exists a nontrivial one-parameter family of scalar fields \(s_w\), with \(s_w\ne0,\pm1\), such that the connections

\[
L_+(w)=\frac{J_+}{1-s_w},\qquad L_-(w)=\frac{J_-}{1+s_w}
\tag{2}
\]

give a universal local zero-curvature representation of the weighted current equations on generic current jets. The spectral fields depend on \(W\) and the constant parameter \(w\), not on a specially chosen solution current. More precisely, the full curvature obeys

\[
\boxed{
\mathcal F(w):=\partial_+L_--\partial_-L_++[L_+,L_-]
=\frac{\mathcal C-s_w\mathcal E}{1-s_w^2}.}
\tag{3}
\]

For actual matrix currents, \(\mathcal C=0\); therefore flatness of any one member with \(s_w\ne0,\pm1\) is equivalent to \(\mathcal E=0\). If the currents are initially treated as independent matrix fields, flatness at two distinct admissible spectral values implies both \(\mathcal C=0\) and \(\mathcal E=0\).

The word “universal” specifies a representation of the equation system, rather than flatness on one degenerate solution such as constant \(M\). The necessity proof below makes its generic-jet condition explicit.

## 2. Necessity of the scalar spectral equations

Write

\[
A=\partial_+J_-,\quad B=\partial_-J_+,\quad C=[J_+,J_-],\quad
p=\partial_+\log W,\quad q=\partial_-\log W.
\]

On a solution of (1),

\[
A=-\tfrac12(C+pJ_-+qJ_+),\qquad
B=\tfrac12(C-pJ_--qJ_+).
\tag{4}
\]

First allow any finite scalar-current ansatz \(L_+=aJ_+\), \(L_-=bJ_-\). Its on-shell curvature is

\[
\mathcal F=left(ab-\frac{a+b}{2}\right)C
+\left(\partial_+b+\frac{a-b}{2}p\right)J_-
+\left(-\partial_-a+\frac{a-b}{2}q\right)J_+.
\tag{5}
\]

For independent generic current directions, the coefficient of each direction vanishes. In particular,

\[
2ab=a+b.
\tag{6}
\]

Apart from the zero connection \(a=b=0\), define \(s=(a-b)/(a+b)\). Equation (6) gives

\[
a=\frac1{1-s},\qquad b=\frac1{1+s}.
\tag{7}
\]

The remaining coefficients in (5) vanish precisely when

\[
\boxed{
\partial_+s=g(s)p,\qquad \partial_-s=h(s)q,\qquad
g(s)=\frac{s(1+s)}{1-s},\quad h(s)=\frac{s(1-s)}{1+s}.}
\tag{8}
\]

This derives the rational form and its scalar compatibility equations within the finite scalar-current ansatz.

### Generic-jet independence is an explicit algebraic condition

A constant target congruence sets \(M=I\) at a point. Its admissible first jets are then symmetric traceless matrices. Choose

\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
K=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]

\[
J_+=uH+vX,\qquad J_-=xH+yX,\qquad
[J_+,J_-]=2(uy-vx)K.
\tag{9}
\]

The determinant of these three columns in the basis \((H,X,K)\) is \(2(uy-vx)^2\). Hence independence holds on the open set \(uy-vx\ne0\).

These are admissible on-shell jets, not merely arbitrary matrix assignments. The required mixed second derivative of \(M\) at \(M=I\) is

\[
M_{+-}=\tfrac12\{J_+,J_-\}-\tfrac12(pJ_-+qJ_+).
\tag{10}
\]

It is symmetric; its trace equals \(\operatorname{Tr}(J_+J_-)\), exactly the mixed derivative of \(\det M=1\). Moreover \(M_{+-}-J_+J_-=A\) and \(M_{+-}-J_-J_+=B\), giving (4). Thus requiring a scalar-current representation for the equation system really does require the three separate coefficients in (5) to vanish.

## 3. The exact Frobenius obstruction

Differentiate (8), retaining both the spectral dependence and the derivatives of \(W\):

\[
\begin{aligned}
\partial_-\partial_+s-\partial_+\partial_-s
&=(g'h-h'g)pq+(g-h)\partial_+\partial_-\log W. 
\end{aligned}
\tag{11}
\]

Direct rational algebra gives

\[
g-h=\frac{4s^2}{1-s^2},\qquad
g'h-h'g=\frac{4s^2}{1-s^2}.
\tag{12}
\]

Because

\[
\partial_+\partial_-\log W+pq=\frac{W_{+-}}W,
\]

the obstruction is exactly

\[
\boxed{\partial_-\partial_+s-\partial_+\partial_-s
=\frac{4s^2}{1-s^2}\frac{W_{+-}}W.}
\tag{13}
\]

For a \(C^2\) solution \(s\) the left side is zero. On the admissible domain \(W>0\), \(s\ne0,\pm1\), its prefactor is nonzero. Hence \(W_{+-}=0\). This proves necessity, with the sign and all denominator conditions explicit.

## 4. Constructive sufficiency and the spectral curve

Assume \(W_{+-}=0\). On a simply connected sufficiently small patch, define a real harmonic conjugate \(\widetilde W\) by

\[
\boxed{\partial_+\widetilde W=\partial_+W,\qquad
\partial_-\widetilde W=-\partial_-W.}
\tag{14}
\]

Equivalently, \(\widetilde W_T=W_R\) and \(\widetilde W_R=W_T\). The one-form \(W_RdT+W_TdR\) is closed exactly when \(W_{TT}-W_{RR}=0\), so this definition is locally consistent. For example, \(W=f(T+R)+g(T-R)\) has \(\widetilde W=f(T+R)-g(T-R)\).

For a constant spectral parameter \(w\), impose

\[
\boxed{w=\widetilde W+\frac W2(s+s^{-1}).}
\tag{15}
\]

The two local roots are

\[
s_w=\frac{w-\widetilde W\ \pm\sqrt{(w-\widetilde W)^2-W^2}}W.
\tag{16}
\]

Choose a branch away from \(w=\widetilde W\pm W\). Locally one may choose real \(w\) with \(|w-\widetilde W|>W\); this gives real nonzero roots different from \(\pm1\). Their product is one.

Put \(c(s)=(s+s^{-1})/2\). Differentiating (15) and using (14), together with

\[
1+c+c'g=0,\qquad -1+c+c'h=0,
\tag{17}
\]

gives precisely (8). The implicit-function derivative is

\[
\frac{\partial s_w}{\partial w}=\frac{2s_w^2}{W(s_w^2-1)}\ne0,
\tag{18}
\]

so this is a genuine spectral family. The formulas construct it explicitly.

Finally, perform the curvature calculation without assuming the current equations. From (1),

\[
A=\tfrac12(\mathcal E+\mathcal C-C-pJ_--qJ_+),\qquad
B=\tfrac12(\mathcal E-\mathcal C+C-pJ_--qJ_+).
\]

Substituting these expressions and (8) into the curvature of (2) gives exactly (3). Thus the constructed family is flat if and only if the weighted shape equation holds for actual matrix currents. This proves sufficiency and the complete Lax equivalence, rather than only scalar compatibility.

## 5. The affine-coupling theorem

Let \(I\subset(0,\infty)\) be an interval, \(w_0\in C^2(I)\), and let \(\rho:U\to I\) be a harmonic area field: \(\rho_{+-}=0\). Suppose \(W=w_0(\rho)\). The chain rule gives

\[
W_{+-}=w_0''(\rho)\rho_+\rho_-.
\tag{19}
\]

Assume that for every \(r\in I\) there is at least one point \(x\in U\) with

\[
\rho(x)=r,\qquad \rho_+(x)\rho_-(x)\ne0.
\tag{20}
\]

This “one non-null point per area value” condition is sufficient; an everywhere non-null harmonic area field covering \(I\) is a stronger convenient condition. Theorem 1 and (19)-(20) give \(w_0''(r)=0\) for every \(r\in I\). The mean-value theorem on each compact subinterval of the connected interval gives

\[
\boxed{w_0(\rho)=c_0+c_1\rho.}
\tag{21}
\]

Conversely, every affine \(w_0\) composed with a harmonic \(\rho\) is harmonic, so every positive such coupling has the Lax family above. Necessity and sufficiency are both proved.

If \(I=(0,\infty)\), the additional shrinking-axis condition \(\lim_{\rho\downarrow0}w_0(\rho)=0\) gives \(c_0=0\). Positive nontrivial coupling gives \(c_1>0\). Therefore

\[
\boxed{W(\rho)=c_1\rho,\qquad c_1>0.}
\tag{22}
\]

For a power \(w_0=c\rho^n\), \(c>0\), \(n\in\mathbb R\),

\[
w_0''=cn(n-1)\rho^{n-2}.
\]

Thus integrability alone gives exactly \(n=0\) or \(n=1\). The axis condition selects \(n=1\).

### Exact treatment of degenerate branches

At \(s=0\), (2) is simply \(L_\pm=J_\pm\); flatness is the Maurer-Cartan identity for every \(W\). The zero connection corresponds to the separate trivial scalar branch \(a=b=0\). Both are excluded by the nontrivial-family hypothesis. The points \(s=\pm1\) are poles of the rational connection.

If \(\rho=f(T+R)\), then \(\rho_-\equiv0\) and every composition \(w_0(\rho)\) is harmonic; it consequently has a local Lax family wherever positive. The conclusion “\(w_0\) affine” specifically uses (20). If \(M\) is constant, every current vanishes, so connection flatness on that one configuration does not test the equation system. Condition (9) specifies the needed generic current sector.

## 6. What integrability gives before harmonic area is separately supplied

For the action derived in `VARIATIONAL_DERIVATION.md`, the trace of the exact metric equation is

\[
\Box F(\rho)=V(\rho).
\tag{23}
\]

On a branch where \(F'\ne0\), put \(X=(\nabla\rho)^2\). The chain rule gives

\[
\Box W=\frac{W'}{F'}V+left(W''-\frac{W'F''}{F'}\right)X.
\tag{24}
\]

Harmonicity in Theorem 1 is equivalent to \(\Box W=0\), since the two-dimensional conformal factor multiplies the wave operator by a nowhere-zero scalar. If, for each fixed area value, the allowed local solution jets include two distinct values of \(X\), the affine expression (24) vanishes at both values only when its two coefficients vanish. On a branch with \(F'W'\ne0\), this gives

\[
V=0,\qquad \left(\frac{W'}{F'}\right)'=0,\qquad
\boxed{W=\alpha F+\beta,\quad\alpha\ne0.}
\tag{25}
\]

This is the exact simultaneous conclusion of the metric trace and generic Lax compatibility. The extra step to physical-area linearity is supplied by harmonic \(\rho\) and condition (20), or independently by the proved single-chart selection theorem.

## 7. An exact remaining-frame family

For \(a>0\), let \(B\) be any smooth function of \(\rho\) with compact support in \((0,\infty)\). For a real constant \(\eta\), define

\[
F=a\rho,\qquad W=a\rho,\qquad V=0,\qquad
U_\eta=\frac a{2\rho}+2a\eta B'(\rho).
\tag{26}
\]

The metric trace gives \(\Box\rho=0\), and the shape equation and Lax construction depend on the same \(W=a\rho\). These actions are related by the exact invertible change of variables

\[
h_0=e^{2\eta B(\rho)}h_\eta.
\tag{27}
\]

Indeed, in two dimensions,

\[
\sqrt{-h_0}FR[h_0]=\sqrt{-h_\eta}\,[FR[h_\eta]-2F\Box_\eta(\eta B)],
\]

and integrating the last term by parts adds exactly \(2F'\eta B'(\nabla\rho)^2\). The shape and area kinetic densities are conformally invariant; \(V=0\). Thus (26)-(27) are an exact family of Lax-equivalent reduced actions.

Their literal four-dimensional block metrics differ. Starting with the flat cylindrical seed, take \(\rho=R\) and

\[
g_\eta=e^{\gamma(R)}(-dT^2+dR^2)+dz^2+R^2d\phi^2,\qquad
\gamma=-2\eta B(R).
\tag{28}
\]

Direct curvature contraction gives

\[
\boxed{R[g_\eta]=-e^{-\gamma}\gamma''.}
\tag{29}
\]

An explicit smooth compactly supported choice is

\[
B(R)=\begin{cases}
\exp[-1/((R-1)(2-R))],&1<R<2,\\
0,&\text{otherwise}.
\end{cases}
\]

At \(R=3/2\), \(B=e^{-4}\), \(B''=-32e^{-4}\), and therefore

\[
R[g_\eta]\big|_{R=3/2}=-64\eta e^{-4}\exp(2\eta e^{-4}).
\tag{30}
\]

This is nonzero for \(\eta\ne0\), while the axis and asymptotic fields agree with the seed. Equation (30) precisely identifies the conformal-frame information that the Lax property leaves free. The independently proved single-chart variational theorem fixes this family by the literal quotient-block calibration.

## 8. Verification delivered

`verify_integrability_complete.py` computes the rational coefficient identities, full off-shell connection-curvature identity, exact Frobenius obstruction, spectral-curve derivatives, generic-current independence determinant, compatible determinant-one second jets, coupled-dilaton identity, power branches, and explicit nonzero frame curvature. It also checks 256 deterministic generic noncommuting current jets with exact rational arithmetic. The output is `integrability_complete_certificate.json`; its exact counts and status are recorded by the executed program.

The theorem is a local classical integrability result for the explicitly quantified scalar-current ansatz. Its positive area-weighted branch follows from three proved implications: scalar compatibility selects harmonic \(W\); harmonic area with (20) selects affine \(W(\rho)\); the shrinking axis and positive kinetic normalization select \(W=c_1\rho\).

### Source alignment

The input conjecture and rational ansatz are the attached `INTEGRABILITY_THEOREM(1).md` and Sections 4-5 of `Voss_Foundations_Integrability_v2_2(1).pdf`. This proof adds the full off-shell curvature equivalence (3), an explicit noncommuting generic-jet necessity argument (9)-(10), the signed harmonic conjugate and constructive spectral family (14)-(18), the minimal non-null fiber condition (20), and exact independent executable certificates.
