# Four-derivative discrimination, literal frame, and corrected asymptotic twist

## A. Exact exclusion of the reduced deformation

Write the even selected action as

\[
 S_*=a\int\sqrt{-h}\left[\rho R[h]+\frac{(\nabla\rho)^2}{2\rho}
 -\frac\rho2 G_{AB}(q)\nabla q^A\cdot\nabla q^B\right]d^2x,
\]

where `a>0` and `G=dP^2+e^{2P}dQ^2`. The Euler constant and completed boundary terms can be appended. Define

\[
 X=h^{ab}\rho_a\rho_b,\quad
 Y=h^{ab}G_{AB}q_a^Aq_b^B,\quad
 K_{ab}=\rho^2G_{AB}q_a^Aq_b^B-\rho_a\rho_b,
 \quad N=h^{ab}K_{ab}=\rho^2Y-X.
\]

Consider the extended action

\[
 S_\Lambda=S_*+\Delta S,\qquad
 \Delta S=\int\sqrt{-h}\,\Lambda(\rho)N^2\,d^2x.
\]

Allowing a function `Lambda(rho)` strengthens the original constant-`lambda` test. `N` has total derivative order two, so `N^2` has total derivative order four even though this deformation uses only first derivatives and consequently has second-order Euler-Lagrange equations.

### Full first variation

Use inverse-metric variations and define

\[
 \delta\Delta S=\int\sqrt{-h}
 [\Delta E_{ab}\delta h^{ab}+\Delta E_\rho\delta\rho
 +\Delta E_P\delta P+\Delta E_Q\delta Q]d^2x
\]

for compactly supported variations. Direct differentiation gives

\[
 \boxed{\Delta E_{ab}=\Lambda\left(2NK_{ab}-\frac12h_{ab}N^2\right).}
\]

Therefore in two base dimensions,

\[
 \boxed{h^{ab}\Delta E_{ab}=\Lambda N^2.}
\]

The area and shape variations are

\[
 \boxed{\Delta E_\rho=\Lambda' N^2+4\Lambda\rho NY
 +4\nabla_a(\Lambda N\nabla^a\rho),}
\]

\[
 \boxed{\Delta E_P=4\Lambda\rho^2Ne^{2P}(\nabla Q)^2
 -4\nabla_a(\Lambda\rho^2N\nabla^aP),}
\]

\[
 \boxed{\Delta E_Q=-4\nabla_a(\Lambda\rho^2Ne^{2P}\nabla^aQ).}
\]

These formulas also show why merely evaluating the deformation's Lagrangian is not enough in general. Here the stronger fact `N=0` identically on a chart implies its derivatives vanish too, so all four Euler-Lagrange variations vanish.

### Why all three flat references miss it

For a constant product, all scalar derivatives vanish, hence `N=0`. For the flat cylinder `rho=r`, `P=-log r`, `Q=0`, one has `X=1`, `Y=1/r^2`, hence `N=0`. For the Milne-polar chart `rho=tr`, `P=log(t/r)`, `Q=0`,

\[
 X=t^2-r^2,\qquad Y=\frac{t^2-r^2}{t^2r^2},\qquad N=0.
\]

Thus every smooth `Lambda` preserves full stationarity of all three flat reference families. This exact statement is stronger than a numerical zero residual.

### Exact curved Levi-Civita reference

For any real `c` and `gamma_0`, take

\[
 \rho=R>0,\quad \psi=c\log R,\quad A=0,\quad
 \gamma=\frac{c^2}{2}\log R+\gamma_0.
\]

The corresponding metric is

\[
 g=e^{2s}(-dT^2+dR^2)+R^c dz^2+R^{2-c}d\phi^2,
\]

\[
 2s=\gamma-\psi=\frac{D}{2}\log R+\gamma_0,
 \qquad D=c(c-2).
\]

The orbit shape variables are `P=(c-1)log R`, `Q=0`. All sixteen Ricci components and all selected action equations vanish exactly. This is a local reference on positive radial patches; no regular-axis or asymptotic conical condition is attached to the generic curved Levi-Civita family.

