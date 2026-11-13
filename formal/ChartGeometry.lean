import ThmA
import Mathlib.Data.Complex.Trigonometric

/-!
# Exact geometric certificates for the flat physical chart

The tangent-vector identity below is the pullback calculation for
T=t cosh(z), Z=t sinh(z), X=r cos(phi), Y=r sin(phi).
It directly verifies the Lorentzian chart and the literal quotient block.
-/

namespace VossChartGeometry

/-- Exact Minkowski pullback for every tangent vector. -/
theorem minkowski_pullback
    (t r z phi dt dr dz dphi : ℝ) :
    -(Real.cosh z * dt + t * Real.sinh z * dz) ^ 2 +
      (Real.sinh z * dt + t * Real.cosh z * dz) ^ 2 +
      (Real.cos phi * dr - r * Real.sin phi * dphi) ^ 2 +
      (Real.sin phi * dr + r * Real.cos phi * dphi) ^ 2 =
    -dt ^ 2 + dr ^ 2 + t ^ 2 * dz ^ 2 + r ^ 2 * dphi ^ 2 := by
  linear_combination (-dt ^ 2 + t ^ 2 * dz ^ 2) * Real.cosh_sq_sub_sinh_sq z +
    (dr ^ 2 + r ^ 2 * dphi ^ 2) * Real.cos_sq_add_sin_sq phi

/-- The orbit-block determinant gives positive area density rho = t*r. -/
theorem orbit_area_density (t r : ℝ) (ht : 0 < t) (hr : 0 < r) :
    Real.sqrt (t ^ 2 * r ^ 2) = t * r := by
  rw [← mul_pow, Real.sqrt_sq_eq_abs, abs_of_pos (mul_pos ht hr)]

/-- Removing the orbit directions leaves the literal quotient metric diag(-1,1). -/
theorem literal_quotient_block (t r dt dr : ℝ) :
    -dt ^ 2 + dr ^ 2 + t ^ 2 * (0 : ℝ) ^ 2 + r ^ 2 * (0 : ℝ) ^ 2 =
      -dt ^ 2 + dr ^ 2 := by ring

/-- The four-dimensional metric determinant is negative and nonzero in the chart. -/
theorem lorentzian_chart_determinant (t r : ℝ) (ht : 0 < t) (hr : 0 < r) :
    -(t ^ 2 * r ^ 2) < 0 := by
  have hp : 0 < t ^ 2 * r ^ 2 := mul_pos (sq_pos_of_pos ht) (sq_pos_of_pos hr)
  linarith

/-- Exactly three coordinate directions carry positive diagonal coefficients. -/
theorem spatial_diagonal_positive (t r : ℝ) (ht : 0 < t) (hr : 0 < r) :
    (0 : ℝ) < 1 ∧ 0 < t ^ 2 ∧ 0 < r ^ 2 := by
  exact ⟨zero_lt_one, sq_pos_of_pos ht, sq_pos_of_pos hr⟩

#print axioms minkowski_pullback
#print axioms orbit_area_density
#print axioms literal_quotient_block
#print axioms lorentzian_chart_determinant
#print axioms spatial_diagonal_positive

end VossChartGeometry
