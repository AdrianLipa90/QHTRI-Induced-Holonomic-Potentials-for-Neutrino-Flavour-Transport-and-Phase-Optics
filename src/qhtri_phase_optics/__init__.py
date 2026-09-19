"""QHTRI neutrino phase-optics reference mathematics.

This package implements mathematical diagnostics and simulation primitives only.
It does not assert physical QHTRI-neutrino coupling.
"""

from .geometry import (
    berry_holonomy,
    closure_residual,
    normalized_phase_state,
    thin_lens_phase,
)
from .flavour import (
    effective_potential,
    evolve_constant_hamiltonian,
    flavour_probabilities,
    matter_potential,
    vacuum_hamiltonian,
    pmns_matrix,
    compose_hamiltonian,
    evolve_piecewise,
)

from .discrimination import DiscriminationResult, run_three_model_discrimination
from .bridge import (
    OscillatorFeatures,
    legacy_phase_imprint_proxy,
    oscillating_drive,
    oscillator_features,
    phase_slope_curvature,
)
from .pullback import (
    U3Projection,
    closure_phase_rate,
    decompose_u3,
    pi_36_to_u3,
    project_operator_to_flavour,
    validate_flavour_embedding,
)

__all__ = [
    "berry_holonomy",
    "closure_residual",
    "normalized_phase_state",
    "thin_lens_phase",
    "effective_potential",
    "evolve_constant_hamiltonian",
    "flavour_probabilities",
    "matter_potential",
    "vacuum_hamiltonian",
    "pmns_matrix",
    "compose_hamiltonian",
    "evolve_piecewise",
    "DiscriminationResult",
    "run_three_model_discrimination",
    "OscillatorFeatures",
    "legacy_phase_imprint_proxy",
    "oscillating_drive",
    "oscillator_features",
    "phase_slope_curvature",
    "U3Projection",
    "closure_phase_rate",
    "decompose_u3",
    "pi_36_to_u3",
    "project_operator_to_flavour",
    "validate_flavour_embedding",
]
