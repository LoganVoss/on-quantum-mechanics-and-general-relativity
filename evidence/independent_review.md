# Independent mathematical review and frozen extensions

This is a working review record, not a public manuscript. All derivations below were completed before public deliverable writing. The independently written `verify_quantum_geometry.py` executes 58 exact symbolic checks and five direct wavefunction quadratures, with a maximum observed absolute fidelity discrepancy 2.220446049250313e-16. It imports no supplied verification code. Exact symbolic checks, numerical quadratures and the analytic proofs below are distinct evidence types; none of these new calculations was initially a Lean proof.

## Audited core claim

The supplied equations support a conditional equivalence theorem. Fields are a two-dimensional Lorentzian metric h, positive area rho, and a symmetric positive determinant-one 2x2 matrix M. The local action is polynomial in derivatives of total order at most two, base-diffeomorphism invariant, and target SL(2,R) invariant. The geometric dictionary uses the literal quotient block in g=h+rho M. All fields are varied independently before evaluating a Milne-polar flat-space calibration. Coefficients are differentiable on one connected positive interval, and the calibration covers that interval.

Full first-variation stationarity of h=-dt^2+dr^2, rho=tr, M=diag(t/r,r/t), t,r>0, selects F=a rho+b, U=a/(2rho), W=a rho, V=0, and constant odd coupling k. Positive nondegenerate shape energy selects a>0. The overall normalization a is not determined. Constant b and k are bulk-inert under compact-support variations, with global boundary terms requiring their stated completion.

The source's use of a single all-field action and genuine derivatives closes common algebraic loopholes. The selection is first-order variational stationarity, not a positive second variation, global dynamical stability, or an assertion about every physical theory. Its derivative-order, field-content, symmetry, literal-frame and calibration assumptions are indispensable. The source explicitly gives higher-derivative and conformal-frame obstructions.

The quantum bridge is between centered one-mode states saturating the canonical Robertson-Schrodinger determinant bound and Gaussian rays/positive unimodular covariance shapes. It uses the calibrated common SL(2,R) congruence representation to identify that shape with the gravity orbit shape. It does not derive the Lorentzian quotient, spacetime dimension, full gravitational quantum dynamics, or an empirical identification of geometry from quantum mechanics alone.

The provided Lean project has seven proof modules with 40 theorem declarations, not 40 proof modules. The all-field differential-geometric variation is written proof plus exact symbolic checks; the Lean theorem begins from explicit chart equations and actual derivative hypotheses. This distinction should remain visible.

## Extension A: the full quantum geometric tensor

Use the same normalized centered Gaussian as the source,

    psi_(u,v)(x)=(v/pi)^(1/4) exp[(iu-v)x^2/2], v>0.

The normalized covariance shape is

    M=(1/v)[[1,u],[u,u^2+v^2]].

Let T_ij=<partial_i psi|partial_j psi>-<partial_i psi|psi><psi|partial_j psi>, with coordinate order (u,v). Gaussian moments E[x^2]=1/(2v), E[x^4]=3/(4v^2) and logarithmic derivatives i x^2/2 and 1/(4v)-x^2/2 give exactly

    T=(1/(8v^2))[[1,i],[-i,1]].

Thus g_FS=Re T=(du^2+dv^2)/(8v^2), QFI=4g_FS=(du^2+dv^2)/(2v^2), and the source's target shape metric is G=8g_FS=2QFI=(du^2+dv^2)/v^2. This retains all normalization factors.

With Berry convention A=i<psi|dpsi>,

    A=-du/(4v),   F_B=dA=-du wedge dv/(4v^2).

For source target coordinates P=-log v, Q=u,

    Omega=e^P dP wedge dQ=du wedge dv/v^2,
    F_B=-Omega/4.

The real and imaginary parts of the same quantum tensor therefore give the target metric and target area form. For any smooth parameter map q from an oriented base patch B, and constant k,

    S_odd=2k integral_B q*Omega
         =-8k integral_B q*F_B
         =-8k integral_boundary(B) q*A.

For a closed ray path C bounding an oriented target surface Sigma, the geometric phase is -Area_G(Sigma)/4 modulo 2pi. This is a quantum-geometric interpretation of the permitted boundary term. It does not fix k, produce a new bulk force, or imply a quantized area. The upper half-plane is contractible, A is globally defined in this Gaussian gauge, and no topological quantization follows.

Sign check: for a counterclockwise rectangle [u0,u1] x [v0,v1], integral A=-(u1-u0)(1/v0-1/v1)/4, equal to -area/4. Reversing orientation or using the opposite Berry-connection convention reverses both signs.

## Extension B: finite separation is exactly measurable through fidelity

For z=u+iv and z'=u'+iv', direct Gaussian integration gives

    <psi_z|psi_z'> = sqrt(2) (vv')^(1/4) / sqrt(v+v'-i(u'-u)),

