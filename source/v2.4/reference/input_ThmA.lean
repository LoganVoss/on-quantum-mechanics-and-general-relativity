import Mathlib

/-!
# Theorem A (single-chart selection): functional statement and proof

STATUS: SOURCE ONLY.  This file has NOT been elaborated by a Lean compiler in the
authoring environment (no `lean`/`lake` binary and no network were available).
Its algebraic certificates were cross-checked independently by exact rational
arithmetic in `lean_certificate_audit.py`; that is evidence about the algebra, not
a substitute for kernel checking.  Run `lake build ThmA` to obtain real verification.

## What is formalized
The cleared-denominator components of the reduced field equations, evaluated on the
flat Milne-polar chart (rho = t*r, quotient metric flat), are taken as HYPOTHESES for
ALL t, r > 0, with F1 = F', F2 = F'' treated as independent functions.  The theorem
derives, for every rho > 0, with NO regularity assumption on any function:

    F'' = 0,   V = 0,   W = rho * F',   2 rho^2 U = W.

## What is NOT formalized (external inputs)
* the variational derivation of the equations (Eq. 19 of the manuscript; checked
  numerically by functional differentiation, not here);
* that F2 is the derivative of F1, hence F' constant on (0, oo) (mean-value theorem);
* the physical premises: literal quotient-block frame, two-derivative class,
  dimension, signature.
-/

namespace VossThmA

/-- Forward direction: the Milne-polar chart equations select the Einstein-normalized
coefficients pointwise.  The proof evaluates the chart at the two boost-related points
`(2s, s/2)` and `(s/2, 2s)` on the hyperbola `t*r = s^2`; this is the range argument. -/
theorem theoremA_forward
    (F1 F2 U W V : ℝ → ℝ)
    (htt : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
      -4 * ρ ^ 2 * F2 ρ * t ^ 2 + 2 * ρ ^ 2 * U ρ * (t ^ 2 + r ^ 2) -
        W ρ * (t ^ 2 + r ^ 2) + 2 * ρ ^ 2 * V ρ = 0)
    (hrr : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
      -4 * ρ ^ 2 * F2 ρ * r ^ 2 + 2 * ρ ^ 2 * U ρ * (t ^ 2 + r ^ 2) -
        W ρ * (t ^ 2 + r ^ 2) - 2 * ρ ^ 2 * V ρ = 0)
    (htr : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
      -2 * ρ ^ 2 * F2 ρ - 2 * ρ * F1 ρ + 2 * ρ ^ 2 * U ρ + W ρ = 0) :
    ∀ ρ : ℝ, 0 < ρ →
      F2 ρ = 0 ∧ V ρ = 0 ∧ W ρ = ρ * F1 ρ ∧ 2 * ρ ^ 2 * U ρ = W ρ := by
  intro ρ hρ
  obtain ⟨s, hs, rfl⟩ : ∃ s : ℝ, 0 < s ∧ s ^ 2 = ρ :=
    ⟨Real.sqrt ρ, Real.sqrt_pos.2 hρ, Real.sq_sqrt hρ.le⟩
  have h2s : (0 : ℝ) < 2 * s := by positivity
  have hs2 : (0 : ℝ) < s / 2 := by positivity
  have hA := htt (2 * s) (s / 2) (s ^ 2) h2s hs2 (by ring)
  have hA' := hrr (2 * s) (s / 2) (s ^ 2) h2s hs2 (by ring)
  have hB := htt (s / 2) (2 * s) (s ^ 2) hs2 h2s (by ring)
  have hB' := hrr (s / 2) (2 * s) (s ^ 2) hs2 h2s (by ring)
  have hC := htr s s (s ^ 2) hs hs (by ring)
  -- difference of tt and rr at the two boost-related points isolates V and F2
  have hv : (s ^ 2) ^ 2 * V (s ^ 2) = 0 := by
    linear_combination (1 / 8 : ℝ) * hA - (1 / 8 : ℝ) * hA' + (1 / 8 : ℝ) * hB -
      (1 / 8 : ℝ) * hB'
  have ha : (s ^ 2) ^ 2 * s ^ 2 * F2 (s ^ 2) = 0 := by
    linear_combination (-1 / 30 : ℝ) * hA + (1 / 30 : ℝ) * hA' + (1 / 30 : ℝ) * hB -
      (1 / 30 : ℝ) * hB'
  have hF2 : F2 (s ^ 2) = 0 := by
    have hne : (s ^ 2) ^ 2 * s ^ 2 ≠ 0 := by positivity
    exact (mul_eq_zero.mp ha).resolve_left hne
  have hV : V (s ^ 2) = 0 := by
    have hne : (s ^ 2) ^ 2 ≠ 0 := by positivity
    exact (mul_eq_zero.mp hv).resolve_left hne
  -- the sum of tt and rr then fixes U in terms of W
  have hU : 2 * (s ^ 2) ^ 2 * U (s ^ 2) = W (s ^ 2) := by
    have hS : (17 / 4 * s ^ 2) * (2 * (s ^ 2) ^ 2 * U (s ^ 2) - W (s ^ 2)) = 0 := by
      linear_combination hA + (4 * (s ^ 2) ^ 2 * (2 * s) ^ 2) * hF2 -
        (2 * (s ^ 2) ^ 2) * hV
    have hne : (17 / 4 * s ^ 2 : ℝ) ≠ 0 := by positivity
    have h0 := (mul_eq_zero.mp hS).resolve_left hne
    linarith
  -- the mixed component fixes W in terms of F'
  have hW : W (s ^ 2) = s ^ 2 * F1 (s ^ 2) := by
    linear_combination (1 / 2 : ℝ) * hC - (1 / 2 : ℝ) * hU + ((s ^ 2) ^ 2) * hF2
  exact ⟨hF2, hV, hW, hU⟩