On this family,

\[
 X=e^{-2s},\qquad
 Y=\frac{(c-1)^2}{R^2}e^{-2s},\qquad
 \boxed{N=D e^{-2s}.}
\]

The full deformation residuals become

\[
 \Delta E_{TT}=\frac12\Lambda D^2e^{-2s},\qquad
 \Delta E_{RR}=\frac32\Lambda D^2e^{-2s},\qquad
 \Delta E_{TR}=0,
\]

\[
 \Delta E_\rho=e^{-4s}\left[
 \Lambda'D(D+4)+\frac{2\Lambda}{R}D(D+2)\right],
\]

\[
 \Delta E_P=-4D(c-1)e^{-4s}
 \left[R\Lambda'+\Lambda\left(1-\frac D2\right)\right],
 \qquad \Delta E_Q=0.
\]

In particular,

\[
 h^{ab}\Delta E_{ab}=\Lambda(R)D^2e^{-4s}.
\]

**Coefficient-isolation theorem.** Require any one fixed Levi-Civita family with `c not in {0,2}` to remain stationary for every `R>0`. Because `D^2>0` and `e^{-4s}>0`, its trace equation forces

\[
 \boxed{\Lambda(R)=0\quad\text{for every }R>0.}
\]

For a constant deformation this gives `lambda=0`. Thus a single nonflat member, varied over radius, removes this entire functional deformation. The particularly simple choice `c=1` gives `D=-1`, constant `M=I`, and trace residual `Lambda(R)e^{-2gamma_0}R`, immediately isolating the coefficient.

Equivalently, a conformal variation `h_ab -> e^{2 epsilon f}h_ab` changes the deformation at first order by

\[
 \delta_f\Delta S=-2\int\sqrt{-h}\,f\Lambda N^2\,d^2x.
\]

On a patch where `Lambda != 0` and `c not in {0,2}`, a suitably supported `f` makes this nonzero. This is an explicit variational witness, not an inference based solely on the value of `N`.

The executable `verify_levi_civita_deformation.py` passed 36 exact identities, including the generic inverse-metric variation, all sixteen Levi-Civita Ricci components, selected field equations, all deformation residuals, and all three flat-reference identities.

## B. Quotient Weyl frame as an explicit premise

The physical dictionary is

\[
 g=h+\rho M,
\]

with `h` the literal base block. A two-dimensional redefinition

\[
 h_0=e^{2\eta B(\rho)}h_\eta
\]

changes the curvature term, modulo a divergence, by

\[
 \sqrt{-h_0}F R[h_0]
 =\sqrt{-h_\eta}\left[F R[h_\eta]
 +2\eta F'B'(\nabla\rho)^2\right]+\text{divergence}.
\]

For `F=a rho`, this gives

\[
 U_\eta=\frac a{2\rho}+2a\eta B'(\rho),\quad
 W=a\rho,\quad V=0.
\]

These actions have the same shape Lax equations and harmonic area. If `h_eta` is still interpreted as the literal base block while the orbit dictionary is held fixed, the four-dimensional metric changes. For a cylindrical flat seed,

\[
 g_\eta=e^{\gamma(R)}(-dT^2+dR^2)+R^2d\phi^2+dz^2,
 \qquad \gamma=-2\eta B(R),
\]

and

\[
 R[g_\eta]=-e^{-\gamma}\gamma''.
\]

A compactly supported nontrivial `B` can preserve both axis and asymptotic data while changing the curvature. Thus the ledger must name the physical frame and the metric dictionary, not identify the Lax system alone with the entire geometry.

This premise was missing from the initial v2.0 input ledger, explicitly identified in the v2.1 audit, explicitly stated in the v2.2 foundations, and supplied with a calibrated massive/orbit-momentum probe selector in v2.3. The new physical-premise proof proves the operator-level frame-identification statement and a simultaneous realization.

## C. Asymptotic twist: exact conservation law and global sector

In the two-polarization dual variables, the exact equations include

\[
 \chi_{TT}-\chi_{RR}-\frac1R\chi_R
 =2(\psi_T\chi_T-\psi_R\chi_R).
\]

Define the twist charge density and flux

\[
 q=R e^{-2\psi}\chi_T,\qquad j=R e^{-2\psi}\chi_R.
\]

Direct substitution gives

\[
 \boxed{\partial_Tq=\partial_Rj.}
\]

The twist potential satisfies `A_R=q`, `A_T=j`. Hence on a finite radial interval,

\[
 Q_L(T)=A(T,L)-A(T,0)=\int_0^Lq(T,R)\,dR,
\]

\[
 \boxed{\frac{dQ_L}{dT}=j(T,L)-j(T,0).}
\]

Regular even data at the axis give `j(T,0)=0`. If the asymptotic flux vanishes, then `Q_infinity` is conserved. Its value is initial data, not fixed to zero by the local equations.

In the metric `e^psi(dz+A dphi)^2`, setting `A(axis)=0` fixes the regular angular axis. A nonzero `A(infinity)` can be removed locally by shifting the orbit coordinate, but when `phi` is periodic that shift changes the global identification into a helical one. The globally untwisted asymptotically conical sector therefore requires

\[
 \boxed{A(\infty)-A(0)=0.}
\]

This belongs in the boundary ledger together with axis regularity, orbit-coordinate normalization, and asymptotic clock normalization.

### Original and corrected initial data

The supplied original velocity profile is

\[
 \chi_T(0,R)=-0.09(1-0.2R^2)e^{-(R/1.5)^2},
\]

with `psi(0,R)=1.6 exp[-(R/1.1)^2]`. Its continuum twist is

\[
 Q_\infty(0)=-0.013089872446886107.
\]

This is the approximately `-0.0131` charge identified by the audit. Correct the initial velocity by

\[
 \chi_T^{\rm corr}(0,R)=\chi_T(0,R)+c_*e^{-(R/1.2)^2},
\]

where the continuum definition is

\[
 \boxed{c_*=-\frac{\int_0^\infty R e^{-2\psi}\chi_T\,dR}
 {\int_0^\infty R e^{-2\psi}e^{-(R/1.2)^2}\,dR}.}
\]

The denominator is strictly positive, so this gives the unique coefficient within the specified one-function correction. Its value is

\[
 c_*=0.05278195754784881.
\]

The integral identity sets the exact continuum charge to zero by construction. Fresh adaptive quadrature returned `3.550762114890027e-18`, with estimated absolute error `1.5536197812261851e-15`. One continuum coefficient was used on every grid, without grid-by-grid retuning.

### Correct historical status

The v2.1 audit gave the correction coefficient and correctly reported that it had not re-evolved the corrected data. The supplied v2.2 package subsequently performed corrected evolutions at 128, 256, 512, and 1024 intervals. The present run independently re-executed those equations and reproduced every listed v2.2 result exactly. Consequently the current status is **corrected and re-evolved**, with discretization and finite-boundary effects measured below.

## D. Fresh nonlinear evolution and boundary-flux verification

The historical finite-difference equations, axis treatment, frozen outer field values, and fourth-order Runge-Kutta update were reused unchanged. The outer radius was `L=8`, the final time `T=0.8`, and the time step approximately `0.16 dR`. New diagnostics independently evaluated the physical outer flux using a second-order one-sided derivative and integrated it using the same Runge-Kutta stages.

| Intervals | Initial discrete twist | Final twist minus initial | Integrated outer twist flux | Twist balance defect | Relative energy drift |
|---:|---:|---:|---:|---:|---:|
| 128 | 4.9344449e-7 | -2.3648118e-4 | -1.7532395e-7 | -2.3630586e-4 | 2.5284905e-4 |
| 256 | 1.2343554e-7 | -5.9351339e-5 | -1.7867687e-7 | -5.9172662e-5 | 6.2785521e-5 |
| 512 | 3.0863153e-8 | -1.4978657e-5 | -1.7945917e-7 | -1.4799198e-5 | 1.5669804e-5 |
| 1024 | 7.7156684e-9 | -3.8798275e-6 | -1.7965080e-7 | -3.7001767e-6 | 3.9157870e-6 |

Here the balance defect is

\[
 Q_L(T)-Q_L(0)-\int_0^T[j(L)-j(0)]\,dt.
\]

It is the discretization error after accounting for actual finite-boundary flux. The raw finite-interval charge is not exactly conserved because the Gaussian tails permit nonzero outer twist flux.

The fine-grid self-convergence orders from 256/512/1024 intervals are:

| Field | Observed order |
|---|---:|
| psi | 2.0000787771 |
| chi | 2.0007182375 |
| psi_T | 1.9975683806 |
| chi_T | 1.9984577214 |

Energy obeys the exact continuum balance law

\[
 \partial_T\gamma_R=\partial_R\gamma_T,\qquad
 \gamma_T=R(\psi_T\psi_R+e^{-2\psi}\chi_T\chi_R).
\]

At the finest `L=8` run, the integrated outer energy flux was approximately `-8.4584e-20`; the observed energy change is therefore numerical and converges quadratically. The final maximum `exp(gamma)` is `2.357971414359752`.

### Outer-radius check at matched grid spacing

To resolve the measured boundary-tail effect, the evolution was repeated at `L=12` with 384, 768, and 1536 intervals, matching the spacings of the `L=8` 256/512/1024 runs. On the finest extended run:

- Integrated outer twist flux: `-2.1108373304e-19`.
- Twist drift: `-3.7000255021e-6`.
- Relative energy drift: `3.9157870259e-6`.
- Initial twist tail outside the domain: `4.5874003372e-28`.

The finest `L=8` flux-corrected defect and the `L=12` raw drift agree to about `1.51e-10`. The residual temporal charge-integration error is about `5.26e-14`; spatial discretization dominates. This identifies the `L=8` discrepancy as a combination of a measured physical boundary flux and a convergent spatial error.

These runs verify classical numerical convergence and the correct conservation accounting. Exact conservation is the continuum identity above; finite-grid defects are reported quantitatively.

## E. Updated premise and verification ledger

| Item | Exact requirement or statement | Original status | Corrected/current status |
|---|---|---|---|
| Quotient Weyl frame | `h` is the literal quotient block in `g=h+rho M`, with calibrated orbit normalization | Omitted as a separate initial ledger premise; identified by v2.1 | Explicit in v2.2; operational probe construction in v2.3 and proved here |
| Derivative order | Polynomial total derivative order at most two for the four-function classification | Stated class; not selected by flatness | Retained explicitly; the specified `Lambda(rho)N^2` extension is removed by one curved Levi-Civita reference |
| Flat deformation blindness | `N=0` on all three flat references | Numerical/algebraic observation | Full Euler-Lagrange blindness proved exactly |
| Curved deformation discriminator | Levi-Civita with `c != 0,2` remains stationary | Conformal-equation argument in audit | Full metric, area, and shape residuals derived; arbitrary `Lambda(rho)` forced to zero |
| Global orbit sector | `A(infinity)-A(axis)=0` with regular axis and fixed periodicity | Original data have charge approximately -0.0131 | Exact continuum correction fixes zero charge |
| Corrected evolution | Evolve the corrected initial data with the same physical equations | v2.1 did not re-evolve | v2.2 did; current run reproduces all four archived grids exactly |
| Charge conservation | `dQ_L/dT=[j]_0^L`; infinity conserved if its boundary flux vanishes | Asymptotic conservation identified | Fresh flux-balanced tests separate outer flux and numerical error; second-order convergence verified |
| Quantum continuum | Additional mathematical construction beyond these local and classical results | Independent claim | Not used in the chart, deformation, or corrected-boundary proofs |

The machine-readable ledger is `premise_ledger_addendum.json`. Source hashes and fresh output receipts are included in that file and in `fresh_boundary/boundary_fresh_receipt.json`.
