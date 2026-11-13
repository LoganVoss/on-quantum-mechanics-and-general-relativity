# Reproduce the research

The bundle contains the source arguments, executable checks, formal proofs, and recorded results. A fresh run writes to a separate output directory so the distributed evidence remains available for comparison.

Run the commands below from the repository root. The fresh scientific verification used **Python 3.12.13**, **SymPy 1.14.0**, **NumPy 2.3.5**, and **SciPy 1.17.0**. The original v2.4 reference receipt reports Python 3.12.14; the two executions are recorded separately.

## Scientific checks

Create a local environment and install the pinned scientific dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the full scientific verification:

```bash
python scripts/reproduce.py --output-dir work/reproduction
```

This entry point runs the original symbolic and nonlinear suite, the quantum-geometry and coefficient-robustness checks, and the independent numerical controls. Read the generated receipts and process exit status. A historical `PASS` file is not a substitute for a new execution.

The original suite in [`source/v2.4`](../source/v2.4/) is executed in a temporary copy. Its wrapper preserves the original scripts and reference inputs, records their hashes, and applies a 120-second timeout to each source program. Scientific outputs include:

- JSON receipts identifying the calculations, environment, result, and source hashes.
- Text logs for the executed source programs.
- CSV tables for benchmark balance, exact-solution errors, and timestep refinement.
- Compressed NumPy state arrays containing the evolved fields and, for the analytic controls, their exact counterparts.

The fixed tests are intentionally bounded. The nonlinear benchmark ends at $T=0.8$; its largest grid has 1,536 intervals. The exact-solution controls use 64, 128, 256, and 512 intervals. The rational current-jet test uses a declared seed. No experimental data or fitted observational parameters are required.

## Formal proofs

Install Lean's `elan` toolchain manager if it is not already available. The project pins **Lean 4.19.0** and a specific mathlib revision. Fetch the declared dependencies and their compiled cache:

```bash
cd formal
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update
lake exe cache get Mathlib.Analysis.SpecialFunctions.Pow.Real Mathlib.Analysis.SpecialFunctions.Sqrt Mathlib.Tactic.LinearCombination Mathlib.Tactic.Positivity Mathlib.Tactic.Linarith Mathlib.Tactic.FieldSimp Mathlib.Analysis.Calculus.MeanValue Mathlib.Data.Complex.Trigonometric Mathlib.Analysis.Calculus.Deriv.Inv Mathlib.Data.Matrix.Basic
cd ..
```

This requests the transitive cache needed by this project's imports. On the audited macOS host, the native cache executable encountered an `SG_READ_ONLY` loader error. Running the same cache code through Lean's interpreter succeeded. If that native-loader issue occurs, use this verified fallback from the repository root:

```bash
cd formal
lake build cache
lake env lean --run .lake/packages/mathlib/Cache/Main.lean get Mathlib.Analysis.SpecialFunctions.Pow.Real Mathlib.Analysis.SpecialFunctions.Sqrt Mathlib.Tactic.LinearCombination Mathlib.Tactic.Positivity Mathlib.Tactic.Linarith Mathlib.Tactic.FieldSimp Mathlib.Analysis.Calculus.MeanValue Mathlib.Data.Complex.Trigonometric Mathlib.Analysis.Calculus.Deriv.Inv Mathlib.Data.Matrix.Basic
cd ..
```

Then invoke the formal verifier from the repository root:

```bash
python scripts/verify_lean.py --project formal --output work/lean
```

The verifier rebuilds the formal project, checks all 48 expected theorem declarations and their axiom dependencies, and tests a positive and a deliberately false compiler control. **Warnings are errors**: a successful formal receipt requires a warning-free build. The dependency cache speeds up compilation; the project's theorem sources still undergo verification. The distributed [formal receipt](../evidence/lean/receipt.json) and [build log](../evidence/lean/build.log) record the completed eight-module build.

After dependency setup, the combined entry point can run both scientific and formal checks:

```bash
python scripts/reproduce.py --output-dir work/reproduction --lean
```

Fetching the Lean toolchain, mathlib, and cache requires network access on a new machine. Subsequent verification uses the installed dependencies. Read the formal receipt for the exact toolchain, mathlib commit, commands, and dependency reports rather than relying on a prose description alone.

## Research figure

The figure is generated from the recorded fidelity quadratures and nonlinear exact-solution error table. To rebuild its high-resolution PNG and vector PDF:

```bash
python -m pip install -r requirements-figures.txt
python scripts/make_figures.py
```

The figure's receipt records input and output hashes. The $N^{-2}$ reference line is offset for readability and is not a fitted result. Two of the five quadrature points overlap near zero distance; all five are preserved in the companion CSV.

## Reading a result correctly

To rebuild the typeset paper, install [Tectonic](https://tectonic-typesetting.github.io/) and run `python scripts/build_paper.py --output-dir work/paper`. The compiler may download TeX resources on its first use. The script rejects final-pass warnings and box-layout issues; visually inspect the resulting PDF as well. The distributed paper was rendered and reviewed on all 12 pages.

Exact symbolic simplification and rational arithmetic test identities without a floating-point tolerance. Wavefunction quadrature and PDE evolution use numerical tolerances and convergence checks. Lean checks propositions with their explicit hypotheses. These evidence types answer different questions.

For the nonlinear benchmark, inspect the boundary-flux terms together with the energy and twist changes. Finite-grid drift is expected and measured. A smaller residual on successive grids supports convergence; it is not exact conservation on those grids.

For timestep refinement, the receipt preserves the unsuccessful coarse regime alongside the successful finer regime. Reproducing the coarse order near 1.2621 is expected; the fourth-order acceptance check applies to the finer sequence with observed order near 3.9291.

Small differences in floating-point diagnostics can arise across platforms. Compare against the stated tolerances and convergence behavior. Source hashes, pinned dependency versions, exact symbolic identities, and formal theorem statements supply the more precise reproducibility anchors.

The [verification guide](VERIFICATION.md) maps each result to its evidence and scope. The [quantum-geometry](QUANTUM_GEOMETRY.md) and [robust-selection](ROBUST_SELECTION.md) notes give the new formulas and their assumptions. The strongest conclusions are conditional mathematical results within the declared model; the numerical runs support finite-time behavior for the recorded tests.
