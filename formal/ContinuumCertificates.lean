import ThmA
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# Scalar certificates for the controlled population/current estimates

These results use genuine derivative hypotheses for the scalar comparison and
explicit numerical inequalities for the remaining estimates. They do not
formalize operator commutator estimates, density matrices, the Casimir operator
identity, material quadrature, field equations, or a quantum continuum limit.
Those preceding mathematical obligations remain external to these signatures.

N is a positive real population parameter; integer populations are a subcase.
The diagonal is parameterized by 0 < s ≤ 1, h=s^5 and eta=s^2, avoiding any
implicit convention for fractional powers. All constants are retained.
-/

noncomputable section
namespace VossContinuumCertificates
open Set

/-- Young's inequality closes the explicitly given squared-deviation estimate. -/
theorem population_young_bound (D a b N : ℝ) (hD : 0 ≤ D) :
    2 * Real.sqrt D * (a * Real.sqrt D + b / N) ≤
      (2 * a + 1) * D + b ^ 2 / N ^ 2 := by
  have hs := sq_nonneg (Real.sqrt D - b / N)
  have hroot := Real.sq_sqrt hD
  have hc : 2 * Real.sqrt D * (b / N) ≤ D + (b / N) ^ 2 := by nlinarith
  have he : 2 * Real.sqrt D * (a * Real.sqrt D + b / N) =
      2 * a * D + 2 * Real.sqrt D * (b / N) := by
    calc
      _ = 2 * a * (Real.sqrt D) ^ 2 + 2 * Real.sqrt D * (b / N) := by ring
      _ = _ := by rw [hroot]
  rw [← div_pow]
  linarith

/-- A convenient exponential envelope for Mathlib's exact Gronwall bound. -/
theorem gronwall_bound_le_exponential (D0 C B t : ℝ)
    (hC : 0 ≤ C) (hB : 0 ≤ B) :
    gronwallBound D0 C B t ≤ Real.exp (C * t) * (D0 + B * t) := by
  by_cases hzero : C = 0
  · simp [hzero, gronwallBound_K0]
  · have hCp : 0 < C := lt_of_le_of_ne hC (Ne.symm hzero)
    rw [gronwallBound_of_K_ne_0 hzero]
    have hex : Real.exp (C * t) * Real.exp (-(C * t)) = 1 := by
      rw [← Real.exp_add]
      simp
    have he : Real.exp (C * t) - 1 ≤ (C * t) * Real.exp (C * t) := by
      have h := mul_le_mul_of_nonneg_left (Real.add_one_le_exp (-(C * t)))
        (Real.exp_pos (C * t)).le
      rw [hex] at h
      nlinarith
    have hm := mul_le_mul_of_nonneg_left he (div_nonneg hB hCp.le)
    calc
      _ ≤ D0 * Real.exp (C * t) + B / C * ((C * t) * Real.exp (C * t)) :=
        add_le_add_left hm _
      _ = Real.exp (C * t) * (D0 + B * t) := by
        field_simp
        ring

/-- Genuine right derivatives and the stated scalar differential inequality
give the population envelope throughout the closed time interval. -/
theorem population_gronwall (D Dprime : ℝ → ℝ) (C B N T : ℝ)
    (hC : 0 ≤ C) (hB : 0 ≤ B) (hN : 0 < N)
    (hcont : ContinuousOn D (Icc 0 T))
    (hderiv : ∀ t ∈ Ico 0 T, HasDerivWithinAt D (Dprime t) (Ici t) t)
    (hbound : ∀ t ∈ Ico 0 T, Dprime t ≤ C * D t + B / N ^ 2) :
    ∀ t ∈ Icc 0 T,
      D t ≤ Real.exp (C * t) * (D 0 + B * t / N ^ 2) := by
  have hG := le_gronwallBound_of_liminf_deriv_right_le hcont
    (fun t ht r hr => (hderiv t ht).liminf_right_slope_le hr)
    (le_refl (D 0)) hbound
  intro t ht
  have h := (hG t ht).trans
    (gronwall_bound_le_exponential (D 0) C (B / N ^ 2) (t - 0)
      hC (div_nonneg hB (sq_pos_of_pos hN).le))
  simpa only [sub_zero, div_mul_eq_mul_div] using h

