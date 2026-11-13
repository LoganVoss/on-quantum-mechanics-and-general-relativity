#!/usr/bin/env bash
set -euo pipefail
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update
lake exe cache get Mathlib.Analysis.SpecialFunctions.Pow.Real Mathlib.Analysis.SpecialFunctions.Sqrt Mathlib.Tactic.LinearCombination Mathlib.Tactic.Positivity Mathlib.Tactic.Linarith Mathlib.Tactic.FieldSimp Mathlib.Analysis.Calculus.MeanValue Mathlib.Data.Complex.Trigonometric Mathlib.Analysis.Calculus.Deriv.Inv Mathlib.Data.Matrix.Basic
lake build
