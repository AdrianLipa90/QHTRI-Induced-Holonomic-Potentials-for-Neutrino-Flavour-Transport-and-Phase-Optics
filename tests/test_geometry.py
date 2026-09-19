import numpy as np

from qhtri_phase_optics.geometry import (
    berry_holonomy,
    closure_residual,
    normalized_phase_state,
    thin_lens_phase,
)


def test_equal_amplitude_36d_state_is_normalized():
    phases = np.linspace(0.0, 2.0 * np.pi, 36, endpoint=False)
    state = normalized_phase_state(phases)
    assert state.shape == (36,)
    assert np.isclose(np.linalg.norm(state), 1.0)


def test_closed_holonomy_is_invariant_under_statewise_global_rephasing():
    paths = []
    for shift in (0.0, 0.2, 0.5, 0.9):
        p = np.linspace(0.0, 1.0, 36) * shift
        paths.append(normalized_phase_state(p))
    states = np.asarray(paths)
    gamma0 = berry_holonomy(states)

    alpha = np.array([0.17, -0.9, 2.1, 0.44])
    rephased = states * np.exp(1j * alpha)[:, None]
    gamma1 = berry_holonomy(rephased)
    assert np.isclose(np.exp(1j * gamma0), np.exp(1j * gamma1), atol=1e-12)


def test_closure_residual_zero_for_exact_model_closure():
    D = 0.12
    epsilon = -0.03
    winding = 1
    gamma = 2.0 * np.pi * (D + epsilon + winding)
    assert abs(closure_residual(gamma, epsilon, D, winding)) < 1e-12


def test_thin_lens_phase_has_expected_quadratic_curvature():
    k = 4.0
    f = 2.0
    h = 1e-4
    phi_m = thin_lens_phase(-h, k, f)
    phi_0 = thin_lens_phase(0.0, k, f)
    phi_p = thin_lens_phase(h, k, f)
    second = (phi_p - 2.0 * phi_0 + phi_m) / h**2
    assert np.isclose(second, -k / f, rtol=1e-7, atol=1e-7)
