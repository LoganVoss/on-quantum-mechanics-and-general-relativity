# Physical premises: constructive realization, classification, and operational frame identification

## 1. Exact contract and the distinction needed for a sound theorem

The supplied theorem is a theorem for a four-dimensional local metric model with a two-dimensional Lorentzian quotient and two spacelike symmetry directions. The field variables are a Lorentzian metric `h`, an orbit area density `rho > 0`, and a positive symmetric unimodular matrix `M`. The geometric dictionary is

\[
 g=h_{ab}(x)dx^a dx^b+\rho(x)M_{IJ}(x)dy^I dy^J.
\]

The coordinate volume and orbit labels are calibrated. The base metric is the literal metric block. All local variations below are smooth and compactly supported in a regular base patch. This avoids imposing any scattering, axis, or asymptotic boundary conditions on the Milne calibration chart.

A precise conditional theorem has the following logical content. The indicated kinematic and calibration data are inputs. Their mathematical consequences are proved, an explicit model realizes every input simultaneously, and the action coefficients are then selected by stationarity. An empirical assertion that the physical universe implements an input is a separate proposition, with measurement evidence as its truth condition. The attached files contain mathematical model definitions and symbolic/numerical checks, not such measurements.

The minimal mathematical selection theorem itself does not require a quantum probe, an asymptotically cylindrical scattering sector, the Lax ansatz, or an interacting quantum continuum. Those objects supply additional interpretations and extensions. Including a canonical probe as below shows that the information-geometric interpretation and the selected geometric action coexist in one explicit model.

## 2. Canonical saturation derives the Gaussian and its orbit shape

Work in the calibrated dimensionless Schrödinger representation on `L^2(R)`, with `Q f=x f`, `P f=-i f'`, and `[Q,P]=iI` on the Schwartz core. The dimensional operators are `q=q_* Q`, `p=p_* P`, where `q_* p_*=hbar`.

Let `varrho` be a positive trace-one density operator with centered finite second moments

\[
 V=\begin{pmatrix}q&c\\c&p\end{pmatrix}>0,
 \qquad qp-c^2=\tfrac14.
\]

Define

\[
 z=u+iv=\frac{c+i/2}{q},\qquad v=\frac1{2q}>0,
 \qquad B=P-zQ.
\]

Finite second moments make the following quadratic-form expression finite. Direct expansion using `PQ=QP-iI` gives

\[
 \operatorname{Tr}(\varrho B^*B)
 =p-2uc-v+(u^2+v^2)q
 =\frac{qp-c^2-1/4}{q}=0.
\]

Write the spectral decomposition `varrho=sum_j p_j |psi_j><psi_j|`, retaining terms with `p_j>0`. Positivity gives

\[
 0=\sum_j p_j\|B\psi_j\|^2,
\]

so every support vector satisfies `B psi_j=0`. The weak first-order equation is

\[
 -i\psi'(x)-zx\psi(x)=0,
\]

whose locally absolutely continuous solutions are `C exp(i z x^2/2)`. Because `v>0`, its square-integrable solution space is one dimensional. Normalization gives

\[
 \psi_{u,v}(x)=\left(\frac v\pi\right)^{1/4}
 \exp\!\left[\frac{i(u+iv)x^2}{2}\right].
\]

Therefore `varrho` has rank one. This argument supplies the Gaussian from uncertainty saturation; Gaussianity is not an extra independent preparation assumption.

Its covariance is

\[
 V=\frac1{2v}\begin{pmatrix}1&u\\u&u^2+v^2\end{pmatrix},
 \qquad
 M=2V=\frac1v\begin{pmatrix}1&u\\u&u^2+v^2\end{pmatrix}.
\]

It follows directly that `M=M^T>0` and `det M=1`. Conversely every such `M` gives `v=1/M_11>0` and `u=M_12/M_11`, hence one normalized Gaussian ray.

### Target metric

The logarithmic parameter derivatives are

\[
 \partial_u\log\psi=\frac{i x^2}{2},\qquad
 \partial_v\log\psi=\frac1{4v}-\frac{x^2}{2}.
\]

Gaussian moments `E[x^2]=1/(2v)` and `E[x^4]=3/(4v^2)` inserted into the pure-state Fisher tensor give

\[
 ds^2_{\rm QFI}=\frac{du^2+dv^2}{2v^2}.
\]

Direct matrix multiplication gives

\[
 \frac12\operatorname{Tr}[(M^{-1}dM)^2]
 =\frac{du^2+dv^2}{v^2}=2ds^2_{\rm QFI}.
\]

With `P=-log v`, `Q=u`, the normalized shape metric is

\[
 G=dP^2+e^{2P}dQ^2.
\]

The factor of two between the normalized shape metric and QFI must be retained when normalizing `W`.

