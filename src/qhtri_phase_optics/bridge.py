from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class OscillatorFeatures:
    """Calibratable summary of one oscillator-bank snapshot."""

    order_parameter: float
    mean_phase: float
    circular_variance: float
    amplitude_rms: float
    weighted_frequency: float


def oscillator_features(
    amplitudes: np.ndarray,
    phases: np.ndarray,
    frequencies: np.ndarray,
) -> OscillatorFeatures:
    """Extract measurable oscillator features without assigning a neutrino coupling.

    ``order_parameter`` is the amplitude-weighted Kuramoto magnitude. The
    function is deliberately agnostic about the physical origin of the input.
    """
    amplitudes = np.asarray(amplitudes, dtype=float)
    phases = np.asarray(phases, dtype=float)
    frequencies = np.asarray(frequencies, dtype=float)
    if amplitudes.ndim != 1 or amplitudes.size == 0:
        raise ValueError("oscillator arrays must be non-empty 1D arrays")
    if phases.shape != amplitudes.shape or frequencies.shape != amplitudes.shape:
        raise ValueError("amplitudes, phases and frequencies must have equal shape")
    if not all(np.all(np.isfinite(x)) for x in (amplitudes, phases, frequencies)):
        raise ValueError("oscillator inputs must be finite")

    weights = np.abs(amplitudes)
    total = float(np.sum(weights))
    if total == 0.0:
        raise ValueError("at least one oscillator amplitude must be non-zero")

    z = np.sum(weights * np.exp(1j * phases)) / total
    r = float(abs(z))
    mean_phase = float(np.angle(z)) if r > 1e-15 else 0.0
    amplitude_rms = float(np.sqrt(np.mean(amplitudes**2)))
    weighted_frequency = float(np.sum(weights * frequencies) / total)
    return OscillatorFeatures(
        order_parameter=r,
        mean_phase=mean_phase,
        circular_variance=1.0 - r,
        amplitude_rms=amplitude_rms,
        weighted_frequency=weighted_frequency,
    )


def phase_slope_curvature(x: np.ndarray, phase: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return first and second spatial derivatives of an unwrapped phase trace."""
    x = np.asarray(x, dtype=float)
    phase = np.asarray(phase, dtype=float)
    if x.ndim != 1 or phase.shape != x.shape or x.size < 3:
        raise ValueError("x and phase must be equal-length 1D arrays with at least 3 samples")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(phase)):
        raise ValueError("x and phase must be finite")
    if np.any(np.diff(x) <= 0.0):
        raise ValueError("x must be strictly increasing")

    unwrapped = np.unwrap(phase)
    edge_order = 2 if x.size >= 3 else 1
    slope = np.gradient(unwrapped, x, edge_order=edge_order)
    curvature = np.gradient(slope, x, edge_order=edge_order)
    return slope, curvature


def oscillating_drive(
    amplitude: float,
    angular_frequency: float,
    t: np.ndarray | float,
    phase: float = 0.0,
) -> np.ndarray:
    """Legacy NASER oscillator scaffold B(t)=B0 cos(omega t + phase).

    This is a drive waveform only; the function makes no coupling claim.
    """
    vals = np.asarray([amplitude, angular_frequency, phase], dtype=float)
    if not np.all(np.isfinite(vals)):
        raise ValueError("drive parameters must be finite")
    t = np.asarray(t, dtype=float)
    if not np.all(np.isfinite(t)):
        raise ValueError("t must be finite")
    return float(amplitude) * np.cos(float(angular_frequency) * t + float(phase))


def legacy_phase_imprint_proxy(
    neutrino_phase_slope: np.ndarray | float,
    drive_phase_slope: np.ndarray | float,
    beta: float,
) -> np.ndarray:
    """Retyped NASER phase-imprint proxy beta*dphi_nu/dx*dphi_drive/dx.

    The equation is retained strictly as a legacy model proxy. ``beta`` is not
    assigned a physical value by this repository and must be calibrated or
    falsified experimentally before physical interpretation.
    """
    if not np.isfinite(beta):
        raise ValueError("beta must be finite")
    a = np.asarray(neutrino_phase_slope, dtype=float)
    b = np.asarray(drive_phase_slope, dtype=float)
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
        raise ValueError("phase slopes must be finite")
    try:
        return float(beta) * a * b
    except ValueError as exc:
        raise ValueError("phase slopes must be broadcast-compatible") from exc
