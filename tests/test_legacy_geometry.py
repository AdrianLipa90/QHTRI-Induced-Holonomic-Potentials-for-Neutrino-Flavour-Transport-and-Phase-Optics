from fractions import Fraction

from qhtri_phase_optics.legacy_geometry import (
    historical_euclidean_geometry_passes,
    historical_gram_determinant,
    historical_triangle_defect,
)


def test_historical_operator_tetrahedron_has_exact_triangle_defect():
    assert historical_triangle_defect() == Fraction(1, 441)


def test_historical_operator_tetrahedron_gram_is_not_positive_semidefinite():
    assert historical_gram_determinant() == Fraction(-468852409, 90812685325761)
    assert historical_gram_determinant() < 0


def test_historical_operator_tetrahedron_fails_euclidean_gate():
    assert historical_euclidean_geometry_passes() is False
