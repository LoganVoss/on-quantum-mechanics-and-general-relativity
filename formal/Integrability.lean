import AnalyticBridge
import Mathlib.Analysis.Calculus.Deriv.Inv

/-!
# Scalar-current integrability selector

The Frobenius identity is proved as a rational identity.  Its use as a selector
explicitly requires a nondegenerate spectral value and non-null area jets.  The
analytic chain then gives one affine W on the connected positive-area domain.
A separate continuity premise at the axis removes the affine intercept.
-/

noncomputable section
namespace VossIntegrability
open Set

def spectralG (s : ℝ) : ℝ := s * (1 + s) / (1 - s)
def spectralH (s : ℝ) : ℝ := s * (1 - s) / (1 + s)
def spectralG1 (s : ℝ) : ℝ := (1 + 2 * s - s ^ 2) / (1 - s) ^ 2
def spectralH1 (s : ℝ) : ℝ := (1 - 2 * s - s ^ 2) / (1 + s) ^ 2

/-- Derivative of the first non-isospectral transport coefficient. -/
theorem spectralG_hasDerivAt (s : ℝ) (hm : 1 - s ≠ 0) :
    HasDerivAt spectralG (spectralG1 s) s := by
  have hd := ((hasDerivAt_id s).mul
    ((hasDerivAt_const s (1 : ℝ)).add (hasDerivAt_id s))).div
      ((hasDerivAt_const s (1 : ℝ)).sub (hasDerivAt_id s)) hm
  convert hd using 1
  dsimp [spectralG1]
  ring

/-- Derivative of the second non-isospectral transport coefficient. -/
theorem spectralH_hasDerivAt (s : ℝ) (hp : 1 + s ≠ 0) :
    HasDerivAt spectralH (spectralH1 s) s := by
  have hd := ((hasDerivAt_id s).mul
    ((hasDerivAt_const s (1 : ℝ)).sub (hasDerivAt_id s))).div
      ((hasDerivAt_const s (1 : ℝ)).add (hasDerivAt_id s)) hp
  convert hd using 1
  dsimp [spectralH1]
  ring

/-- The complete scalar Frobenius obstruction after differentiating log W. -/
theorem frobenius_identity (s W Wp Wm Wpm : ℝ)
    (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0) (hW : W ≠ 0) :
    (spectralG1 s * spectralH s - spectralH1 s * spectralG s) *
        (Wp / W) * (Wm / W) +
      (spectralG s - spectralH s) * (Wpm / W - Wp * Wm / W ^ 2) =
      (4 * s ^ 2 / ((1 - s) * (1 + s))) * (Wpm / W) := by
  dsimp [spectralG1, spectralH1, spectralG, spectralH]
  field_simp
  ring

/-- A genuine spectral value makes Frobenius compatibility equivalent to harmonic W. -/
theorem obstruction_zero_iff_harmonic (s W Wpm : ℝ)
    (hs : s ≠ 0) (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0) (hW : W ≠ 0) :
    (4 * s ^ 2 / ((1 - s) * (1 + s))) * (Wpm / W) = 0 ↔ Wpm = 0 := by
  have hc : 4 * s ^ 2 / ((1 - s) * (1 + s)) ≠ 0 :=
    div_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 2 hs)) (mul_ne_zero hm hp)
  constructor
  · intro h
    have hz : Wpm / W = 0 := (mul_eq_zero.mp h).resolve_left hc
    exact (div_eq_zero_iff.mp hz).resolve_right hW
  · intro h
    simp only [h, zero_div, mul_zero]

/-- For harmonic area, the chain-rule term is W'' rho_+ rho_-.
Its vanishing forces W''=0 exactly when the area gradient is non-null. -/
theorem harmonic_composition_forces_second_derivative_zero
    (W2 p m : ℝ) (hn : p * m ≠ 0) (h : W2 * p * m = 0) : W2 = 0 := by
  have h' : W2 * (p * m) = 0 := by simpa only [mul_assoc] using h
  exact (mul_eq_zero.mp h').resolve_right hn

/-- Integrability selects one affine W on the connected positive-area interval. -/
theorem integrability_selects_affine
    (W W1 W2 p m : ℝ → ℝ) (s : ℝ)
    (hs : s ≠ 0) (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0)
    (positiveW : ∀ ρ : ℝ, 0 < ρ → 0 < W ρ)
    (dW : ∀ ρ : ℝ, 0 < ρ → HasDerivAt W (W1 ρ) ρ)
    (dW1 : ∀ ρ : ℝ, 0 < ρ → HasDerivAt W1 (W2 ρ) ρ)
    (nonnull : ∀ ρ : ℝ, 0 < ρ → p ρ * m ρ ≠ 0)
    (compatible : ∀ ρ : ℝ, 0 < ρ →
      (4 * s ^ 2 / ((1 - s) * (1 + s))) * (W2 ρ * p ρ * m ρ / W ρ) = 0) :
    ∃ a b : ℝ, ∀ ρ : ℝ, 0 < ρ →
      W ρ = a * ρ + b ∧ W1 ρ = a ∧ W2 ρ = 0 := by
  have hzero : ∀ ρ : ℝ, 0 < ρ → W2 ρ = 0 := by
    intro ρ hρ
    have hcomp := (obstruction_zero_iff_harmonic s (W ρ) (W2 ρ * p ρ * m ρ)
      hs hm hp (positiveW ρ hρ).ne').mp (compatible ρ hρ)
    exact harmonic_composition_forces_second_derivative_zero
      (W2 ρ) (p ρ) (m ρ) (nonnull ρ hρ) hcomp
  obtain ⟨a, b, hab⟩ := VossAnalyticBridge.affine_on_positive_of_second_derivative_zero
    W W1 W2 dW dW1 hzero
  refine ⟨a, b, ?_⟩
  intro ρ hρ
  exact ⟨(hab ρ hρ).2, (hab ρ hρ).1, hzero ρ hρ⟩

/-- Axis normalization removes the intercept only with continuity to the axis. -/
theorem axis_continuity_removes_intercept
    (W : ℝ → ℝ) (a b : ℝ)
    (hcont : ContinuousOn W (Ici 0)) (haxis : W 0 = 0)
    (haffine : ∀ ρ : ℝ, 0 < ρ → W ρ = a * ρ + b) : b = 0 := by
  have heq : (Ioi 0).EqOn W (fun ρ => a * ρ + b) := haffine
  have hca : ContinuousOn (fun ρ : ℝ => a * ρ + b) (Ici 0) :=
    ((continuous_const.mul continuous_id).add continuous_const).continuousOn
  have hext := heq.of_subset_closure hcont hca
    Ioi_subset_Ici_self (by rw [closure_Ioi])
  have hz : (0 : ℝ) = b := by
    simpa only [haxis, mul_zero, zero_add] using hext (show (0 : ℝ) ∈ Ici 0 by simp)
  exact hz.symm

/-- Once the intercept is removed, positivity at one area selects the positive branch. -/
theorem positive_linear_branch
    (W : ℝ → ℝ) (a : ℝ) (h1 : 0 < W 1)
    (haffine : ∀ ρ : ℝ, 0 < ρ → W ρ = a * ρ) : 0 < a := by
  have h := haffine 1 (by norm_num)
  simpa only [h, mul_one] using h1

#print axioms spectralG_hasDerivAt
#print axioms spectralH_hasDerivAt
#print axioms frobenius_identity
#print axioms obstruction_zero_iff_harmonic
#print axioms harmonic_composition_forces_second_derivative_zero
#print axioms integrability_selects_affine
#print axioms axis_continuity_removes_intercept
#print axioms positive_linear_branch

end VossIntegrability
