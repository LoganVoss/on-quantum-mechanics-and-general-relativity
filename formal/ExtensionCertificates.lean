import ThmA

/-!
# Algebraic certificates for the frozen research extensions

These declarations certify explicit scalar residual maps, inverses, bounds,
and rational energy/force formulas. The geometric derivation of the residuals,
the source/matter calibration, the identification of coordinate derivatives,
and the quantum operator construction are NOT premises proved in this file.
In particular, no variational field theorem or continuum quantum dynamics is
claimed here. The source assumptions remain in the accompanying derivations.

The real scalar h in the energy formulas denotes the calibrated product ℏω.
-/

noncomputable section
namespace VossExtensionCertificates

def helicalTT (pitch norm f w potential : ℝ) : ℝ :=
  pitch ^ 2 * (f - w) / norm + potential * norm / 2

def helicalRR (pitch norm f w potential : ℝ) : ℝ :=
  pitch ^ 2 * (f - w) / norm - potential * norm / 2

/-- Invert the two specified helical metric-residual expressions. -/
theorem helical_inverse (pitch norm f w potential : ℝ)
    (hp : pitch ≠ 0) (hn : norm ≠ 0) :
    f - w = norm * (helicalTT pitch norm f w potential +
      helicalRR pitch norm f w potential) / (2 * pitch ^ 2) ∧
    potential = (helicalTT pitch norm f w potential -
      helicalRR pitch norm f w potential) / norm := by
  constructor
  · dsimp [helicalTT, helicalRR]
    field_simp
    ring
  · dsimp [helicalTT, helicalRR]
    field_simp
    ring

/-- Vanishing of these calibrated residuals selects the relative constants. -/
theorem helical_selection (pitch norm f w potential : ℝ)
    (hp : pitch ≠ 0) (hn : norm ≠ 0) :
    (helicalTT pitch norm f w potential = 0 ∧
      helicalRR pitch norm f w potential = 0) ↔ (f = w ∧ potential = 0) := by
  constructor
  · rintro ⟨hT, hR⟩
    obtain ⟨hfw, hV⟩ := helical_inverse pitch norm f w potential hp hn
    simp only [hT, hR, add_zero, sub_zero, mul_zero, zero_div] at hfw hV
    exact ⟨sub_eq_zero.mp hfw, hV⟩
  · rintro ⟨hfw, hV⟩
    simp [helicalTT, helicalRR, hfw, hV]

/-- Pointwise residual bounds, in the declared metric-component normalization. -/
theorem helical_error_bounds (pitch norm f w potential ε : ℝ)
    (hp : pitch ≠ 0) (hn : 0 < norm)
    (hT : |helicalTT pitch norm f w potential| ≤ ε)
    (hR : |helicalRR pitch norm f w potential| ≤ ε) :
    |f - w| ≤ norm * ε / pitch ^ 2 ∧ |potential| ≤ 2 * ε / norm := by
  obtain ⟨hfw, hV⟩ := helical_inverse pitch norm f w potential hp hn.ne'
  have hp2 : 0 < pitch ^ 2 := sq_pos_of_ne_zero hp
  have hs : |helicalTT pitch norm f w potential +
      helicalRR pitch norm f w potential| ≤ 2 * ε := by
    calc
      _ ≤ |helicalTT pitch norm f w potential| +
          |helicalRR pitch norm f w potential| := abs_add _ _
      _ ≤ ε + ε := add_le_add hT hR
      _ = 2 * ε := by ring
  have hd : |helicalTT pitch norm f w potential -
      helicalRR pitch norm f w potential| ≤ 2 * ε := by
    calc
      _ ≤ |helicalTT pitch norm f w potential| +
          |helicalRR pitch norm f w potential| := abs_sub _ _
      _ ≤ ε + ε := add_le_add hT hR
      _ = 2 * ε := by ring
  constructor
  · rw [hfw, abs_div, abs_mul, abs_of_pos hn,
      abs_of_pos (show 0 < 2 * pitch ^ 2 by positivity)]
    apply (div_le_iff₀ (show 0 < 2 * pitch ^ 2 by positivity)).2
    calc
      _ ≤ norm * (2 * ε) := mul_le_mul_of_nonneg_left hs hn.le
      _ = (norm * ε / pitch ^ 2) * (2 * pitch ^ 2) := by
        field_simp
        ring
  · rw [hV, abs_div, abs_of_pos hn]
    exact div_le_div_of_nonneg_right hd hn.le

/-- Zero pitch loses the relative-coupling constraint, even at nonzero norm. -/
theorem zero_pitch_counterexample (norm f w : ℝ) :
    helicalTT 0 norm f w 0 = 0 ∧ helicalRR 0 norm f w 0 = 0 := by
  simp [helicalTT, helicalRR]

def dustResidual (α β : ℝ) : ℝ := -16 * α - (16 / 3 : ℝ) * β
def electrovacResidual (β : ℝ) : ℝ := -(13 / 8748 : ℝ) * β

