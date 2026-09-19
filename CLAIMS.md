# Claims and Evidence Ledger

This file is normative for claim status in this repository.

| ID | Claim | Status | Promotion requirement |
|---|---|---|---|
| C0 | Standard three-flavour propagation can be represented by a Hermitian Hamiltonian. | STANDARD | Established baseline. |
| C1 | A Hermitian matrix-valued perturbation can be decomposed as `v0 I + sum xi_a lambda_a`. | STANDARD / MATHEMATICAL | Algebraic identity. |
| C2 | A common scalar potential proportional to identity changes global phase but not flavour probabilities. | STANDARD / DERIVED | Unit test + analytic proof. |
| C3 | Closed-loop discrete Berry holonomy is invariant under independent global rephasing of sampled states. | STANDARD / DERIVED | Unit test + analytic proof. |
| C4 | The repository can generate programmable quadratic phase profiles and their target curvature. | IMPLEMENTED / SIMULATED | Unit tests. |
| C5 | The working Euler-Berry closure relation `Gamma/(2pi) = D + epsilon + m + residual` is a useful internal constraint. | DERIVED_IN_MODEL | Internal consistency and independent derivation. |
| C6 | Piecewise-constant propagation preserves path ordering and reduces to constant-H evolution for one segment. | IMPLEMENTED / DERIVED | Unit tests + matrix-exponential construction. |
| C7 | The frozen M0/M1/M2 computational discriminator rejects a scalar identity potential as a source of flavour-selective probability changes. | IMPLEMENTED / SIMULATED | Deterministic regression tests. |
| C8 | NASER oscillator/phase quantities can be retyped into explicit calibrated drive, phase-gradient, curvature and coherence features without importing symbolic variables. | IMPLEMENTED / PROVENANCE | Source-anchored bridge note + regression tests. |
| C9 | Given a typed Hermitian pullback `Pi_{36->nu}`, the flavour coefficients are uniquely `v0=Tr(Pi)/3` and `xi_a=Tr(lambda_a Pi)/2`; an isometric projection `W^dagger H_Q W` preserves Hermiticity and is flavour-basis covariant. | DERIVED / IMPLEMENTED | Analytic derivation + reconstruction/covariance tests. |
| C10 | Three oriented complex pair couplings `J_e_mu,J_mu_tau,J_tau_e` define a Hermitian three-flavour exchange operator; `arg(H_e_mu H_mu_tau H_tau_e)` is invariant under local flavour rephasing. | DERIVED / IMPLEMENTED | Hermiticity + rephasing regression tests. |
| C11 | The historical v11 six-edge operator-tetrahedron set fails an ordinary Euclidean interpretation: one face violates the triangle inequality by exactly `1/441` and its reconstructed Gram determinant is negative. | LEGACY_GEOMETRY_FAIL / PROVENANCE | Exact rational regression tests; do not assign physical meaning to the defect. |
| HνQ | Physical QHTRI oscillator geometry couples measurably to neutrino phase/flavour transport. | PHYSICAL_HYPOTHESIS | Blinded controlled experiment; independent replication. |
| Hfocus | HνQ is strong and controllable enough to produce useful flavour-selective focusing. | PHYSICAL_HYPOTHESIS | Spatially resolved reciprocity/focusing experiment. |
| Hg | QHTRI modifies physical spacetime metric `g_mu_nu`, not only an effective flavour-space Hamiltonian. | STRONG_PHYSICAL_HYPOTHESIS | Independent metric-sensitive measurement excluding effective-medium explanations. |
| HZPE | The relevant QHTRI oscillator correlations should be interpreted as engineered zero-point-energy/vacuum structure. | INTERPRETIVE_PHYSICAL_HYPOTHESIS | Observable predictions distinguishing it from ordinary driven/noisy-field dynamics. |

## Working-prior rule

`P(HνQ)=0.65` may be used for research prioritisation only. It must never be quoted as an experimentally measured probability. Bayesian updating begins only after likelihood models for HνQ and explicit null hypotheses are frozen before analysing blinded data.

## Fail-closed rule

If an observation can be explained by electromagnetic pickup, thermal drift, mechanical vibration, timing leakage, software coupling, shared clocks, common power rails, or analysis leakage, it does not promote HνQ.
