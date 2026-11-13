# A selected reciprocal quantum–shape coupling

The original state–shape dictionary identifies a geometry. This extension supplies an interaction law: the shape determines a quantum Hamiltonian, and the quantum state produces a reciprocal shape response. Within the explicitly stated class, the matrix-valued coupling is fixed by frame covariance and one calibrated oscillator gap.

There are two distinct realizations. A fully quantum shape–probe cell has linear, unitary joint evolution and can generate entanglement. A variational model with classical shape coordinates gives explicit response equations and a conserved source current. Neither realization is asserted to solve the gravitational quantum constraints or the interacting field continuum.

## 1. Select the interaction before choosing a trajectory

Let $M$ be the positive symmetric unimodular target matrix. Introduce an independent canonical probe with dimensionless quadratures

```math
\widehat R=(\widehat Q,\widehat P)^T,
\qquad [\widehat Q,\widehat P]=i.
```

The physical quadrature scales satisfy $q_*p_*=\hbar$. The geometry and the prepared probe are independent variables; the same state is not counted twice as both geometry and matter.

The coupling class assumes:

- An instantaneous algebraic dependence on $M$, with no target derivatives, external backgrounds, or additional scalar fields.
- A centered, Weyl-ordered quadratic Hamiltonian with a positive symmetric coefficient matrix $K(M)$.
- The calibrated common $SL(2,\mathbb R)$ frame action.
- A fixed positive oscillator gap $\hbar\omega$ and a specified zero of internal energy.

Frame covariance requires

```math
K(AMA^T)=A^{-T}K(M)A^{-1},\qquad A\in SL(2,\mathbb R).
```

At $M=I$, rotational isotropy forces $K(I)$ to be a scalar matrix. A quarter-turn already forces its off-diagonal entry to vanish and its diagonal entries to agree. The gap calibration fixes that scalar to $\hbar\omega$. For $M=AA^T$, covariance then gives

```math
\boxed{K(M)=\hbar\omega M^{-1}.}
```

Any target-only scalar additive term is constant by transitivity. With the ground energy subtracted, the selected Hamiltonian is

```math
\boxed{
\widehat H^{\mathrm{ex}}_M
=\frac{\hbar\omega}{2}\widehat R^T M^{-1}\widehat R
-\frac{\hbar\omega}{2}I\ge0.}
```

The canonical transformation $\widehat R'=M^{-1/2}\widehat R$ turns this into the ordinary oscillator excitation Hamiltonian. Its unique ground ray has covariance $M/2$, exactly the Gaussian ray used by the original dictionary. Thus the geometry selects the probe's local ground state and its entire quadratic Hamiltonian, rather than a Hamiltonian being fitted to an already chosen trajectory.

The magnitude of $\omega$ remains calibrated against the declared probe clock. The smooth state-fluid action uses proper time along its timelike flow; the cell Hamiltonian uses its specified time parameter. Changing clock normalization changes the numerical frequency and Hamiltonian normalization together.

In the original two-Killing model, allowing dependence on the independent area scalar would permit $\omega(\rho)$. In the one-Killing target model there is no such independent area scalar; target-only algebraic equivariance makes the coefficient constant. Derivative couplings, additional fields, or prescribed backgrounds would enlarge the class again.

### Why the coupling-class assumptions matter

Ground-state matching and the first gap alone do not select arbitrary interactions. Let $\widehat n_M=\widehat H_M^{\mathrm{ex}}/(\hbar\omega)$. The family

```math
\widehat H'_M
=\hbar\omega\widehat n_M
+\zeta\widehat n_M(\widehat n_M-1),\qquad \zeta\ge0,
```

is equally frame covariant and has the same ground state and first gap. It is nonquadratic and generally takes Gaussian states outside the Gaussian family. For a squeezed vacuum with mean occupation $\bar n$,

```math
\langle\widehat n_M(\widehat n_M-1)\rangle
=3\bar n^2+\bar n.
```

