import Integrability

/-!
# Exact witnesses for the derivative and nondegeneracy premises

These witnesses prevent the coefficient labels, a degenerate spectral value,
a null area gradient, or a bare endpoint assignment from silently replacing the
corresponding premises of the proved selectors.
-/

namespace VossPremiseObstructions

/-- Algebraic chart equations permit a nonconstant F1 when F2 is only an independent label. -/
theorem independent_labels_counterexample :
    VossAnalyticBridge.ChartEquations (fun ρ => ρ) (fun _ => 0)
      (fun _ => (1 : ℝ) / 2) (fun ρ => ρ ^ 2) (fun _ => 0) ∧
    ¬ (∃ a : ℝ, ∀ ρ : ℝ, 0 < ρ → ρ = a) := by
  constructor
  · have pos : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ → ρ ≠ 0 := by
      intro t r ρ ht hr he
      rw [← he]
      exact (mul_pos ht hr).ne'
    constructor
    · intro t r ρ ht hr he
      have hn := pos t r ρ ht hr he
      field_simp
      ring
    · intro t r ρ ht hr he
      have hn := pos t r ρ ht hr he
      field_simp
      ring
    · intro t r ρ ht hr he
      have hn := pos t r ρ ht hr he
      field_simp
      ring
  · rintro ⟨a, ha⟩
    have h1 := ha 1 (by norm_num)
    have h2 := ha 2 (by norm_num)
    linarith

/-- At spectral value s=0 the scalar Frobenius obstruction vanishes for every Wpm. -/
theorem zero_spectral_value_loses_constraint (W Wpm : ℝ) :
    (4 * (0 : ℝ) ^ 2 / ((1 - 0) * (1 + 0))) * (Wpm / W) = 0 := by ring

/-- A null area jet hides arbitrary W2 in the harmonic-composition equation. -/
theorem null_area_jet_loses_constraint (W2 m : ℝ) : W2 * 0 * m = 0 := by ring

/-- Assigning W(0)=0 alone preserves a nonzero affine intercept on the open interval. -/
theorem axis_value_without_continuity :
    let W : ℝ → ℝ := fun ρ => if ρ = 0 then 0 else ρ + 1
    W 0 = 0 ∧ (∀ ρ : ℝ, 0 < ρ → W ρ = ρ + 1) ∧
      ¬ (∃ a : ℝ, ∀ ρ : ℝ, 0 < ρ → W ρ = a * ρ) := by
  dsimp
  refine ⟨by simp, ?_, ?_⟩
  · intro ρ hρ
    simp only [if_neg hρ.ne']
  · rintro ⟨a, ha⟩
    have h1 := ha 1 (by norm_num)
    have h2 := ha 2 (by norm_num)
    norm_num at h1 h2
    linarith

#print axioms independent_labels_counterexample
#print axioms zero_spectral_value_loses_constraint
#print axioms null_area_jet_loses_constraint
#print axioms axis_value_without_continuity

end VossPremiseObstructions
