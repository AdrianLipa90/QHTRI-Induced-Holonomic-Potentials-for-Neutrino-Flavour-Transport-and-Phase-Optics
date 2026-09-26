# Montgomery–Dyson Phase Spectroscopy v0.1 — Phase Microscope / QHTRI Phase Optics

Status: CANDIDATE / IMPLEMENTED mathematical diagnostic.

The phase-optics repository owns transition and wavefront geometry. This integration deliberately separates two objects:

1. spatial phase geometry Phi(r), grad Phi and Hess Phi;
2. an extracted spectral/eigenphase coordinate set {x_j} on which spacing statistics may be defined.

Raw phase-screen pixels are not automatically a Montgomery–Dyson spectrum.

For an explicitly declared unfolded spectral coordinate u_j,

Phi_j = 2*pi*u_j,

and the GUE reference is

R_2(Delta Phi) = 1 - [sin(Delta Phi/2)/(Delta Phi/2)]^2.

The arithmetic reference family uses

omega_(p,m) = m log p,
w_(p,m) = log(p)/p^(m/2),

with a phase-scramble reverse control that preserves omega and w.

## Microscope binding

- unwrap_phase_screen and phase_screen_form_factor operate on the existing spatial phase output as geometry diagnostics.
- gue_pair_correlation_phase may be applied only after a declared spectral/eigenphase extraction and unfolding.
- No GUE statistic is inferred directly from a spatial image by default.
- The prime-power basis is a mathematical control/probe. It is not a claim of prime-driven optics, neutrino coupling, or a new force.
- None of HnuQ, Hfocus, Hg or HZPE is promoted by this module.
- Existing Berry holonomy, phase-gradient, Hessian, lens-Jacobian and caustic equations remain unchanged.

This is the phase-microscope adapter in the shared chain:
state/transition source -> phase geometry -> extracted spectral coordinate -> phase statistics -> null/reverse controls.
