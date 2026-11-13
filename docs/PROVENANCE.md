# Provenance and version boundaries

This release is **On Quantum Mechanics and General Relativity**, research edition 1.0.0, November 13, 2026, by Logan Voss. Its principal supplied source is the November 12 v2.4 chart-selection supplement. The earlier v2.3 archive was recovered from the author's prior research conversation and matched the SHA-256 already recorded in the v2.4 input manifest:

```text
d6579e52193d1307a016c53fedb65289803e68bcd795803b7c80033ea23d684f
```

| Location | Identity and status |
|---|---|
| `source/v2.4/` | Preserved original package: manuscript, notes, source scripts, Lean files, compiled historical objects, and historical receipts. Its original `SHA256SUMS` remains intact. |
| `archive/voss-verification-v2.3-original.zip` | Byte-identical recovered earlier archive, including v2.0/v2.1 manuscripts and v2.2/v2.3 lineage. Historical claims and blocked-build notices remain historical. This entire older archive was not rerun for the present release. |
| `formal/` | Seven unchanged original proof modules, plus the new `ResidualInversion.lean`, pinned configuration, and no distributed dependency/build cache. |
| `evidence/source_suite/` | Newly executed original scientific checks; receipts are separate from the source snapshot. |
| `evidence/lean/` | Newly executed full 48-theorem formal build, dependency audit, and true/false proposition controls. |
| `evidence/quantum_geometry/` | Independent exact algebra and wavefunction-quadrature checks. |
| `evidence/numerical_controls/` | Independent exact-solution and timestep controls, including the coarse-regime limitation. |
| `evidence/phase_freeze.json` | Records that mathematical derivations were completed before public authoring began. |
| `evidence/independent_review.md` | Frozen mathematical review, derivations, and qualifications from the separate review pass; retained as an audit record. |

The original source manifest lists ten earlier inputs. A manifest entry alone does not imply a fresh reproduction of that input. The recovered archive repairs the principal lineage gap; the executable evidence used for current claims is mapped explicitly in [Verification](VERIFICATION.md). The separate working review was performed by an independently tasked AI reviewer, not external peer review.

The current edition supersedes the earlier reader-facing summary where it referred to “40 modules” or unrestricted stability. The original formal package contains 40 theorems in seven modules. The current package contains 48 in eight. First-variation stationarity, positive radiative energy, and finite numerical convergence have different meanings and are described separately.

Root `SHA256SUMS` covers the distributed files except itself and generated working/Git state. Hashes identify bytes; they do not establish authorship, physical truth, or independent execution. Reproduction commands create new receipts in a user-selected output directory. Dependency hashes, runtime versions, and the original source hashes make the verification inspectable on another machine.
