import numpy as np
import pytest

from qhtri_phase_optics.pullback import (
    closure_phase_rate,
    decompose_u3,
    pi_36_to_u3,
    project_operator_to_flavour,
    validate_flavour_embedding,
)


def canonical_embedding():
    W = np.zeros((36, 3), dtype=complex)
    W[0, 0] = 1.0
    W[1, 1] = 1.0
    W[2, 2] = 1.0
    return W


def test_projection_matches_selected_subspace():
    rng = np.random.default_rng(123)
    A = rng.normal(size=(36, 36)) + 1j * rng.normal(size=(36, 36))
    H = 0.5 * (A + A.conj().T)
    W = canonical_embedding()
    assert np.allclose(project_operator_to_flavour(H, W), H[:3, :3], atol=1e-12)


def test_identity_projection_has_only_scalar_u1_component():
    result = pi_36_to_u3(2.5 * np.eye(36), canonical_embedding())
    assert np.isclose(result.scalar, 2.5)
    assert np.allclose(result.coefficients, 0.0, atol=1e-12)


def test_projection_is_covariant_under_flavour_basis_rotation():
    rng = np.random.default_rng(5)
    A = rng.normal(size=(36, 36)) + 1j * rng.normal(size=(36, 36))
    H = 0.5 * (A + A.conj().T)
    B = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    U, _ = np.linalg.qr(B)
    W = canonical_embedding()

    original = project_operator_to_flavour(H, W)
    rotated = project_operator_to_flavour(H, W @ U)
    assert np.allclose(rotated, U.conj().T @ original @ U, atol=1e-12)


def test_u3_decomposition_reconstructs_matrix():
    H = np.array(
        [[0.4, 0.2 + 0.1j, -0.05j],
         [0.2 - 0.1j, -0.3, 0.07],
         [0.05j, 0.07, 0.8]],
        dtype=complex,
    )
    result = decompose_u3(H)
    reconstructed = result.scalar * np.eye(3, dtype=complex)
    from qhtri_phase_optics.flavour import gell_mann
    for coefficient, lam in zip(result.coefficients, gell_mann()):
        reconstructed += coefficient * lam
    assert np.allclose(reconstructed, H, atol=1e-12)


def test_embedding_must_be_isometric():
    with pytest.raises(ValueError):
        validate_flavour_embedding(np.ones((36, 3), dtype=complex))


def test_closure_phase_rate_recovers_neutrino_phase_gradient():
    x = np.linspace(0.0, 1.0, 101)
    epsilon_slope = 0.37
    D = 0.02 * x**2
    gamma = 2.0 * np.pi * (D + epsilon_slope * x)
    rate = closure_phase_rate(x, gamma, D)
    assert np.allclose(rate, 2.0 * np.pi * epsilon_slope, atol=1e-10)
