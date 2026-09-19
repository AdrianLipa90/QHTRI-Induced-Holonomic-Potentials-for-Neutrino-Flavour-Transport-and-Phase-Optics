"""Orbit/epicycle to radial-scalar phase-curvature identities.

Mathematical bridge only. No spacetime-metric promotion is implied.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


class OrbitCurvatureError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise OrbitCurvatureError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise OrbitCurvatureError(f"{name} must be > 0")
    return value


@dataclass(frozen=True)
class RadialScalarCurvature:
    radial: float
    tangential_1: float
    tangential_2: float

    @property
    def trace(self) -> float:
        return self.radial + self.tangential_1 + self.tangential_2


def epicyclic_sq(radius: float, omega_sq: float, d_omega_sq_dr: float) -> float:
    r = _positive("radius", radius)
    return 4.0 * _finite("omega_sq", omega_sq) + r * _finite(
        "d_omega_sq_dr", d_omega_sq_dr
    )


def radial_scalar_gradient(radius: float, omega_sq: float) -> float:
    """Return Phi'(r)=r Omega^2."""

    r = _positive("radius", radius)
    return r * _finite("omega_sq", omega_sq)


def radial_scalar_second_derivative(omega_sq: float, kappa_sq: float) -> float:
    """Return Phi''=kappa^2-3 Omega^2."""

    return _finite("kappa_sq", kappa_sq) - 3.0 * _finite("omega_sq", omega_sq)


def radial_hessian_eigenvalues(
    omega_sq: float, kappa_sq: float
) -> RadialScalarCurvature:
    w2 = _finite("omega_sq", omega_sq)
    radial = radial_scalar_second_derivative(w2, kappa_sq)
    return RadialScalarCurvature(radial=radial, tangential_1=w2, tangential_2=w2)


def transverse_phase_gradient(
    radius: float, impact_parameter: float, omega_sq: float
) -> float:
    r = _positive("radius", radius)
    b = _finite("impact_parameter", impact_parameter)
    if abs(b) > r:
        raise OrbitCurvatureError("|impact_parameter| must be <= radius")
    return b * _finite("omega_sq", omega_sq)


def transverse_phase_curvature(
    radius: float,
    impact_parameter: float,
    omega_sq: float,
    kappa_sq: float,
) -> float:
    r = _positive("radius", radius)
    b = _finite("impact_parameter", impact_parameter)
    if abs(b) > r:
        raise OrbitCurvatureError("|impact_parameter| must be <= radius")
    beta2 = (b / r) ** 2
    w2 = _finite("omega_sq", omega_sq)
    k2 = _finite("kappa_sq", kappa_sq)
    return beta2 * k2 + (1.0 - 4.0 * beta2) * w2


def power_law_curvature_signature(
    exponent_q: float, omega_sq: float
) -> RadialScalarCurvature:
    q = _finite("exponent_q", exponent_q)
    w2 = _finite("omega_sq", omega_sq)
    k2 = (4.0 - q) * w2
    return radial_hessian_eigenvalues(w2, k2)


def central_consistency_residual(
    radius: float,
    omega_sq: float,
    d_omega_sq_dr: float,
    measured_kappa_sq: float,
) -> float:
    return _finite("measured_kappa_sq", measured_kappa_sq) - epicyclic_sq(
        radius, omega_sq, d_omega_sq_dr
    )
