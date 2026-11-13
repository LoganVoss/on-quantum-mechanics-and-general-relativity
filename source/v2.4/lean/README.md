# Voss chart-selection and integrability certificates

## Verified result

`VossAnalyticBridge.complete_selection` is one simultaneous theorem. Its inputs are
all three division-form chart Euler-Lagrange equations on the positive Milne-polar
chart, `HasDerivAt F (F1 rho) rho`, and `HasDerivAt F1 (F2 rho) rho` for every
`rho > 0`. Its conclusion provides one common pair of real constants `a,b` such that

- `F rho = a*rho+b`;
- `F1 rho = a` and `F2 rho = 0`;
- `U rho = a/(2*rho)`;
- `W rho = a*rho`;
- `V rho = 0`.

`complete_selection_positive` adds `a > 0` from `W rho0 > 0` at one positive area.
The proof uses the connected interval `(0,infinity)` and genuine derivatives;
continuity of the second derivative is not needed.

## Modules

| Module | Verified statements |
| --- | --- |
| `ThmA.lean` | Chart algebra, converse, normalization, sharp residual bounds, power branches |
| `ThmABridge.lean` | Exact division/cleared-equation equivalence and Lax coefficient identities |
| `AnalyticBridge.lean` | Zero derivative implies constant; affine F; simultaneous chart selector; positive normalization; constant odd coupling |
| `ChartGeometry.lean` | Minkowski pullback, positive orbit area, literal quotient block, Lorentzian diagonal signs |
| `Integrability.lean` | Genuine derivatives of spectral coefficients, Frobenius identity, harmonic W, affine W, continuous-axis normalization |
| `PremiseObstructions.lean` | Four exact witnesses distinguishing the derivative, spectral, non-null-area, and axis-continuity premises |
| `LaxCertificates.lean` | Scalar and arbitrary-matrix curvature decomposition, EOM equivalence, spectral-curve derivative and conservation coefficients |

The accompanying analytic derivation establishes the first variation of the action,
its chart evaluation, and the physical action-class premises. These Lean modules
establish the stated algebraic, geometric, and analytic certificates with explicit
hypotheses. The matrix curvature proof keeps the commutator as an arbitrary matrix;
it makes no commutativity assumption about the currents.

## Reproduce

Install Lean through elan, then run from this folder:

```sh
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update
lake exe cache get Mathlib.Analysis.SpecialFunctions.Pow.Real Mathlib.Analysis.SpecialFunctions.Sqrt Mathlib.Tactic.LinearCombination Mathlib.Tactic.Positivity Mathlib.Tactic.Linarith Mathlib.Tactic.FieldSimp Mathlib.Analysis.Calculus.MeanValue Mathlib.Data.Complex.Trigonometric Mathlib.Analysis.Calculus.Deriv.Inv Mathlib.Data.Matrix.Basic
lake build
```

The `lean-toolchain` and `lakefile.lean` pin Lean 4.19.0 and Mathlib commit
`c44e0c8ee63ca166450922a373c7409c5d26b00b`. Warnings are treated as errors.
Every theorem is followed by an axiom report. The accepted logical dependencies are
`propext`, `Classical.choice`, and `Quot.sound`; there are no proof placeholders or
additional mathematical axioms in these modules.

`build_receipt.json` records the actual build result, source SHA-256 values,
compiled object SHA-256 values, toolchain, and theorem count. `build.log` contains
the compiler's complete successful theorem-axiom output.