/-- Consequences of the supplied scalar Casimir/depletion relation. -/
theorem casimir_depletion_bounds (S β d N : ℝ)
    (hβ : 0 ≤ β) (hd : 1 ≤ d) (hN : 0 < N)
    (hS : S = 2 * β + (d - 1) / N) :
    0 ≤ S ∧ 2 * β ≤ S ∧ β ≤ S / 2 := by
  have hrest : 0 ≤ (d - 1) / N := div_nonneg (sub_nonneg.mpr hd) hN.le
  constructor
  · linarith
  constructor <;> linarith

/-- A supplied pure-target marginal estimate composes with Casimir control.
The density-operator inequalities themselves are not assumed as new axioms. -/
theorem casimir_marginal_bound (S β d N k error : ℝ)
    (hβ : 0 ≤ β) (hd : 1 ≤ d) (hN : 0 < N) (hk : 0 ≤ k)
    (hS : S = 2 * β + (d - 1) / N)
    (herr : error ≤ 2 * Real.sqrt (k * β)) :
    error ≤ Real.sqrt (2 * k * S) := by
  obtain ⟨_, hbeta, _⟩ := casimir_depletion_bounds S β d N hβ hd hN hS
  apply herr.trans
  apply Real.le_sqrt_of_sq_le
  rw [mul_pow, Real.sq_sqrt (mul_nonneg hk hβ)]
  nlinarith [mul_le_mul_of_nonneg_left hbeta hk]

/-- Scalar quadratic-current error from a full absolute deviation bound. -/
theorem quadratic_current_difference (x y δ : ℝ)
    (hδ : 0 ≤ δ) (herr : |x - y| ≤ δ) :
    |x ^ 2 - y ^ 2| ≤ δ * (2 * |y| + δ) := by
  have heq : x ^ 2 - y ^ 2 = (x - y) * (x + y) := by ring
  have hsum : |x + y| ≤ 2 * |y| + δ := by
    calc
      _ = |(x - y) + (y + y)| := by congr 1; ring
      _ ≤ |x - y| + |y + y| := abs_add _ _
      _ ≤ δ + (|y| + |y|) := add_le_add herr (abs_add _ _)
      _ = 2 * |y| + δ := by ring
  rw [heq, abs_mul]
  exact mul_le_mul herr hsum (abs_nonneg _) hδ

/-- A bounded quadratic form obeys the same contact-error estimate, including
indefinite metric contractions. This is a real Hilbert-space statement; the
preceding quantum/kernel RMS estimate is not formalized here. -/
theorem bounded_quadratic_current_difference
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (A : E →L[ℝ] E) (x y : E) (δ : ℝ)
    (hδ : 0 ≤ δ) (herr : ‖x - y‖ ≤ δ) :
    |@inner ℝ E _ x (A x) - @inner ℝ E _ y (A y)| ≤
      ‖A‖ * δ * (2 * ‖y‖ + δ) := by
  have heq : @inner ℝ E _ x (A x) - @inner ℝ E _ y (A y) =
      @inner ℝ E _ (x - y) (A (x - y)) + @inner ℝ E _ (x - y) (A y) +
      @inner ℝ E _ y (A (x - y)) := by
    simp only [map_sub, inner_sub_left, inner_sub_right]
    ring
  have hA : ‖A (x - y)‖ ≤ ‖A‖ * δ :=
    (A.le_opNorm (x - y)).trans (mul_le_mul_of_nonneg_left herr (norm_nonneg A))
  have h1 : |@inner ℝ E _ (x - y) (A (x - y))| ≤ δ * (‖A‖ * δ) :=
    (abs_real_inner_le_norm _ _).trans
      (mul_le_mul herr hA (norm_nonneg _) hδ)
  have h2 : |@inner ℝ E _ (x - y) (A y)| ≤ δ * (‖A‖ * ‖y‖) :=
    (abs_real_inner_le_norm _ _).trans
      (mul_le_mul herr (A.le_opNorm y) (norm_nonneg _) hδ)
  have h3 : |@inner ℝ E _ y (A (x - y))| ≤ ‖y‖ * (‖A‖ * δ) :=
    (abs_real_inner_le_norm _ _).trans
      (mul_le_mul_of_nonneg_left hA (norm_nonneg y))
  rw [heq]
  calc
    _ ≤ |@inner ℝ E _ (x - y) (A (x - y)) + @inner ℝ E _ (x - y) (A y)| +
        |@inner ℝ E _ y (A (x - y))| := abs_add _ _
    _ ≤ (|@inner ℝ E _ (x - y) (A (x - y))| + |@inner ℝ E _ (x - y) (A y)|) +
        |@inner ℝ E _ y (A (x - y))| := add_le_add_right (abs_add _ _) _
    _ ≤ (δ * (‖A‖ * δ) + δ * (‖A‖ * ‖y‖)) + ‖y‖ * (‖A‖ * δ) :=
        add_le_add (add_le_add h1 h2) h3
    _ = ‖A‖ * δ * (2 * ‖y‖ + δ) := by ring

