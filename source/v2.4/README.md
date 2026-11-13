# Voss chart selection and integrability — verified supplement v2.4

This package closes the supplied chart-selection proof with an explicit first variation, genuine real-derivative hypotheses, a complete all-field converse, and a simultaneous physical realization. It also proves the independent rational Lax selector, sharpens the quadratic-curvature degeneracy, excludes an arbitrary coefficient function in the specified reduced four-derivative deformation, and re-evolves the corrected asymptotic-twist benchmark with boundary-flux accounting.

## Read the result

The main manuscript is `paper/Voss_Chart_Selection_Proof_v2_4.pdf`. Its source and generated result tables are in the same directory. Detailed derivations are retained in `notes/`.

The main coefficient conclusion is

\[
F(\rho)=a\rho+b,\qquad U(\rho)=\frac{a}{2\rho},\qquad W(\rho)=a\rho,\qquad V(\rho)=0,
\]

with constant odd coupling. Positive nondegenerate shape energy gives `a > 0`. All constants apply to the same connected positive domain and the same action.

The integrability conclusion is the exact identity

\[
\mathcal F=\frac{\mathsf{MC}-s\mathcal E}{1-s^2},\qquad
\partial_-\partial_+s-\partial_+\partial_-s=
\frac{4s^2}{1-s^2}\frac{W_{+-}}W.
\]

The manuscript states the regular spectral branch, generic-current requirement, harmonic-area premise, non-null coverage, and shrinking-axis condition explicitly.

## Reproduce the mathematical verification

The reference environment is Python 3.12.14. Install the exact scientific dependencies and run the suite:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_all.py
```

This runs five independently inspectable programs and writes current receipts and logs to `evidence/`:

| Program | Verification |
|---|---|
| `verify_variation.py` | First variation, exact chart equations, all-field converse, generic off-shell four-dimensional curvature identity |
| `verify_physical_premises.py` | Common physical witness, all Riemann components, covariance and probe identities |
| `verify_integrability_complete.py` | Full Lax curvature identity, Frobenius obstruction, spectral curve, noncommuting rational current jets |
| `verify_levi_civita_deformation.py` | Generic metric variation of the deformation and exact curved Levi-Civita residuals |
| `verify_boundary_fresh.py` | Seven corrected nonlinear evolutions, all-field convergence, energy and twist boundary-flux balance |

The nonlinear verifier imports the unchanged historical PDE implementation in `reference/pde_repro.py`, applies the single continuum initial-data correction, and adds diagnostics. Its source hash is recorded. The historical v2.2 comparison values are separate reference data, never inputs to the evolution.

## Compile the formal proofs

The `lean/` directory is a portable Lake project pinned to Lean 4.19.0 and the exact mathlib revision recorded in its configuration and receipt. With Lean's `elan` toolchain manager available:

```bash
cd lean
lake update
lake exe cache get
lake build
```

Warnings are treated as errors. The build prints the axiom dependencies of every theorem. The receipt records the executed compiler version, commands, exit codes, source hashes, and printed dependencies.

The variational and differential-geometric derivations are written mathematical proofs audited by exact symbolic calculations. The Lean modules certify the explicit algebraic, geometric-component, calculus, and integrability implications stated in their theorem signatures. Their assumptions remain visible in those signatures; the receipt does not replace them.

## Physical inputs and boundary conditions

The local Lorentzian quotient, two spacelike symmetry directions, common frame representation, local derivative-order class, vacuum calibration, radiative positivity, and calibrated minimal probe coupling are explicit physical hypotheses. The package constructs compatible exact local and cylindrical witnesses for one selected action. Experimental applicability is represented as an operational premise, rather than inferred from synthetic computation.

The literal quotient Weyl frame and the zero asymptotic-twist boundary sector are explicit ledger entries. The local Milne boost-orbit calibration and cylindrical scattering evolution are distinct configurations of the same selected action. Constant curvature and odd couplings are bulk-null under compactly supported variations; global boundary functionals require their declared boundary completion.

## Provenance

`reference/input_manifest.json` records the names, byte sizes, and SHA-256 hashes of all ten supplied inputs. The original standalone theorem files are preserved in `reference/input_ThmA.lean` and `reference/input_ThmABridge.lean`. The principal historical sources are the supplied v2.0 manuscript, v2.1 audit, v2.2 foundations supplement, and v2.3 verification bundle. The final manuscript cites the primary literature used for the reduction, quadratic gravity, and local-coupling integrability.

`claim_ledger_v2_4.json` and the execution receipts distinguish analytic proof, Lean kernel verification, exact symbolic verification, synthetic numerical convergence, and physical input. `SHA256SUMS` covers the distributed files.
