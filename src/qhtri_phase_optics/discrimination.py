from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .flavour import (
    compose_hamiltonian,
    effective_potential,
    evolve_constant_hamiltonian,
    flavour_probabilities,
)


@dataclass(frozen=True)
class DiscriminationResult:
    """Probabilities and contrasts for the frozen M0/M1/M2 comparison."""

    p_m0: np.ndarray
    p_m1: np.ndarray
    p_m2: np.ndarray

    @property
    def scalar_control_delta(self) -> float:
        return float(np.max(np.abs(self.p_m1 - self.p_m0)))

    @property
    def flavour_effect_delta(self) -> float:
        return float(np.max(np.abs(self.p_m2 - self.p_m0)))


def run_three_model_discrimination(
    base_hamiltonian: np.ndarray,
    initial_state: np.ndarray,
    distance: float,
    *,
    scalar: float,
    coefficients: np.ndarray,
) -> DiscriminationResult:
    """Run the frozen computational controls M0, M1 and M2.

    M0 = H_base
    M1 = H_base + scalar*I
    M2 = H_base + scalar*I + sum_a xi_a lambda_a

    The function is a computational discriminator only. It does not infer a
    physical origin for ``coefficients``.
    """
    H0 = compose_hamiltonian(base_hamiltonian)
    V1 = effective_potential(np.zeros(8, dtype=float), scalar=scalar)
    V2 = effective_potential(coefficients, scalar=scalar)

    psi0 = evolve_constant_hamiltonian(H0, initial_state, distance)
    psi1 = evolve_constant_hamiltonian(compose_hamiltonian(H0, V1), initial_state, distance)
    psi2 = evolve_constant_hamiltonian(compose_hamiltonian(H0, V2), initial_state, distance)

    return DiscriminationResult(
        p_m0=flavour_probabilities(psi0),
        p_m1=flavour_probabilities(psi1),
        p_m2=flavour_probabilities(psi2),
    )