/-- Exact inverse of the stipulated dust and electrovac calibration components. -/
theorem sourced_inverse (α β : ℝ) :
    β = -(8748 / 13 : ℝ) * electrovacResidual β ∧
    α = -dustResidual α β / 16 + (2916 / 13 : ℝ) * electrovacResidual β := by
  constructor <;> dsimp [dustResidual, electrovacResidual] <;> ring

/-- The two explicit source-residual expressions vanish exactly at α=β=0. -/
theorem sourced_selection (α β : ℝ) :
    (dustResidual α β = 0 ∧ electrovacResidual β = 0) ↔ (α = 0 ∧ β = 0) := by
  constructor
  · rintro ⟨hD, hR⟩
    obtain ⟨hb, ha⟩ := sourced_inverse α β
    simp only [hD, hR, mul_zero, neg_zero, zero_div, zero_add] at hb ha
    exact ⟨ha, hb⟩
  · rintro ⟨ha, hb⟩
    simp [dustResidual, electrovacResidual, ha, hb]

/-- Calibrated curvature coefficients are bounded by the two residual errors. -/
theorem sourced_error_bounds (α β εD εR : ℝ)
    (hD : |dustResidual α β| ≤ εD)
    (hR : |electrovacResidual β| ≤ εR) :
    |β| ≤ (8748 / 13 : ℝ) * εR ∧
    |α| ≤ εD / 16 + (2916 / 13 : ℝ) * εR := by
  obtain ⟨hb, ha⟩ := sourced_inverse α β
  obtain ⟨d1, d2⟩ := abs_le.mp hD
  obtain ⟨r1, r2⟩ := abs_le.mp hR
  constructor <;> apply abs_le.mpr <;> constructor <;> linarith

def tensorResponse (β z : ℝ) : ℝ := 1 / (1 - β * z)
def scalarResponse (α β z : ℝ) : ℝ := 1 / (1 + (6 * α + 2 * β) * z)
def inverseResponseResidual (response z : ℝ) : ℝ := (1 / response - 1) / z

/-- Recover α,β from the assumed finite nonzero two-channel transfer functions. -/
theorem two_channel_response_inverse (α β z : ℝ)
    (hz : z ≠ 0) (h2 : 1 - β * z ≠ 0)
    (h0 : 1 + (6 * α + 2 * β) * z ≠ 0) :
    tensorResponse β z ≠ 0 ∧ scalarResponse α β z ≠ 0 ∧
    β = -inverseResponseResidual (tensorResponse β z) z ∧
    α = (inverseResponseResidual (scalarResponse α β z) z +
      2 * inverseResponseResidual (tensorResponse β z) z) / 6 := by
  refine ⟨one_div_ne_zero h2, one_div_ne_zero h0, ?_, ?_⟩
  · dsimp [inverseResponseResidual, tensorResponse]
    field_simp
  · dsimp [inverseResponseResidual, tensorResponse, scalarResponse]
    field_simp
    ring

/-- Error amplification of the exact affine two-channel inverse. -/
theorem response_error_bounds (δ0 δ2 ε0 ε2 : ℝ)
    (h0 : |δ0| ≤ ε0) (h2 : |δ2| ≤ ε2) :
    |(δ0 + 2 * δ2) / 6| ≤ (ε0 + 2 * ε2) / 6 ∧ |-δ2| ≤ ε2 := by
  obtain ⟨a, b⟩ := abs_le.mp h0
  obtain ⟨c, d⟩ := abs_le.mp h2
  constructor
  · exact abs_le.mpr ⟨by linarith, by linarith⟩
  · simpa only [abs_neg] using h2

def mismatchEnergy (h x y u v : ℝ) : ℝ :=
  h * ((x - u) ^ 2 + (y - v) ^ 2) / (4 * y * v)

/-- Positivity of the coordinate mismatch energy on the upper half-plane. -/
theorem mismatch_energy_nonnegative (h x y u v : ℝ)
    (hh : 0 ≤ h) (hy : 0 < y) (hv : 0 < v) :
    0 ≤ mismatchEnergy h x y u v := by
  unfold mismatchEnergy
  positivity

/-- At positive calibrated gap, zero mismatch energy is exactly coordinate match. -/
theorem mismatch_energy_zero_iff (h x y u v : ℝ)
    (hh : 0 < h) (hy : 0 < y) (hv : 0 < v) :
    mismatchEnergy h x y u v = 0 ↔ (x = u ∧ y = v) := by
  constructor
  · intro hz
    unfold mismatchEnergy at hz
    have hd : 4 * y * v ≠ 0 := ne_of_gt (by positivity)
    have hp := (div_eq_zero_iff.mp hz).resolve_right hd
    have hs := (mul_eq_zero.mp hp).resolve_left hh.ne'
    have hx2 : (x - u) ^ 2 = 0 := by nlinarith [sq_nonneg (y - v)]
    have hy2 : (y - v) ^ 2 = 0 := by nlinarith [sq_nonneg (x - u)]
    exact ⟨sub_eq_zero.mp (sq_eq_zero_iff.mp hx2),
      sub_eq_zero.mp (sq_eq_zero_iff.mp hy2)⟩
  · rintro ⟨hx, hyv⟩
    simp [mismatchEnergy, hx, hyv]

