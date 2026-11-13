# Frozen curvature-response research findings

Scratch research record, not a public deliverable. Calculations completed on November 13, 2026 before public extension writing. No original research repository files were changed.

## Exact class and conventions

Use signature (-,+,+,+), the Riemann/Ricci convention already fixed in the Voss bundle, and the normalized four-dimensional action

S = (1/(2κ)) ∫√−g [R + α R² + β R_ab R^ab + γ E4] d⁴x + S_m[g,matter],

with κ>0 and constant real coefficients. α,β have dimensions length². E4 is the four-dimensional Euler density; its constant coefficient is bulk-invisible with the appropriate boundary prescription. A constant □R term is also a boundary term. Matter and the meaning of the physical metric/source are fixed. No Killing ansatz is imposed in the action or its variations.

This is the parity-even constant-coefficient quadratic-curvature class after Gauss–Bonnet reduction. If the review uses unnormalized ΔS=∫√−g[A R²+B Ricci²], our α=2κA and β=2κB. The original selected gravity normalization “a” should not be confused with these deformation coefficients.

The exact equations are

G_ab + α H1_ab + β H2_ab = κ T_ab,

H1_ab = 2 R R_ab − (1/2)g_ab R² + 2(g_ab□−∇a∇b)R,

H2_ab = □R_ab + (1/2)g_ab□R − ∇a∇bR + 2R_acbd R^cd − (1/2)g_ab R_cdR^cd.

Equivalently, H2=2Bach+H1/3. The exact trace is

−R + (6α+2β)□R = κ T.

This agrees with the published Weyl-squared/R² equations after the precise basis conversion. The mathematical mechanism and quadratic-gravity spectrum are established; do not label them newly discovered physics.

## A. A complete full-4D sourced-calibration selector

**Theorem.** Within the above class with fixed κ and minimal source actions, require both (i) the stated spatially flat dust FLRW solution with its calibrated dust stress and (ii) the stated charged electrovac solution with its calibrated Maxwell field to remain solutions under unrestricted metric variation. This holds iff α=β=0. The constant Euler coefficient remains free.

**Dust calibration.** On t>0,

 ds²=−dt²+t^(4/3)(dx²+dy²+dz²),
 κρ_dust=4/(3t²), p_dust=0.

Direct curvature calculation gives R=4/(3t²), □R=−8/(3t⁴). Its Einstein tensor is diag(4/(3t²),0,0,0); stress conservation follows from ρdot+3Hρ=0, H=2/(3t). The fixed dust source already gives −R=κT. The exact quadratic trace therefore requires (6α+2β)□R=0. Since □R≠0 throughout this regular patch, 3α+β=0.

**Electrovac calibration.** In geometric units choose M=1, Q=1/2,

 f(r)=1−2/r+1/(4r²),
 ds²=−f dt²+f^(−1) dr²+r²(dθ²+sin²θ dφ²),
 F_tr=1/(2r²).

For the standard Maxwell action −(1/4)∫√−g F² and κ=2 in these units, all Maxwell equations and all sixteen Einstein–Maxwell equations hold. (For a general fixed κ, rescale the physical electric charge while keeping the geometric Q fixed.) R=0 exactly, so H1=0. Direct tensor differentiation gives

 H2^a_b = [(4r²−8r+1)/(4r⁸)] diag(−3,−1,2,2).

At r=3, the lapse is 13/36>0, safely outside the outer horizon, and

 H2^t_t = −13/8748 ≠0.

The fixed Maxwell stress continues to equal G/κ. Thus the quadratic correction can vanish only when β=0; the dust condition then gives α=0. Conversely those coefficients leave the two standard Einstein-matter solutions unchanged. The test is local on regular patches; no use of the singular center is made.

**Quantitative exact inverse.** In the displayed dimensionless calibration units let yD be the trace of the full gravitational-minus-source residual on dust at t=1, and yR its mixed t–t component on electrovac at r=3. Then

 (yD,yR)^T = [[−16,−16/3],[0,−13/8748]] (α,β)^T,
 det =52/2187,
 β=−(8748/13)yR,
 α=−yD/16+(2916/13)yR.

Consequently |yD|≤εD, |yR|≤εR imply

 |β|≤(8748/13)εR,
 |α|≤εD/16+(2916/13)εR.