/-- Converse: the selected coefficients satisfy every chart equation. -/
theorem theoremA_converse
    (F1 F2 U W V : ℝ → ℝ)
    (h : ∀ ρ : ℝ, 0 < ρ →
      F2 ρ = 0 ∧ V ρ = 0 ∧ W ρ = ρ * F1 ρ ∧ 2 * ρ ^ 2 * U ρ = W ρ) :
    (∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
      -4 * ρ ^ 2 * F2 ρ * t ^ 2 + 2 * ρ ^ 2 * U ρ * (t ^ 2 + r ^ 2) -
        W ρ * (t ^ 2 + r ^ 2) + 2 * ρ ^ 2 * V ρ = 0) ∧
    (∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
      -4 * ρ ^ 2 * F2 ρ * r ^ 2 + 2 * ρ ^ 2 * U ρ * (t ^ 2 + r ^ 2) -
        W ρ * (t ^ 2 + r ^ 2) - 2 * ρ ^ 2 * V ρ = 0) ∧
    (∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ →
      -2 * ρ ^ 2 * F2 ρ - 2 * ρ * F1 ρ + 2 * ρ ^ 2 * U ρ + W ρ = 0) := by
  have key : ∀ t r ρ : ℝ, 0 < t → 0 < r → t * r = ρ → 0 < ρ := by
    intro t r ρ ht hr hρ
    rw [← hρ]
    exact mul_pos ht hr
  refine ⟨?_, ?_, ?_⟩
  · intro t r ρ ht hr hρ
    obtain ⟨h1, h2, _, h4⟩ := h ρ (key t r ρ ht hr hρ)
    linear_combination (-4 * ρ ^ 2 * t ^ 2) * h1 + (t ^ 2 + r ^ 2) * h4 +
      (2 * ρ ^ 2) * h2
  · intro t r ρ ht hr hρ
    obtain ⟨h1, h2, _, h4⟩ := h ρ (key t r ρ ht hr hρ)
    linear_combination (-4 * ρ ^ 2 * r ^ 2) * h1 + (t ^ 2 + r ^ 2) * h4 -
      (2 * ρ ^ 2) * h2
  · intro t r ρ ht hr hρ
    obtain ⟨h1, _, h3, h4⟩ := h ρ (key t r ρ ht hr hρ)
    linear_combination (-2 * ρ ^ 2) * h1 + h4 + 2 * h3

/-- Normalization: once `F'` is the constant `a`, the selected coefficients are the
Einstein-frame ones `W = a ρ`, `U = a / (2 ρ)`. -/
theorem einstein_direction (a ρ F1 U W : ℝ) (hρ : 0 < ρ) (hF1 : F1 = a)
    (hW : W = ρ * F1) (hU : 2 * ρ ^ 2 * U = W) :
    W = a * ρ ∧ U = a / (2 * ρ) := by
  have hW' : W = a * ρ := by
    linear_combination hW + ρ * hF1
  refine ⟨hW', ?_⟩
  have hne : (2 * ρ : ℝ) ≠ 0 := by positivity
  rw [eq_div_iff hne]
  have hz : ρ * (U * (2 * ρ) - a) = 0 := by
    linear_combination hU + hW'
  have h0 := (mul_eq_zero.mp hz).resolve_left hρ.ne'
  linarith

/-- Residual of the cleared tt equation (not assumed zero). -/
def ttRes (F2 U W V ρ t r : ℝ) : ℝ :=
  -4 * ρ ^ 2 * F2 * t ^ 2 + 2 * ρ ^ 2 * U * (t ^ 2 + r ^ 2) -
    W * (t ^ 2 + r ^ 2) + 2 * ρ ^ 2 * V

