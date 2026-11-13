import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

/-!
# Bridge lemmas for Theorem A (separate file on purpose)

STATUS: KERNEL-CHECKED with Lean 4.19.0 and pinned Mathlib.
The field-simplification proofs pass with warnings treated as errors.

* The division-form chart components (as printed in the manuscript) vanish exactly when
  the cleared forms used in `ThmA.lean` vanish, for `ρ ≠ 0`.
* Three coefficient identities from the Lax / Frobenius computation (Eqs. 19-22 of v2.2).
-/

namespace VossThmABridge

theorem iff_of_mul (E P c : ℝ) (hc : c ≠ 0) (key : c * E = P) : E = 0 ↔ P = 0 := by
  subst key
  constructor
  · intro h
    rw [h, mul_zero]
  · intro h
    exact (mul_eq_zero.mp h).resolve_left hc

theorem tt_iff (F2 U W V ρ t r : ℝ) (hρ : ρ ≠ 0) :
    (-F2 * t ^ 2 + U * (t ^ 2 + r ^ 2) / 2 - W * (t ^ 2 + r ^ 2) / (4 * ρ ^ 2) + V / 2 = 0) ↔
    (-4 * ρ ^ 2 * F2 * t ^ 2 + 2 * ρ ^ 2 * U * (t ^ 2 + r ^ 2) -
        W * (t ^ 2 + r ^ 2) + 2 * ρ ^ 2 * V = 0) := by
  refine iff_of_mul _ _ (4 * ρ ^ 2) (mul_ne_zero (by norm_num) (pow_ne_zero 2 hρ)) ?_
  field_simp
  ring

theorem rr_iff (F2 U W V ρ t r : ℝ) (hρ : ρ ≠ 0) :
    (-F2 * r ^ 2 + U * (t ^ 2 + r ^ 2) / 2 - W * (t ^ 2 + r ^ 2) / (4 * ρ ^ 2) - V / 2 = 0) ↔
    (-4 * ρ ^ 2 * F2 * r ^ 2 + 2 * ρ ^ 2 * U * (t ^ 2 + r ^ 2) -
        W * (t ^ 2 + r ^ 2) - 2 * ρ ^ 2 * V = 0) := by
  refine iff_of_mul _ _ (4 * ρ ^ 2) (mul_ne_zero (by norm_num) (pow_ne_zero 2 hρ)) ?_
  field_simp
  ring

theorem tr_iff (F1 F2 U W ρ : ℝ) (hρ : ρ ≠ 0) :
    (-(ρ * F2 + F1) + ρ * U + W / (2 * ρ) = 0) ↔
    (-2 * ρ ^ 2 * F2 - 2 * ρ * F1 + 2 * ρ ^ 2 * U + W = 0) := by
  refine iff_of_mul _ _ (2 * ρ) (mul_ne_zero (by norm_num) hρ) ?_
  field_simp
  ring

/-- Eq. (19)-(20): the parametrization `a = 1/(1-s)`, `b = 1/(1+s)` solves `2ab = a+b`. -/
theorem lax_ab (s : ℝ) (h1 : 1 - s ≠ 0) (h2 : 1 + s ≠ 0) :
    2 * (1 / (1 - s)) * (1 / (1 + s)) = 1 / (1 - s) + 1 / (1 + s) := by
  field_simp
  ring

/-- Coefficient of `W_{+-}/W` in the Frobenius obstruction, Eq. (22): `g - h = 4 s²/(1-s²)`
with `g = s(1+s)/(1-s)` and `h = s(1-s)/(1+s)`. -/
theorem lax_obstruction_coeff (s : ℝ) (h1 : 1 - s ≠ 0) (h2 : 1 + s ≠ 0) :
    s * (1 + s) / (1 - s) - s * (1 - s) / (1 + s) = 4 * s ^ 2 / ((1 - s) * (1 + s)) := by
  field_simp
  ring

/-- `g * h = s²`, the identity behind `g' h - h' g = 4 s²/(1-s²)`. -/
theorem lax_gh (s : ℝ) (h1 : 1 - s ≠ 0) (h2 : 1 + s ≠ 0) :
    (s * (1 + s) / (1 - s)) * (s * (1 - s) / (1 + s)) = s ^ 2 := by
  field_simp
  ring

#print axioms iff_of_mul
#print axioms tt_iff
#print axioms rr_iff
#print axioms tr_iff
#print axioms lax_ab
#print axioms lax_obstruction_coeff
#print axioms lax_gh

end VossThmABridge