## 3. The equivariant orbit map is unique once its representation is calibrated

Let `B(M)` be the orbit shape assigned to a covariance shape, and require

\[
 B(AMA^T)=A B(M)A^T,\qquad A\in SL(2,\mathbb R),
 \qquad B(I)=I.
\]

For any positive unimodular `M`, its positive square root `A=M^{1/2}` has determinant one and satisfies `M=AA^T`. Therefore

\[
 B(M)=B(AIA^T)=AB(I)A^T=AA^T=M.
\]

The calibration `B(I)=I` itself follows from positivity, unit determinant, and equivariance: rotations stabilize `I`, so `B(I)` commutes with every planar rotation; a symmetric such matrix is `lambda I`; positivity and determinant one give `lambda=1`.

The representation is part of the calibration. If covariance frames and orbit frames are related through the dual representation, the map is correspondingly inverted, which is a fixed orbit-frame relabeling in two dimensions. The theorem above uses the stated common congruence representation and cannot silently interchange the two.

## 4. Dimension, signature, and absence of mixed connections follow inside the geometric realization

For the stipulated direct block decomposition,

\[
 \dim g=2+2=4,\qquad
 \det g=\det h\,\det(\rho M)=\rho^2\det h.
\]

Since `h` has one negative and one positive direction while `rho M` is positive definite, Sylvester inertia gives

\[
 \operatorname{signature}(g)=(-,+,+,+).
\]

Independence of all coefficients from `y^I` proves that `partial_{y^I}` are commuting Killing fields. The orbit block is positive definite, so they span a spacelike two-plane. The base coordinate planes are orthogonal to that orbit plane and integrate to the surfaces `y^I=constant`, proving orthogonal transitivity for this realization.

The Lorentzian base, number of blocks, and geometric interpretation are specified physical inputs. The signature and dimension conclusions above are rigorous consequences of those inputs, not consequences of the positive quantum Fisher metric by itself.

## 5. Complete invariant action classification at total derivative order two

Assume locality; invariance under base diffeomorphisms; invariance under constant target `SL(2,R)` congruences; polynomial dependence on derivatives with total derivative order at most two; and no additional fields. Do not assume parity.

The target is the homogeneous space of positive unimodular matrices. At `M=I`, its tangent space consists of real traceless symmetric matrices

\[
 X=\begin{pmatrix}x&y\\y&-x\end{pmatrix}.
\]

Conjugation by a planar rotation acts as a rotation through twice the angle on `(x,y)`. Consequently:

1. There is no nonzero invariant target covector: a rotation through `pi/2` in the original frame acts as `-I` on this tangent space.
2. There is exactly one invariant symmetric target bilinear form up to scale, because a symmetric matrix commuting with all planar rotations is scalar.
3. There is exactly one invariant alternating target bilinear form up to scale, the oriented area form.
4. Every invariant target scalar is constant, because the group acts transitively.

Thus every scalar coefficient depends only on `rho`; no mixed `grad rho · grad q` coupling survives; the even shape kinetic term is fixed up to a function `W(rho)`; the only metric curvature scalar at this derivative order is `R[h]`; and a term `C(rho) box rho` integrates into the radial kinetic term. Linear target second derivatives reduce by integration by parts to the invariant kinetic term, with no independent invariant one-form available.

Modulo divergences, the full action is therefore

\[
 S=\int\sqrt{-h}\left[
 F(\rho)R[h]+U(\rho)(\nabla\rho)^2
 -\frac{W(\rho)}2 G_{AB}(q)\nabla q^A\cdot\nabla q^B
 +V(\rho)\right]d^2x+S_{\rm odd}.
\]

In the global target coordinates above,

\[
 \Omega=e^P dP\wedge dQ=d(e^P dQ),
\]

and, choosing the oriented base coordinates `(t,r)`,

\[
 S_{\rm odd}=\int 2k(\rho)e^P(P_t Q_r-P_r Q_t)\,dt\,dr.
\]

### The chart removes the parity-odd bulk coupling

Its `Q` Euler-Lagrange derivative, with convention `EL=partial L/partial Q-partial_a(partial L/partial Q_a)`, is

\[
 E_Q^{\rm odd}=2 k'(\rho)e^P(\rho_t P_r-\rho_r P_t).
\]

On `rho=tr`, `P=log(t/r)`, `Q=0`, this equals

\[
 E_Q^{\rm odd}=-4\frac tr k'(tr).
\]

Since every `rho>0` is attained and `t/r>0`, stationarity forces `k'(rho)=0`. Connectedness then gives a constant `k`. For constant `k`, `S_odd=2k int d(e^P dQ)` is a boundary functional. Thus parity need not be postulated: the permitted parity-odd bulk term is eliminated by full chart stationarity.

