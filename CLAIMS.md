# Claims and Evidence Ledger

This file is normative for claim status in this repository.

| ID | Claim | Status | Promotion requirement |
|---|---|---|---|
| C0 | Standard three-flavour propagation can be represented by a Hermitian Hamiltonian. | STANDARD | Established baseline. |
| C1 | A Hermitian matrix-valued perturbation can be decomposed as `v0 I + sum xi_a lambda_a`. | STANDARD / MATHEMATICAL | Algebraic identity. |
| C2 | A common scalar potential proportional to identity does not change internal flavour probabilities; if it varies spatially it may still change the common spatial wavefront. | STANDARD / DERIVED | Unit test + analytic proof; keep spatial optics distinct from flavour conversion. |
| C3 | Closed-loop discrete Berry holonomy is invariant under independent global rephasing of sampled states. | STANDARD / DERIVED | Unit test + analytic proof. |
| C4 | The repository can generate programmable quadratic phase profiles and their target curvature. | IMPLEMENTED / SIMULATED | Unit tests. |
| C5 | The working Euler-Berry closure relation `Gamma/(2pi) = D + epsilon + m + residual` is a useful internal constraint. | DERIVED_IN_MODEL | Internal consistency and independent derivation. |
| C6 | Piecewise-constant propagation preserves path ordering and reduces to constant-H evolution for one segment. | IMPLEMENTED / DERIVED | Unit tests + matrix-exponential construction. |
| C7 | The frozen M0/M1/M2 computational discriminator rejects a scalar identity potential as a source of flavour-selective probability changes. | IMPLEMENTED / SIMULATED | Deterministic regression tests. |
| C8 | NASER oscillator/phase quantities can be retyped into explicit calibrated drive, phase-gradient, curvature and coherence features without importing symbolic variables. | IMPLEMENTED / PROVENANCE | Source-anchored bridge note + regression tests. |
| C9 | Given a typed Hermitian pullback `Pi_{36->nu}`, the flavour coefficients are uniquely `v0=Tr(Pi)/3` and `xi_a=Tr(lambda_a Pi)/2`; an isometric projection `W^dagger H_Q W` preserves Hermiticity and is flavour-basis covariant. | DERIVED / IMPLEMENTED | Analytic derivation + reconstruction/covariance tests. |
| C10 | Three oriented complex pair couplings `J_e_mu,J_mu_tau,J_tau_e` define a Hermitian three-flavour exchange operator; `arg(H_e_mu H_mu_tau H_tau_e)` is invariant under local flavour rephasing. | DERIVED / IMPLEMENTED | Hermiticity + rephasing regression tests. |
| C11 | The historical v11 six-edge operator-tetrahedron set fails an ordinary Euclidean interpretation: one face violates the triangle inequality by exactly `1/441` and its reconstructed Gram determinant is negative. | LEGACY_GEOMETRY_FAIL / PROVENANCE | Exact rational regression tests; do not assign physical meaning to the defect. |
| C12 | For the admitted RF-L3 information potential `U_I=(alpha_I/kappa_E) Xi_I`, any admitted relational-state update changes the potential by exactly `Delta U_I=(alpha_I/kappa_E) Delta Xi_I`. | DERIVED / IMPLEMENTED | Parent RF-L3 definition + exact update regression tests. |
| C13 | If two realizations instantiate the same typed tuple `(p,pi,A_rel,alpha_I,kappa_E)`, they reconstruct the same `U_I`; the functional itself does not depend on a substrate label. | DERIVED_MODEL_INVARIANCE | Deterministic replay across implementations; does not identify unrelated physical carrier couplings. |
| C14 | After a route-specific phase coupling is declared, gradients and Hessians of `Xi_I` map linearly to phase steering and focusing; uniform `Delta Xi_I` gives only a common phase shift. | DERIVED / IMPLEMENTED | Phase-screen regression tests + spatial simulation. |
| C15 | For a declared carrier action scale `eta_phi`, the potential contribution obeys `dPhi/dt=-U/eta_phi`, and Hamilton-Jacobi gives `p=eta_phi grad(Phi)`. | DERIVED_MODEL_MECHANICS / IMPLEMENTED | Analytic derivation + phase-mechanics regression tests. |
| C16 | The phase Hessian determines the paraxial lens Jacobian `J=I+(L/k)Hess(Phi)`; `det(J)=0` is the model critical/caustic condition, and the 2D Hessian separates into convergence plus shear. | DERIVED / IMPLEMENTED | Analytic thin-screen derivation + regression tests. |
| C17 | The phase-gradient route reproduces the standard weak-field point-mass deflection magnitude `4GM/(bc^2)`. | STANDARD_GR_CROSSCHECK / IMPLEMENTED | Standard weak-field GR derivation + numerical regression. This does not promote `Hg`. |
| C18 | GREMLIN's role-separated orbital kernel can be composed algebraically with an admitted radial `U_I(r)` term to give `omega^2=mu_source eta_G/r^3 + (1/(m_I r)) dU_I/dr`. | CONDITIONAL_DERIVATION / CANDIDATE_BRIDGE | Requires independent source binding showing that `U_I` enters the orbital carrier Lagrangian. |
| C19 | On the RF-S22 matched-H branch, `E_G=H_Phi^EB`; composing this with GREMLIN v0.8 `mu_source=C_mu E_Sigma` gives `mu_source=C_mu H_Phi^EB`, and therefore `omega^2=C_mu H_Phi^EB eta_G/r^3 + alpha_I/(m_I r kappa_E) dXi_I/dr` after the C18 Lagrangian admission. | CONDITIONAL_CROSS_REPO_DERIVATION | `C_mu`, `eta_G`, physical EB realization and the `U_I` carrier admission remain source-gated. |
| C20 | The shared sinc-square two-point phase law is DERIVED_IN_FRAMEWORK / FORCED_PREDICTION in the imported Hardy–CAR sector; this repository can compute the corresponding phase coordinates/form factors, while a raw spatial phase screen is not automatically such a spectrum. | DERIVED_MATHEMATICAL / FORCED_CORE + DOMAIN_BINDING_CANDIDATE | Imported no-target-leakage theorem + local regression tests + explicit spectral/eigenphase extraction/binding contract; does not promote HνQ, Hfocus, Hg or HZPE. |
| HEB | An EB-condensate observable set supplies the typed relational-state/source map needed to realize the orbital `U_I` bridge. | PHYSICAL_SOURCE_BINDING_HYPOTHESIS | Freeze EB observables, role labels and source map; predict held-out orbital/phase observables without target fitting. |
| HνQ | Physical QHTRI oscillator geometry couples measurably to neutrino phase/flavour transport. | PHYSICAL_HYPOTHESIS | Blinded controlled experiment; independent replication. |
| Hfocus | HνQ is strong and controllable enough to produce useful flavour-selective focusing. | PHYSICAL_HYPOTHESIS | Spatially resolved reciprocity/focusing experiment. |
| Hg | QHTRI modifies physical spacetime metric `g_mu_nu`, not only an effective flavour-space Hamiltonian. | STRONG_PHYSICAL_HYPOTHESIS | Independent metric-sensitive measurement excluding effective-medium explanations. |
| HZPE | The relevant QHTRI oscillator correlations should be interpreted as engineered zero-point-energy/vacuum structure. | INTERPRETIVE_PHYSICAL_HYPOTHESIS | Observable predictions distinguishing it from ordinary driven/noisy-field dynamics. |

## Working-prior rule

`P(HνQ)=0.65` may be used for research prioritisation only. It must never be quoted as an experimentally measured probability. Bayesian updating begins only after likelihood models for HνQ and explicit null hypotheses are frozen before analysing blinded data.

## Fail-closed rule

If an observation can be explained by electromagnetic pickup, thermal drift, mechanical vibration, timing leakage, software coupling, shared clocks, common power rails, or analysis leakage, it does not promote HνQ.