/-- The explicit large-population choice makes the parcel RMS envelope ≤s^8. -/
theorem diagonal_population_rms (s A N δ : ℝ)
    (hs : 0 < s) (hA : 0 ≤ A) (hN : 0 < N)
    (hpop : A ^ 2 / s ^ 26 ≤ N)
    (hrms : δ ≤ A / Real.sqrt (N * (s ^ 5) ^ 2)) :
    δ ≤ s ^ 8 := by
  have hp : 0 < N * (s ^ 5) ^ 2 := by positivity
  have hroot : (Real.sqrt (N * (s ^ 5) ^ 2)) ^ 2 = N * (s ^ 5) ^ 2 :=
    Real.sq_sqrt hp.le
  have hlarge : A ^ 2 ≤ N * s ^ 26 :=
    (div_le_iff₀ (pow_pos hs 26)).mp hpop
  have hsq : (s ^ 8 * Real.sqrt (N * (s ^ 5) ^ 2)) ^ 2 = N * s ^ 26 := by
    rw [mul_pow, hroot]
    ring
  have ha : A ≤ s ^ 8 * Real.sqrt (N * (s ^ 5) ^ 2) := by
    apply (sq_le_sq₀ hA (by positivity)).mp
    rw [hsq]
    exact hlarge
  apply hrms.trans
  exact (div_le_iff₀ (Real.sqrt_pos.mpr hp)).mpr ha

/-- Exact integer-power balances for d=2, h=s^5 and eta=s^2. -/
theorem diagonal_kernel_identities (s : ℝ) (hs : s ≠ 0) :
    (s ^ 2) ^ 2 = s ^ 4 ∧
    (s ^ 5) ^ 2 / (s ^ 2) ^ 3 = s ^ 4 ∧
    s ^ 8 / (s ^ 2) ^ 2 = s ^ 4 ∧
    s ^ 8 / s ^ 2 = s ^ 6 := by
  constructor
  · ring
  constructor
  · field_simp
    ring
  constructor
  · field_simp
    ring
  · field_simp
    ring