The bounds are individually sharp in this two-residual norm because the map is invertible and the appropriate rectangle corners are attained by actual constant coefficient pairs. If physical lengths are restored with reference L0, use αbar=α/L0², βbar=β/L0² and ybar=L0² y for the displayed numerical matrix.

**Interpretation.** This is a genuine broader action-class discrimination result with finite concrete matter calibrations. It does not infer the new source/background premises from the original flat-vacuum theorem. If those sourced responses are stipulated, the conclusion is conditional; this is not empirical exclusion of measured corrections. Dust and charged geometry are established references. The class is unrestricted four-dimensional even though the informative calibration solutions are symmetric.

## B. Exact sourced linear response and robust inference

About Minkowski spacetime, for an arbitrary metric perturbation,

 (1+β□) G^L_ab +(2α+β)(η_ab□−∂a∂b)R^L =κT_ab.

The independent script obtains this by differentiating the quadratic curvature action in all ten symmetric amplitude variables, not by assuming the transfer functions. It also verifies the Bianchi identities and gauge-null directions.

For Fourier exp(ik·x), put z=k²>0, so □→−z. Decompose a conserved source into transverse traceless and transverse scalar sectors. The TT curvature response and scalar-curvature trace response, normalized to Einstein response, are

 r2(z)=G^L_TT/(κT_TT)=1/(1−βz),
 r0(z)=R^L/(−κT)=1/[1+(6α+2β)z].

These expressions refer to the particular sourced Fourier response with the chosen boundary/Green-function prescription; arbitrary added homogeneous waves are excluded. Both response observables are gauge invariant at linear order about flat space.

Define y2=(r2^−1−1)/z and y0=(r0^−1−1)/z. Then

 β=−y2,
 α=(y0+2y2)/6.

This map is injective for a fixed nonzero spacelike z with finite nonzero responses. Thus r0=r2=1 at this scale iff α=β=0 within the declared constant quadratic class. This is more informative than Ricci-flat background survival or tests limited to on-shell Einstein perturbations.

If inverse-response residual errors satisfy |δy0|≤ε0 and |δy2|≤ε2, the sharp bounds are

 |δα|≤(ε0+2ε2)/6, |δβ|≤ε2.

For direct transfer estimates rhat_i with errors ε_i<rhat_i and positive response, exact admissible intervals are

 yi ∈ [(1/(rhat_i+ε_i)−1)/z, (1/(rhat_i−ε_i)−1)/z].

Apply the affine inverse above to obtain sharp coefficient intervals. Near the Einstein value, |ri−1|≤δi<1 implies |yi|≤δi/[z(1−δi)].

### Unknown gravitational normalization and an overidentification check

If κ is unknown, measure unnormalized P2=G_TT/T_TT and P0=−R/T. Their inverses obey

 X2(z)=1/P2(z)=(1−βz)/κ,
 X0(z)=1/P0(z)=[1+(6α+2β)z]/κ.

Two distinct nonzero scales z1,z2 in the tensor channel plus the scalar channel at z1 identify all three parameters. Define

 q=(z2 X2(z1)−z1 X2(z2))/(z2−z1),
 s2=(X2(z2)−X2(z1))/(z2−z1),
 s0=(X0(z1)−q)/z1.

Then κ=1/q, β=−s2/q, α=(s0+2s2)/(6q). The three-row design determinant is z1(z2−z1)≠0. A fourth observation X0(z2) supplies the exact model-class consistency test

 z2 X0(z1)−z1 X0(z2)−z2 X2(z1)+z1 X2(z2)=0.

Thus the test can estimate rather than simply assume the leading gravitational normalization, and additional data can test the response class.

### Exact limitation/negative control

An added six-derivative scalar term can replace the inverse scalar response by

 1+(c−d z0)z+d z², c=6α+2β.

It matches 1+cz exactly at z=z0 for every d, and differs elsewhere by d z(z−z0). One-scale response data do not reject arbitrary higher operators. The declared class matters.

## C. A concrete exterior-potential application

In the non-tachyonic parameter range β<0 and c=6α+2β>0, put

 m2²=−1/β, m0²=1/c.

