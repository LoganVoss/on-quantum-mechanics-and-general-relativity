# Provenance and version boundaries

This is **On Quantum Mechanics and General Relativity**, research edition 3.0, November 13, 2026, by Logan Voss. The [version 1.0 release](https://github.com/LoganVoss/on-quantum-mechanics-and-general-relativity/releases/tag/v1.0.0) preserves the foundation unchanged. The latest preserved edition-2 package is [v2.0.1](https://github.com/LoganVoss/on-quantum-mechanics-and-general-relativity/releases/tag/v2.0.1), which adds a CI-only patch to v2.0.0. Edition 2.0 added the selected reciprocal interaction, one-Killing inverse calibration, current-corrected matter construction, and source-conditioned quadratic-curvature discrimination. Edition 3.0 adds a controlled matter-sector continuum for an explicitly augmented large-population family, plus a separate linearized spatial-continuum theorem. The nonlinear geometric cutoff and Einstein constraints remain open.

## Preserved foundation

The principal supplied foundation is the November 12 v2.4 chart-selection supplement. The earlier v2.3 archive was recovered from the author's prior research conversation and matched the SHA-256 already recorded in the v2.4 input manifest:

```text
d6579e52193d1307a016c53fedb65289803e68bcd795803b7c80033ea23d684f
```

| Location | Identity and status |
| --- | --- |
| [Original v2.4 package](../source/v2.4/) | Preserved manuscript, notes, scripts, Lean files, historical compiled objects and receipts. Its original `SHA256SUMS` remains intact. |
| [Recovered v2.3 archive](../archive/voss-verification-v2.3-original.zip) | Byte-identical earlier archive containing the v2.0/v2.1 manuscripts and v2.2/v2.3 lineage. Earlier claims and blocked-build notices remain historical; the entire archive was not rerun for this release. |
| [Foundation scientific evidence](../evidence/source_suite/) | Executed foundation checks, stored separately from the original source snapshot. |
| [Preserved edition-1.0 formal evidence](../evidence/baseline_v1/lean/) | The 48-theorem, eight-module build receipt, logs and controls retained before replacing the current formal receipt with the enlarged build. |
| [Quantum-geometry evidence](../evidence/quantum_geometry/) | Independent exact algebra and wavefunction-quadrature checks from the foundation edition. |
| [Numerical controls](../evidence/numerical_controls/) | Independent exact-solution and timestep controls, including the retained coarse-regime limitation. |
| [Foundation phase record](../evidence/phase_freeze.json) | Records completion of foundation derivations before its public authoring. |
| [Foundation independent review](../evidence/independent_review.md) | Separately tasked mathematical review retained as an audit record. |

The original input manifest lists ten earlier inputs. A manifest entry establishes an identified source, not a fresh reproduction of its contents. Current claims point to their actual proofs and executions in [the claim ledger](../CLAIMS.json) and [verification guide](VERIFICATION.md).

## Extension inputs, solving and independent review

A supplied research review motivated the new questions and supplied two Hessian-response controls. Its titles, byte sizes and hashes are recorded in [the review-input manifest](../evidence/extensions/review_input_manifest.json). Its raw contents are not redistributed, and its reported calculations are distinct from this release's fresh checks. It is not presented as external peer review.

All extension derivations and the bounded independent review were completed before public extension authoring. The [extension freeze record](../evidence/extensions/frozen/extensions_freeze.json) identifies the frozen proofs, calculation sources, review and formal module. It records the unchanged foundation commit `bf67ebc131901e1542f932664b5eb5e25789216e` as its baseline. The frozen research records remain available for the [dynamical coupling](../evidence/extensions/frozen/DYNAMICS_FROZEN.md), [one-Killing extension](../evidence/extensions/frozen/FROZEN_ONE_KILLING_FINDINGS.md), and [quadratic-curvature response](../evidence/extensions/frozen/FROZEN_CURVATURE_FINDINGS.md).

The [independent extension review](../evidence/extensions/review/REVIEW.md) used separately implemented calculations and produced [31 exact checks](../evidence/extensions/review/receipt.json). It directly varied the Ricci-squared density and rederived selected projection, helical and current-duality identities. It did not import the proposed verifier implementations or reproduce every finite-regulator calculation.

That review identified an observable-domain gap in the proposed continuum directional response. The final theorem uses a bounded smooth observable $O=\zeta(r)X_1$, equal to $X_1$ near the initial compact packet's support. The correction preserves the exact initial response coefficient without assuming later-time finiteness of an unbounded moment. The repaired statement was confirmed before the extension freeze. The finite-grid observable was already bounded.

The independent pass was AI-assisted work assigned separately within this research workflow. It is not external replication, external peer review, or a certification of worldwide priority.

## Edition-2.0 extension evidence retained

| Location | Retained extension evidence |
| --- | --- |
| [Edition-2.0 formal receipt](../evidence/baseline_v2/lean/receipt.json) | The 63-theorem, nine-module build is preserved separately. Its proof sources are retained in the enlarged current project. |
| [Current Lean receipt](../evidence/lean/receipt.json) | Enlarged clean 75-theorem build with zero warnings and errors, axiom reports, pinned dependencies, and separate true/false proposition controls. |
| [Extension formal module](../formal/ExtensionCertificates.lean) | Fifteen algebraic certificates for helical residuals, sourced coefficient inverses, transfer-response inverses, and energy/force identities and bounds. |
| [Dynamics receipt](../evidence/extensions/dynamics/dynamical_extension_receipt.json) | 41 exact checks, positive 512-/768-dimensional quantum regulators, Fock-cutoff comparison, and a separate reciprocal variational-cell evolution. |
| [One-Killing receipt](../evidence/extensions/one_killing/one_killing_receipt.json) | 309 exact checks of the helical calibration, flat lift, response inverse and old cylindrical sector. |
| [Generic reduction receipt](../evidence/extensions/one_killing/generic_reduction_receipt.json) | Fifteen exact checks of the off-shell reduction, current-corrected dual action and source obstruction. |
| [Curvature-response receipt](../evidence/extensions/curvature/curvature_response_receipt.json) | 88 exact symbolic identities and finite inverse controls for the specified quadratic response class. |
| [Sourced-calibration receipt](../evidence/extensions/curvature/sourced_calibration_receipt.json) | 73 exact checks of the dust/electrovac discriminator and coefficient inverse. |
| [Independent radial variation](../evidence/extensions/independent_rn/independent_rn_receipt.json) | Separate variation of the raw Ricci-squared action's lapse equation on the charged reference geometry. |
| [Ground-band receipt](../evidence/extensions/projection/projection_receipt.json) | Thirteen exact projection, factorization, packet and initial-leakage checks. |
| [Portable extension sources](../scripts/extension_checks/) | Inspectable calculation programs rerun by the [extension runner](../scripts/verify_extensions.py). |

Counts refer to declarations or checked identities/components, not independent physical discoveries. The original formal package contained 40 theorems in seven modules; edition 1.0 contained 48 in eight; edition 2.0 contained 63 in nine; edition 3.0 contains 75 in ten. The added Lean statements certify their explicit algebraic assumptions. Full tensor variations, Gaussian reconstruction, closed-operator arguments, fluid variations and continuum interpretations retain separate analytic or computational status.

## Edition-3.0 continuum freeze and evidence

The [global continuum freeze](../evidence/continuum/frozen/continuum_global_freeze.json) records completion of the new derivations, controls and independent review before public continuum authoring. Its local date is November 13, 2026; the UTC timestamp falls on November 14. It identifies the unchanged edition-2.0 baseline commit `bc1a63feffc206dbb682dd78f44f977025b0c2ba`, frozen source hashes, the main endpoint and the outstanding obligations.

The [frozen synthesis](../evidence/continuum/frozen/SYNTHESIS.md) combines the population, material, current and ordered-cutoff arguments. The main endpoint keeps finite geometric and internal cutoffs, prescribes a smooth $h_3$, and works before caustics. Full oscillator removal is an ordered corollary with a common regular interval and higher-moment assumptions. The separate spatial theorem concerns the quadratic/linearized sector on an exact Einstein-dust background.

| Location | Edition-3.0 evidence and scope |
| --- | --- |
| [Continuum certificates](../formal/ContinuumCertificates.lean) | Twelve added theorems for scalar differential comparison, Casimir-bound composition, quadratic-current error and explicit diagonal bookkeeping. They do not formalize the full operator or continuum construction. |
| [Mean-field receipt](../evidence/continuum/meanfield/meanfield_receipt.json) | 164 exact checks and finite clock, preparation, root/source, coherence and partial-trace controls. |
| [Field/material receipt](../evidence/continuum/field/field_continuum_receipt.json) | 92 exact checks, reciprocal material quadrature, strong current/contact controls, internal cutoff and linearized spatial controls. |
| [Moving-parcel receipt](../evidence/continuum/moving_parcels/moving_parcels_receipt.json) | Bounded coupled transport calculations with reference and tolerance comparisons. |
| [Obstruction receipt](../evidence/continuum/obstructions/obstruction_receipt.json) | 28 exact checks, three Fock controls and five collective-mass controls. |
| [Synthesis receipt](../evidence/continuum/synthesis/synthesis_receipt.json) | Ten exact identities checking the stated parameter balances. |
| [Independent continuum review](../evidence/continuum/review/REVIEW.md) | Separately tasked examination of the positive argument and its limit ordering. |
| [Independent review receipt](../evidence/continuum/review/review_receipt.json) | Twelve exact identities and twelve bounded controls, with reviewed source hashes. |
| [Portable continuum sources](../scripts/continuum_checks/) | Inspectable programs for the separate stages; numerical executions retain their own scopes. |

The continuum review corrected or clarified the proper-clock orientation, full Hamilton–Jacobi domain, lattice-to-continuum fluctuation normalization, quantum-current ordering and cutoff-dependent error bookkeeping before the freeze. In particular, the linearized RMS estimate retains its $\pi/2$ fluctuation factor and its zero-mode qualification. This review was AI-assisted work assigned separately, not external human peer review or experimental replication.

The current formal project retains all 63 preceding theorems and adds twelve in one module: **75 theorems across ten modules**. The new Grönwall certificate uses actual scalar derivative hypotheses; the operator commutator estimate that supplies those hypotheses remains an analytic proof. The Casimir and marginal certificates likewise consume explicit scalar relations rather than formalize density matrices. [Formal inventory](FORMAL_PROOFS.md).

## Boundaries preserved across editions

The original two-orbit shape matrix and the new Killing norm/twist matrix are distinct geometric dictionaries. Their targets share a hyperbolic metric, and the old cylindrical equations are recovered by a checked further reduction. This does not identify all physical observables between the formulations.

The unchanged one-probe quantum cell is not a spatial matter regulator. Edition 3.0 supplies the missing transport and preparation architecture through an explicitly augmented, localized, large-population weak-coupling family. Its controlled endpoint is the nonlinear matter action with reciprocal projected shape equations at fixed geometric/internal cutoffs, on prescribed $h_3$ before caustics. Conditional ordered oscillator removal retains a common regular interval and higher moments. Nonlinear geometric-cutoff removal, full pointwise twist closure and Einstein constraints are not supplied by the fixed-basis theorem.

The constant oscillator gap still uses the three-dimensional Einstein-frame clock; an ordinary minimally coupled four-dimensional matter uplift remains open. Strong current convergence justifies a specified ordered contact functional, not exact finite-population quantum scalar/connection dualization. The Hardy floor, frozen-branch purity and weak-current defect remain counterexamples to raw-refinement shortcuts; the augmented theorem does not erase them.

The four-dimensional quadratic-curvature selector introduces its own fixed-source calibration premises and finite operator class. Those premises do not follow from the original flat-vacuum selector or the Gaussian dictionary alone. First-variation stationarity, positive energy, finite simulation convergence and laboratory observation remain separate evidence categories. No physical measurements are supplied.

Root `SHA256SUMS` identifies distributed bytes, excluding itself and generated working/Git state. Hashes do not establish physical truth or independent execution. Reproduction commands write new receipts to a user-selected directory; pinned runtimes, dependency revisions, source hashes, raw logs and controls make that reproduction inspectable. The [research roadmap](RESEARCH_ROADMAP.md) names the remaining tests and limit proofs.
