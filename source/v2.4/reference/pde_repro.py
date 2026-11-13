"""Independent re-implementation of the Sec. 9.1 benchmark (own code, not the paper's)."""
import numpy as np
from scipy.integrate import cumulative_trapezoid, trapezoid

def data(R):
    psi = 1.6 * np.exp(-(R / 1.1) ** 2)
    chi = 0.9 * (1 + 0.3 * R ** 2) * np.exp(-(R / 1.6) ** 2)
    psiT = 0.12 * np.exp(-(R / 1.3) ** 2)
    chiT = -0.09 * (1 - 0.2 * R ** 2) * np.exp(-(R / 1.5) ** 2)
    return psi, chi, psiT, chiT

def dR1(f, dR):
    g = np.zeros_like(f); g[1:-1] = (f[2:] - f[:-2]) / (2 * dR); g[0] = 0.0; g[-1] = 0.0; return g

def lap(f, R, dR):
    out = np.zeros_like(f)
    out[1:-1] = (f[2:] - 2 * f[1:-1] + f[:-2]) / dR ** 2 + (f[2:] - f[:-2]) / (2 * dR * R[1:-1])
    out[0] = 4 * (f[1] - f[0]) / dR ** 2        # f_RR + f_R/R -> 2 f_RR, f_RR ~ 2(f1-f0)/dR^2
    return out

def rhs(y, R, dR):
    psi, chi, pT, cT = y
    pR, cR = dR1(psi, dR), dR1(chi, dR)
    aps = lap(psi, R, dR) - np.exp(-2 * psi) * (cT ** 2 - cR ** 2)
    ach = lap(chi, R, dR) + 2 * (pT * cT - pR * cR)
    aps[-1] = 0; ach[-1] = 0; aps[0] = aps[0];
    d = np.array([pT.copy(), cT.copy(), aps, ach]); d[0, -1] = 0; d[1, -1] = 0
    return d

def energy_gamma(y, R, dR):
    psi, chi, pT, cT = y
    pR, cR = dR1(psi, dR), dR1(chi, dR)
    dens = 0.5 * R * (pT ** 2 + pR ** 2 + np.exp(-2 * psi) * (cT ** 2 + cR ** 2))
    return cumulative_trapezoid(dens, R, initial=0.0)

def run(N, Rmax=8.0, Tend=0.8):
    R = np.linspace(0, Rmax, N + 1); dR = R[1] - R[0]; dT = 0.16 * dR
    psi, chi, pT, cT = data(R)
    y = np.array([psi, chi, pT, cT])
    g0 = energy_gamma(y, R, dR)
    nst = int(round(Tend / dT)); dT = Tend / nst
    for _ in range(nst):
        k1 = rhs(y, R, dR)
        k2 = rhs(y + 0.5 * dT * k1, R, dR)
        k3 = rhs(y + 0.5 * dT * k2, R, dR)
        k4 = rhs(y + dT * k3, R, dR)
        y = y + dT / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y[0, -1], y[1, -1] = psi[-1], chi[-1]
    gT = energy_gamma(y, R, dR)
    return R, y, g0, gT, dR

res = {}
for N in (128, 256, 512):
    R, y, g0, gT, dR = run(N)
    drift = abs(gT[-1] - g0[-1]) / g0[-1]
    res[N] = (R, y)
    # flux constraint (31): gamma_T = R[psi_T psi_R + e^{-2psi} chi_T chi_R] vs d/dT gamma; test via finite difference of gamma in time
    print(f"N={N:4d}  gamma_inf(0)={g0[-1]:.6f}  gamma_inf(T)={gT[-1]:.6f}  rel. drift={drift:.3e}  e^gamma_max(T)={np.exp(gT.max()):.5f}  e^gamma_max(0)={np.exp(g0.max()):.5f}")

# observed convergence order on psi at final time (common coarse points)
def sub(N, M):
    k = N // M; return res[N][1][0][::k]
e1 = np.linalg.norm(sub(256, 128) - sub(128, 128)) ; e2 = np.linalg.norm(sub(512, 128)[:] - sub(256, 128)[:] * 0 - 0) if False else None
a = res[128][1][0]; b = res[256][1][0][::2]; c = res[512][1][0][::4]
print("observed order (psi, grid-difference ratio):", np.log2(np.linalg.norm(a - b) / np.linalg.norm(b - c)))

# global regularity of the benchmark data: asymptotic twist A(infty) = int_0^{Rmax} R e^{-2 psi} chi_T dR  (conserved)
R = np.linspace(0, 8, 4001)
psi, chi, pT, cT = data(R)
Ainf = trapezoid(R * np.exp(-2 * psi) * cT, R)
print(f"asymptotic twist of the benchmark data  A(inf)-A(axis) = {Ainf:+.5f}   (a regular asymptotically-conical class needs 0)")
chiR = np.gradient(chi, R)
print(f"   same quantity ignoring e^(-2psi): {trapezoid(R*cT, R):+.5f}")

# project the data onto the constraint A(inf)=0 by rescaling chi_T amplitude, rerun, and see what changes in e^gamma
def data_c(R, amp):
    psi, chi, pT, cT = data(R); return psi, chi, pT, amp * cT
from scipy.optimize import brentq
f = lambda amp: trapezoid(R * np.exp(-2 * data(R)[0]) * amp * data(R)[3], R)
print("   (A(inf) is linear in the chi_T amplitude; it vanishes only at amp=0 for this fixed profile shape;")
print("    a corrected profile needs a counter-term, e.g. add c*R^0 exp(-R^2) to chi_T with c solving A(inf)=0)")
# explicit fix: chi_T -> chi_T + c * exp(-(R/1.2)^2)
g = lambda c: trapezoid(R * np.exp(-2 * psi) * (cT + c * np.exp(-(R / 1.2) ** 2)), R)
cstar = brentq(g, -1, 1)
print(f"   counter-term coefficient c*={cstar:.5f} makes A(inf)=0")
