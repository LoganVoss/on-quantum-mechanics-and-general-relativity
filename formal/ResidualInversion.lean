import ThmA

/-!
# Exact inversion of division-form chart residuals

At a fixed positive area ρ, the four diagonal residuals come from the two
chart points (2√ρ, √ρ/2) and (√ρ/2, 2√ρ). The mixed residual is the fifth
measurement. These theorems are finite algebraic identities and error bounds;
they do not assert physical measurement errors or dynamical stability.

The intended physical chart has ρ > 0. The algebraic identities also hold
for all real ρ under Lean's total division convention.
F1 and F2 are scalar labels here; genuine derivative identifications are
required separately to interpret them as F′ and F″.
-/

noncomputable section
namespace VossResidualInversion

def r1 (ρ F2 U W V : ℝ) : ℝ :=
  -4 * ρ * F2 + (17 * ρ / 8) * U - 17 * W / (16 * ρ) + V / 2

def r2 (ρ F2 U W V : ℝ) : ℝ :=
  -ρ * F2 / 4 + (17 * ρ / 8) * U - 17 * W / (16 * ρ) - V / 2

def r3 (ρ F2 U W V : ℝ) : ℝ :=
  -ρ * F2 / 4 + (17 * ρ / 8) * U - 17 * W / (16 * ρ) + V / 2

def r4 (ρ F2 U W V : ℝ) : ℝ :=
  -4 * ρ * F2 + (17 * ρ / 8) * U - 17 * W / (16 * ρ) - V / 2

def r5 (ρ F1 F2 U W : ℝ) : ℝ := -ρ * F2 - F1 + ρ * U + W / (2 * ρ)

theorem invert_potential (ρ F2 U W V : ℝ) :
    V = (r1 ρ F2 U W V - r2 ρ F2 U W V +
      r3 ρ F2 U W V - r4 ρ F2 U W V) / 2 := by
  dsimp [r1, r2, r3, r4]
  ring

theorem invert_second_derivative (ρ F2 U W V : ℝ) :
    ρ * F2 = (2 / 15 : ℝ) * (-r1 ρ F2 U W V + r2 ρ F2 U W V +
      r3 ρ F2 U W V - r4 ρ F2 U W V) := by
  dsimp [r1, r2, r3, r4]
  ring

theorem invert_shape (ρ F1 F2 U W V : ℝ) :
    W / ρ - F1 = r5 ρ F1 F2 U W - (2 / 17 : ℝ) *
      (r1 ρ F2 U W V + r2 ρ F2 U W V + r3 ρ F2 U W V + r4 ρ F2 U W V) := by
  dsimp [r1, r2, r3, r4, r5]
  ring

theorem invert_area (ρ F1 F2 U W V : ℝ) :
    2 * ρ * U - F1 = r5 ρ F1 F2 U W +
      (-38 * r1 ρ F2 U W V + 98 * r2 ρ F2 U W V +
        98 * r3 ρ F2 U W V - 38 * r4 ρ F2 U W V) / 255 := by
  dsimp [r1, r2, r3, r4, r5]
  ring

theorem potential_bound (ρ F2 U W V ε : ℝ)
    (h1 : |r1 ρ F2 U W V| ≤ ε) (h2 : |r2 ρ F2 U W V| ≤ ε)
    (h3 : |r3 ρ F2 U W V| ≤ ε) (h4 : |r4 ρ F2 U W V| ≤ ε) :
    |V| ≤ 2 * ε := by
  have h := invert_potential ρ F2 U W V
  obtain ⟨a, b⟩ := abs_le.mp h1
  obtain ⟨c, d⟩ := abs_le.mp h2
  obtain ⟨e, f⟩ := abs_le.mp h3
  obtain ⟨g, i⟩ := abs_le.mp h4
  exact abs_le.mpr ⟨by linarith, by linarith⟩

theorem second_derivative_bound (ρ F2 U W V ε : ℝ)
    (h1 : |r1 ρ F2 U W V| ≤ ε) (h2 : |r2 ρ F2 U W V| ≤ ε)
    (h3 : |r3 ρ F2 U W V| ≤ ε) (h4 : |r4 ρ F2 U W V| ≤ ε) :
    |ρ * F2| ≤ 8 * ε / 15 := by
  have h := invert_second_derivative ρ F2 U W V
  obtain ⟨a, b⟩ := abs_le.mp h1
  obtain ⟨c, d⟩ := abs_le.mp h2
  obtain ⟨e, f⟩ := abs_le.mp h3
  obtain ⟨g, i⟩ := abs_le.mp h4
  exact abs_le.mpr ⟨by linarith, by linarith⟩

theorem shape_bound (ρ F1 F2 U W V ε : ℝ)
    (h1 : |r1 ρ F2 U W V| ≤ ε) (h2 : |r2 ρ F2 U W V| ≤ ε)
    (h3 : |r3 ρ F2 U W V| ≤ ε) (h4 : |r4 ρ F2 U W V| ≤ ε)
    (h5 : |r5 ρ F1 F2 U W| ≤ ε) :
    |W / ρ - F1| ≤ 25 * ε / 17 := by
  have h := invert_shape ρ F1 F2 U W V
  obtain ⟨a, b⟩ := abs_le.mp h1
  obtain ⟨c, d⟩ := abs_le.mp h2
  obtain ⟨e, f⟩ := abs_le.mp h3
  obtain ⟨g, i⟩ := abs_le.mp h4
  obtain ⟨j, k⟩ := abs_le.mp h5
  exact abs_le.mpr ⟨by linarith, by linarith⟩

theorem area_bound (ρ F1 F2 U W V ε : ℝ)
    (h1 : |r1 ρ F2 U W V| ≤ ε) (h2 : |r2 ρ F2 U W V| ≤ ε)
    (h3 : |r3 ρ F2 U W V| ≤ ε) (h4 : |r4 ρ F2 U W V| ≤ ε)
    (h5 : |r5 ρ F1 F2 U W| ≤ ε) :
    |2 * ρ * U - F1| ≤ 31 * ε / 15 := by
  have h := invert_area ρ F1 F2 U W V
  obtain ⟨a, b⟩ := abs_le.mp h1
  obtain ⟨c, d⟩ := abs_le.mp h2
  obtain ⟨e, f⟩ := abs_le.mp h3
  obtain ⟨g, i⟩ := abs_le.mp h4
  obtain ⟨j, k⟩ := abs_le.mp h5
  exact abs_le.mpr ⟨by linarith, by linarith⟩

#print axioms invert_potential
#print axioms invert_second_derivative
#print axioms invert_shape
#print axioms invert_area
#print axioms potential_bound
#print axioms second_derivative_bound
#print axioms shape_bound
#print axioms area_bound

end VossResidualInversion
