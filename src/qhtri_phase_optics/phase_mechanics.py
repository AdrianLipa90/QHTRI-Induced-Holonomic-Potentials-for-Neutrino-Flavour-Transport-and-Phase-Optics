from __future__ import annotations

import math
from typing import Sequence

import numpy as np


def _finite_nonzero(value: float, name: str) -> float:
    x = float(value)
    if not math.isfinite(x) or x == 0.0:
        raise ValueError(f"{name} must be finite and nonzero")
    return x


def _finite_positive(value: float, name: str) -> float:
    x = float(value)
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name} must be finite and positive")
    return x


def phase_rate_from_potential(
    potential: Sequence[float] | np.ndarray | float,
    *,
    action_scale: float,
) -> np.ndarray:
    """Return dPhi/dt = -U/action_scale for a declared phase-action scale."""
    eta = _finite_nonzero(action_scale, "action_scale")
    u = np.asarray(potential, dtype=float)
    if not np.all(np.isfinite(u)):
        raise ValueError("potential must be finite")
    return -u / eta


def canonical_momentum_from_phase_gradient(
    phase_gradient: Sequence[float] | np.ndarray,
    *,
    action_scale: float,
) -> np.ndarray:
    """Hamilton-Jacobi interface p = action_scale * grad(Phi)."""
    eta = _finite_nonzero(action_scale, "action_scale")
    grad = np.asarray(phase_gradient, dtype=float)
    if not np.all(np.isfinite(grad)):
        raise ValueError("phase_gradient must be finite")
    return eta * grad


def informational_force_from_curvature_gradient(
    xi_gradient: Sequence[float] | np.ndarray,
    *,
    alpha_i: float,
    kappa_e: float,
) -> np.ndarray:
    """F_I = -(alpha_I/kappa_E) grad(Xi_I)."""
    alpha = float(alpha_i)
    kappa = _finite_nonzero(kappa_e, "kappa_e")
    grad = np.asarray(xi_gradient, dtype=float)
    if not math.isfinite(alpha) or not np.all(np.isfinite(grad)):
        raise ValueError("alpha_i and xi_gradient must be finite")
    return -(alpha / kappa) * grad


def phase_hessian_from_information_hessian(
    xi_hessian: Sequence[Sequence[float]] | np.ndarray,
    *,
    alpha_i: float,
    kappa_e: float,
    phase_measure: float,
) -> np.ndarray:
    """Thin-screen Hess(Phi) = -chi_phi*(alpha_I/kappa_E)*Hess(Xi_I)."""
    alpha = float(alpha_i)
    kappa = _finite_nonzero(kappa_e, "kappa_e")
    chi = float(phase_measure)
    h = np.asarray(xi_hessian, dtype=float)
    if h.ndim != 2 or h.shape[0] != h.shape[1]:
        raise ValueError("xi_hessian must be a finite square matrix")
    if not math.isfinite(alpha) or not math.isfinite(chi) or not np.all(np.isfinite(h)):
        raise ValueError("alpha_i, phase_measure and xi_hessian must be finite")
    return -chi * (alpha / kappa) * h


def inverse_focal_tensor_from_information_hessian(
    xi_hessian: Sequence[Sequence[float]] | np.ndarray,
    *,
    alpha_i: float,
    kappa_e: float,
    phase_measure: float,
    wavenumber: float,
) -> np.ndarray:
    """F^{-1} = chi_phi*alpha_I/(k*kappa_E)*Hess(Xi_I)."""
    k = _finite_nonzero(wavenumber, "wavenumber")
    hphi = phase_hessian_from_information_hessian(
        xi_hessian,
        alpha_i=alpha_i,
        kappa_e=kappa_e,
        phase_measure=phase_measure,
    )
    return -hphi / k


def lens_jacobian_from_phase_hessian(
    phase_hessian: Sequence[Sequence[float]] | np.ndarray,
    *,
    propagation_distance: float,
    wavenumber: float,
) -> np.ndarray:
    """J = I + (L/k) Hess(Phi) for a paraxial thin phase screen."""
    length = float(propagation_distance)
    k = _finite_nonzero(wavenumber, "wavenumber")
    h = np.asarray(phase_hessian, dtype=float)
    if h.ndim != 2 or h.shape[0] != h.shape[1] or not np.all(np.isfinite(h)):
        raise ValueError("phase_hessian must be a finite square matrix")
    if not math.isfinite(length):
        raise ValueError("propagation_distance must be finite")
    return np.eye(h.shape[0], dtype=float) + (length / k) * h


def caustic_determinant(
    phase_hessian: Sequence[Sequence[float]] | np.ndarray,
    *,
    propagation_distance: float,
    wavenumber: float,
) -> float:
    """det(J); a critical/caustic surface occurs at det(J)=0 in this model."""
    return float(
        np.linalg.det(
            lens_jacobian_from_phase_hessian(
                phase_hessian,
                propagation_distance=propagation_distance,
                wavenumber=wavenumber,
            )
        )
    )


def point_mass_weak_field_deflection(
    mass: float,
    impact_parameter: float,
    *,
    gravitational_constant: float,
    light_speed: float,
) -> float:
    """Standard weak-field GR cross-check: |alpha| = 4GM/(b c^2)."""
    m = _finite_positive(mass, "mass")
    b = _finite_positive(impact_parameter, "impact_parameter")
    g = _finite_positive(gravitational_constant, "gravitational_constant")
    c = _finite_positive(light_speed, "light_speed")
    return 4.0 * g * m / (b * c * c)


def convergence_and_shear_from_lensing_hessian(
    lensing_hessian: Sequence[Sequence[float]] | np.ndarray,
) -> tuple[float, float, float]:
    """Return (convergence, gamma1, gamma2) for a symmetric 2x2 lensing Hessian."""
    h = np.asarray(lensing_hessian, dtype=float)
    if h.shape != (2, 2) or not np.all(np.isfinite(h)):
        raise ValueError("lensing_hessian must be a finite 2x2 matrix")
    if not np.allclose(h, h.T, atol=1e-12, rtol=0.0):
        raise ValueError("lensing_hessian must be symmetric")
    convergence = 0.5 * float(h[0, 0] + h[1, 1])
    gamma1 = 0.5 * float(h[0, 0] - h[1, 1])
    gamma2 = float(h[0, 1])
    return convergence, gamma1, gamma2
