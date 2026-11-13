# Working derivations: selected state–shape dynamics

Scratch research record. Public source files have not been edited. The derivations and bounded checks here were completed before any public writing of this extension. `verify_dynamical_extension.py` and `dynamical_extension_receipt.json` are the executable record (41 exact checks; two fully quantum finite regulators; two tolerances for a semiquantum ODE).

## 1. Precise selection principle

Let M be a positive symmetric unimodular 2x2 target matrix. Let Rhat=(Qhat,Phat) with [Qhat,Phat]=i in dimensionless calibrated quadratures. The physical scales obey q_*p_*=hbar. Introduce an **independent probe state**; the geometry M is not double-counted as that same probe state.

Assume an instantaneous, algebraic, target-only, centered quadratic probe Hamiltonian

    H_M = (1/2) Rhat^T K(M) Rhat + c I,

with Weyl ordering, K(M) positive symmetric, no derivative/background/extra-scalar dependence, and calibrated common canonical frame covariance

    K(A M A^T)=A^{-T}K(M)A^{-1},   A∈SL(2,R).

At M=I, invariance under rotations forces K(I)=hbar*omega I. (Quarter-turn invariance already forces equal diagonal entries and zero off-diagonal entry.) For M=A A^T, covariance then forces

    K(M)=hbar*omega M^{-1}.

Target transitivity makes c constant. Fixing the ground-energy reference gives

    H_M^ex = (hbar*omega/2) Rhat^T M^{-1} Rhat - hbar*omega/2 I >=0.

The number gap omega>0 is calibrated; no numerical value is derived. The ground state has covariance M/2 and is the exact Gaussian ray already used by the geometric dictionary. This follows by the metaplectic transformation Rhat'=M^{-1/2}Rhat to the ordinary oscillator. Thus the coupling is selected before choosing any trajectory, rather than reconstructed after choosing a desired state path.

The extra no-derivative/quadratic/target-only assumptions are essential. In the original two-Killing model a spectator area rho permits omega(rho). In the one-Killing extension there is no independent rho and the target is transitive, so an algebraic target-only coefficient is constant. Explicit spacetime backgrounds, curvature dependence, or extra fields would reopen functional freedom.

A direct negative control is H'=hbar*omega n_M + zeta n_M(n_M-1), zeta>=0. It is equally frame covariant and has the same ground state and first energy gap, but is not quadratic and generally does not preserve Gaussian evolution. For squeezed vacuum with mean n, <n_M(n_M-1)>=3n^2+n. Thus a universal coupling theorem outside the stated class is false. Quadraticity can be motivated by requiring linear canonical propagation; that requirement is additional physical structure, not a consequence of the previous vacuum selection theorem.

## 2. Compact equation and force law

For an independent centered saturated Gaussian probe with N=2Sigma, det N=1,

    E(M,N)=<H_M^ex> = hbar*omega/4 [Tr(M^{-1}N)-2]
           = hbar*omega/2 (cosh d_G(M,N)-1)
           = hbar*omega sinh^2(d_G/2)
           = hbar*omega (F^{-2}-1),

where F=|<psi_M|psi_N>|^2=sech(d_G/2) is **squared fidelity**. In coordinates M=M(x,y), N=M(u,v), y,v>0,

    E = hbar*omega [(x-u)^2+(y-v)^2]/(4yv).

This is the strongest compact “energy–geometry–overlap” equation selected by this model. It is a calibrated oscillator/shape identity, not a replacement for E=mc^2 or a new universal gravitational law. It is the ordinary squeezed-oscillator excitation energy expressed in the model's exact target metric.

The reciprocal shape source is minus the target gradient of E. Since |grad d|=1 away from the coincident point,

    ||grad_M E||_G^2 = E(E+hbar*omega).

