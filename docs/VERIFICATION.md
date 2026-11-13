# What has been verified

The central result is a conditional selection theorem: within the stated action class and geometric dictionary, independent first variation on the calibration chart selects the coefficient family. The quantum connection identifies an exact common geometry for a specified class of Gaussian states and the gravitational shape field. Each part has evidence matched to the claim it supports.

“Stationary” means that the first variation vanishes. It does not by itself mean a positive second variation, stability under every perturbation, or global existence of the evolution.

## Evidence at a glance

| Layer | Fresh result | What it establishes |
|---|---|---|
| Analytic derivation | Explicit hypotheses, first variation, converse, and geometric dictionary | The mathematical argument and its domain |
| Formal proofs | 48 theorem declarations across eight Lean proof modules | The original 40 statements plus eight new residual-inference lemmas, with hypotheses visible in their signatures |
| Original symbolic suite | 373 exact symbolic checks and 256 exact rational current-jet cases passed | Reproducible algebraic and component checks of the written derivations |
| Quantum geometry and coefficient robustness | 58 exact symbolic checks and five direct wavefunction quadratures passed | Exact identities, sharp pointwise residual bounds, and an independent numerical check of Gaussian fidelity |
| Nonlinear benchmark | Seven fresh finite-domain evolutions passed | Convergence and energy/twist balance for the specified initial data through $T=0.8$ |
| Independent numerical controls | Exact linear and nonlinear solution tests, plus timestep refinement, passed | Solver accuracy against an analytic oracle and temporal convergence in a resolved regime |
| Physical applicability | Explicit operational assumptions | A model contract to test; the bundle contains no experimental measurements |

Check counts describe executed calculations. Several are tensor components or special cases; their number is not a count of independent physical discoveries.

## Formal verification and its boundary

The original **40 theorems are in seven modules**, rather than 40 modules. This bundle adds a module containing **four exact residual-inversion identities and four pointwise error bounds**, for **48 theorem declarations across eight proof modules**. The integrated near-affine estimates are established by the written calculus argument; these eight new formal lemmas certify its pointwise algebraic foundation.

The fresh build uses Lean 4.19.0 and mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Compiler warnings are errors. The complete build finished with **zero warnings and zero errors**. All 48 theorem dependency reports contain only `propext`, `Classical.choice`, and `Quot.sound`, the standard logical foundations used by these Lean proofs. The [formal receipt](../evidence/lean/receipt.json) and [build log](../evidence/lean/build.log) record the execution.

The formal verifier also checks its own route through the compiler: a true proposition must compile, and the deliberately false proposition `example : (0 : Nat) = 1 := by decide` must be rejected. These controls increase confidence that the recorded command actually invokes a working checker. They are not a proof that the compiler or host system is uncompromised.

The theorem signatures remain the authoritative statement of what Lean proves. In particular, the analytic bridge starts from explicit chart equations and genuine derivative hypotheses. The full differential-geometric variation and physical interpretation have written arguments and exact symbolic checks; they are not all formalized inside Lean.

## Exact symbolic evidence

The [fresh source-suite receipt](../evidence/source_suite/python_suite_receipt.json) records the executed scripts, source hashes, and exit codes. Its four symbolic programs report:

| Calculation | Exact checks |
|---|---:|
| First variation and reduction identities | 29 |
| Physical-model realization, including 256 Riemann components | 276 |
| Integrability identities | 32 |
| Reduced deformation and curved reference | 36 |
| **Total** | **373** |

The integrability program separately checks **256 exact rational, noncommuting current jets**. Symbolic zero residuals use exact expressions; these results are distinct from floating-point values that happen to be small.

The [quantum-geometry receipt](../evidence/quantum_geometry/quantum_geometry_receipt.json) adds **58 exact symbolic checks** and **five numerical overlap integrals**, with maximum observed absolute fidelity discrepancy $2.23\times10^{-16}$ after rounding upward. The quadratures use declared finite test cases and tolerances. The analytic Gaussian integral establishes the identity; the quadratures provide an independent computational check.

The new checks include a useful failure of overgeneralization: the oscillator vacuum and first excited state have the same normalized covariance shape but zero overlap. The exact shape–fidelity correspondence requires the centered, pure, uncertainty-saturating Gaussian domain. See [Quantum geometry](QUANTUM_GEOMETRY.md) and [Robust coefficient selection](ROBUST_SELECTION.md) for the complete formulas and assumptions.

