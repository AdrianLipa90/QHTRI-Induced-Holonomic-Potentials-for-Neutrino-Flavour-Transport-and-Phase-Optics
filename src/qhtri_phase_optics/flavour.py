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


def pmns_matrix(
    theta12: float,
    theta13: float,
    theta23: float,
    delta_cp: float = 0.0,
) -> np.ndarray:
    """Return the standard three-flavour PMNS matrix without Majorana phases.

    Angles and ``delta_cp`` are in radians. Majorana phases are omitted because
    they do not affect ordinary flavour-oscillation probabilities.
    """
    vals = np.asarray([theta12, theta13, theta23, delta_cp], dtype=float)
    if not np.all(np.isfinite(vals)):
        raise ValueError("PMNS parameters must be finite")

    s12, s13, s23 = np.sin([theta12, theta13, theta23])
    c12, c13, c23 = np.cos([theta12, theta13, theta23])
    ep = np.exp(1j * float(delta_cp))
    em = np.conj(ep)

    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * em],
            [
                -s12 * c23 - c12 * s23 * s13 * ep,
                c12 * c23 - s12 * s23 * s13 * ep,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * ep,
                -c12 * s23 - s12 * c23 * s13 * ep,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


def compose_hamiltonian(*terms: np.ndarray) -> np.ndarray:
    """Sum finite Hermitian 3x3 Hamiltonian terms and fail closed otherwise."""
    if not terms:
        raise ValueError("at least one Hamiltonian term is required")
    total = np.zeros((3, 3), dtype=complex)
    for term in terms:
        term = np.asarray(term, dtype=complex)
        if term.shape != (3, 3) or not np.all(np.isfinite(term)):
            raise ValueError("each Hamiltonian term must be a finite 3x3 matrix")
        if not np.allclose(term, term.conj().T, atol=1e-12):
            raise ValueError("each Hamiltonian term must be Hermitian")
        total = total + term
    return total


def evolve_piecewise(
    hamiltonians: np.ndarray,
    state: np.ndarray,
    distances: np.ndarray,
) -> np.ndarray:
    """Path-ordered evolution through piecewise-constant Hamiltonian segments.

    The first Hamiltonian acts first. This is the minimal numerical surface for
    non-commuting spatial potentials; no physical QHTRI coupling is assumed.
    """
    hamiltonians = np.asarray(hamiltonians, dtype=complex)
    distances = np.asarray(distances, dtype=float)
    if hamiltonians.ndim != 3 or hamiltonians.shape[1:] != (3, 3):
        raise ValueError("hamiltonians must have shape (N, 3, 3)")
    if distances.shape != (hamiltonians.shape[0],):
        raise ValueError("distances must contain one value per Hamiltonian")
    if not np.all(np.isfinite(distances)) or np.any(distances < 0.0):
        raise ValueError("distances must be finite and non-negative")

    out = np.asarray(state, dtype=complex)
    for H, distance in zip(hamiltonians, distances):
        out = evolve_constant_hamiltonian(H, out, float(distance))
    return out