The total derivative-order requirement remains explicit. Replacing it only by "second-order field equations" changes the class. For example a polynomial nonlinear in first-derivative invariants can have second-order Euler-Lagrange equations while having total derivative order four or more. This is why the exact derivative premise must appear in the theorem statement.

## 6. Positive radiative energy selects the sign of the free coefficient

The local shape Lagrangian in a conformal quotient chart `h=e^{2s}(-dT^2+dR^2)` is

\[
 \mathcal L_{\rm shape}=\frac{W(\rho)}2
 G_{AB}(q)(q_T^Aq_T^B-q_R^Aq_R^B).
\]

The conformal factor cancels because the base is two dimensional. The canonical momentum and Hamiltonian density are

\[
 \Pi_A=W G_{AB}q_T^B,
\]

\[
 \mathcal H_{\rm shape}=
 \frac1{2W}G^{AB}\Pi_A\Pi_B+
 \frac W2 G_{AB}q_R^Aq_R^B.
\]

Since `G` is positive definite, strict positivity and nondegeneracy of the radiative kinetic energy are equivalent to `W>0`. The selected relation `W=a rho` and `rho>0` then imply `a>0`. This is a sign selection, not a numerical determination of Newton's constant. The radial dilaton kinetic coefficient `U` is part of a constrained metric-dilaton system, so testing its isolated sign as if it were an independent matter scalar would be inappropriate.

If the Einstein-Hilbert normalization is adopted after the off-shell identity, the coefficient is `a=V_y/(16 pi G_4)` for the chosen orbit coordinate volume `V_y`. Fixing units or a measured response fixes `a`; local flat stationarity leaves its magnitude free.

## 7. Massive or orbit-momentum probes identify the literal metric frame

Fix `h,rho,M` and consider

\[
 g_\sigma=e^{2\sigma(x)}h_{ab}dx^a dx^b+
 \rho M_{IJ}dy^I dy^J.
\]

Specify the calibrated probe action

\[
 S_{\rm pr}=-\frac12\int\sqrt{-g_\sigma}
 [g_\sigma^{\mu\nu}\partial_\mu\Phi^*\partial_\nu\Phi
 +m^2\Phi^*\Phi]d^4x.
\]

An irrelevant real-field normalization may be used instead. The absolute kinetic normalization, mass parameter, and orbit-coordinate momentum convention are held fixed. Compactly supported variation gives `(box_{g_sigma}-m^2)Phi=0`. For a mode `Phi=phi(x)exp(i k_I y^I)`,

\[
 \sqrt{-g_\sigma}=e^{2\sigma}\rho\sqrt{-h},\quad
 g_\sigma^{ab}=e^{-2\sigma}h^{ab},\quad
 g_\sigma^{IJ}=\rho^{-1}M^{IJ}.
\]

The exact mode equation is

\[
 e^{-2\sigma}D_0\phi-V_k\phi=0,
\]

\[
 D_0=\frac1{\rho\sqrt{-h}}
 \partial_a(\rho\sqrt{-h}h^{ab}\partial_b),\qquad
 V_k=m^2+\rho^{-1}M^{IJ}k_I k_J.
\]

Normalizing the leading differential part to the fixed operator `D0` gives

\[
 P_\sigma=D_0-e^{2\sigma}V_k.
\]

If `V_k>0` and two candidate calibrated operators agree, their zero-order coefficients agree, hence `e^{2sigma_1}=e^{2sigma_2}` and `sigma_1=sigma_2`. If only source-free solutions are used, the same conclusion holds wherever a common solution is nonzero:

\[
 e^{2\sigma}=\frac{D_0\phi}{V_k\phi}.
\]

Multiple solutions cover nodal sets. With an external source, its normalization must be retained when the full operator is multiplied by `e^{2sigma}`; homogeneous operator equality and sourced response equality must not be conflated. If `m=k=0`, then `V_k=0` and this probe has no frame sensitivity. For `m>0`, positivity is automatic; for `m=0,k!=0`, positivity follows from `M>0`.

The test-field limit is obtained by scaling the probe amplitude by `epsilon`: its stress tensor scales as `epsilon^2`, while the normalized homogeneous mode equation is unchanged. Thus the frame identification is compatible with an unperturbed background in the zero-amplitude limit.

## 8. One simultaneous realization

Take an open rectangle `U=(t_0,t_1) x (r_0,r_1)` with `0<t_0<t_1` and `0<r_0<r_1`; the construction extends to the full positive quadrant. Use compactly supported variations in `U`. Let

\[
 h=-dt^2+dr^2,\quad \rho=tr,\quad
 M=\operatorname{diag}(t/r,r/t),\quad
 P=\log(t/r),\quad Q=0.
\]

