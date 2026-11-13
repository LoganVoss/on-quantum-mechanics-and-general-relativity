# Exact variational derivation and complete single-chart converse

## 1. Statement with quantified hypotheses

Let \(I=(0,\infty)\), \(F\in C^2(I)\), and \(U,W,V\in C^1(I)\). On an oriented two-dimensional Lorentzian base \(B\), take a nondegenerate metric \(h\) of signature \((-+)\), a positive scalar \(\rho\), and a smooth symmetric positive matrix \(M\) with \(\det M=1\). All variations below have compact support in a coordinate patch, and the fields have the differentiability required for their displayed second derivatives. Define

\[
J_a=M^{-1}\partial_aM,\quad T_{ab}=\operatorname{Tr}(J_aJ_b),\quad
X=h^{ab}\partial_a\rho\partial_b\rho,\quad T=h^{ab}T_{ab},
\]

\[
S=\int_B\sqrt{-h}\left[F(\rho)R[h]+U(\rho)X-\frac{W(\rho)}4T+V(\rho)\right]d^2x.
\tag{1}
\]

Use the curvature convention
\(R_{ab}=\partial_c\Gamma^c_{ab}-\partial_b\Gamma^c_{ac}+\Gamma^c_{cd}\Gamma^d_{ab}-\Gamma^c_{bd}\Gamma^d_{ac}\).
The metric is varied independently of \(\rho,M\), before evaluation on any reference chart.

**Theorem.** The configuration

\[
h=-dt^2+dr^2,\quad \rho=tr,\quad
M=\begin{pmatrix}t/r&0\\0&r/t\end{pmatrix},\qquad t,r>0,
\tag{2}
\]

is stationary for every compactly supported variation if and only if there exist real constants \(a,b\) such that

\[
F(\rho)=a\rho+b,\qquad U(\rho)=\frac a{2\rho},\qquad
W(\rho)=a\rho,\qquad V(\rho)=0.
\tag{3}
\]

If a nondegenerate shape kinetic term with positive Hamiltonian is required, then \(a>0\). If the invariant parity-odd term described in Section 7 is also admitted, the additional necessary and sufficient condition is that its coefficient \(k\) be constant.

## 2. First variation, including its boundary current

Write \(v^{ab}=\delta h^{ab}\), \(v=h_{ab}v^{ab}\), \(f=\delta\rho\), and \(\eta=M^{-1}\delta M\). Then

\[
\delta\sqrt{-h}=-\frac12\sqrt{-h}\,v,
\qquad
\delta R=R_{ab}v^{ab}+\Box v-\nabla_a\nabla_bv^{ab}.
\tag{4}
\]

Consequently

