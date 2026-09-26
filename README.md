# QHTRI-Induced Holonomic Potentials for Neutrino Flavour Transport and Phase Optics

A falsifiable research programme for testing whether controlled QHTRI oscillator-correlation geometry can induce effective holonomic potentials in neutrino flavour transport and, if so, whether those potentials can be shaped into phase-optical elements.

## Scope

The repository separates four evidential levels:

- **STANDARD** — established neutrino oscillation / matter-potential / geometric-phase mathematics used as a baseline.
- **DERIVED_IN_MODEL** — consequences of the explicit mathematical model implemented here.
- **SIMULATED** — numerical results produced by repository code and tests.
- **PHYSICAL_HYPOTHESIS** — claims that require independent physical measurement.

The central physical hypothesis is **not** treated as established fact:

> **HνQ:** a physical QHTRI oscillator state couples measurably to neutrino phase/flavour transport.

A stronger hypothesis is tracked separately:

> **Hg:** QHTRI modifies the physical spacetime metric rather than only an effective flavour-space Hamiltonian/connection.

No result for HνQ implies Hg automatically.

## Core model

In natural units, the baseline propagation equation is

```text
i d|nu>/dx = [H_vac + V_MSW + V_QHTRI] |nu>.
```

The model represents the QHTRI contribution as a Hermitian flavour-space potential

```text
V_QHTRI(x) = v0(x) I + sum_a xi_a(x) lambda_a,
```

where `lambda_a` are the eight Gell-Mann generators. A purely scalar term `v0 I` can add a common phase but cannot by itself change flavour probabilities.

The phase-optics layer asks whether a spatially programmed QHTRI holonomy can realize a quadratic phase profile of the form

```text
Phi_a(r) = Phi_a0 - k_a r^2 / (2 f_a),
```

for one or more propagation eigenmodes.

## Repository layout

- `THEORY.md` — mathematical core and explicit claim boundaries.
- `CLAIMS.md` — current evidence ledger.
- `ROADMAP.md` — falsification-first research plan.
- `PROVENANCE.md` — project ancestry and source hashes.
- `src/qhtri_phase_optics/` — minimal reference implementation.
- `tests/` — invariance and regression tests.
- `legacy/NASER_2025/` — provenance notes for the 2025 NASER precursor.

## Working confidence

A numerical confidence such as `0.65` is treated only as a **working engineering prior** for HνQ. It is not a measured posterior probability. Promotion requires blinded, controlled physical data with explicit null models and likelihoods.

## Status

Foundation v0.1. The code establishes mathematical invariants and a simulation surface. It does **not** demonstrate physical neutrino coupling, neutrino focusing, zero-point-energy engineering, or spacetime-metric modification.

## AI/ML training policy

Ordinary use of this repository is distinct from training model weights. See `AI_TRAINING_POLICY.md`.


## Phase microscope / Montgomery–Dyson spectroscopy candidate

The mathematical diagnostic is implemented in src/qhtri_phase_optics/phase_spectroscopy.py and bounded by docs/MONTGOMERY_DYSON_PHASE_SPECTROSCOPY_V0_1.md. Spatial phase-screen geometry remains distinct from an extracted spectral/eigenphase sequence; GUE spacing statistics are never inferred from raw phase pixels by default.


Phase-spectroscopy status refinement: the shared sinc-square pair law is DERIVED_IN_FRAMEWORK / FORCED_PREDICTION in the Hardy–CAR sector. A QHTRI/phase-microscope realization of that spectral sector remains CANDIDATE; raw phase-screen geometry alone does not supply the binding.
