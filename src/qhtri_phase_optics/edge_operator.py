from __future__ import annotations

import numpy as np

FLAVOUR_ORDER = ("e", "mu", "tau")


def assemble_oriented_flavour_exchange(
    j_e_mu: complex,
    j_mu_tau: complex,
    j_tau_e: complex,
    diagonal: np.ndarray | tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> np.ndarray:
    """Assemble a Hermitian three-flavour operator from oriented complex edges."""
    values = np.asarray([j_e_mu, j_mu_tau, j_tau_e], dtype=complex)
    if not np.all(np.isfinite(values)):
        raise ValueError("edge couplings must be finite")
    d = np.asarray(diagonal, dtype=float)
    if d.shape != (3,) or not np.all(np.isfinite(d)):
        raise ValueError("diagonal must contain three finite real values")
    H = np.diag(d.astype(complex))
    H[0, 1] = values[0]
    H[1, 0] = np.conj(values[0])
    H[1, 2] = values[1]
    H[2, 1] = np.conj(values[1])
    H[2, 0] = values[2]
    H[0, 2] = np.conj(values[2])
    if not np.allclose(H, H.conj().T, atol=1e-13):
        raise RuntimeError("edge assembly failed Hermiticity")
    return H


def flavour_cycle_phase(matrix: np.ndarray, *, zero_tolerance: float = 1e-15) -> float | None:
    """Return arg(H_e_mu H_mu_tau H_tau_e), a flavour-rephasing invariant."""
    H = np.asarray(matrix, dtype=complex)
    if H.shape != (3, 3) or not np.all(np.isfinite(H)):
        raise ValueError("matrix must be a finite 3x3 array")
    if not np.allclose(H, H.conj().T, atol=1e-12):
        raise ValueError("matrix must be Hermitian")
    product = H[0, 1] * H[1, 2] * H[2, 0]
    if abs(product) <= float(zero_tolerance):
        return None
    return float(np.angle(product))


def rephase_flavour_operator(matrix: np.ndarray, phases: np.ndarray) -> np.ndarray:
    """Apply H -> D^dagger H D for a local flavour-basis rephasing."""
    H = np.asarray(matrix, dtype=complex)
    phi = np.asarray(phases, dtype=float)
    if H.shape != (3, 3) or phi.shape != (3,):
        raise ValueError("matrix must be 3x3 and phases must have shape (3,)")
    if not np.all(np.isfinite(H)) or not np.all(np.isfinite(phi)):
        raise ValueError("inputs must be finite")
    D = np.diag(np.exp(1j * phi))
    return D.conj().T @ H @ D


def traceless_part(matrix: np.ndarray) -> np.ndarray:
    """Remove the common U(1) identity component."""
    H = np.asarray(matrix, dtype=complex)
    if H.shape != (3, 3) or not np.all(np.isfinite(H)):
        raise ValueError("matrix must be a finite 3x3 array")
    return H - (np.trace(H) / 3.0) * np.eye(3, dtype=complex)


def route_mismatch(
    pullback_matrix: np.ndarray,
    edge_matrix: np.ndarray,
    *,
    remove_identity: bool = True,
) -> float:
    """Max-absolute mismatch between pullback and edge-assembly routes."""
    A = np.asarray(pullback_matrix, dtype=complex)
    B = np.asarray(edge_matrix, dtype=complex)
    if A.shape != (3, 3) or B.shape != (3, 3):
        raise ValueError("both operators must be 3x3")
    if not np.all(np.isfinite(A)) or not np.all(np.isfinite(B)):
        raise ValueError("operators must be finite")
    if remove_identity:
        A = traceless_part(A)
        B = traceless_part(B)
    return float(np.max(np.abs(A - B)))
