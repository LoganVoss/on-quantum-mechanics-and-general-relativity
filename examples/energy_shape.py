#!/usr/bin/env python3
"""Calculate the selected Gaussian probe's dimensionless energy/shape relation.

Fidelity means squared overlap. Energy and source magnitude are in units of
hbar*omega. This is the centered saturated Gaussian domain, not arbitrary states.
"""
import argparse
import json
import math

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--fidelity', type=float, default=0.8)
args = p.parse_args()
F = args.fidelity
if not math.isfinite(F) or not 0 < F <= 1:
    p.error('Squared fidelity must be finite and in (0,1].')
energy = F**-2 - 1
distance = 2 * math.acosh(1 / F)
source = math.sqrt(energy * (energy + 1))
print(json.dumps({'squared_fidelity': F, 'intrinsic_hyperbolic_distance': distance,
                  'excitation_energy_over_hbar_omega': energy,
                  'source_norm_over_hbar_omega': source,
                  'scope': 'Selected positive quadratic probe; centered pure Gaussian covariance.'}, indent=2))