/-- The four normalized bias/quadrature/path/amplitude terms sum to ≤4s^4.
External kernel/material constants multiply this scalar estimate separately. -/
theorem diagonal_current_rate (s δpath δamp : ℝ)
    (hs : 0 < s) (hs1 : s ≤ 1)
    (hp : δpath ≤ s ^ 8) (ha : δamp ≤ s ^ 8) :
    (s ^ 2) ^ 2 + (s ^ 5) ^ 2 / (s ^ 2) ^ 3 +
      δpath / (s ^ 2) ^ 2 + δamp / s ^ 2 ≤ 4 * s ^ 4 := by
  obtain ⟨h1, h2, h3, h4⟩ := diagonal_kernel_identities s hs.ne'
  have hpath : δpath / (s ^ 2) ^ 2 ≤ s ^ 4 := by
    rw [← h3]
    exact div_le_div_of_nonneg_right hp (by positivity)
  have hamp : δamp / s ^ 2 ≤ s ^ 6 := by
    rw [← h4]
    exact div_le_div_of_nonneg_right ha (sq_nonneg s)
  have hs2 : s ^ 2 ≤ 1 := by nlinarith
  have hs64 : s ^ 6 ≤ s ^ 4 := by
    calc
      s ^ 6 = s ^ 4 * s ^ 2 := by ring
      _ ≤ s ^ 4 * 1 := mul_le_mul_of_nonneg_left hs2 (by positivity)
      _ = s ^ 4 := by ring
  rw [h1, h2]
  rw [h1] at hpath
  linarith

/-- A≥1 controls integer-population rounding under the same diagonal. -/
theorem diagonal_rounding_rate (s A N : ℝ)
    (hs : 0 < s) (hs1 : s ≤ 1) (hA : 1 ≤ A) (hN : 0 < N)
    (hpop : A ^ 2 / s ^ 26 ≤ N) :
    1 / (N * (s ^ 5) ^ 2 * s ^ 2) ≤ s ^ 14 ∧ s ^ 14 ≤ s ^ 4 := by
  have hA2 : 1 ≤ A ^ 2 := by nlinarith
  have hlarge : A ^ 2 ≤ N * s ^ 26 :=
    (div_le_iff₀ (pow_pos hs 26)).mp hpop
  constructor
  · apply (div_le_iff₀ (show 0 < N * (s ^ 5) ^ 2 * s ^ 2 by positivity)).mpr
    have heq : s ^ 14 * (N * (s ^ 5) ^ 2 * s ^ 2) = N * s ^ 26 := by ring
    rw [heq]
    linarith
  · have hs10 : s ^ 10 ≤ 1 := pow_le_one₀ hs.le hs1
    calc
      s ^ 14 = s ^ 4 * s ^ 10 := by ring
      _ ≤ s ^ 4 * 1 := mul_le_mul_of_nonneg_left hs10 (by positivity)
      _ = s ^ 4 := by ring

/-- Positive rest mass supplies a regular clock denominator and Legendre identity.
kinetic is the nonnegative squared spatial momentum in a fixed local metric. -/
theorem positive_mass_clock (m0 internal kinetic : ℝ)
    (hm : 0 < m0) (hi : 0 ≤ internal) (hk : 0 ≤ kinetic) :
    let mass := m0 + internal
    let energy := Real.sqrt (kinetic + mass ^ 2)
    0 < energy ∧ 0 < mass / energy ∧ mass / energy ≤ 1 ∧
      kinetic / energy - energy = -mass * (mass / energy) := by
  dsimp
  have hmpos : 0 < m0 + internal := by linarith
  have hepos : 0 < Real.sqrt (kinetic + (m0 + internal) ^ 2) :=
    Real.sqrt_pos.mpr (by nlinarith)
  have hemass : m0 + internal ≤ Real.sqrt (kinetic + (m0 + internal) ^ 2) :=
    Real.le_sqrt_of_sq_le (by linarith)
  have hesq := Real.sq_sqrt (show 0 ≤ kinetic + (m0 + internal) ^ 2 by positivity)
  refine ⟨hepos, div_pos hmpos hepos, ?_, ?_⟩
  · exact (div_le_one hepos).mpr hemass
  · apply (mul_right_cancel₀ hepos.ne')
    field_simp
    nlinarith

#print axioms population_young_bound
#print axioms gronwall_bound_le_exponential
#print axioms population_gronwall
#print axioms casimir_depletion_bounds
#print axioms casimir_marginal_bound
#print axioms quadratic_current_difference
#print axioms bounded_quadratic_current_difference
#print axioms diagonal_population_rms
#print axioms diagonal_kernel_identities
#print axioms diagonal_current_rate
#print axioms diagonal_rounding_rate
#print axioms positive_mass_clock

end VossContinuumCertificates
