import ThmA
import Mathlib.Analysis.Calculus.MeanValue
import ThmABridge

/-!
# Analytic completion of the single-chart selection theorem

The hypotheses below make the derivative identifications explicit.  No continuity
of the second derivative is required: differentiability of F and F1 with the stated
pointwise derivatives suffices.  Connectedness is carried by the domain `(0,∞)`.
The metric chart equations are the division-form Euler-Lagrange components.
-/

namespace VossAnalyticBridge
open Set

/-- A derivative equal to zero makes a function constant on a connected open real set. -/
theorem constant_on_open_of_hasDerivAt_zero
    (s : Set ℝ) (hs : IsOpen s) (hc : IsPreconnected s)
    (g g1 : ℝ → ℝ)
    (hg : ∀ x ∈ s, HasDerivAt g (g1 x) x)
    (hzero : ∀ x ∈ s, g1 x = 0)
    {x y : ℝ} (hx : x ∈ s) (hy : y ∈ s) : g x = g y := by
  apply hs.is_const_of_deriv_eq_zero hc
  · intro z hz
    exact (hg z hz).differentiableAt.differentiableWithinAt
  · intro z hz
    change deriv g z = 0
    rw [(hg z hz).deriv, hzero z hz]
  · exact hx
  · exact hy

/-- Explicit completion of the step F2 = 0: F1 is constant and F is affine. -/
theorem affine_on_positive_of_second_derivative_zero
    (F F1 F2 : ℝ → ℝ)
    (dF : ∀ x : ℝ, 0 < x → HasDerivAt F (F1 x) x)
    (dF1 : ∀ x : ℝ, 0 < x → HasDerivAt F1 (F2 x) x)
    (zeroF2 : ∀ x : ℝ, 0 < x → F2 x = 0) :
    ∃ a b : ℝ, ∀ x : ℝ, 0 < x → F1 x = a ∧ F x = a * x + b := by
  let a := F1 1
  have constF1 : ∀ x : ℝ, 0 < x → F1 x = a := by
    intro x hx
    exact constant_on_open_of_hasDerivAt_zero (Ioi 0) isOpen_Ioi
      isPreconnected_Ioi F1 F2 dF1 zeroF2 hx (by norm_num)
  let G : ℝ → ℝ := fun x => F x - a * x
  have dG : ∀ x : ℝ, 0 < x → HasDerivAt G 0 x := by
    intro x hx
    have h := (dF x hx).sub ((hasDerivAt_id x).const_mul a)
    simpa only [constF1 x hx, mul_one, sub_self] using h
  have constG : ∀ x : ℝ, 0 < x → G x = G 1 := by
    intro x hx
    exact constant_on_open_of_hasDerivAt_zero (Ioi 0) isOpen_Ioi
      isPreconnected_Ioi G (fun _ => 0) dG (by intro z hz; rfl) hx (by norm_num)
  refine ⟨a, F 1 - a, ?_⟩
  intro x hx
  refine ⟨constF1 x hx, ?_⟩
  have h := constG x hx
  dsimp [G] at h
  linarith

/-- The three metric Euler-Lagrange components on the Milne-polar chart. -/
structure ChartEquations (F1 F2 U W V : ℝ → ℝ) : Prop where
  tt : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
    -F2 ρ * t ^ 2 + U ρ * (t ^ 2 + r ^ 2) / 2 -
      W ρ * (t ^ 2 + r ^ 2) / (4 * ρ ^ 2) + V ρ / 2 = 0
  rr : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
    -F2 ρ * r ^ 2 + U ρ * (t ^ 2 + r ^ 2) / 2 -
      W ρ * (t ^ 2 + r ^ 2) / (4 * ρ ^ 2) - V ρ / 2 = 0
  tr : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
    -(ρ * F2 ρ + F1 ρ) + ρ * U ρ + W ρ / (2 * ρ) = 0

