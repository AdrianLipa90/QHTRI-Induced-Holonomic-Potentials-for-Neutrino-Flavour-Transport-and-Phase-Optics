from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .flavour import gell_mann

TAU = 2.0 * np.pi


@dataclass(frozen=True)
class U3Projection:
    """Typed result of a 36D-QHTRI -> u(3) operator projection."""

    matrix: np.ndarray
    scalar: float
    coefficients: np.ndarray

    @property
    def traceless(self) -> np.ndarray:
        return self.matrix - self.scalar * np.eye(3, dtype=complex)


def _as_hermitian(matrix: np.ndarray, shape: tuple[int, int], name: str) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=complex)
    if matrix.shape != shape or not np.all(np.isfinite(matrix)):
        raise ValueError(f"{name} must be a finite matrix with shape {shape}")
    if not np.allclose(matrix, matrix.conj().T, atol=1e-12):
        raise ValueError(f"{name} must be Hermitian")
    return matrix


def validate_flavour_embedding(embedding: np.ndarray) -> np.ndarray:
    """Validate an isometric embedding W: C^3 -> C^36.

    Columns define the three flavour-carrier directions inside the 36D
    computational carrier. The embedding is an explicit typed input: this
    function does not derive or fit it.
    """
    W = np.asarray(embedding, dtype=complex)
    if W.shape != (36, 3) or not np.all(np.isfinite(W)):
        raise ValueError("embedding must be a finite 36x3 complex matrix")
    if not np.allclose(W.conj().T @ W, np.eye(3), atol=1e-12):
        raise ValueError("embedding columns must be orthonormal")
    return W


def project_operator_to_flavour(
    h_qhtri: np.ndarray,
    embedding: np.ndarray,
) -> np.ndarray:
    """Apply Pi_W(H)=W^dagger H W from the 36D operator to u(3)."""
    H = _as_hermitian(h_qhtri, (36, 36), "h_qhtri")
    W = validate_flavour_embedding(embedding)
    projected = W.conj().T @ H @ W
    if not np.allclose(projected, projected.conj().T, atol=1e-12):
        raise RuntimeError("Hermiticity was not preserved by the projection")
    return projected


def decompose_u3(matrix: np.ndarray) -> U3Projection:
    """Decompose a Hermitian 3x3 matrix as v0*I + sum xi_a lambda_a.

    With Tr(lambda_a lambda_b)=2 delta_ab,
    v0 = Tr(H)/3 and xi_a = Tr(lambda_a H)/2.
    """
    H = _as_hermitian(matrix, (3, 3), "matrix")
    scalar_complex = np.trace(H) / 3.0
    if abs(float(np.imag(scalar_complex))) > 1e-12:
        raise RuntimeError("Hermitian trace unexpectedly has an imaginary component")
    scalar = float(np.real(scalar_complex))
    coeffs = np.array(
        [0.5 * np.real(np.trace(lam @ H)) for lam in gell_mann()],
        dtype=float,
    )
    reconstructed = scalar * np.eye(3, dtype=complex)
    for coefficient, lam in zip(coeffs, gell_mann()):
        reconstructed = reconstructed + coefficient * lam
    if not np.allclose(reconstructed, H, atol=1e-11):
        raise RuntimeError("u(3) decomposition failed its reconstruction gate")
    return U3Projection(matrix=H, scalar=scalar, coefficients=coeffs)


def pi_36_to_u3(h_qhtri: np.ndarray, embedding: np.ndarray) -> U3Projection:
    """Typed candidate interface Pi_{36->nu} followed by canonical u(3) decomposition."""
    return decompose_u3(project_operator_to_flavour(h_qhtri, embedding))


def closure_phase_rate(
    x: np.ndarray,
    gamma_ebi: np.ndarray,
    D_lambda: np.ndarray,
) -> np.ndarray:
    """Return dGamma_EBI/dx - 2*pi*dD_lambda/dx for a fixed winding branch.

    Under the model closure Gamma_EBI/(2*pi)=m+D_lambda+epsilon_nu,
    this equals 2*pi*d epsilon_nu/dx. The function is a consistency
    diagnostic and does not establish physical coupling.
    """
    x = np.asarray(x, dtype=float)
    gamma_ebi = np.asarray(gamma_ebi, dtype=float)
    D_lambda = np.asarray(D_lambda, dtype=float)
    if x.ndim != 1 or x.size < 3:
        raise ValueError("x must be a 1D array with at least three samples")
    if gamma_ebi.shape != x.shape or D_lambda.shape != x.shape:
        raise ValueError("gamma_ebi and D_lambda must match x")
    if not all(np.all(np.isfinite(v)) for v in (x, gamma_ebi, D_lambda)):
        raise ValueError("closure arrays must be finite")
    if np.any(np.diff(x) <= 0.0):
        raise ValueError("x must be strictly increasing")
    gamma_unwrapped = np.unwrap(gamma_ebi)
    dgamma = np.gradient(gamma_unwrapped, x, edge_order=2)
    dD = np.gradient(D_lambda, x, edge_order=2)
    return dgamma - TAU * dD
