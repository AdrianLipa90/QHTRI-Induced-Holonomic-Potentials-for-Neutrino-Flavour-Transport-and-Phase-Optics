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
]
