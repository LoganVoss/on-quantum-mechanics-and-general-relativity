# What Lean proves

The release contains **75 machine-checked theorem statements in ten Lean modules**: the 40 original theorems, eight version-1 residual theorems, 15 version-2 extension certificates, and 12 version-3 continuum-estimate certificates. A fresh build on November 13, 2026 completed with **zero warnings and zero errors**. The previous 63 theorem sources remain unchanged.

The full [execution receipt](../evidence/lean/receipt.json) records the source hashes, exact dependency revisions, compiled-object hashes, commands, and all 75 theorem names and axiom reports. The [build log](../evidence/lean/build.log) is retained.

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
| [ContinuumCertificates](../formal/ContinuumCertificates.lean) | 12 | Genuine-derivative Gronwall; scalar Casimir implications; quadratic-current bounds; population/kernel diagonal; positive-mass clock algebra |
| **Total** | **75** | **Ten modules** |

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

The version-2 [extension module](../formal/ExtensionCertificates.lean) certifies 15 statements from the frozen extension formulas:

- Three helical inverse/selection/error results and a zero-pitch counterexample.
- Three dust–electrovac inverse/selection/error results.
- Two regular two-channel response inverse/error results.
- Two coordinate mismatch-energy positivity and zero-condition results.
- Four pure/general covariance force, shifted-energy, and uncertainty-bound results.

The [exact coverage ledger](../evidence/lean/extension_coverage.json) maps every theorem to its assumptions. The scalar residuals, transfer functions, coordinate energy, and force expressions are explicit definitions in these signatures. Their derivation from tensor variations and quantum operators is supplied by the written proofs and separate symbolic calculations. The compiler does not turn these algebraic certificates into a formal proof of the complete physical theory.

In particular, the band-leakage theorem, positive operator extension, conserved-current duality, full matter Ward identity, and field-reduction geometry remain analytic/symbolic results. No new mathematical axioms were introduced to represent them.

## Version-3 continuum-estimate certificates

The [continuum module](../formal/ContinuumCertificates.lean) adds 12 mathematical certificates. The [coverage ledger](../evidence/lean/continuum_coverage.json) records their exact assumptions and the preceding results that remain outside Lean.

**Three differential-comparison certificates.** Young's inequality closes the specified squared-deviation estimate. A genuine right-derivative Gronwall theorem then proves

```math
D'(t)\le CD(t)+\frac{B}{N^2}
\quad\Longrightarrow\quad
D(t)\le e^{Ct}\left[D(0)+\frac{Bt}{N^2}\right]
\qquad(0\le t\le T).
```

The signature requires $C,B\ge0$, $N>0$, continuity on $[0,T]$, and the stated right derivatives and inequality on $[0,T)$. This is an analytic comparison using Mathlib's Gronwall theorem. Deriving the differential inequality from quantum operators remains a separate written proof. The signature also does not replace the upper-Dini-derivative argument for the material maximum error.

**Two scalar consequences of the Casimir relation.** Given

```math
S=2\beta+\frac{d-1}{N},\qquad
\beta\ge0,\quad d\ge1,\quad N>0,
```

Lean proves $\beta\le S/2$ and combines a supplied marginal-error estimate $e\le2\sqrt{k\beta}$ with $k\ge0$ to give $e\le\sqrt{2kS}$. The symmetric-sector operator identity, density matrices, and pure-target trace-distance estimate are not represented by these scalar theorems. Their physical marginal application also requires $k\le N$ in the external density-operator argument.

**Two quadratic-current error bounds.** Alongside the scalar-square estimate, a theorem on a real inner-product space proves, for any bounded real linear map $A$,

```math
\|x-y\|\le\delta,\quad\delta\ge0
\quad\Longrightarrow\quad
|\langle x,Ax\rangle-\langle y,Ay\rangle|
\le\|A\|\,\delta(2\|y\|+\delta).
```

This includes bounded indefinite metric contractions; $A$ need not be positive. The result applies in particular to real Hilbert spaces. Establishing the preceding operator-current/kernel RMS estimate and identifying the physical contact observable remain external obligations.

**Four explicit diagonal certificates.** With $0<s\le1$, $h=s^5$, $\eta=s^2$, and positive $N$, the condition $N\ge A^2/s^{26}$ gives

```math
\delta\le\frac{A}{\sqrt{Nh^2}}
\quad\Longrightarrow\quad\delta\le s^8
\qquad(A\ge0).
```

Exact power identities then bound the sum of the normalized bias, quadrature, path, and amplitude terms by $4s^4$. The rounding estimate is

```math
\frac1{Nh^2\eta}\le s^{14}\le s^4,
```

with the additional explicit condition $A\ge1$. Kernel, material, cutoff, and time-dependent constants multiply these scalar estimates separately. These certificates do not assert that such constants remain uniform when cutoffs are removed.

**One positive-mass clock certificate.** For $m_0>0$, nonnegative internal energy $e$, and nonnegative squared momentum $p^2$, Lean proves positivity of $E=\sqrt{p^2+(m_0+e)^2}$, the clock bound $0<(m_0+e)/E\le1$, and the corresponding scalar Legendre identity. Quantum mass averaging and the worldline-to-fluid variational equivalence are separate derivations.

These twelve results provide checked links in the controlled-limit argument. They do not formalize the bounded-operator square-root theorem, the nonlinear material quadrature theorem, oscillator-cutoff removal, spatial field estimates, or Einstein constraints. In particular, they do not prove removal of the full nonlinear geometric cutoff or a fixed-coupling quantum-gravity continuum.

## Integrability: the precise formal boundary

Lean verifies the rational curvature and Frobenius identities, their nondegenerate algebraic consequences, and the real-calculus passage from a zero second derivative to an affine coefficient. The matrix curvature theorem is entrywise and allows an arbitrary matrix in the commutator position; it does not assume that the currents commute.

The local construction of the spectral parameter, the geometric interpretation of the currents, and the complete physical necessity/sufficiency argument remain written mathematical proofs supported by the symbolic verifier. Quantum-state reconstruction, the action-class assumptions, and the four-dimensional field-equation derivation are also outside these Lean signatures.

## Reproduction and trust

The project pins Lean **4.19.0** and Mathlib commit
`c44e0c8ee63ca166450922a373c7409c5d26b00b`. The fresh run used the published Mathlib dependency cache, then compiled all ten project modules from source. No historical project `.olean` objects were reused. The original seven proof-source files remain byte-identical to the supplied v2.4 files.

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
