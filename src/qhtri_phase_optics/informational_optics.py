from __future__ import annotations

import math
from typing import Sequence

import numpy as np


def _probability_vector(values: Sequence[float], name: str, *, strictly_positive: bool = False) -> np.ndarray:
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or x.size < 2 or not np.all(np.isfinite(x)):
        raise ValueError(f"{name} must be a finite one-dimensional probability vector")
    if strictly_positive:
        if np.any(x <= 0.0):
            raise ValueError(f"{name} entries must be strictly positive")
    elif np.any(x < 0.0):
        raise ValueError(f"{name} entries must be non-negative")
    if not np.isclose(float(x.sum()), 1.0, atol=1e-12, rtol=0.0):
        raise ValueError(f"{name} must sum to one")
    return x


def relative_information_nat(p: Sequence[float], reference: Sequence[float]) -> float:
    """Natural-log KL divergence D_KL(p || reference)."""
    p_vec = _probability_vector(p, "p")
    ref = _probability_vector(reference, "reference", strictly_positive=True)
    if p_vec.shape != ref.shape:
        raise ValueError("p and reference must have the same shape")
    mask = p_vec > 0.0
    return float(np.sum(p_vec[mask] * np.log(p_vec[mask] / ref[mask])))


def information_curvature(
    p: Sequence[float],
    reference: Sequence[float],
    relational_area: float,
) -> float:
    """RF-L3/RF-L4A information scalar Xi_I = D_KL / A_rel."""
    area = float(relational_area)
    if not math.isfinite(area) or area <= 0.0:
        raise ValueError("relational_area must be finite and positive")
    return relative_information_nat(p, reference) / area


def information_scalar_potential(
    p: Sequence[float],
    reference: Sequence[float],
    relational_area: float,
    *,
    alpha_i: float,
    kappa_e: float,
) -> float:
    """U_I = (alpha_I / kappa_E) Xi_I."""
    alpha = float(alpha_i)
    kappa = float(kappa_e)
    if not math.isfinite(alpha) or not math.isfinite(kappa) or kappa == 0.0:
        raise ValueError("alpha_i and nonzero kappa_e must be finite")
    return (alpha / kappa) * information_curvature(p, reference, relational_area)


def observation_potential_shift(
    before: Sequence[float],
    after: Sequence[float],
    reference: Sequence[float],
    *,
    area_before: float,
    area_after: float | None = None,
    alpha_i: float,
    kappa_e: float,
) -> float:
    """Exact potential update caused by an admitted relational-state update."""
    if area_after is None:
        area_after = area_before
    u0 = information_scalar_potential(
        before, reference, area_before, alpha_i=alpha_i, kappa_e=kappa_e
    )
    u1 = information_scalar_potential(
        after, reference, area_after, alpha_i=alpha_i, kappa_e=kappa_e
    )
    return u1 - u0


def phase_screen_from_potential(
    potential: Sequence[float] | np.ndarray,
    *,
    phase_measure: float,
) -> np.ndarray:
    """Map a potential profile to phase after a declared propagation coupling.

    phase_measure is the typed route-specific integral factor that converts the
    potential coordinate to dimensionless accumulated phase. It is not inferred
    by this module.
    """
    measure = float(phase_measure)
    u = np.asarray(potential, dtype=float)
    if not math.isfinite(measure) or not np.all(np.isfinite(u)):
        raise ValueError("phase_measure and potential must be finite")
    return -measure * u


def phase_screen_from_information_curvature(
    xi_field: Sequence[float] | np.ndarray,
    *,
    alpha_i: float,
    kappa_e: float,
    phase_measure: float,
) -> np.ndarray:
    """Compose Xi_I -> U_I -> Phi_I for an already-constructed Xi field."""
    alpha = float(alpha_i)
    kappa = float(kappa_e)
    xi = np.asarray(xi_field, dtype=float)
    if not math.isfinite(alpha) or not math.isfinite(kappa) or kappa == 0.0:
        raise ValueError("alpha_i and nonzero kappa_e must be finite")
    if not np.all(np.isfinite(xi)):
        raise ValueError("xi_field must be finite")
    return phase_screen_from_potential((alpha / kappa) * xi, phase_measure=phase_measure)
