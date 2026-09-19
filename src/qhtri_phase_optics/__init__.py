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
from .edge_operator import (
    assemble_oriented_flavour_exchange,
    flavour_cycle_phase,
    rephase_flavour_operator,
    route_mismatch,
    traceless_part,
)
from .legacy_geometry import (
    historical_euclidean_geometry_passes,
    historical_gram_determinant,
    historical_triangle_defect,
)
from .informational_optics import (
    information_curvature,
    information_scalar_potential,
    observation_potential_shift,
    phase_screen_from_information_curvature,
    phase_screen_from_potential,
    relative_information_nat,
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
    "assemble_oriented_flavour_exchange",
    "flavour_cycle_phase",
    "rephase_flavour_operator",
    "route_mismatch",
    "traceless_part",
    "historical_euclidean_geometry_passes",
    "historical_gram_determinant",
    "historical_triangle_defect",
    "information_curvature",
    "information_scalar_potential",
    "observation_potential_shift",
    "phase_screen_from_information_curvature",
    "phase_screen_from_potential",
    "relative_information_nat",
]
