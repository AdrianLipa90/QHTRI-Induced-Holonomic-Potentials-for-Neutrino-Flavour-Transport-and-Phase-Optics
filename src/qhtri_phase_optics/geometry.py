from __future__ import annotations

import numpy as np

TAU = 2.0 * np.pi


def _wrap_turns(x: float) -> float:
    """Wrap a dimensionless turn count to [-1/2, 1/2)."""
    return float((x + 0.5) % 1.0 - 0.5)


def normalized_phase_state(
    phases: np.ndarray,
    amplitudes: np.ndarray | None = None,
) -> np.ndarray:
    """Return a normalized complex phase state.

    With ``amplitudes=None`` this is the equal-amplitude QHTRI lift
    exp(i phi_j)/sqrt(N). No physical coupling claim is implied.
    """
    phases = np.asarray(phases, dtype=float)
    if phases.ndim != 1 or phases.size == 0:
        raise ValueError("phases must be a non-empty 1D array")
    if not np.all(np.isfinite(phases)):
        raise ValueError("phases must be finite")

    if amplitudes is None:
        amplitudes = np.ones_like(phases)
    else:
        amplitudes = np.asarray(amplitudes, dtype=float)
        if amplitudes.shape != phases.shape:
            raise ValueError("amplitudes must match phases")
        if not np.all(np.isfinite(amplitudes)):
            raise ValueError("amplitudes must be finite")

    state = amplitudes.astype(complex) * np.exp(1j * phases)
    norm = np.linalg.norm(state)
    if norm == 0.0:
        raise ValueError("state norm must be non-zero")
    return state / norm


def berry_holonomy(states: np.ndarray, *, overlap_floor: float = 1e-14) -> float:
    """Closed discrete Pancharatnam/Berry holonomy in radians.

    The returned phase is arg(prod_k <psi_k|psi_(k+1)>), including the
    final-to-first overlap. Each row is normalized internally.
    """
    states = np.asarray(states, dtype=complex)
    if states.ndim != 2 or states.shape[0] < 2 or states.shape[1] < 1:
        raise ValueError("states must have shape (N>=2, M>=1)")
    norms = np.linalg.norm(states, axis=1)
    if np.any(~np.isfinite(norms)) or np.any(norms == 0.0):
        raise ValueError("all states must be finite and non-zero")
    states = states / norms[:, None]

    product = 1.0 + 0.0j
    for i in range(states.shape[0]):
        overlap = np.vdot(states[i], states[(i + 1) % states.shape[0]])
        if abs(overlap) <= overlap_floor:
            raise ValueError("holonomy undefined for near-orthogonal adjacent states")
        product *= overlap / abs(overlap)
    return float(np.angle(product))


def closure_residual(
    gamma: float,
    epsilon_nu: float,
    D: float,
    winding: int = 0,
) -> float:
    """Wrapped residual of the working Euler-Berry closure relation.

    Model relation: gamma/(2*pi) = D + epsilon_nu + winding + residual.
    Returns residual in turns, wrapped to [-1/2, 1/2).
    """
    vals = np.asarray([gamma, epsilon_nu, D], dtype=float)
    if not np.all(np.isfinite(vals)):
        raise ValueError("closure inputs must be finite")
    raw = gamma / TAU - D - epsilon_nu - int(winding)
    return _wrap_turns(float(raw))


def thin_lens_phase(r: np.ndarray | float, k: float, focal_length: float) -> np.ndarray:
    """Ideal quadratic thin-lens phase -k r^2/(2 f)."""
    if not np.isfinite(k) or not np.isfinite(focal_length) or focal_length == 0.0:
        raise ValueError("k and non-zero focal_length must be finite")
    r = np.asarray(r, dtype=float)
    if not np.all(np.isfinite(r)):
        raise ValueError("r must be finite")
    return -float(k) * r * r / (2.0 * float(focal_length))
