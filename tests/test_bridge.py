import numpy as np

from qhtri_phase_optics.bridge import (
    legacy_phase_imprint_proxy,
    oscillating_drive,
    oscillator_features,
    phase_slope_curvature,
)


def test_aligned_oscillators_have_unit_order_parameter():
    features = oscillator_features(
        np.ones(36),
        np.full(36, 0.37),
        np.full(36, 2.0 * np.pi * 7.83),
    )
    assert np.isclose(features.order_parameter, 1.0, atol=1e-12)
    assert np.isclose(features.circular_variance, 0.0, atol=1e-12)


def test_uniform_phase_ring_has_near_zero_order_parameter():
    phases = np.linspace(0.0, 2.0 * np.pi, 36, endpoint=False)
    features = oscillator_features(np.ones(36), phases, np.ones(36))
    assert features.order_parameter < 1e-12


def test_quadratic_phase_recovers_constant_curvature():
    x = np.linspace(-1.0, 1.0, 101)
    a, b, c = 0.4, -0.2, 0.1
    phase = a * x**2 + b * x + c
    slope, curvature = phase_slope_curvature(x, phase)
    assert np.allclose(slope[2:-2], 2.0 * a * x[2:-2] + b, atol=1e-10)
    assert np.allclose(curvature[2:-2], 2.0 * a, atol=1e-10)


def test_oscillating_drive_matches_legacy_scaffold():
    t = np.array([0.0, np.pi / 2.0, np.pi])
    out = oscillating_drive(2.0, 1.0, t)
    assert np.allclose(out, [2.0, 0.0, -2.0], atol=1e-12)


def test_legacy_phase_imprint_proxy_is_explicit_product():
    nu = np.array([1.0, 2.0, -1.0])
    drive = np.array([0.5, -0.25, 3.0])
    assert np.allclose(legacy_phase_imprint_proxy(nu, drive, 0.2), 0.2 * nu * drive)