Then

\[
 g=-dt^2+dr^2+t^2dz^2+r^2d\phi^2.
\]

The explicit map

\[
 X^0=t\cosh z,\quad X^3=t\sinh z,\quad
 X^1=r\cos\phi,\quad X^2=r\sin\phi
\]

pulls the Minkowski metric back to `g`. This proves local flatness directly. The local orbit labels can be restricted so the map is injective. Taking `phi` periodic gives the usual angular orbit if desired; the proof uses a local angular chart. The `z` Killing direction is a spacelike boost orbit, which is why no asymptotic translational scattering conditions are attached to this calibration.

Choose any `a>0`, any real `b`, and any constant `k`, and set

\[
 F=a\rho+b,\quad U=\frac a{2\rho},\quad
 W=a\rho,\quad V=0.
\]

The quotient is flat, `box rho=0`, and

\[
 X=(\nabla\rho)^2=t^2-r^2,
 \qquad G^a{}_a=-\frac1{t^2}+\frac1{r^2}
 =\frac X{\rho^2}.
\]

All three metric equations vanish upon substitution. The area equation is

\[
 E_\rho=F'R-U'X-2U\Box\rho-
 \frac{W'}2 G^a{}_a+V'
 =\frac a{2\rho^2}X-\frac a2\frac X{\rho^2}=0.
\]

The `P` equation reduces to

\[
 -\partial_t(WP_t)+\partial_r(WP_r)
 =-\partial_t(ar)+\partial_r(-at)=0,
\]

and the `Q` equation vanishes because `Q=0` and `k'=0`. Thus the full action is stationary, including area and both shape variations; metric stationarity alone has not been substituted for full stationarity.

The canonical information probe at every point can be chosen as

\[
 \psi_{t,r}(x)=\left(\frac r{\pi t}\right)^{1/4}
 \exp\!\left(-\frac r{2t}x^2\right).
\]

Its covariance is `V=M/2`, it saturates uncertainty, and it realizes exactly the same orbit shape. Its normalization, two variances, and determinant were checked symbolically.

For a calibrated test mass `m>0` and orbit momentum `k_I=0`, the reduced operator is

\[
 D_0=-\partial_t^2-\frac1t\partial_t+
 \partial_r^2+\frac1r\partial_r.
\]

Choose two time-only solutions of

\[
 f''+\frac1t f'+m^2f=0
\]

with independent initial data at some `t_*>0`:
`f_1(t_*)=1, f_1'(t_*)=0`, `f_2(t_*)=0, f_2'(t_*)=1`.
Existence and uniqueness hold on every compact positive time interval. Abel's identity yields the Wronskian

\[
 f_1 f_2'-f_1'f_2=\frac{t_*}{t}\ne0.
\]

They never vanish simultaneously. Therefore their nonzero sets cover `U`. For either available probe, `D0 f_j=m^2 f_j`, and the frame reconstruction gives `e^{2sigma}=1`. This explicitly identifies the chosen literal frame everywhere on the patch using a finite probe family and calibrated principal normalization.

This is one simultaneous model of the geometry, canonical probe, target covariance, selected action, full stationarity, positive radiative energy, and frame-identifying probe. It is a mathematical existence witness, not an assertion of an unperformed laboratory experiment.

## 9. Boundary and analytic precision

The constant `b` gives no bulk field equation under compactly supported variations: the two-dimensional Einstein tensor is identically zero and derivatives of `b` vanish. On manifolds with boundary, identifying the complete term as an Euler invariant requires its Gauss-Bonnet boundary and corner completion; `int sqrt(-h)R` alone is not a topology-only quantity with arbitrary boundary data.

Likewise, the constant odd term is harmless for local variations, and its global effect is a boundary functional. A global variational problem must specify the boundary functional and boundary data. No axis limit is needed for the selection proof on `rho>0`.

For `F''=0 -> F'=constant`, only differentiability of `F'` on the connected positive interval is required. The mean-value theorem applies on each compact segment between two positive points because differentiability implies continuity. One further mean-value application to `F-a rho` gives `F=a rho+b`. Connectedness is essential: on a disconnected domain there can be different slopes on different components. The same argument makes `k` constant from `k'=0`.

## 10. Executed verification

`verify_physical_premises.py` independently checked 276 exact symbolic identities using SymPy 1.14.0. These include the full Minkowski pullback, all 256 four-dimensional Riemann components, all quotient metric equations, area and shape equations, the parity-odd chart derivative, Gaussian normalization and covariance, and the conformal probe volume and differential operator identities. All passed. The receipt is `physical_premises_checks.json`.

The checks establish algebraic identities for the stated model. The analytic existence and mean-value arguments above are proved mathematically and are separate from these symbolic calculations.
