import Integrability
import Mathlib.Data.Matrix.Basic

/-!
# Curvature and spectral-curve certificates

Matrix products are represented by an arbitrary matrix C, which can be instantiated
with the noncommutative commutator [J+,J-].  No commutativity of current matrices is used.
-/

noncomputable section
namespace VossLaxCertificates
open VossIntegrability

/-- Entrywise curvature identity, retaining both the Maurer-Cartan and EOM terms. -/
theorem scalar_curvature_decomposition
    (s A B C Jp Jm wp wm : ℝ) (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0) :
    (1 / (1 + s)) * A - (1 / (1 - s)) * B +
      (1 / (1 - s)) * (1 / (1 + s)) * C -
      ((1 / (1 + s)) ^ 2 * spectralG s * wp) * Jm -
      ((1 / (1 - s)) ^ 2 * spectralH s * wm) * Jp =
    (A - B + C - s * (A + B + wp * Jm + wm * Jp)) /
      ((1 - s) * (1 + s)) := by
  dsimp [spectralG, spectralH]
  field_simp
  ring

/-- The same identity for arbitrary real matrices; C may be the actual commutator. -/
theorem matrix_curvature_decomposition {n : Type*}
    (s wp wm : ℝ) (A B C Jp Jm : Matrix n n ℝ)
    (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0) :
    (1 / (1 + s)) • A - (1 / (1 - s)) • B +
      ((1 / (1 - s)) * (1 / (1 + s))) • C -
      ((1 / (1 + s)) ^ 2 * spectralG s * wp) • Jm -
      ((1 / (1 - s)) ^ 2 * spectralH s * wm) • Jp =
    (1 / ((1 - s) * (1 + s))) •
      (A - B + C - s • (A + B + wp • Jm + wm • Jp)) := by
  ext i j
  simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
  have h := scalar_curvature_decomposition s (A i j) (B i j) (C i j)
    (Jp i j) (Jm i j) wp wm hm hp
  simpa only [div_eq_mul_inv, one_mul, mul_assoc, mul_comm, mul_left_comm] using h

/-- With Maurer-Cartan zero, a nonzero spectral value detects the EOM exactly. -/
theorem curvature_zero_iff_eom (s MC E : ℝ)
    (hs : s ≠ 0) (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0) (hMC : MC = 0) :
    (MC - s * E) / ((1 - s) * (1 + s)) = 0 ↔ E = 0 := by
  rw [hMC]
  have hd : (1 - s) * (1 + s) ≠ 0 := mul_ne_zero hm hp
  constructor
  · intro h
    have hz := (div_eq_zero_iff.mp h).resolve_right hd
    have hmul : s * E = 0 := by linarith
    exact (mul_eq_zero.mp hmul).resolve_left hs
  · intro h
    simp only [h, mul_zero, sub_zero, zero_div]

def spectralC (s : ℝ) : ℝ := (s + 1 / s) / 2
def spectralC1 (s : ℝ) : ℝ := (1 - 1 / s ^ 2) / 2

/-- The conserved spectral-curve coefficient has its stated derivative. -/
theorem spectralC_hasDerivAt (s : ℝ) (hs : s ≠ 0) :
    HasDerivAt spectralC (spectralC1 s) s := by
  have hi := (hasDerivAt_id s).inv hs
  have hd := ((hasDerivAt_id s).add hi).div_const 2
  change HasDerivAt (fun x : ℝ => (x + 1 / x) / 2) (spectralC1 s) s
  simpa only [spectralC1, id_eq, one_div, sub_eq_add_neg, neg_div] using hd

/-- These two identities prove ∂±[Z+W C(s)]=0 when Z+=W+, Z-=-W-. -/
theorem spectral_curve_coefficients (s : ℝ)
    (hs : s ≠ 0) (hm : 1 - s ≠ 0) (hp : 1 + s ≠ 0) :
    1 + spectralC s + spectralC1 s * spectralG s = 0 ∧
      -1 + spectralC s + spectralC1 s * spectralH s = 0 := by
  constructor
  · dsimp [spectralC, spectralC1, spectralG]
    field_simp
    ring
  · dsimp [spectralC, spectralC1, spectralH]
    field_simp
    ring

#print axioms scalar_curvature_decomposition
#print axioms matrix_curvature_decomposition
#print axioms curvature_zero_iff_eom
#print axioms spectralC_hasDerivAt
#print axioms spectral_curve_coefficients

end VossLaxCertificates
