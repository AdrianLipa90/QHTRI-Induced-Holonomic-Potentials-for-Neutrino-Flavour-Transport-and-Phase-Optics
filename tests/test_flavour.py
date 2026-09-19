import numpy as np

from qhtri_phase_optics.flavour import (
    effective_potential,
    evolve_constant_hamiltonian,
    flavour_probabilities,
    vacuum_hamiltonian,
    pmns_matrix,
    compose_hamiltonian,
    evolve_piecewise,
)


def test_effective_potential_is_hermitian():
    coeffs = np.array([0.1, -0.2, 0.3, 0.05, 0.0, -0.04, 0.07, 0.11])
    V = effective_potential(coeffs, scalar=0.9)
    assert np.allclose(V, V.conj().T)


def test_scalar_identity_potential_does_not_change_probabilities():
    H0 = np.array([[0.2, 0.03, 0.0], [0.03, 0.4, 0.02], [0.0, 0.02, 0.7]], complex)
    psi0 = np.array([1.0, 0.0, 0.0], complex)
    L = 3.4
    p0 = flavour_probabilities(evolve_constant_hamiltonian(H0, psi0, L))
    p1 = flavour_probabilities(
        evolve_constant_hamiltonian(H0 + 2.5 * np.eye(3), psi0, L)
    )
    assert np.allclose(p0, p1, atol=1e-12)


def test_evolution_preserves_norm():
    H = effective_potential(np.arange(8, dtype=float) * 0.01)
    psi = np.array([1.0, 1.0j, -0.4], complex)
    out = evolve_constant_hamiltonian(H, psi, 7.0)
    assert np.isclose(np.linalg.norm(out), 1.0, atol=1e-12)


def test_vacuum_hamiltonian_accepts_unitary_mixing_and_is_hermitian():
    U = np.eye(3, dtype=complex)
    H = vacuum_hamiltonian(np.array([0.0, 1.0, 3.0]), U, energy=2.0)
    assert np.allclose(H, H.conj().T)
    assert np.allclose(np.diag(H), [0.0, 0.25, 0.75])


def test_pmns_parameterisation_is_unitary():
    U = pmns_matrix(0.59, 0.15, 0.84, delta_cp=3.4)
    assert np.allclose(U.conj().T @ U, np.eye(3), atol=1e-12)


def test_piecewise_single_segment_matches_constant_evolution():
    H = np.array([[0.1, 0.03, 0.0], [0.03, 0.4, 0.02j], [0.0, -0.02j, 0.7]], complex)
    psi0 = np.array([1.0, 0.0, 0.0], complex)
    direct = evolve_constant_hamiltonian(H, psi0, 2.3)
    piecewise = evolve_piecewise(np.array([H]), psi0, np.array([2.3]))
    assert np.allclose(direct, piecewise, atol=1e-12)


def test_noncommuting_piecewise_order_changes_output_probabilities():
    H1 = np.array([[0.0, 0.7, 0.0], [0.7, 0.0, 0.0], [0.0, 0.0, 0.2]], complex)
    H2 = np.array([[0.0, 0.0, 0.4], [0.0, 0.8, 0.0], [0.4, 0.0, 1.3]], complex)
    psi0 = np.array([1.0, 0.0, 0.0], complex)
    p12 = flavour_probabilities(evolve_piecewise(np.array([H1, H2]), psi0, np.array([0.9, 1.1])))
    p21 = flavour_probabilities(evolve_piecewise(np.array([H2, H1]), psi0, np.array([1.1, 0.9])))
    assert not np.allclose(p12, p21, atol=1e-8)


def test_compose_hamiltonian_recovers_baseline_when_qhtri_is_zero():
    Hvac = np.diag([0.0, 0.2, 0.5]).astype(complex)
    Vmsw = np.diag([0.1, 0.0, 0.0]).astype(complex)
    Vq = np.zeros((3, 3), complex)
    assert np.allclose(compose_hamiltonian(Hvac, Vmsw, Vq), Hvac + Vmsw)