## The nonlinear benchmark

The original solver evolves the four fields $(\psi,\chi,\psi_T,\chi_T)$ using second-order radial differences and fourth-order Runge–Kutta time integration. The fresh runs use outer radii $L=8$ and $L=12$, with up to 1,536 intervals, and end at $T=0.8$ in the model's dimensionless coordinates. Outer field values are frozen; the axis uses the regular radial limit.

The initial twist correction uses one continuum coefficient on every grid:

$$
\chi_T(R)\longmapsto\chi_T(R)
+c_\star e^{-(R/1.2)^2},
\qquad c_\star\approx0.052781957547848805.
$$

Its defining integral cancels the continuum initial twist exactly. The quadrature evaluation is approximately $1.45\times10^{-18}$; discrete-grid twist remains nonzero and is reported rather than relabeled exact conservation.

The finite-domain identities being tested are

$$
\frac{d}{dT}\int_0^L R e^{-2\psi}\chi_T\,dR
=\left[R e^{-2\psi}\chi_R\right]_0^L,
$$

$$
\frac{d\gamma(L)}{dT}
=\left[R\left(\psi_T\psi_R+e^{-2\psi}\chi_T\chi_R\right)\right]_0^L.
$$

The fresh results show:

- All-field spatial convergence orders from **1.9914 to 2.0028**.
- Finest-grid relative energy drift of approximately **$3.916\times10^{-6}$**.
- Energy and twist balance defects converging at approximately second order after accounting for outer flux.
- Finite saved states and nondecreasing accumulated energy on every grid.
- Historical comparison values reproduced within **$8.9\times10^{-16}$**.

The $L=8$ outer twist flux is small but nonzero. Increasing the radius to $L=12$ at matched spatial spacings makes the outer-tail contribution much smaller. This separates boundary effects from spatial discretization error.

Inspect the [full benchmark receipt](../evidence/source_suite/boundary/boundary_fresh_receipt.json), [CSV](../evidence/source_suite/boundary/boundary_fresh_convergence.csv), and [additional state and balance checks](../evidence/source_suite/additional_boundary_checks.json). These are finite-time tests of one nonlinear benchmark, not a theorem of global stability or arbitrary-data evolution.

## An exact nonlinear solution as an independent control

An analytic solution provides a stronger solver test than comparing successive grids alone. Let

$$
f(T,R)=A J_0(kR)\cos(kT),\qquad J_0(kL)=0,
$$

where $J_0$ is the order-zero Bessel function. It solves the regular radial wave equation. The target-geodesic map

$$
\boxed{\psi=-\log\cosh f,\qquad\chi=\tanh f}
$$

then solves both nonlinear field equations exactly. With primes denoting derivatives with respect to $f$,

$$
\psi''+e^{-2\psi}(\chi')^2=0,
\qquad \chi''-2\psi'\chi'=0,
\qquad (\psi')^2+e^{-2\psi}(\chi')^2=1.
$$

The last identity says that the nonlinear solution has the same energy density as its generating scalar wave. It is a useful exact family within the model, obtained by a standard target-geodesic construction; no claim of historical priority is made.

At $A=1.6$, $L=8$, and $T=0.8$, four grids from 64 to 512 intervals recover the exact nonlinear solution with approximately second-order convergence. The finest maximum error across all four evolved fields is **$4.087\times10^{-7}$** after rounding upward; the finest observed order is **1.9994**. A separate linear Bessel control passes as well. This exact family has commuting currents, so it complements the generic nonlinear benchmark without replacing it.

## A retained timestep limitation

On the fixed 128-interval nonlinear benchmark grid, timesteps $0.01$, $0.005$, and $0.0025$ give an observed temporal order of **3.9291**, consistent with the fourth-order scheme.

The exploratory coarser sequence $0.04$, $0.02$, and $0.01$ gave **1.2621**. It did **not** establish fourth-order convergence in that regime. Both sequences are retained in the [control receipt](../evidence/numerical_controls/independent_controls_receipt.json) and [timestep CSV](../evidence/numerical_controls/time_refinement.csv). The accepted result is confined to the finer tested regime.

The complete exact-solution comparison data are in [this CSV](../evidence/numerical_controls/exact_solution_errors.csv), alongside the numerical and exact state arrays. Follow [Reproducibility](REPRODUCIBILITY.md) to regenerate the evidence.