\[
\delta(\sqrt{-h}FR)=\sqrt{-h}
\{[FG_{ab}+(h_{ab}\Box-\nabla_a\nabla_b)F]v^{ab}+F'Rf\}
+\partial_a(\sqrt{-h}\,\Theta_F^a),
\tag{5}
\]

where

\[
\Theta_F^a=F(\nabla^av-\nabla_bv^{ab})-v\nabla^aF+v^{ab}\nabla_bF.
\tag{6}
\]

This follows by two integrations by parts, retaining both derivative-of-\(F\) contributions. In two dimensions \(G_{ab}\equiv0\); this is the precise place where the base dimension enters the metric equation.

For the area kinetic term,

\[
\delta(\sqrt{-h}UX)=\sqrt{-h}\left[
U(\rho_a\rho_b-\tfrac12h_{ab}X)v^{ab}
-(U'X+2U\Box\rho)f\right]
+\partial_a(\sqrt{-h}\,2U\nabla^a\rho\,f).
\tag{7}
\]

The current identity \(\delta J_a=\partial_a\eta+[J_a,\eta]\) and symmetry of \(h^{ab}\) give

\[
\delta\!\left(-\frac{\sqrt{-h}W}4T\right)=\sqrt{-h}\left[
-\frac W4(T_{ab}-\tfrac12h_{ab}T)v^{ab}
-\frac{W'}4T f+\frac12\operatorname{Tr}\big(\nabla_a(WJ^a)\eta\big)\right]
-\partial_a\left(\frac{\sqrt{-h}W}2\operatorname{Tr}(J^a\eta)\right).
\tag{8}
\]

The commutator contribution vanishes because \(h^{ab}[J_a,J_b]=0\). For the potential,

\[
\delta(\sqrt{-h}V)=\sqrt{-h}\left(-\tfrac12h_{ab}Vv^{ab}+V'f\right).
\tag{9}
\]

Thus the full first variation is

\[
\delta S=\int\sqrt{-h}\left[E_{ab}v^{ab}+E_\rho f+\tfrac12\operatorname{Tr}(\mathcal K\eta)\right]d^2x
+\int\partial_a(\sqrt{-h}\,\Theta^a)d^2x,
\tag{10}
\]

\[
\boxed{E_{ab}=(h_{ab}\Box-\nabla_a\nabla_b)F
+U(\rho_a\rho_b-\tfrac12h_{ab}X)
-\frac W4(T_{ab}-\tfrac12h_{ab}T)-\tfrac12h_{ab}V,}
\tag{11}
\]

\[
\boxed{E_\rho=F'R-U'X-2U\Box\rho-\tfrac14W'T+V',\qquad
\mathcal K=\nabla_a(WJ^a),}
\tag{12}
\]

\[
\Theta^a=\Theta_F^a+2U\nabla^a\rho\,f-\tfrac W2\operatorname{Tr}(J^a\eta).
\tag{13}
\]

Compact support makes the boundary integral zero. The fundamental lemma applied to independent metric and scalar variations gives \(E_{ab}=0\), \(E_\rho=0\), and the shape equation. The shape equation can be stated as \(\mathcal K=0\): \(\mathcal K\) is traceless and \(M\)-self-adjoint, hence lies in the same tangent subspace as \(\eta\); its trace pairing with every allowed \(\eta\) is nondegenerate.

Equivalently, parameterize the target without constrained variations:

\[
M=\begin{pmatrix}e^P&e^PQ\\ e^PQ&e^{-P}+e^PQ^2\end{pmatrix},\qquad
\tfrac12 T_{ab}=P_aP_b+e^{2P}Q_aQ_b.
\tag{14}
\]

The two ordinary scalar Euler equations are

\[
E_P=\nabla_a(W\nabla^aP)-We^{2P}(\nabla Q)^2=0,\qquad
E_Q=\nabla_a(We^{2P}\nabla^aQ)=0.
\tag{15}
\]

No field equations were used in obtaining (10)-(15).

## 3. Evaluation on the exact chart

For (2), \(P=\log(t/r)\), \(Q=0\), and

\[
\rho_t=r,\quad\rho_r=t,\quad\rho_{tt}=\rho_{rr}=0,\quad\rho_{tr}=1,\quad
\Box\rho=0,\quad X=t^2-r^2.
\tag{16}
\]

The matrix currents and their contractions are

\[
J_t=\operatorname{diag}(1/t,-1/t),\quad
J_r=\operatorname{diag}(-1/r,1/r),
\]

\[
T_{tt}=2/t^2,\quad T_{rr}=2/r^2,\quad T_{tr}=-2/(tr),\quad
T=2(t^2-r^2)/\rho^2.
\tag{17}
\]

Crucially,

\[
\partial_t^2F(\rho)=F''r^2,\quad
\partial_r^2F(\rho)=F''t^2,\quad
\partial_t\partial_rF(\rho)=\rho F''+F',\quad
\Box F=F''(t^2-r^2).
\tag{18}
\]

Put \(s=t^2+r^2\). Substituting (16)-(18) into (11), term by term, gives

\[
\boxed{
E_{tt}=-F''t^2+\frac{Us}{2}-\frac{Ws}{4\rho^2}+\frac V2,\quad
E_{rr}=-F''r^2+\frac{Us}{2}-\frac{Ws}{4\rho^2}-\frac V2,
}
\tag{19}
\]

\[
\boxed{E_{tr}=-(\rho F''+F')+\rho U+\frac W{2\rho}.}
\tag{20}
\]

Every coupling and its derivative in these equations is evaluated at \(\rho=tr\). Multiplying the first two equations by \(4\rho^2\) and the third by \(2\rho\) yields exactly the polynomial hypotheses in the supplied `ThmA.lean`. Those factors are strictly positive on this chart, so denominator clearing is an equivalence.

## 4. Pointwise selection and integration

Subtracting the first two equations gives

\[
V(\rho)=F''(\rho)(t^2-r^2).
\tag{21}
\]

Fix any \(\rho>0\). Both \((t,r)=(\sqrt\rho,\sqrt\rho)\) and \((2\sqrt\rho,\sqrt\rho/2)\) belong to the same chart with that product. The first gives \(V(\rho)=0\). The second gives \(0=(15\rho/4)F''(\rho)\), hence \(F''(\rho)=0\). This is exact finite algebra; it is unnecessary to appeal to a range limit or an asymptotic argument.

Equation (19) now gives \(U=W/(2\rho^2)\), since \(s>0\). Equation (20) then gives \(W=\rho F'\). These identities hold at every \(\rho>0\).

For any \(0<x<y\), the mean-value theorem applied to \(F'\) on \([x,y]\) gives a \(\xi\in(x,y)\) such that

\[
F'(y)-F'(x)=F''(\xi)(y-x)=0.
\tag{22}
\]

Thus \(F'\) is the same constant \(a=F'(1)\) on the whole connected interval. Applying the mean-value theorem once more to \(F(\rho)-a\rho\) gives \(F(\rho)=a\rho+b\), where \(b=F(1)-a\). Substitution gives (3). A twice-differentiable \(F\) is sufficient for this integration step; the stated \(C^2\) regularity also supports the classical variational equations directly.

## 5. Full converse: all fields are stationary

The metric equations vanish upon inserting (3). On the chart the remaining equations reduce to

\[
E_\rho=(t^2-r^2)\left[-U'-\frac{W'}{2\rho^2}\right]+V',\qquad
E_P=\frac{t^2+r^2}{\rho}\left(\frac W\rho-W'\right),\qquad E_Q=0.
\tag{23}
\]

For (3), \(U'=-a/(2\rho^2)\), \(W'=a\), and \(V'=0\), so every expression is zero. The first-variation identity (10) then proves stationarity under all compactly supported metric, area, and shape variations.

The diffeomorphism identity provides a separate consistency check:

\[
2\nabla^aE_{ab}+E_\rho\partial_b\rho+E_P\partial_bP+E_Q\partial_bQ=0.
\tag{24}
\]

On the chart \(d\rho\wedge dP=-2\,dt\wedge dr\), so \(d\rho,dP\) are independent. In the even sector \(E_Q=0\) there, and the metric equations already imply both remaining scalar equations through (24).

## 6. Gauge fixing and positive normalization

The restriction \(h=-dt^2+dr^2\) is imposed only after varying the unrestricted metric. A variation restricted from the start to \(h=e^{2\sigma}\eta\) gives only the trace \(\Box F-V=0\). The trace-free metric equations, including (20), come from the other independent metric variations and must also be retained.

In a local orthonormal base frame, the shape kinetic Lagrangian is

\[
\mathcal L_{\rm shape}=\frac W2[P_t^2+e^{2P}Q_t^2-P_r^2-e^{2P}Q_r^2].
\]

For \(W\ne0\), its canonical Hamiltonian density is

\[
\mathcal H_{\rm shape}=\frac{\pi_P^2+e^{-2P}\pi_Q^2}{2W}
+\frac W2(P_r^2+e^{2P}Q_r^2).
\tag{25}
\]

This quadratic form is nonnegative and nondegenerate exactly when \(W>0\). Since \(W=a\rho\) and \(\rho>0\), that condition is equivalent to \(a>0\). Chart stationarity alone permits \(a=0\); the positivity/nondegeneracy premise selects the positive branch by (25).

## 7. Inclusion and selection of the parity-odd coupling

Fix the orientation \(\epsilon^{tr}=1/\sqrt{-h}\). The invariant target area form is \(\Omega=e^P dP\wedge dQ\), and the general additional two-derivative odd density is

\[
\mathcal L_{\rm odd}=\sqrt{-h}\,k(\rho)\epsilon^{ab}\Omega_{ij}\partial_a\phi^i\partial_b\phi^j
=2k(\rho)e^P(P_tQ_r-P_rQ_t).
\tag{26}
\]

This density is metric independent. On the chart, its area and \(P\) Euler derivatives vanish, whereas

\[
E_Q^{\rm odd}=2e^Pk'(\rho)(\rho_tP_r-\rho_rP_t)
=-4(t/r)k'(\rho).
\tag{27}
\]

Full chart stationarity therefore requires \(k'=0\) at every \(\rho>0\); connectedness gives \(k=k_0\). Conversely a constant coupling is a local divergence because \(\Omega=d(e^P dQ)\):

\[
\mathcal L_{\rm odd}=2k_0\{\partial_t(e^PQ_r)-\partial_r(e^PQ_t)\}.
\tag{28}
\]

Its compactly supported variation is zero. The sign in (27) reverses if the base orientation is reversed; the selected condition is unchanged.

## 8. Exact gravitational interpretation and boundary term

For the literal four-dimensional block metric

\[
g=h_{ab}dx^adx^b+\rho M_{IJ}dy^Idy^J,
\tag{29}
\]

put \(G=\rho M\) and \(K_a=G^{-1}\partial_aG\). The only mixed Christoffel symbols are

\[
\Gamma^a_{IJ}=-\tfrac12h^{ab}\partial_bG_{IJ},\qquad
\Gamma^I_{aJ}=\tfrac12(K_a)^I{}_J.
\tag{30}
\]

The Ricci contractions obtained from these expressions are

\[
R_{ab}[g]=R_{ab}[h]-\tfrac12\nabla_b\operatorname{Tr}K_a-\tfrac14\operatorname{Tr}(K_aK_b),
\]

\[
G^{IJ}R_{IJ}[g]=-\tfrac12\nabla_a\operatorname{Tr}K^a
-\tfrac14\operatorname{Tr}K_a\operatorname{Tr}K^a.
\tag{31}
\]

Since \(K_a=(\partial_a\log\rho)I+J_a\), \(\operatorname{Tr}J_a=0\), and the orbit dimension is two, their sum is

\[
R[g]=R[h]-2\Box\log\rho-\tfrac32(\nabla\log\rho)^2-\tfrac14T.
\tag{32}
\]

Using \(\sqrt{-g}=\rho\sqrt{-h}\) and
\(\rho\Box\log\rho=\Box\rho-X/\rho\),

\[
\boxed{\sqrt{-g}R[g]
=\sqrt{-h}\left[\rho R[h]+\frac X{2\rho}-\frac\rho4T\right]
-2\partial_a(\sqrt{-h}\nabla^a\rho).}
\tag{33}
\]

Thus the selected local action is exactly the orbit-volume-normalized Einstein-Hilbert action multiplied by \(a\), plus the two-dimensional constant-curvature coupling \(b\int\sqrt{-h}R[h]\) and the displayed boundary terms. No equations of motion entered (30)-(33); this is an off-shell identity.

The reference chart (2) has the explicit coordinate realization

\[
X^0=t\cosh z,\quad X^3=t\sinh z,\quad X^1=r\cos\phi,\quad X^2=r\sin\phi,
\]

which gives \(g=-(dX^0)^2+\sum_{i=1}^3(dX^i)^2\). The map is locally invertible for \(t,r>0\). This proves its flatness independently of the selected field equations.

The reduction also retains every four-dimensional vacuum equation. For a block metric independent of the orbit coordinates, the mixed components obey \(R_{aI}[g]=0\) identically. Arbitrary variations of \(h\) give \(E_{ab}=a\rho G_{ab}[g]\); arbitrary variations of positive \(\rho\) and determinant-one \(M\) span all symmetric variations of the positive orbit block \(G=\rho M\). Therefore, for \(a\ne0\), the reduced Euler equations are equivalent to all components of \(G_{\mu\nu}[g]=0\), and hence to \(R_{\mu\nu}[g]=0\). This is a direct variational reduction; the omitted mixed equations vanish identically in the stated orthogonally transitive ansatz.

## 9. Executed independent verification

`verify_variation.py` executes 29 exact symbolic checks with SymPy 1.14.0; every residual equals the exact integer zero. The resulting `variation_certificate.json` records each check. The checks include all three metric chart components, the scalar and shape converse, the target metric identity, the curvature first-variation integration-by-parts identity, the odd-sector equation, four identically vanishing mixed Ricci components, and an independent direct four-dimensional Christoffel/Ricci calculation at arbitrary first- and second-order jets. The last calculation normalizes \(M=I\) and the conformal factor to one at the point through constant frame transformations while preserving all derivative jets; it verifies (32)-(33) on generic off-shell fields. These calculations audit the analytic proof; their status is symbolic computation, distinct from Lean kernel checking.

### Source alignment

The action and geometric conventions are those of the attached v2.3 bundle's `baseline_v2_2/source_audit/Voss_v2_0_Manuscript.pdf`, equations (12)-(14), (19), and (25)-(26). The one-chart formulation is `Voss_v2_1_Audit.pdf`, result A; its parity extension is result B. Equations (19)-(20) above agree exactly with the supplied standalone `ThmA.lean` and `ThmABridge.lean`. The present contribution supplies the analytic first variation with boundary current, all-field converse, explicit derivative bridge, and the independent exact symbolic certificates.
