# NASER 2025 -> QHTRI measurable bridge

This note records a conservative retyping of selected NASER equations into instrument-level quantities. It does not promote the original symbolic interpretation to physical fact.

## Preserved source anchors

From `NASER/Latex RAW/Chapter 2/2.2.txt`:

```text
B(t) = B0 cos(omega t + phi_intent(t))
Delta phi(x) = integral [d phi_intent/dx + kappa(x)] dx
```

The current repository retypes `phi_intent` as a calibrated drive phase `phi_drive`; `kappa(x)` is treated as a measurable spatial phase curvature.

From `NASER/Latex RAW/Chapter 1/1.1/1.1.4.txt`:

```text
delta phi = beta * (d phi_nu/dx) * (d phi_intent/dx)
```

The code preserves this only as `legacy_phase_imprint_proxy`. The coefficient `beta` has no promoted physical value.

From `NASER/Latex RAW/Chapter 2/2.4.txt` and `Appendices/Appendix E.txt`, the legacy gate uses the magnitude of a second spatial derivative of phase. The current project retains phase slope and curvature as measurable steering/focusing observables while dropping the symbolic gate requirement.

## Retyping table

| NASER legacy quantity | Current measurable quantity | Status |
|---|---|---|
| `B(t)` | oscillator drive waveform | IMPLEMENTED / INSTRUMENTAL |
| `phi_intent` | calibrated oscillator/drive phase `phi_drive` | RETYPED |
| `delta phi` | measured or estimated phase residual | RETYPED |
| `kappa(x)` | spatial second derivative of unwrapped phase | IMPLEMENTED |
| recursive phase feedback | controller state / measured next-frame phase | ENGINEERING TARGET |
| `CG[n]`, glyph variables | no physical-core equivalent | QUARANTINED |

## QHTRI feature surface

For an oscillator bank the current implementation exposes

```text
A_i, phi_i, omega_i
-> order parameter R
-> mean phase
-> circular variance
-> amplitude RMS
-> amplitude-weighted frequency
```

These features may be used as inputs to a future candidate map

```text
F_a(features, Gamma_Q, correlations, spectra) -> xi_a
```

but this repository does not currently identify or fit `F_a` as a physical neutrino coupling.
