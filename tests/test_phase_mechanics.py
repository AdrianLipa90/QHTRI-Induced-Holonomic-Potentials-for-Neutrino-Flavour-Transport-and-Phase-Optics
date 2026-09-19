import math

import numpy as np

from qhtri_phase_optics.phase_mechanics import (
    caustic_determinant,
    canonical_momentum_from_phase_gradient,
    convergence_and_shear_from_lensing_hessian,
    informational_force_from_curvature_gradient,
    inverse_focal_tensor_from_information_hessian,
    lens_jacobian_from_phase_hessian,
    phase_hessian_from_information_hessian,
    phase_rate_from_potential,
    point_mass_weak_field_deflection,
)


def test_phase_rate_is_potential_over_action_scale():
    assert np.allclose(
        phase_rate_from_potential([2.0, 4.0], action_scale=2.0),
        [-1.0, -2.0],
    )


def test_hamilton_jacobi_momentum_interface():
    assert np.allclose(
        canonical_momentum_from_phase_gradient([1.0, 2.0], action_scale=3.0),
        [3.0, 6.0],
    )


def test_information_gradient_generates_force():
    assert np.allclose(
        informational_force_from_curvature_gradient([1.0, -2.0], alpha_i=2.0, kappa_e=4.0),
        [-0.5, 1.0],
    )


def test_information_hessian_maps_to_phase_hessian():
    xi_hessian = 2.0 * np.eye(2)
    got = phase_hessian_from_information_hessian(
        xi_hessian,
        alpha_i=2.0,
        kappa_e=4.0,
        phase_measure=3.0,
    )
    assert np.allclose(got, -3.0 * np.eye(2))


def test_information_hessian_maps_to_inverse_focal_tensor():
    xi_hessian = 2.0 * np.eye(2)
    got = inverse_focal_tensor_from_information_hessian(
        xi_hessian,
        alpha_i=2.0,
        kappa_e=4.0,
        phase_measure=3.0,
        wavenumber=6.0,
    )
    assert np.allclose(got, 0.5 * np.eye(2))


def test_caustic_condition_is_zero_jacobian_determinant():
    hphi = -2.0 * np.eye(2)
    jac = lens_jacobian_from_phase_hessian(
        hphi,
        propagation_distance=3.0,
        wavenumber=6.0,
    )
    assert np.allclose(jac, np.zeros((2, 2)))
    assert abs(
        caustic_determinant(
            hphi,
            propagation_distance=3.0,
            wavenumber=6.0,
        )
    ) < 1e-15


def test_point_mass_gr_crosscheck():
    got = point_mass_weak_field_deflection(
        1.0,
        2.0,
        gravitational_constant=3.0,
        light_speed=4.0,
    )
    assert math.isclose(got, 0.375)


def test_lensing_hessian_splits_convergence_and_shear():
    assert convergence_and_shear_from_lensing_hessian(
        [[2.0, 1.0], [1.0, 4.0]]
    ) == (3.0, -1.0, 1.0)


def test_asymmetric_lensing_hessian_is_rejected():
    try:
        convergence_and_shear_from_lensing_hessian([[1.0, 2.0], [0.0, 1.0]])
    except ValueError:
        return
    raise AssertionError("asymmetric lensing Hessian must fail closed")
