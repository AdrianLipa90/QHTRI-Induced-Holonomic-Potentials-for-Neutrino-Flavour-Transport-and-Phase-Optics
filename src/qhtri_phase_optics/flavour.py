from __future__ import annotations

import numpy as np


def gell_mann() -> tuple[np.ndarray, ...]:
    """Return the standard eight Hermitian Gell-Mann generators."""
    z = 0.0j
    one = 1.0 + 0.0j
    i = 1.0j
    return (
        np.array([[0, one, z], [one, 0, z], [z, z, 0]], complex),
        np.array([[0, -i, z], [i, 0, z], [z, z, 0]], complex),
        np.array([[1, z, z], [z, -1, z], [z, z, 0]], complex),
        np.array([[0, z, one], [z, 0, z], [one, z, 0]], complex),
        np.array([[0, z, -i], [z, 0, z], [i, z, 0]], complex),
        np.array([[0, z, z], [z, 0, one], [z, one, 0]], complex),
        np.array([[0, z, z], [z, 0, -i], [z, i, 0]], complex),
        np.array([[1, z, z], [z, 1, z], [z, z, -2]], complex) / np.sqrt(3.0),
    )


def effective_potential(coefficients: np.ndarray, scalar: float = 0.0) -> np.ndarray:
    """Build V = scalar*I + sum_a coefficients[a]*lambda_a.

    Coefficients are real so the result is Hermitian.
    """
    coefficients = np.asarray(coefficients, dtype=float)
    if coefficients.shape != (8,) or not np.all(np.isfinite(coefficients)):
        raise ValueError("coefficients must be eight finite real values")
    if not np.isfinite(scalar):
        raise ValueError("scalar must be finite")
    V = float(scalar) * np.eye(3, dtype=complex)
    for c, lam in zip(coefficients, gell_mann()):
        V = V + float(c) * lam
    return V


def vacuum_hamiltonian(mass_squared: np.ndarray, mixing: np.ndarray, energy: float) -> np.ndarray:
    """Return U diag(m_i^2) U^dagger/(2E) in natural units."""
    mass_squared = np.asarray(mass_squared, dtype=float)
    mixing = np.asarray(mixing, dtype=complex)
    if mass_squared.shape != (3,) or not np.all(np.isfinite(mass_squared)):
        raise ValueError("mass_squared must contain three finite values")
    if mixing.shape != (3, 3) or not np.all(np.isfinite(mixing)):
        raise ValueError("mixing must be a finite 3x3 matrix")
    if not np.isfinite(energy) or energy <= 0.0:
        raise ValueError("energy must be finite and positive")
    ident = mixing.conj().T @ mixing
    if not np.allclose(ident, np.eye(3), atol=1e-10):
        raise ValueError("mixing must be unitary")
    H = mixing @ np.diag(mass_squared / (2.0 * float(energy))) @ mixing.conj().T
    return 0.5 * (H + H.conj().T)


def matter_potential(v_cc: float) -> np.ndarray:
    """Standard flavour-basis charged-current matter potential diag(Vcc,0,0)."""
    if not np.isfinite(v_cc):
        raise ValueError("v_cc must be finite")
    return np.diag([float(v_cc), 0.0, 0.0]).astype(complex)


def evolve_constant_hamiltonian(H: np.ndarray, state: np.ndarray, distance: float) -> np.ndarray:
    """Unitary evolution exp(-i H L)|state> for constant Hermitian H."""
    H = np.asarray(H, dtype=complex)
    state = np.asarray(state, dtype=complex)
    if H.shape != (3, 3) or state.shape != (3,):
        raise ValueError("H must be 3x3 and state must have shape (3,)")
    if not np.all(np.isfinite(H)) or not np.all(np.isfinite(state)):
        raise ValueError("H and state must be finite")
    if not np.isfinite(distance):
        raise ValueError("distance must be finite")
    if not np.allclose(H, H.conj().T, atol=1e-12):
        raise ValueError("H must be Hermitian")
    norm = np.linalg.norm(state)
    if norm == 0.0:
        raise ValueError("state must be non-zero")
    state = state / norm
    eigvals, eigvecs = np.linalg.eigh(H)
    phases = np.exp(-1j * eigvals * float(distance))
    return eigvecs @ (phases * (eigvecs.conj().T @ state))


def flavour_probabilities(state: np.ndarray) -> np.ndarray:
    """Return normalized flavour probabilities |nu_alpha|^2."""
    state = np.asarray(state, dtype=complex)
    if state.shape != (3,) or not np.all(np.isfinite(state)):
        raise ValueError("state must be a finite length-3 vector")
    p = np.abs(state) ** 2
    total = float(np.sum(p))
    if total == 0.0:
        raise ValueError("state must be non-zero")
    return p / total