This extends continuously to d=0. It also follows directly by differentiating the rational coordinate expression. For any centered finite-covariance state, let N=2Sigma (now det N>=1). The same quadratic coupling gives the exact identity

    ||grad_M E||_G^2
      = E(E+hbar*omega) - (hbar*omega)^2(det N-1)/4
      <= E(E+hbar*omega).

Equality recovers covariance uncertainty saturation, hence the centered pure Gaussian family under the earlier reconstruction hypotheses. An isotropic thermal covariance has positive energy but zero directional force; energy alone does not fix the response direction or certify a pure state.

Applications with declared calibration:

* A measured Gaussian overlap determines excitation energy: E/(hbar*omega)=F^{-2}-1.
* An energy budget Emax gives d<=2 asinh sqrt(Emax/(hbar*omega)) and F>=[1+Emax/(hbar*omega)]^{-1/2}.
* F=4/5 gives E=9 hbar*omega/16, d=2 log2, and force norm 15 hbar*omega/16.
* At M=I, N+=diag(4,1/4) and N-=diag(1/4,4) have that same energy and the same entire oscillator number distribution, but opposite target-y forces +/-15 hbar*omega/16. These are phase-sensitive source predictions of the selected coupling, not a claim of different total energy.

## 3. Fully quantum shape/probe operator

On H=L²(H²,dvol_G) tensor L²(R), choose a calibrated positive shape inertia I and

    Hjoint = -hbar²/(2I) Delta_G + H_M^ex.

The shape kinetic form and the fiberwise nonnegative oscillator form are closed nonnegative forms with dense common domain containing compactly supported smooth shape functions times Schwartz probe functions. Their sum defines a positive self-adjoint operator by the Friedrichs/form representation construction. Therefore its joint evolution is linear, unitary, and energy conserving for the appropriate energy domain. It can entangle shape and probe and transfer energy reciprocally. No nonlinear-state fundamental hybrid is required.

This is an exact finite-cell quantum model of the selected target coupling. It does not by itself solve the quantum gravitational constraints, establish the interacting field continuum, or show that the shape Hilbert space is a fundamental spacetime Hilbert space. The coefficient I is calibrated; it is not a newly derived universal constant. A finite lattice of such cells is likewise a declared regulator, not a continuum theorem.

The geometric and quantum actions of SL(2,R) act jointly and commute with Hjoint. In particular, take the canonical quarter-turn A=J=[[0,1],[-1,0]]. For det M=1 this sends M to M^{-1}. Introduce hyperboloid coordinates

    X0=Tr M/2, X1=(M11-M22)/2, X2=M12,
    X0²-X1²-X2²=1,
    grad X_A · grad X_B = X_A X_B - eta_AB,
    eta=diag(1,-1,-1).

A quarter-turn fixes X0 and reverses X1,X2. Let chi(M) be any normalized smooth compactly supported radial shape packet centered at I. Take probe rays with N±=diag(e^r,e^{-r}) and its swap. The common radial packet is invariant, while the metaplectic quarter-turn exchanges the probes. The two initial JOINT states are related by a unitary commuting with Hjoint, and consequently have identical **full joint-energy spectral measures**, not only equal mean energy or equal bare-probe energy distributions.

Their directional responses nevertheless reverse. For a rigorous bounded continuum observable, choose O=ζ(r_shape) X1, where ζ is smooth, radial, compactly supported, and identically one on a neighborhood of the initial compact packet's support. O is bounded and reverses under the quarter-turn. At t=0,

    d²<O>/dt² = +/- hbar*omega/(2I) (1+kappa) sinh r,
    kappa=<X1²>=<X2²> >=0.