This is an explicit counterexample to a stronger uniqueness claim. Quadraticity can be stated operationally as linear canonical propagation, but it remains added physical structure. Gaussian symplectic dynamics and the associated variational framework have established precedents. [Hackl and Bianchi](https://arxiv.org/abs/2010.15518v4), [Hackl et al.](https://arxiv.org/abs/2004.01015v4).

## 2. The reciprocal source is fixed as well

For a centered saturated Gaussian probe with covariance $N/2$, define the excitation energy

```math
E(M,N)=\langle\widehat H_M^{\mathrm{ex}}\rangle
=\frac{\hbar\omega}{4}\left[\mathrm{Tr}(M^{-1}N)-2\right].
```

The shape source is $\mathcal S=-\nabla_M E$, using the target metric $G$. In upper-half-plane coordinates $M=M(x,y)$ and $N=M(u,v)$,

```math
E=\frac{\hbar\omega}{4yv}
\left[(x-u)^2+(y-v)^2\right],\qquad y,v>0.
```

Both directions of the interaction come from the same energy. The quantum state responds to $\widehat H_M$, while the shape responds to its variation. The exact energy–distance–fidelity identity and the sharp source relation are developed in [Energy and shape](ENERGY_SHAPE_RELATION.md).

Here “shape source” means force per dimensionless target coordinate. It is not, without a further observation map and physical units, a measured spacetime force.

## 3. A fully quantum shape–probe cell

Use the Hilbert space

```math
\mathcal H=L^2(\mathbb H^2,d\mathrm{vol}_G)\otimes L^2(\mathbb R),
\qquad
\widehat{\mathsf H}
=-\frac{\hbar^2}{2I}\Delta_G+\widehat H_M^{\mathrm{ex}},
\qquad I>0.
```

The shape inertia $I$ is a positive calibrated cell parameter. The Laplacian form and the fiberwise oscillator-excitation form are nonnegative closed quadratic forms. Their common form domain is dense: it contains smooth compactly supported shape functions times Schwartz probe functions. The sum therefore defines a positive self-adjoint operator by the closed-form representation construction.

The resulting joint evolution is linear and unitary. Total energy is conserved on its energy domain, and the interaction permits energy transfer and entanglement between the two factors. It uses ordinary quantum mechanics; a fundamental nonlinear state-evolution rule is not introduced.

This is an exact quantum model of a regulated shape degree of freedom coupled to a probe. Its self-adjointness is not a proof that the full gravitational constraints have been quantized, or that a spatially refined interacting continuum exists.

## 4. Equal full energy distributions, opposite shape responses

The joint target and metaplectic frame actions commute with $\widehat{\mathsf H}$. This supplies a particularly clean comparison between preparations.

Write the target as a hyperboloid:

```math
X_0=\frac12\mathrm{Tr}M,\qquad
X_1=\frac{M_{11}-M_{22}}2,\qquad X_2=M_{12},
\qquad X_0^2-X_1^2-X_2^2=1.
```

The canonical quarter-turn $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ sends $M$ to $M^{-1}$, fixes $X_0$, and reverses $X_1,X_2$. Choose one normalized smooth compactly supported radial shape packet $\Phi(M)$ centered at $I$, and two probe rays with

```math
N_+=\begin{pmatrix}e^s&0\\0&e^{-s}\end{pmatrix},\qquad
N_-=\begin{pmatrix}e^{-s}&0\\0&e^s\end{pmatrix},\qquad s>0.
```

The initial joint states $\Phi\otimes\psi_{N_+}$ and $\Phi\otimes\psi_{N_-}$ are related by a unitary commuting with the full joint Hamiltonian. They therefore have identical **joint-energy spectral measures**, a statement stronger than equality of one mean or a few moments.

To measure directional response with a bounded continuum observable, let $r=d_G(I,M)$ and choose a smooth compact radial cutoff $\zeta(r)$ equal to one on a neighborhood of the initial packet's support. Set

```math
O=\zeta(r)X_1,\qquad
\kappa_\Phi=\langle X_1^2\rangle_\Phi
=\langle X_2^2\rangle_\Phi\ge0.
```

Then the exact initial acceleration is

```math
\boxed{
\left.\frac{d^2\langle O\rangle_\pm}{dt^2}\right|_{t=0}
=\pm\frac{\hbar\omega}{2I}(1+\kappa_\Phi)\sinh s.}
```

To verify the coefficient, use

```math
\nabla X_A\cdot\nabla X_B=X_AX_B-\eta_{AB},
\qquad \eta=\mathrm{diag}(1,-1,-1).
```

The free kinetic double-commutator is odd under the quarter-turn and averages to zero in the radial shape packet. The interaction contributes $-I^{-1}\langle\nabla O\cdot\nabla\widehat H_M^{\mathrm{ex}}\rangle$. On the initial support, $O$ and all its relevant derivatives agree with $X_1$. For probe coordinates $Y_0=\cosh s$, $Y_1=\pm\sinh s$, $Y_2=0$,

```math
E=\frac{\hbar\omega}{2}
\left(\eta_{AB}X_AY_B-1\right).
```

Radial symmetry gives $\langle X_1X_0\rangle=\langle X_1X_2\rangle=0$, which yields the displayed result. The initial compact-support/Schwartz vector is in the required operator domain, and $O$ is bounded. No assertion about finite later-time moments of the unbounded $X_1$ is needed.

For example, the smooth packet $\Phi=C\exp[-1/(1-r^2)]$ for $r<1$, zero outside, gives $\kappa_\Phi\simeq0.11146598698569911$ by a declared quadrature. One may take $\zeta=1$ for $r\le1.1$ and $\zeta=0$ for $r\ge2$, with a smooth interpolation.

The comparison distinguishes the selected orientation-sensitive interaction from an uncoupled or energy-only isotropic response model. It does not exclude every semiclassical theory, and symmetry-related equal-energy states with rotated responses are not by themselves a new quantum-gravity effect.

## 5. Executed fully quantum controls

The checker uses a positive hyperbolic-polar finite-volume shape kinetic matrix on a $4\times8$ grid with outer target radius $1.2$. It couples this to exact projected oscillator-quadratic matrix elements at 16 and 24 Fock levels. It does not square truncated position and momentum matrices and assert an exact finite-dimensional canonical commutator.

The finite domain does not preserve the full noncompact target group. It does preserve the quarter-turn used by the comparison. In units $\hbar=\omega=1$, $I=1/2$, the 24-level run gives:

| Check or observable | Result |
|---|---:|
| Joint Hilbert-space dimension | 768 |
| Joint symmetry commutator norm | $5.81\times10^{-13}$ |
| Initial directional accelerations | $+0.8231656470$ and $-0.8231656470$ |
| Directional responses at $t=0.35$ | $+0.0262193691$ and $-0.0262193691$ |
| Uncoupled directional response | Below $2.3\times10^{-16}$ |
| Shape–probe entanglement at $t=0.35$ | $0.1490367$ bits |
| Uncoupled entanglement | Numerical zero |
| Maximum norm error | $3.56\times10^{-15}$ |
| Maximum total-energy error | $1.96\times10^{-14}$ |

Shape energy rises from approximately $5.95400383$ to $5.99045643$, while probe energy falls from $0.22207748$ to $0.18562488$. Their sum is conserved to the reported accuracy. Increasing the oscillator cutoff from 16 to 24 changes the largest directional response by $6.22\times10^{-8}$.

This is a Fock-cutoff check at a fixed shape grid. It is not a shape-grid continuum demonstration. The numerical radial Gaussian packet also differs from the compact bump in the continuum acceleration example, so the two acceleration coefficients should not be numerically identified.

The [executed receipt](../evidence/extensions/dynamics/dynamical_extension_receipt.json) records the parameters, 41 exact checks, positive and uncoupled controls, and both cutoffs. The [checker](../scripts/extension_checks/verify_dynamical_extension.py) can be run without modifying archived evidence:

```bash
mkdir -p work/dynamics
cp scripts/extension_checks/verify_dynamical_extension.py work/dynamics/
python work/dynamics/verify_dynamical_extension.py
```

Install the root pinned scientific requirements first. The script writes its results beside this temporary copy.

## 6. A closed response system in the variational model

The classical-shape/Gaussian-probe action

```math
L=\frac{\mu}{2y^2}(\dot x^2+\dot y^2)
-\frac{\hbar\dot u}{4v}-E(x,y,u,v),\qquad \mu>0,
```

uses the same selected energy and the Gaussian Berry one-form. It gives

```math
\begin{aligned}
\ddot x-\frac{2\dot x\dot y}{y}
&=-\frac{\hbar\omega y(x-u)}{2\mu v},\\
\ddot y+\frac{\dot x^2-\dot y^2}{y}
&=\frac{\hbar\omega}{4\mu v}
\left[v^2+(x-u)^2-y^2\right],\\
\dot u&=\frac\omega y\left[v^2-y^2-(u-x)^2\right],\\
\dot v&=\frac{2\omega v(x-u)}y.
\end{aligned}
```

The last two equations agree exactly with the quadratic Schrödinger covariance evolution

```math
\dot N=\omega\left(JM^{-1}N-NM^{-1}J\right),
\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
```

Centering, positivity, Gaussianity, and determinant are preserved. The total energy and shear charge are conserved:

```math
E_{\mathrm{cell}}
=\frac{\mu}{2y^2}(\dot x^2+\dot y^2)+E,
\qquad
\mathcal C=\frac{\mu\dot x}{y^2}-\frac\hbar{4v}
=p_x-\frac\hbar2\langle\widehat Q^2\rangle.
```

Finite initial energy bounds the speed on the complete hyperbolic target and bounds the probe's distance from the geometry. On every finite time interval, the coordinates and velocities stay in a compact region of the phase space. Smooth ODE continuation therefore supplies global solutions for this finite-cell system. This does not prove a global field-PDE result.

Linearizing around a common isotropic equilibrium gives two nonzero positive response frequencies,

```math
\Omega_\pm=\sqrt{\omega^2+g}\pm\omega,
\qquad g=\frac{\hbar\omega}{2\mu},
\qquad
\Omega_+\Omega_-=g,\quad\Omega_+-\Omega_-=2\omega.
```

The frozen-geometry Gaussian covariance oscillates at $2\omega$. Reciprocal response produces the two sidebands; the slower branch tends to zero at infinite shape inertia. The characteristic polynomial and conservation equations are checked exactly. A tolerance-refined evolution through $t=20$ has maximum energy drift below $8.57\times10^{-12}$ in the finer run.

## 7. Ground-band compression predicts unavoidable initial recoil

A further exact calculation tests the approximation that the probe always stays in its local ground ray. In this section use geometry coordinates $(u,v)$ and probe coordinate $\xi$, and let $\mathcal P$ be the fiberwise projector onto $\psi_M(\xi)$. For an initial normalized state $\Phi(M)\psi_M(\xi)$ with $\Phi\in C_c^\infty(\mathbb H^2)$, set $\alpha=\hbar^2/(2I)$. The exact compressed operator is

```math
\mathcal P\widehat{\mathsf H}\mathcal P
=\alpha\left(-\Delta_{\mathcal A}+\frac14\right),
\qquad \mathcal A=-\frac{du}{4v}.
```

The scalar wavefunction uses the covariant derivative $\partial-i\mathcal A$. In these coordinates the operator is

```math
\alpha\left[-v^2(\partial_u^2+\partial_v^2)
-\frac{iv}{2}\partial_u+\frac5{16}\right].
```

Compression is an operator identity; it does not make this band invariant. Define

```math
D=v(\partial_v-i\partial_u)+\frac14.
```

The component outside the ground band is exactly

```math
(1-\mathcal P)\widehat{\mathsf H}(\Phi\psi_M)
=\alpha v D\Phi
\left(\xi^2-\frac1{2v}\right)\psi_M.
```

For the measure $du dv/v^2$, $D^\dagger D$ equals the compressed operator divided by $\alpha$. The Gaussian variance of $\xi^2$ is $1/(2v^2)$. Thus, writing $E_{\mathrm{joint}}=\langle\Phi\psi_M,\widehat{\mathsf H}\Phi\psi_M\rangle$,

```math
\left\|(1-\mathcal P)\widehat{\mathsf H}(\Phi\psi_M)\right\|^2
=\frac\alpha2 E_{\mathrm{joint}},
\qquad
\boxed{P_{\mathrm{out}}(t)
=\frac{E_{\mathrm{joint}}}{4I}t^2+o(t^2).}
```

This is a small-time coefficient, not a finite-time upper bound. Its independence of $\omega$ does not imply a uniform adiabatic limit. The condition $D\Phi=0$ would make $v^{1/4}\Phi$ holomorphic; a nonzero compactly supported packet cannot satisfy it. Exact autonomous ground-band evolution is therefore unavailable for this packet class.

The [projection checker](../scripts/extension_checks/verify_projection.py) executes 13 exact checks; its [receipt](../evidence/extensions/projection/projection_receipt.json) separates symbolic identities from the operator-domain and small-time arguments.

## 8. Relation to the sourced gravitational model

The finite quantum cell and the smooth state-fluid construction are different mathematical descriptions. The cell gives a complete joint quantum Hamiltonian for its declared variables. The state-fluid action uses classical quotient geometry and quantum internal states transported by a conserved timelike flow. Generic expectation-value backreaction has substantial precedent in semiclassical and stochastic gravity. [Hu and Verdaguer](https://arxiv.org/abs/0802.0658v1).

In a one-Killing interpretation, $M$ is built from Killing norm $\lambda$ and twist $\chi$. A generic probe sources $\chi$, so the old vacuum reconstruction $F=-\lambda^{-2}*d\chi$ cannot simply be retained. Shear dressing of the probe adds its current to the conserved twist current. The repaired reconstruction uses that total current, with a smooth density or finite regulator; a squared delta-function worldline current is not defined.

The selected coupling, reciprocal cell dynamics, and repaired smooth-current action therefore provide explicit model extensions with clear roles. They do not establish an anomaly-free continuum quantization, laboratory evidence, or worldwide priority. The contribution is a fixed interaction and a checkable observation chain within the stated class.