where the square root uses the branch with positive real part. Define squared fidelity (transition probability) F=|<psi_z|psi_z'>|^2, not the unsquared fidelity convention. Then

    F=2 sqrt(vv') / sqrt((v+v')^2+(u-u')^2)
     =1/sqrt(det((M+M')/2)).

For the curvature-minus-one target metric G, its intrinsic hyperbolic geodesic distance d obeys

    cosh d = 1+[(u-u')^2+(v-v')^2]/(2vv')
           =Tr(M^(-1)M')/2.

Consequently,

    F=sech(d/2),     d=2 arcosh(1/F).

The local expansion F=1-d^2/8+O(d^4) agrees with g_FS=G/8. This d is the intrinsic distance of the Gaussian submanifold, not the ambient projective-space geodesic distance arccos(sqrt(F)).

A rigorous negative control prevents overgeneralization. Vacuum |0> and the first excited oscillator state |1> have covariances I/2 and 3I/2. Both have normalized covariance shape I, yet their overlap is zero. The first excited state is not uncertainty-saturating. Shape alone therefore cannot determine arbitrary quantum states or their fidelities. Four exact integral checks establish this negative control.

Known Gaussian fidelity and squeezed-state geometric phases already have primary literature. These are exact corollaries newly made explicit for the supplied model and conventions, not claims of priority for Gaussian quantum geometry:

- Banchi, Braunstein and Pirandola, Quantum fidelity for arbitrary Gaussian states, Phys. Rev. Lett. 115, 260501 (2015), https://arxiv.org/abs/1507.01941v1, https://doi.org/10.1103/PhysRevLett.115.260501.
- Garcia-Chung, On the geometric phase for Gaussian states (2020), https://arxiv.org/abs/2004.14204v1. Full primary text inspected at https://arxiv.org/html/2004.14204v1. Its one-mode example gives gamma=-pi sinh^2(R), consistent with the hyperbolic-area law under coordinate/convention conversion.

## Extension C: exact robustness of coefficient inference

The supplied ThmA.lean already proves sharp V and F-second-derivative bounds for denominator-cleared residuals (robust_V and robust_F2). The present extension credits those inherited partial estimates: its additions are raw-residual normalization, the complete U/W inversion and sharp constants, and integrated near-affine error bounds.

This concerns approximate Euler residuals in the fixed dimensionless calibrated chart, not dynamical stability. For each rho in a connected interval I subset (0,infinity), define the two points A=(2sqrt(rho),sqrt(rho)/2) and B=(sqrt(rho)/2,2sqrt(rho)). Define

    e1=E_tt(A), e2=E_rr(A), e3=E_tt(B), e4=E_rr(B), e5=E_tr(A)=E_tr(B).

All coefficients below are evaluated at rho, and f1=F'(rho), f2=F''(rho). Using the source's unscaled Euler components:

    e1=-4rho f2 +17rho U/8 -17W/(16rho)+V/2,
    e2=-rho f2/4+17rho U/8 -17W/(16rho)-V/2,
    e3=-rho f2/4+17rho U/8 -17W/(16rho)+V/2,
    e4=-4rho f2 +17rho U/8 -17W/(16rho)-V/2,
    e5=-rho f2-f1+rho U+W/(2rho).

Exact inversion identities are

    V=(e1-e2+e3-e4)/2,
    rho f2=(2/15)(-e1+e2+e3-e4),
    W/rho-f1=e5-(2/17)(e1+e2+e3+e4),
    2rho U-f1=e5+(-38e1+98e2+98e3-38e4)/255.

Suppose all five residual magnitudes are at most a common epsilon>=0 at every rho in I. The triangle inequality gives

    |V| <=2epsilon,
    |F''| <=8epsilon/(15rho),
    |W-rho F'| <=25rho epsilon/17,
    |U-F'/(2rho)| <=31epsilon/(30rho).

These four pointwise constants are individually sharp for the algebraic inference problem. Exact sign witnesses for (e1,e2,e3,e4;e5)/epsilon are respectively (+,-,+,-;0), (-,+,+,-;0), (+,+,+,+;-1), and (-,+,+,-;+1). They obey the necessary compatibility e1+e2=e3+e4. The script reconstructs actual coefficient values and verifies all five residuals for each witness. Sharpness here concerns pointwise coefficient jets, not a uniform optimum under additional physical or global constraints.

Fix rho0 in I and set a=F'(rho0), b=F(rho0)-a rho0, L=|log(rho/rho0)|, H=rho log(rho/rho0)-rho+rho0>=0. Integrating the F'' bound on the segment between rho0 and rho gives

    |F'(rho)-a| <=(8epsilon/15)L,
    |F(rho)-(a rho+b)| <=(8epsilon/15)H,
    |W(rho)-a rho| <=rho epsilon[25/17+(8/15)L],
    |U(rho)-a/(2rho)| <=(epsilon/rho)[31/30+(4/15)L].

The second inequality follows by Taylor's integral remainder. For rho>rho0, integrate (rho-s)/s from rho0 to rho; for rho<rho0, integrate (s-rho)/s from rho to rho0. Both evaluate to H. No numerical fitting or asymptotic approximation is used. At epsilon=0 these inequalities recover the exact selected coefficients on I. Uniform bounds require a fixed connected area interval and the stated uniform residual envelope; no uniform near-axis control follows for fixed nonzero epsilon.

## Reproduce

From the project workspace:

    work/numerical_audit/venv/bin/python work/independent_math/verify_quantum_geometry.py

Environment: Python 3.12.13, SymPy 1.14.0, SciPy 1.17.0. Output: `quantum_geometry_receipt.json`. Quadrature uses five declared pairs, absolute and relative integration tolerances 1e-12, limit 200, and a final discrepancy threshold 2e-11. These quadratures supplement the analytic Gaussian integration, rather than proving it.