def mismatchDx (h x y u v : ℝ) : ℝ := h * (x - u) / (2 * y * v)
def mismatchDy (h x y u v : ℝ) : ℝ :=
  h * (y ^ 2 - v ^ 2 - (x - u) ^ 2) / (4 * y ^ 2 * v)

/-- Rational certificate for the pure-state energy/target-force relation.
The accompanying calculus identifies mismatchDx,mismatchDy as derivatives. -/
theorem pure_energy_force_identity (h x y u v : ℝ)
    (hy : y ≠ 0) (hv : v ≠ 0) :
    y ^ 2 * (mismatchDx h x y u v ^ 2 + mismatchDy h x y u v ^ 2) =
      mismatchEnergy h x y u v * (mismatchEnergy h x y u v + h) := by
  dsimp [mismatchDx, mismatchDy, mismatchEnergy]
  field_simp
  ring

def covarianceDet (n11 n12 n22 : ℝ) : ℝ := n11 * n22 - n12 ^ 2
def covarianceEnergy (h x y n11 n12 n22 : ℝ) : ℝ :=
  (h / 4) * (((x ^ 2 + y ^ 2) * n11 - 2 * x * n12 + n22) / y - 2)
def covarianceDx (h x y n11 n12 : ℝ) : ℝ := h * (x * n11 - n12) / (2 * y)
def covarianceDy (h x y n11 n12 n22 : ℝ) : ℝ :=
  h * ((y ^ 2 - x ^ 2) * n11 + 2 * x * n12 - n22) / (4 * y ^ 2)
def covarianceForceSquared (h x y n11 n12 n22 : ℝ) : ℝ :=
  y ^ 2 * (covarianceDx h x y n11 n12 ^ 2 +
    covarianceDy h x y n11 n12 n22 ^ 2)

/-- General covariance identity, with the determinant/uncertainty slack explicit. -/
theorem covariance_energy_force_identity (h x y n11 n12 n22 : ℝ)
    (hy : y ≠ 0) :
    covarianceForceSquared h x y n11 n12 n22 =
      covarianceEnergy h x y n11 n12 n22 *
        (covarianceEnergy h x y n11 n12 n22 + h) -
      h ^ 2 * (covarianceDet n11 n12 n22 - 1) / 4 := by
  dsimp [covarianceForceSquared, covarianceDx, covarianceDy,
    covarianceEnergy, covarianceDet]
  field_simp
  ring

/-- Restoring the oscillator ground offset rewrites the same force identity. -/
theorem shifted_energy_force_identity (h x y n11 n12 n22 : ℝ)
    (hy : y ≠ 0) :
    covarianceForceSquared h x y n11 n12 n22 =
      (covarianceEnergy h x y n11 n12 n22 + h / 2) ^ 2 -
        h ^ 2 * covarianceDet n11 n12 n22 / 4 := by
  rw [covariance_energy_force_identity h x y n11 n12 n22 hy]
  ring

/-- Uncertainty slack bounds the force; equality detects determinant saturation.
No reconstruction of a quantum density operator is formalized by this statement. -/
theorem covariance_force_bound_and_equality (h x y n11 n12 n22 : ℝ)
    (hh : 0 < h) (hy : y ≠ 0) (hdet : 1 ≤ covarianceDet n11 n12 n22) :
    covarianceForceSquared h x y n11 n12 n22 ≤
      covarianceEnergy h x y n11 n12 n22 *
        (covarianceEnergy h x y n11 n12 n22 + h) ∧
    (covarianceForceSquared h x y n11 n12 n22 =
      covarianceEnergy h x y n11 n12 n22 *
        (covarianceEnergy h x y n11 n12 n22 + h) ↔
      covarianceDet n11 n12 n22 = 1) := by
  have hi := covariance_energy_force_identity h x y n11 n12 n22 hy
  have hh2 : 0 < h ^ 2 := sq_pos_of_pos hh
  have slack : 0 ≤ h ^ 2 * (covarianceDet n11 n12 n22 - 1) :=
    mul_nonneg (sq_nonneg h) (sub_nonneg.mpr hdet)
  constructor
  · linarith
  · constructor
    · intro he
      nlinarith
    · intro hd
      rw [hd] at hi
      simpa only [sub_self, mul_zero, zero_div, sub_zero] using hi

#print axioms helical_inverse
#print axioms helical_selection
#print axioms helical_error_bounds
#print axioms zero_pitch_counterexample
#print axioms sourced_inverse
#print axioms sourced_selection
#print axioms sourced_error_bounds
#print axioms two_channel_response_inverse
#print axioms response_error_bounds
#print axioms mismatch_energy_nonnegative
#print axioms mismatch_energy_zero_iff
#print axioms pure_energy_force_identity
#print axioms covariance_energy_force_identity
#print axioms shifted_energy_force_identity
#print axioms covariance_force_bound_and_equality

end VossExtensionCertificates