For a calibrated static point mass, the decaying asymptotically flat linearized solution in Newtonian/isotropic gauge is

 Φ(r)=−GM/r [1+(1/3)e^(−m0r)−(4/3)e^(−m2r)],
 Ψ(r)=−GM/r [1−(1/3)e^(−m0r)−(2/3)e^(−m2r)].

The script independently solves the actual linearized 00 and 22 equations and checks all ten components against these Fourier-space potentials. These Yukawa formulas are established quadratic-gravity results, credited to Stelle and later reviews.

Let U=−rΦ/(GM), V=−rΨ/(GM). At a known r>0,

 e^(−m0r)=U−2V+1,
 e^(−m2r)=(2−U−V)/2.

When both reconstructed quantities lie strictly between zero and one, their logarithms determine the two masses, and hence β and α. Absent modes are limiting cases. Interpreting actual observations requires source size, boundary conditions, gauge/coordinate definition, and independent extraction of the two potentials; a single force measurement is not automatically two local potential measurements.

## D. Structural selection via no additional poles

Within the exact finite polynomial class, β≠0 creates an additional spin-2 response pole; c≠0 creates a scalar-curvature pole. Hence requiring no additional finite response poles in both sectors gives β=c=0, and therefore α=0 modulo Euler. For β<0 the TT metric propagator splits as

 1/[z(1+z/m2²)]=1/z−1/(z+m2²),

showing the opposite massive residue. This is established quadratic-gravity spectrum physics. “No additional poles/initial data” is an additional structural premise, not a deduction from the Voss state/shape dictionary. When the action is only a low-energy EFT truncation, poles beyond its validity range cannot be used as proof that the corresponding Wilson coefficients vanish. Nonlocal entire-function modifications also lie outside this class.

## E. Field-redefinition and interpretation boundary

A perturbative local metric redefinition can shift R²/Ricci² terms into source interactions. For δg_ab=u R_ab+v R g_ab,

 δS_EH=(1/(2κ))∫√−g [−u Ricci²+(u/2+v)R²],
 δS_m=(1/2)∫√−g [u T^ab R_ab+v TR].

Therefore the response identification fixes a physical metric and matter prescription; it is not a basis-independent assertion that every appearance of curvature-squared symbols is observable or must vanish. Same-metric, same-source conditions are explicit hypotheses.

## Verification and provenance

- `verify_curvature_response.py`: 88 exact symbolic identities, five finite rational inverse examples; full10component linear symbol from the quadratic action, Bianchi/gauge tests, reviewer Hessian reproduction, response inversion, pole factorization, point-source potentials, unknown-κ inverse, and higher-order negative control. Python3.12.13, SymPy1.14.0. Runtime about2seconds.
- `verify_sourced_calibrations.py`: 73 exact checks; full4D dust curvature/Einstein components, electrovac curvature/Maxwell/Einstein components, nonzero H_Ric² witness, its covariant conservation, finite residual inverse and sharpness corners. Runtime about1.6seconds.
- No Lean claims yet, no experimental measurements, no novelty certification.
- The review’s two Hessian sectors and determinant−18 are explicitly credited as reviewer calculations; the full nonlinear matter-calibration selector and source-transfer inverse are the additions made in this pass.

Primary literature checked:
1. Pravda et al., *Exact solutions to quadratic gravity* (2017), https://arxiv.org/html/1606.02646v3 , eqs.(1)–(5): exact Weyl/R² equations, Bach identity, Einstein-background degeneracy.
2. Salvio, *Quadratic Gravity* (2018), https://arxiv.org/abs/1804.09944v2 and https://arxiv.org/html/1804.09944v2 : established mode content, poles and Newtonian potential. This is an author-authored technical review with original derivations, not experimental evidence.
3. Donoghue, *General relativity as an effective field theory: The leading quantum corrections* (1994), https://arxiv.org/abs/gr-qc/9405057 : distinguishes exact polynomial models from low-energy EFT inference.
4. Buoninfante et al., *Dust collapse and horizon formation in Quadratic Gravity* (2025), https://arxiv.org/abs/2410.05941 : closely related dust/FLRW precedent; the homogeneous-isotropic sector probes R² but is blind to Weyl².

The small numerical matrix coefficients and sharp inverse intervals are new-to-this-bundle derivations. The theory class and physical mechanisms have substantial prior art; a claim of monumental or worldwide-new gravity would not follow.