/-- One simultaneous theorem: chart equations and genuine derivatives imply all
selected coefficients, with one common pair of constants a,b on the full domain. -/
theorem complete_selection
    (F F1 F2 U W V : ℝ → ℝ)
    (chart : ChartEquations F1 F2 U W V)
    (dF : ∀ x : ℝ, 0 < x → HasDerivAt F (F1 x) x)
    (dF1 : ∀ x : ℝ, 0 < x → HasDerivAt F1 (F2 x) x) :
    ∃ a b : ℝ, ∀ ρ : ℝ, 0 < ρ →
      F ρ = a * ρ + b ∧ F1 ρ = a ∧ F2 ρ = 0 ∧
      U ρ = a / (2 * ρ) ∧ W ρ = a * ρ ∧ V ρ = 0 := by
  have positive : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ → 0 < ρ := by
    intro t r ρ ht hr he
    rw [← he]
    exact mul_pos ht hr
  have selected := VossThmA.theoremA_forward F1 F2 U W V
    (fun t r ρ ht hr he =>
      (VossThmABridge.tt_iff (F2 ρ) (U ρ) (W ρ) (V ρ) ρ t r
        (positive t r ρ ht hr he).ne').mp (chart.tt t r ρ ht hr he))
    (fun t r ρ ht hr he =>
      (VossThmABridge.rr_iff (F2 ρ) (U ρ) (W ρ) (V ρ) ρ t r
        (positive t r ρ ht hr he).ne').mp (chart.rr t r ρ ht hr he))
    (fun t r ρ ht hr he =>
      (VossThmABridge.tr_iff (F1 ρ) (F2 ρ) (U ρ) (W ρ) ρ
        (positive t r ρ ht hr he).ne').mp (chart.tr t r ρ ht hr he))
  obtain ⟨a, b, hab⟩ := affine_on_positive_of_second_derivative_zero
    F F1 F2 dF dF1 (fun x hx => (selected x hx).1)
  refine ⟨a, b, ?_⟩
  intro ρ hρ
  obtain ⟨hF2, hV, hW, hU⟩ := selected ρ hρ
  obtain ⟨hF1, hF⟩ := hab ρ hρ
  obtain ⟨hWa, hUa⟩ := VossThmA.einstein_direction a ρ (F1 ρ) (U ρ) (W ρ)
    hρ hF1 hW hU
  exact ⟨hF, hF1, hF2, hUa, hWa, hV⟩

/-- Positivity of the sigma-model coefficient at one positive area fixes a > 0. -/
theorem complete_selection_positive
    (F F1 F2 U W V : ℝ → ℝ)
    (chart : ChartEquations F1 F2 U W V)
    (dF : ∀ x : ℝ, 0 < x → HasDerivAt F (F1 x) x)
    (dF1 : ∀ x : ℝ, 0 < x → HasDerivAt F1 (F2 x) x)
    (ρ0 : ℝ) (hρ0 : 0 < ρ0) (positiveW : 0 < W ρ0) :
    ∃ a b : ℝ, 0 < a ∧ ∀ ρ : ℝ, 0 < ρ →
      F ρ = a * ρ + b ∧ F1 ρ = a ∧ F2 ρ = 0 ∧
      U ρ = a / (2 * ρ) ∧ W ρ = a * ρ ∧ V ρ = 0 := by
  obtain ⟨a, b, h⟩ := complete_selection F F1 F2 U W V chart dF dF1
  have hW0 : W ρ0 = a * ρ0 := (h ρ0 hρ0).2.2.2.2.1
  have ha : 0 < a := by nlinarith
  exact ⟨a, b, ha, h⟩

/-- A chart equation forcing k' = 0 selects only a constant odd coupling. -/
theorem constant_odd_coupling
    (k k1 : ℝ → ℝ)
    (dk : ∀ ρ : ℝ, 0 < ρ → HasDerivAt k (k1 ρ) ρ)
    (qEquation : ∀ t r : ℝ, 0 < t → 0 < r → -4 * (t / r) * k1 (t * r) = 0) :
    ∃ c : ℝ, ∀ ρ : ℝ, 0 < ρ → k ρ = c := by
  have hk1 : ∀ ρ : ℝ, 0 < ρ → k1 ρ = 0 := by
    intro ρ hρ
    have h := qEquation ρ 1 hρ (by norm_num)
    simp only [div_one, mul_one] at h
    have hn : -4 * ρ ≠ 0 := mul_ne_zero (by norm_num) hρ.ne'
    exact (mul_eq_zero.mp h).resolve_left hn
  refine ⟨k 1, ?_⟩
  intro ρ hρ
  exact constant_on_open_of_hasDerivAt_zero (Ioi 0) isOpen_Ioi
    isPreconnected_Ioi k k1 dk hk1 hρ (by norm_num)

#print axioms constant_on_open_of_hasDerivAt_zero
#print axioms affine_on_positive_of_second_derivative_zero
#print axioms complete_selection
#print axioms complete_selection_positive
#print axioms constant_odd_coupling

end VossAnalyticBridge
