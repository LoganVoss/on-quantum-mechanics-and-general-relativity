# Next tests that can change the conclusion

Research edition 2.0 completes three scoped advances: a selected reciprocal probe interaction, a sourced discriminator for the constant quadratic-curvature class, and an inverse calibration in a one-Killing theory. Their proofs narrow the remaining questions; they do not remove the assumptions that define each construction.

| Completed advance | What remains to establish |
| --- | --- |
| A target-equivariant quadratic interaction, positive joint quantum cell, and exact energy–force relations | Controlled field/continuum limits, gravitational constraints, and an operational identification with spacetime response |
| Full four-dimensional dust/electrovac selection and two-channel inversion in the constant quadratic class | Physical source and response calibration; discrimination of enlarged operator classes and EFT effects |
| One-Killing inverse calibration, off-shell reduction, and exact recovery of the cylindrical sector | Broader solution families, global reconstruction, and a specified four-dimensional matter uplift |

The original two-orbit shape matrix and the new Killing norm/twist matrix have different geometric meanings. The shared hyperbolic target allows precise mathematical correspondences; it does not make every observable or clock in the two formulations identical.

## 1. Converge the joint quantum calculation in all regulator directions

The current positive regulators check two Fock cutoffs at one shape grid. Next, refine the radial and angular shape grid, enlarge the finite target domain, and increase the oscillator cutoff separately. Use the same normalized initial packet and the same bounded directional observable across refinements. Include an independently implemented discretization and the uncoupled control.

A useful success condition is a converged error interval for directional response, energy transfer, and shape–probe entanglement through a declared finite time. Preserved norm and total energy are necessary checks, but alone do not establish convergence to the continuum Hamiltonian. [Current quantum controls](DYNAMICAL_COUPLING.md).

The exact ground-band result supplies a second test. Prepare a normalized packet in the local Gaussian ground band and compare its initial off-band probability to

```math
P_{\perp}(t)=\frac{E}{4I}t^2+o(t^2).
```

Resolve the small-time coefficient separately from shape-grid and Fock-cutoff errors. This checks the initial leakage law, not an exact autonomous ground-band evolution or a finite-time upper bound.

## 2. Derive, rather than assume, a bridge to the state-fluid description

The fully quantum cell and the covariant variational state-fluid are distinct constructions. A controlled connection would need an explicit family of many-cell states, a scaling or mean-field parameter, and estimates showing when the reduced state/current equations approximate the joint quantum evolution. Derive the stress tensor and twist current from that same limit, and bound the correlations or entanglement discarded by the approximation.

Success would be a stated regime and error estimate for both observables and reciprocal source equations. Until then, each model keeps its own assumptions. A positive finite Hamiltonian does not itself establish a constrained interacting quantum-gravity continuum. Reduced-gravity renormalization programs provide relevant precedent, not a replacement for a limit proof here. [Niedermaier, *Dimensionally reduced gravity theories are asymptotically safe*](https://arxiv.org/abs/hep-th/0304117v1).

## 3. Construct the four-dimensional matter uplift and calibrate its clock

The smooth-current action has consistent local field equations and current-corrected twist reconstruction. The next obligation is an explicit four-dimensional covariant matter action whose reduction yields those sources, the cross interaction, and the current-squared contact term.

Clock normalization is a decisive part of this test. The selected constant oscillator gap uses the three-dimensional Einstein-frame proper time. For a horizontal trajectory,

```math
d\tau_4=\lambda^{-1/2}ds_3.
```

A constant four-dimensional proper-time gap therefore has a different reduced dependence. A proposed uplift must account for this factor and reproduce the complete reduced variational equations, including metric dependence of the current. If that cannot be established within a chosen matter class, the three-dimensional model remains a useful construction with its stated clock calibration. [Current action and reconstruction](CURRENT_AND_RECONSTRUCTION.md).

For localized sources, define a finite-width current or regulator before using the contact term. Demonstrate a controlled limit or retain a finite source scale; a squared delta-function current is not an unregulated matter model.

## 4. Test the sourced response class at additional scales

The dust and charged calibrations now distinguish the two constant quadratic coefficients under the fixed-source contract. The response inverse adds an error-aware route to the same parameters. The next step is to specify how each source amplitude and curvature channel would be independently prepared or inferred, including normalization, boundary conditions, and nonlinear corrections.

Use two tensor-channel scales and one scalar-channel observation to estimate the coefficients and leading normalization. Hold out a fourth observation to test the shared-intercept prediction. A successful test produces simultaneous parameter intervals and an independently predicted held-out response. Agreement at finitely many scales does not establish the operator class at every scale. [Response construction and intervals](RESPONSE_TOMOGRAPHY.md).

To enlarge the action class, list the added operators and construct enough independent response channels to distinguish them. The supplied higher-derivative counterexample already shows why one-scale agreement cannot exclude arbitrary additional terms. Interpret poles only within the declared theory's validity range; an exact polynomial model and a low-energy EFT truncation support different conclusions. [Quadratic selector and its limits](QUADRATIC_SELECTION.md).

## 5. Exercise the genuinely larger one-Killing solution space

The one-Killing action permits dependence on two quotient spatial coordinates. A useful next calculation would solve its constraints for initial data with explicit angular dependence, then evolve a bounded nonlinear example that is not confined to the cylindrical sector. Verify the full three-dimensional Einstein/wave-map equations and the local four-dimensional reconstruction, with separate spatial, temporal, and boundary controls.

The success condition is a resolved example in the enlarged field space. It would complement the action-selection theorem; it would not alone prove generic global existence or stability. Global reconstruction additionally needs the twist periods and bundle data. [One-Killing model and old-sector recovery](ONE_KILLING_EXTENSION.md).

Retain the exact nonlinear Bessel/geodesic oracle and the original independent-profile benchmark as regression controls. Longer evolutions should preserve the distinction between finite numerical evidence and a PDE theorem.

## 6. Test the calibrated quantum observation chain

Prepare centered one-mode states with independently characterized covariance, displacement, purity, and phase reference. Compare measured transition probabilities to $\operatorname{sech}(d_G/2)$ and closed-path geometric phases to minus one quarter of the oriented hyperbolic area. Then, for the specified oscillator interaction, test the energy–overlap relation and the opposite directional responses of symmetry-related preparations.

Keep the negative controls visible: the vacuum and first excited state share normalized covariance shape but are orthogonal; an isotropic mixed covariance can have positive energy and zero directional source; an uncoupled model does not produce the selected reciprocal response. Account for loss, leakage and uncertainty before drawing conclusions. [Quantum geometry](QUANTUM_GEOMETRY.md) and [energy–shape relations](ENERGY_SHAPE_RELATION.md).

These tests concern the prepared quantum systems and calibrated interaction. Demonstrating that the target represents a physical spacetime orbit or Killing norm/twist requires an additional geometric observation map. No such laboratory identification is claimed by the present calculations.

## 7. Turn approximate calibration into justified coefficient intervals

The original five-residual inverse and the new helical and sourced inverses provide explicit uncertainty maps. Apply them only to the equations, units, and source prescriptions they were derived for. Establish a simultaneous residual envelope over the required domain before using integrated coefficient bounds; a few sampled area values do not prove a uniform interval premise.

A useful outcome is a reproducible interval for each coefficient, supported by a measurement-to-residual model or independently controlled computation. Re-evaluating an action already selected by the theorem cannot supply independent empirical evidence for its calibration assumptions. [Original robustness theorem](ROBUST_SELECTION.md) and [machine-readable claim ledger](../CLAIMS.json).
