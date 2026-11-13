# What Lean proves

The release contains **63 machine-checked theorem statements in nine Lean modules**: the 40 original theorems, eight version-1 residual theorems, and 15 version-2 extension certificates. A fresh build on November 13, 2026 completed with **zero warnings and zero errors**.

The full [execution receipt](../evidence/lean/receipt.json) records the source hashes, exact dependency revisions, compiled-object hashes, commands, and all 63 theorem names and axiom reports. The [build log](../evidence/lean/build.log) is retained.

## The central selection theorem

[`VossAnalyticBridge.complete_selection_positive`](../formal/AnalyticBridge.lean) assumes:

1. The three stated division-form chart equations hold for every positive pair $t,r$, with $\rho=tr$.
2. The labels $F_1,F_2$ are genuine derivatives: $F'=F_1$ and $F_1'=F_2$ at every $\rho>0$.
3. $W(\rho_0)>0$ at one positive area $\rho_0$.

It proves that there are common constants $a>0$ and $b$, valid throughout the positive-area domain, such that

```math
F(\rho)=a\rho+b,\qquad F'(\rho)=a,\qquad F''(\rho)=0,
```

```math
U(\rho)=\frac{a}{2\rho},\qquad W(\rho)=a\rho,\qquad V(\rho)=0.
```

The derivation of the chart equations from the action is supplied as a written variational proof with exact symbolic checks. Lean begins from those explicitly stated equations. It does not silently assume that arbitrary coefficient labels are derivatives: that connection is a separate, indispensable hypothesis in the formal theorem.

## Complete module inventory

| Module | Theorems | Formalized content |
|---|---:|---|
| [ThmA](../formal/ThmA.lean) | 6 | Chart algebra and converse, normalization, two cleared-residual bounds, power branches |
| [ThmABridge](../formal/ThmABridge.lean) | 7 | Division/cleared-equation equivalence and rational spectral identities |
| [AnalyticBridge](../formal/AnalyticBridge.lean) | 5 | Genuine derivative and connected-domain completion, positive normalization, constant odd coupling |
| [ChartGeometry](../formal/ChartGeometry.lean) | 5 | Minkowski tangent-vector pullback, orbit-area density, quotient block, diagonal signs |
| [Integrability](../formal/Integrability.lean) | 8 | Spectral-coefficient derivatives, Frobenius identity, harmonic/affine selector, continuous-axis normalization |
| [PremiseObstructions](../formal/PremiseObstructions.lean) | 4 | Exact witnesses showing why derivative, nonzero spectral, non-null area, and axis-continuity premises matter |
| [LaxCertificates](../formal/LaxCertificates.lean) | 5 | Scalar/matrix curvature identities, EOM equivalence, spectral-curve derivative and coefficients |
| [ResidualInversion](../formal/ResidualInversion.lean) | 8 | Four exact division-residual inversions and four pointwise error bounds; added in version 1.0 |
| [ExtensionCertificates](../formal/ExtensionCertificates.lean) | 15 | Helical and sourced selectors; response inverse; energy positivity, force identities, uncertainty bound |
| **Total** | **63** | **Nine modules** |

## Version-1 quantitative certificates

The residual module uses the five division-form residuals $e_1,\ldots,e_5$ defined explicitly in its source. If each residual satisfies $|e_i|\leq\varepsilon$, the formal proofs give

```math
|V|\leq2\varepsilon,\qquad
|\rho F_2|\leq\frac{8}{15}\varepsilon,
```

```math
\left|\frac{W}{\rho}-F_1\right|\leq\frac{25}{17}\varepsilon,
\qquad
|2\rho U-F_1|\leq\frac{31}{15}\varepsilon.
```

These are exact finite algebraic implications. Interpreting $F_1,F_2$ as derivatives requires the derivative assumptions above. Interpreting $\varepsilon$ as an experimental uncertainty requires a measurement protocol. The bounds quantify coefficient selection; they are not a proof of nonlinear dynamical stability. The intended physical use has $\rho>0$.

## Version-2 certificates

The new [extension module](../formal/ExtensionCertificates.lean) certifies 15 statements from the frozen extension formulas:

- Three helical inverse/selection/error results and a zero-pitch counterexample.
- Three dust–electrovac inverse/selection/error results.
- Two regular two-channel response inverse/error results.
- Two coordinate mismatch-energy positivity and zero-condition results.
- Four pure/general covariance force, shifted-energy, and uncertainty-bound results.

The [exact coverage ledger](../evidence/lean/extension_coverage.json) maps every theorem to its assumptions. The scalar residuals, transfer functions, coordinate energy, and force expressions are explicit definitions in these signatures. Their derivation from tensor variations and quantum operators is supplied by the written proofs and separate symbolic calculations. The compiler does not turn these algebraic certificates into a formal proof of the complete physical theory.

In particular, the band-leakage theorem, positive operator extension, conserved-current duality, full matter Ward identity, and field-reduction geometry remain analytic/symbolic results. No new mathematical axioms were introduced to represent them.

## Integrability: the precise formal boundary

Lean verifies the rational curvature and Frobenius identities, their nondegenerate algebraic consequences, and the real-calculus passage from a zero second derivative to an affine coefficient. The matrix curvature theorem is entrywise and allows an arbitrary matrix in the commutator position; it does not assume that the currents commute.

The local construction of the spectral parameter, the geometric interpretation of the currents, and the complete physical necessity/sufficiency argument remain written mathematical proofs supported by the symbolic verifier. Quantum-state reconstruction, the action-class assumptions, and the four-dimensional field-equation derivation are also outside these Lean signatures.

## Reproduction and trust

The project pins Lean **4.19.0** and Mathlib commit
`c44e0c8ee63ca166450922a373c7409c5d26b00b`. The fresh run used the published Mathlib dependency cache, then compiled all nine project modules from source. No historical project `.olean` objects were reused. The original seven proof-source files remain byte-identical to the supplied v2.4 files.

After preparing the pinned dependencies as described in [Reproducibility](REPRODUCIBILITY.md), run from the repository root:

```sh
python3 scripts/verify_lean.py --project formal --output work/lean
```

The verifier removes only the project's generated `formal/.lake/build` directory to force a fresh project build. It checks that every proof module is included in the Lake roots, every theorem has an axiom report, every actual report matches the source inventory, dependency checkouts match their pinned commits, and the proof build contains zero warnings and zero errors. It refuses proof placeholders, additional source axioms, selected trust overrides, and unexpected axiom dependencies.

Every theorem reports only the standard logical dependencies
`propext`, `Classical.choice`, and `Quot.sound`. There is no `sorryAx` or added mathematical axiom in the project proof dependencies. This is a statement about the exact formal signatures under Lean's usual kernel and imported-library trust model; it does not certify the physical assumptions or empirical applicability.

Two small controls make the verification behavior visible. Lean accepts
`example : (0 : Nat) = 0 := by decide` and rejects
`example : (0 : Nat) = 1 := by decide`. The latter produces the deliberate proof error recorded in the [negative-control log](../evidence/lean/negative_control.log); it is separate from the zero-error research proof build. A failed control makes the verifier fail.

The initial native Mathlib cache executable encountered a macOS loader incompatibility on this host. Running the same pinned cache program through Lean's interpreter completed successfully without changing proof sources or dependencies. This setup workaround is documented in the reproduction guide; it did not alter the subsequent proof build.