Proof: the free kinetic double-commutator of O is shape-odd and has zero expectation in the radial packet. Since ζ=1 on a neighborhood of its support, O and all derivatives entering the local commutators agree there with X1. The interaction double-commutator therefore contributes -I^{-1}<grad X1 · grad Hprobe>. Writing probe hyperboloid coordinates Y0=cosh r,Y1=+/-sinh r,Y2=0, E=hbar*omega/2(eta_AB X_A Y_B-1). The gradient identity gives grad X1·grad E=hbar*omega/2(X1 eta_AB X_A Y_B-Y1). Radial symmetry makes <X1X0>=0 and <X1X2>=0, leaving the displayed nonzero coefficient. The initial smooth compact-support/Schwartz vector belongs to D(Hjoint²), and bounded O permits differentiation of its expectation at t=0; its local commutators preserve the required core. This statement does not assert that the unbounded expectation <X1>(t) remains finite at later times; that would need a separate moment-propagation theorem.

For the explicit packet chi=C exp[-1/(1-r_shape²)] on r_shape<1 and zero outside, choose ζ=1 for r_shape≤1.1 and ζ=0 for r_shape≥2, with a smooth radial interpolation. Then kappa=0.11146598698569911 by declared one-dimensional quadrature. The theorem itself does not rely on this numerical value.

This is a distinguishing prediction against an uncoupled or energy-only isotropic response model with the same preparation contract. It is not a new force beyond the specified Hamiltonian, nor a demonstration of laboratory gravity.

## 4. Fully quantum bounded computation

The verification script constructs a positive hyperbolic-polar finite-volume shape kinetic matrix on 4 radial by 8 angular cells with radius 1.2, and couples it to the exact projected oscillator quadratic matrix at 16 and 24 Fock levels. It does not square truncated Q/P matrices and pretend they satisfy exact CCR. The full SL2 symmetry is not preserved by the finite domain; the tested quarter-turn symmetry is preserved by this regulator.

Joint dimensions are 512 and 768. On the 24-level run:

* joint symmetry commutator norm: 5.81e-13;
* matched-state initial shape accelerations: +0.8231656470474908 and -0.8231656470474902;
* at t=0.35, shape responses: +/-0.0262193691255806;
* maximum norm error: 3.55e-15;
* maximum total-energy error: 1.95e-14;
* shape/probe entanglement at t=0.35: 0.1490367367821729 bits, versus numerical zero for the uncoupled control;
* shape energy rises from 5.954003829208501 to 5.9904564302751, while probe energy falls from 0.2220774810143197 to 0.18562487994771928.

The largest 16-versus-24-level directional response difference is 6.22e-8. This is a Fock-cutoff check at fixed shape grid. No shape-grid convergence or continuum claim is made. The finite-grid X1 observable is bounded because the shape domain is finite. The finite-grid radial Gaussian packet differs from the compact bump used in the continuum acceleration example, so those coefficients must not be numerically equated.

## 5. Explicit reciprocal semiquantum response limit

For classical geometry (x,y) with inertia mu>0 and an independent saturated Gaussian probe (u,v), the action

    L=mu/(2y²)(xdot²+ydot²) - hbar udot/(4v) - E(x,y,u,v)

gives

    xddot -2 xdot ydot/y = -hbar*omega*y(x-u)/(2mu v),
    yddot +(xdot²-ydot²)/y = hbar*omega[v²+(x-u)²-y²]/(4mu v),
    udot=omega[v²-y²-(u-x)²]/y,
    vdot=2omega v(x-u)/y.

The quantum equations are exactly Ndot=omega[J M^{-1}N-N M^{-1}J] and preserve Gaussianity, centering, positivity, and determinant. The total energy Kshape+E is conserved; the shear Noether charge is

    mu xdot/y² - hbar/(4v) = p_x - hbar <Q²>/2.

With finite initial energy, the complete hyperbolic target bounds geometry speed and target displacement on every finite time interval. E bounds the relative distance, so the probe target also stays in a compact region. Smooth ODE continuation therefore gives global solutions for this finite-cell semiquantum model. This is not a theorem of stability for the full field PDE.

Around a common isotropic equilibrium, g=hbar*omega/(2mu), the nonzero linear mode frequencies are

    Omega_±=sqrt(omega²+g) +/- omega,
    Omega_+ Omega_-=g,    Omega_+ -Omega_-=2omega.

