# Phase Mechanics, GREMLIN Orbital Crosswalk, and EB-Condensate Frontier

Status: `DERIVED_MODEL_MECHANICS / STANDARD_GR_LENSING_CROSSCHECK / GREMLIN_CANDIDATE_ORBITAL_BRIDGE / EB_CONDENSATE_BINDING_OPEN`

Date: 2026-09-19

## 1. Scope and namespace firewall

This note extends the informational phase-optics layer into a phase-mechanics theorem chain.

The project label `EB-condensate` is kept distinct from the existing `Euler-Berry` closure. No identity between an EB-condensate carrier and the Euler-Berry closure is assumed by notation alone.

## 2. Derived phase-mechanics chain

RFC RF-L3 supplies

```text
Xi_I = D_KL(p || pi) / A_rel
U_I  = (alpha_I / kappa_E) Xi_I
```

For a declared carrier action scale `eta_phi`, let

```text
S_I[C]   = - integral_C U_I dt
Phi_I[C] = S_I[C] / eta_phi
```

so locally

```text
dPhi_I/dt = -U_I / eta_phi.
```

The Hamilton-Jacobi interface is

```text
p_phi = eta_phi grad(Phi_I)
```

and therefore

```text
F_I = -grad(U_I)
    = -(alpha_I/kappa_E) grad(Xi_I).
```

These are model identities once the typed potential and carrier action scale are admitted.

## 3. Lens tensor and caustic gate

For a thin phase screen,

```text
Hess(Phi_I)
  = -chi_phi (alpha_I/kappa_E) Hess(Xi_I).
```

Comparison with the quadratic thin-lens phase gives the inverse focal tensor

```text
F^{-1}
  = chi_phi alpha_I / (k kappa_E) Hess(Xi_I).
```

For propagation distance `L`,

```text
J = I + (L/k) Hess(Phi_I).
```

The model critical/caustic condition is

```text
det(J) = 0.
```

For a two-dimensional lensing Hessian `H_psi`,

```text
convergence = (H_11 + H_22)/2
gamma_1     = (H_11 - H_22)/2
gamma_2     = H_12.
```

Thus trace curvature generates isotropic convergence while traceless curvature generates shear.

## 4. Standard weak-field gravitational-lensing cross-check

For a standard weak-field point-mass lens, the eikonal route gives

```text
|alpha_g| = 4 G M / (b c^2).
```

The executable primitive in `phase_mechanics.py` reproduces this standard expression.

This validates the phase-gradient/lens-Jacobian machinery against known gravitational-lensing mathematics.

It does **not** prove

```text
U_I == Phi_N
```

or

```text
U_I -> physical g_mu_nu.
```

That stronger identification remains the repository hypothesis `Hg`.

## 5. GREMLIN source crosswalk

GREMLIN already contains a source-gated orbital chain.

### 5.1 Newton-Einstein-AB candidate

`GREMLIN_SEMANTIC_ORBITAL_NEWTON_EINSTEIN_AB_BRIDGE_V0_2` supplies

```text
omega_K^2 = mu_sem / r^3
V_N       = -mu_sem/r
tau_total = tau_rot + tau_GR + tau_AB
```

with physical source ownership explicitly OPEN.

### 5.2 RFC source-density bridge

`GREMLIN_SEMANTIC_ORBITAL_RFC_SOURCE_DENSITY_V0_4` crosswalks the lifted orbital phase into the RFC source-density coordinate while preserving winding and source gates.

### 5.3 Mass-role firewall

`GREMLIN_SEMANTIC_ORBITAL_MASS_ROLE_FIREWALL_V0_6` separates

```text
mu_source
q_coupling
m_inertial
```

and gives the role-separated circular kernel

```text
omega^2 = (mu_source/r^3) (q_coupling/m_inertial).
```

Define

```text
eta_G = q_coupling/m_inertial
```

so

```text
omega^2 = mu_source eta_G / r^3.
```

This is the correct GREMLIN parent for orbital composition. It prevents an untyped semantic-mass field from being silently reused as source mass, inertial mass and coupling charge.

### 5.4 EB Hamiltonian source composition

RFC RF-S22 supplies, on its admitted matched-H branch,

```text
E_G = H_Phi^EB.
```

GREMLIN v0.8 keeps the source conversion explicit,

```text
mu_source = C_mu E_Sigma.
```

When the admitted extensive source is the RF-S22 generator source,

