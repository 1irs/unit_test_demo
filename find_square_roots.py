"""docs"""
from math import sqrt
from typing import Tuple, Optional


def find_square_roots(
    coef_a: float, coef_b: float, coef_c: float
) -> Tuple[Optional[float], Optional[float]]:
    """docs"""
    discr = coef_b * coef_b - 4 * coef_a * coef_c

    if discr < 0:
        return None, None

    x_1 = (-coef_b - sqrt(discr)) / (2 * coef_a)

    if discr == 0:
        x_2 = None
    else:
        x_2 = (-coef_b + sqrt(discr)) / (2 * coef_a)

    return x_1, x_2
