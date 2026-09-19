from __future__ import annotations

from fractions import Fraction

E_IM = Fraction(2, 7)
E_IAMU = Fraction(2, 9)
E_IATAU = Fraction(1, 7)
E_MAMU = Fraction(2, 49)
E_MATAU = Fraction(20, 49)
E_AMUATAU = Fraction(18, 49)


def historical_triangle_defect() -> Fraction:
    return E_AMUATAU - E_IAMU - E_IATAU


def historical_gram_matrix() -> tuple[tuple[Fraction, ...], ...]:
    def dot(a: Fraction, b: Fraction, distance: Fraction) -> Fraction:
        return (a * a + b * b - distance * distance) / 2

    g12 = dot(E_IM, E_IAMU, E_MAMU)
    g13 = dot(E_IM, E_IATAU, E_MATAU)
    g23 = dot(E_IAMU, E_IATAU, E_AMUATAU)
    return (
        (E_IM * E_IM, g12, g13),
        (g12, E_IAMU * E_IAMU, g23),
        (g13, g23, E_IATAU * E_IATAU),
    )


def determinant3(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("matrix must be 3x3")
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def historical_gram_determinant() -> Fraction:
    return determinant3(historical_gram_matrix())


def historical_euclidean_geometry_passes() -> bool:
    return historical_triangle_defect() <= 0 and historical_gram_determinant() >= 0
