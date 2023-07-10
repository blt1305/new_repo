from unittest import mock
from unittest.mock import call

import pytest

from logic.math_func import calculate, calculate_formula


def test_calculate_with_positive_args():
    result = calculate(a=4, b=10)
    assert result == 4.8


@pytest.mark.parametrize(
    ["a", "b", "result"], [
        (4, 10, 4.8),
        (-2, 10, 3.54),
        (0, 2, 4),
        (3, -5, 2.8),
        (-5, -10, 5.15)
    ]
)
def test_calculate(a, b, result):
    assert result == calculate(a, b)


def test_calculate_raises_exception():
    with pytest.raises(ZeroDivisionError):
        calculate(1, 0)


@pytest.mark.parametrize(
    ["a", "b", "c", "result"], [
        (4, 10, 7, 38.699999999999996),
        (-2, 10, -3, 11.166666666666666),
        (4, 2, 40, 89.3),
        (3, -5, -15, 14.733333333333334),
        (-5, -10, 27, 12.27222222222222)
    ]
)
def test_calculate_formula(a, b, c, result):
    assert result == calculate_formula(a, b, c)


@mock.patch("logic.math_func.calculate")
def test_calculate_formula_with_mock(calculate_mock):
    calculate_mock.side_effect = [1, 2, 3, 4, 5, 6]
    assert 21 == calculate_formula(a=1, b=2, c=3)
    calculate_mock.assert_has_calls(calls=[
        call(1, 2),
        call(1, 3),
        call(2, 3),
        call(2, 1),
        call(3, 1),
        call(3, 2)
    ])