/-- Residual of the cleared rr equation (not assumed zero). -/
def rrRes (F2 U W V ρ t r : ℝ) : ℝ :=
  -4 * ρ ^ 2 * F2 * r ^ 2 + 2 * ρ ^ 2 * U * (t ^ 2 + r ^ 2) -
    W * (t ^ 2 + r ^ 2) - 2 * ρ ^ 2 * V

/-- Quantitative stability, potential: if the four boost-pair residuals are at most
`ε` in absolute value, then `ρ² |V| ≤ ε / 2` (ρ = s²).  The constant is sharp. -/
theorem robust_V (F2 U W V s ε : ℝ)
    (hA : |ttRes F2 U W V (s ^ 2) (2 * s) (s / 2)| ≤ ε)
    (hA' : |rrRes F2 U W V (s ^ 2) (2 * s) (s / 2)| ≤ ε)
    (hB : |ttRes F2 U W V (s ^ 2) (s / 2) (2 * s)| ≤ ε)
    (hB' : |rrRes F2 U W V (s ^ 2) (s / 2) (2 * s)| ≤ ε) :
    |(s ^ 2) ^ 2 * V| ≤ ε / 2 := by
  have e : (s ^ 2) ^ 2 * V =
      (ttRes F2 U W V (s ^ 2) (2 * s) (s / 2) - rrRes F2 U W V (s ^ 2) (2 * s) (s / 2) +
        ttRes F2 U W V (s ^ 2) (s / 2) (2 * s) -
        rrRes F2 U W V (s ^ 2) (s / 2) (2 * s)) / 8 := by
    simp only [ttRes, rrRes]
    ring
  rw [e]
  obtain ⟨a1, a2⟩ := abs_le.mp hA
  obtain ⟨b1, b2⟩ := abs_le.mp hA'
  obtain ⟨c1, c2⟩ := abs_le.mp hB
  obtain ⟨d1, d2⟩ := abs_le.mp hB'
  exact abs_le.mpr ⟨by linarith [a1, a2, b1, b2, c1, c2, d1, d2],
    by linarith [a1, a2, b1, b2, c1, c2, d1, d2]⟩

/-- Quantitative stability, dilaton second derivative: `ρ² s² |F''| ≤ 2 ε / 15`. -/
theorem robust_F2 (F2 U W V s ε : ℝ)
    (hA : |ttRes F2 U W V (s ^ 2) (2 * s) (s / 2)| ≤ ε)
    (hA' : |rrRes F2 U W V (s ^ 2) (2 * s) (s / 2)| ≤ ε)
    (hB : |ttRes F2 U W V (s ^ 2) (s / 2) (2 * s)| ≤ ε)
    (hB' : |rrRes F2 U W V (s ^ 2) (s / 2) (2 * s)| ≤ ε) :
    |(s ^ 2) ^ 2 * s ^ 2 * F2| ≤ 2 * ε / 15 := by
  have e : (s ^ 2) ^ 2 * s ^ 2 * F2 =
      (-ttRes F2 U W V (s ^ 2) (2 * s) (s / 2) + rrRes F2 U W V (s ^ 2) (2 * s) (s / 2) +
        ttRes F2 U W V (s ^ 2) (s / 2) (2 * s) -
        rrRes F2 U W V (s ^ 2) (s / 2) (2 * s)) / 30 := by
    simp only [ttRes, rrRes]
    ring
  rw [e]
  obtain ⟨a1, a2⟩ := abs_le.mp hA
  obtain ⟨b1, b2⟩ := abs_le.mp hA'
  obtain ⟨c1, c2⟩ := abs_le.mp hB
  obtain ⟨d1, d2⟩ := abs_le.mp hB'
  exact abs_le.mpr ⟨by linarith [a1, a2, b1, b2, c1, c2, d1, d2],
    by linarith [a1, a2, b1, b2, c1, c2, d1, d2]⟩

/-- Power-law corollary of the integrability selector (`W'' = c n (n-1) ρ^(n-2)`):
the positive constant-coefficient branches are exactly `n = 0` and `n = 1`. -/
theorem power_branch (c n ρ : ℝ) (hc : 0 < c) (hρ : 0 < ρ)
    (h : c * (n * (n - 1)) * ρ ^ (n - 2) = 0) : n = 0 ∨ n = 1 := by
  have hp : ρ ^ (n - 2) ≠ 0 := (Real.rpow_pos_of_pos hρ _).ne'
  have h2 : c * (n * (n - 1)) = 0 := (mul_eq_zero.mp h).resolve_right hp
  have h3 : n * (n - 1) = 0 := (mul_eq_zero.mp h2).resolve_left hc.ne'
  rcases mul_eq_zero.mp h3 with h4 | h4
  · exact Or.inl h4
  · exact Or.inr (by linarith)

#print axioms theoremA_forward
#print axioms theoremA_converse
#print axioms einstein_direction
#print axioms robust_V
#print axioms robust_F2
#print axioms power_branch

end VossThmA