The characteristic polynomial is z²[z⁴+(4omega²+2g)z²+g²]. The frozen-geometry probe alone has covariance frequency 2omega; the reciprocal model has two sidebands, with a vanishing slow branch in the infinite-inertia limit. The common equilibrium-shift modes have zero frequency.

A declared DOP853 evolution through t=20 with hbar=omega=1, mu=1/2 preserves positivity. Tightening rtol from 1e-9 to 1e-11 changes the endpoint by 9.06e-10; the finer maximum energy drift is 8.57e-12 and Noether drift 5.15e-12. The script uses no fitted target trajectory.

## 6. One-Killing twist consistency

For the symmetry extension identify x=chi (twist), y=lambda (norm). Naively retaining the vacuum relation F=-lambda^{-2} *dchi after adding a generic chi-dependent probe is wrong: the sourced chi equation makes that F nonclosed.

The exact shear dressing Psi=exp(i chi Q²/2) psi_tilde removes chi from the oscillator Hamiltonian and adds -hbar<Q²/2> dchi to the Berry action. For a smooth probe current J, the total conserved twist current is C=f lambda^{-2}dchi+J, where f is the selected gravitational coefficient. The consistent curvature is F=-*C/f. The symmetry agent has derived the corresponding dual action and signs. Delta-function worldline current squared would be undefined; a smooth state-fluid or a finite regulator is required. A common 4D sourced interpretation must use that repaired action/dictionary, not silently substitute the vacuum twist map.

## 7. Independent check of root's projected ground band

I independently differentiated psi_(u,v), confirming the root calculation. With kappa0=hbar²/(2I), A_B=-du/(4v), and a compact smooth scalar packet chi,

    P Hjoint P chi = kappa0[-v²(chi_uu+chi_vv)-i v chi_u/2+5chi/16]
                     =kappa0(-Delta_A+1/4)chi.

The off-band component is

    Q Hjoint(chi psi)=kappa0 v Dchi (x_probe²-1/(2v))psi,
    D=v(partial_v-i partial_u)+1/4.

With measure du dv/v², D†=-v partial_v-i v partial_u+5/4 and D†D is precisely the displayed projected operator divided by kappa0. Since Var(x_probe²)=1/(2v²),

    ||Q Hjoint(chi psi)||² = kappa0 E/2,
    P_offband(t)=E t²/(4I)+o(t²).

The initial coefficient is independent of omega, but this is not a uniform adiabatic limit in time. Treating P H P as autonomous exact evolution would be false. Dchi=0 means v^{1/4}chi is holomorphic; no nonzero compactly supported packet satisfies that. This supplies an exact unavoidable recoil/leakage statement on the declared packet class.

## 8. Prior work and scientific positioning

Primary literature verified:

* Hackl and Bianchi, Bosonic and fermionic Gaussian states from Kähler structures, SciPost Phys. Core 4,025 (2021), version4 https://arxiv.org/abs/2010.15518v4. Gaussian symplectic covariance and quadratic dynamics are established.
* Hackl, Guaita, Shi, Haegeman, Demler, Cirac, Geometry of variational methods: dynamics of closed quantum systems, SciPost Phys.9,048 (2020), https://arxiv.org/abs/2004.01015v4. The variational framework and energy-conserving Gaussian dynamics have substantial precedent.
* Hu and Verdaguer, Stochastic Gravity: Theory and Applications, Living Rev.Relativity11,3 (2008), https://arxiv.org/abs/0802.0658v1. Generic quantum expectation-value backreaction is longstanding and is not claimed as a new invention here.

The contribution supportable here is a selected interaction and observable chain in this calibrated target model, an exact full-quantum finite-cell completion, matched-full-energy-spectrum directional responses, and explicit limits/negative controls. Worldwide priority is unassessed; no experimental observation is supplied. The existing one-Killing selection, repaired smooth-current action, and curvature-squared discrimination must retain their own stated assumptions when combined.
