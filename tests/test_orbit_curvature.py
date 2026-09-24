import pytest

from qhtri_phase_optics.orbit_curvature import (
    OrbitCurvatureError,
    central_consistency_residual,
    epicyclic_sq,
    power_law_curvature_signature,
    radial_hessian_eigenvalues,
    radial_scalar_gradient,
    radial_scalar_second_derivative,
    transverse_phase_curvature,
    transverse_phase_gradient,
)


@pytest.mark.parametrize(
    ("q", "expected"),
    [
        (3.0, (-2.0, 1.0, 1.0)),
        (2.0, (-1.0, 1.0, 1.0)),
        (0.0, (1.0, 1.0, 1.0)),
    ],
)
def test_power_law_hessian_signatures(q, expected):
    curv = power_law_curvature_signature(q, 2.5)
    scale = 2.5
    assert (
        curv.radial / scale,
        curv.tangential_1 / scale,
        curv.tangential_2 / scale,
    ) == pytest.approx(expected)


def test_radial_gradient_and_second_derivative():
    r = 4.0
    omega_sq = 0.5
    kappa_sq = 0.8
    assert radial_scalar_gradient(r, omega_sq) == pytest.approx(2.0)
    assert radial_scalar_second_derivative(omega_sq, kappa_sq) == pytest.approx(
        -0.7
    )
    curv = radial_hessian_eigenvalues(omega_sq, kappa_sq)
    assert curv.radial == pytest.approx(-0.7)
    assert curv.tangential_1 == pytest.approx(0.5)
    assert curv.tangential_2 == pytest.approx(0.5)


def test_transverse_bridge():
    r = 5.0
    b = 3.0
    omega_sq = 2.0
    kappa_sq = 3.0
    beta2 = (b / r) ** 2
    expected = beta2 * kappa_sq + (1.0 - 4.0 * beta2) * omega_sq
    assert transverse_phase_gradient(r, b, omega_sq) == pytest.approx(
        b * omega_sq
    )
    assert transverse_phase_curvature(r, b, omega_sq, kappa_sq) == pytest.approx(
        expected
    )


def test_axis_curvature_equals_tangential_eigenvalue():
    assert transverse_phase_curvature(3.0, 0.0, 1.7, 9.0) == pytest.approx(1.7)


def test_epicyclic_consistency_residual():
    r = 2.0
    omega_sq = 0.7
    derivative = -0.2
    predicted = epicyclic_sq(r, omega_sq, derivative)
    assert central_consistency_residual(
        r, omega_sq, derivative, predicted
    ) == pytest.approx(0.0)


@pytest.mark.parametrize(
    "call",
    [
        lambda: radial_scalar_gradient(0.0, 1.0),
        lambda: transverse_phase_gradient(1.0, 2.0, 1.0),
        lambda: transverse_phase_curvature(1.0, -2.0, 1.0, 1.0),
    ],
)
def test_fail_closed(call):
    with pytest.raises(OrbitCurvatureError):
        call()
