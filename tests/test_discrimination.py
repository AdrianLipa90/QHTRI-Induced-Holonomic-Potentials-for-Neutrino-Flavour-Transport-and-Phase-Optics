import numpy as np

from qhtri_phase_optics.discrimination import run_three_model_discrimination


def test_m1_scalar_control_cannot_fake_flavour_change():
    H0 = np.array([[0.1, 0.04, 0.0], [0.04, 0.35, 0.03], [0.0, 0.03, 0.8]], complex)
    state = np.array([1.0, 0.0, 0.0], complex)
    result = run_three_model_discrimination(
        H0,
        state,
        5.0,
        scalar=1.7,
        coefficients=np.zeros(8),
    )
    assert result.scalar_control_delta < 1e-12
    assert result.flavour_effect_delta < 1e-12


def test_m2_nontrivial_flavour_potential_is_detectable_in_simulation():
    H0 = np.array([[0.1, 0.04, 0.0], [0.04, 0.35, 0.03], [0.0, 0.03, 0.8]], complex)
    state = np.array([1.0, 0.0, 0.0], complex)
    coefficients = np.zeros(8)
    coefficients[0] = 0.12
    coefficients[3] = -0.08
    result = run_three_model_discrimination(
        H0,
        state,
        5.0,
        scalar=1.7,
        coefficients=coefficients,
    )
    assert result.scalar_control_delta < 1e-12
    assert result.flavour_effect_delta > 1e-4
