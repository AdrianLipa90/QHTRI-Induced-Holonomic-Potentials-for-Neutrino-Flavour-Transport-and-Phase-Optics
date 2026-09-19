import numpy as np

from qhtri_phase_optics.informational_optics import (
    information_curvature,
    information_scalar_potential,
    observation_potential_shift,
    phase_screen_from_information_curvature,
    phase_screen_from_potential,
    relative_information_nat,
)


def test_reference_state_has_zero_information_and_zero_potential():
    ref = [0.2, 0.3, 0.5]
    assert relative_information_nat(ref, ref) == 0.0
    assert information_curvature(ref, ref, 2.0) == 0.0
    assert information_scalar_potential(ref, ref, 2.0, alpha_i=3.0, kappa_e=4.0) == 0.0


def test_observation_update_changes_potential_by_exact_kl_difference():
    ref = [1 / 3, 1 / 3, 1 / 3]
    before = [0.4, 0.3, 0.3]
    after = [0.7, 0.2, 0.1]
    area = 2.5
    alpha = 0.8
    kappa = 1.7
    expected = (alpha / (kappa * area)) * (
        relative_information_nat(after, ref) - relative_information_nat(before, ref)
    )
    got = observation_potential_shift(
        before, after, ref, area_before=area, alpha_i=alpha, kappa_e=kappa
    )
    assert np.isclose(got, expected, atol=1e-14)


def test_area_update_is_part_of_information_curvature_update():
    ref = [0.5, 0.5]
    p = [0.8, 0.2]
    alpha = 2.0
    kappa = 5.0
    got = observation_potential_shift(
        p, p, ref, area_before=2.0, area_after=4.0, alpha_i=alpha, kappa_e=kappa
    )
    u0 = information_scalar_potential(p, ref, 2.0, alpha_i=alpha, kappa_e=kappa)
    u1 = information_scalar_potential(p, ref, 4.0, alpha_i=alpha, kappa_e=kappa)
    assert np.isclose(got, u1 - u0, atol=1e-14)
    assert got < 0.0


def test_zero_information_coupling_blocks_potential_update():
    ref = [0.5, 0.5]
    got = observation_potential_shift(
        [0.5, 0.5],
        [0.9, 0.1],
        ref,
        area_before=1.0,
        alpha_i=0.0,
        kappa_e=2.0,
    )
    assert got == 0.0


def test_phase_screen_requires_only_potential_and_declared_phase_measure():
    potential = np.array([0.0, 1.0, 4.0])
    phase = phase_screen_from_potential(potential, phase_measure=0.25)
    assert np.allclose(phase, [0.0, -0.25, -1.0])


def test_information_curvature_to_phase_composition_is_linear():
    xi = np.array([0.0, 1.0, 4.0])
    phase = phase_screen_from_information_curvature(
        xi, alpha_i=2.0, kappa_e=4.0, phase_measure=3.0
    )
    assert np.allclose(phase, -1.5 * xi)


def test_quadratic_information_potential_produces_constant_phase_curvature():
    x = np.linspace(-2.0, 2.0, 101)
    u = 0.75 * x**2 + 0.2
    phase = phase_screen_from_potential(u, phase_measure=2.0)
    dx = x[1] - x[0]
    second = (phase[:-2] - 2.0 * phase[1:-1] + phase[2:]) / dx**2
    assert np.allclose(second, -3.0, atol=1e-10)