```text
E_Sigma = E_G = H_Phi^EB,
mu_source = C_mu H_Phi^EB.
```

GREMLIN v0.9 implements this composition together with phase winding, Berry/connection holonomy, condensate quantum pressure and the informational radial-gradient term. `C_mu` and all physical realization bindings remain OPEN.

## 6. Conditional orbital composition with the informational potential

If, and only if, a later source-binding gate admits `U_I(r)` as an actual term in the orbital carrier Lagrangian,

```text
L_orb
 = (m_I/2)(r_dot^2 + r^2 theta_dot^2)
   + mu_source q_coupling/r
   - U_I(r),
```

then the circular-orbit Euler-Lagrange equation gives

```text
m_I r omega^2
  = mu_source q_coupling/r^2
    + dU_I/dr
```

and therefore

```text
omega^2
  = mu_source eta_G/r^3
    + (1/(m_I r)) dU_I/dr.
```

Using the RFC information potential,

```text
omega^2
  = mu_source eta_G/r^3
    + alpha_I/(m_I r kappa_E) dXi_I/dr.
```

The algebra after the Lagrangian assumption is derived. The physical admission of that Lagrangian term is **OPEN**.

This equation is the principal GREMLIN handoff for the EB-condensate investigation.

## 7. EB-condensate candidate route

The next candidate graph is

```text
EB condensate state
  -> typed density/phase/order-parameter observables
  -> source-owned relational-state map
  -> Xi_I(r,t)
  -> U_I(r,t)
  -> phase mechanics
  -> orbital omega(r,t), precession, stability and lens tensor
```

GREMLIN must reject a route that jumps directly from an EB label to a gravitational or informational potential without a source-owned map.

Required candidate observables should therefore include, at minimum,

```text
density/order parameter
phase and phase gradient
current/velocity field
orbital radius or radial coordinate
time/tick provenance
source and inertial role labels
```

before orbital inference is admitted.

## 8. What is known vs suspected

### DERIVED / STANDARD

- `Xi_I -> U_I` inside the admitted RFC potential model;
- `U -> action -> phase rate` after a typed action scale is declared;
- `grad(Phi) -> canonical momentum`;
- `Hess(Phi) -> focal tensor / Jacobian / caustic condition`;
- standard weak-field point-mass deflection `4GM/(bc^2)`;
- GREMLIN role-separated Kepler/Newton algebra on its declared candidate surface.

### CANDIDATE / OPEN

- `U_I` as a physical force term for the orbital carrier;
- identification of an EB-condensate observable set with the RFC relational state;
- `U_I -> g_mu_nu`;
- physical ownership of GREMLIN `mu_source`, `q_coupling`, rotation and AB phases;
- any claim that the EB-condensate route generates physical gravitational lensing.

## 9. Cross-domain readout

Once an EB source binding exists, one common potential can be interrogated through independent downstream routes:

```text
U_I(r) -> orbital mechanics
U_I(x,y) -> phase optics / lensing
U_I(omega) -> spectroscopy
U_I(R_nuc) -> chemical energy landscape
```

Agreement between independently constructed routes is a cross-domain consistency test. A route must not be fitted to another route and then counted as independent evidence.

## 10. Parent surfaces

- `docs/INFORMATIONAL_PHASE_OPTICS.md`
- `THEORY.md`
- GREMLIN `spec/GREMLIN_SEMANTIC_ORBITAL_NEWTON_EINSTEIN_AB_BRIDGE_V0_2.md`
- GREMLIN `spec/GREMLIN_SEMANTIC_ORBITAL_RFC_SOURCE_DENSITY_V0_4.md`
- GREMLIN `spec/GREMLIN_SEMANTIC_ORBITAL_MASS_ROLE_FIREWALL_V0_6.md`
- GREMLIN `spec/GREMLIN_EB_CONDENSATE_ORBITAL_PHASE_BRIDGE_V0_9.md`
- RFC `formalism/RF_GREMLIN_EB_ORBITAL_PHASE_CROSSWALK_V0_1.md`
- Resonant-Chemistry `docs/INFORMATIONAL_PHASE_EB_ORBITAL_SPECTROSCOPY_CROSSWALK.md`
- PhaseNav Telescope `docs/INFORMATIONAL_PHASE_EB_ORBITAL_SPECTRAL_CROSSWALK.md`

The GREMLIN surfaces remain candidate/source-gated and are cross-referenced rather than promoted here.
