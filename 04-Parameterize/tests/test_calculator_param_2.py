"""
pytest.mark.parametrize + mark.xfail/skip
"""
import pytest  # for pytest.fixture

from src.calculator import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator


@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3),
     (2, 2, 4),
     (2, 7, 9)])
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.xfail(rason="wrong result")
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 6),
     (2, 2, 5),
     (2, 7, 2),
     ])
def test_add_fail(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(5, 1, 4),
     (3, 2, 1),
     (10, 2, 8)])
def test_subtract(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(5, 1, 6),
     (3, 2, 2),
     (10, 2, 1)])
def test_subtract_fail(calculator, a, b, expected):
    assert calculator.subtract(5, 1) != 6

"""
tests/test_calculator_param_2.py::test_add_fail[1-2-6] XPASS                                                                                                                                       [ 33%]
tests/test_calculator_param_2.py::test_add_fail[2-2-5] XPASS                                                                                                                                       [ 66%]
tests/test_calculator_param_2.py::test_add_fail[2-7-2] XPASS                                                                                                                                       [100%]


tests/test_calculator_param_2.py::test_add_fail[1-2-6] XFAIL                                                                                                                                       [ 33%]
tests/test_calculator_param_2.py::test_add_fail[2-2-5] XFAIL                                                                                                                                       [ 66%]
tests/test_calculator_param_2.py::test_add_fail[2-7-2] XFAIL                                                                                                                                       [100%]

"""

@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 2, 4),
     (5, 6, 30),
     (9, 3, 27)])
def test_multiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [pytest.param(2, 2, 0, marks=pytest.mark.xfail),
     pytest.param(5, 6, 31, marks=pytest.mark.xfail(reason="wrong result")),
     (9, 3, 12)])
def test_multiply_fail(calculator, a, b, expected):
    assert calculator.multiply(a, b) != expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(8, 2, 4),
     (9, 3, 3),
     (12, 6, 2),
     pytest.param(8, 2, 9, marks=pytest.mark.xfail),
     pytest.param(9, 3, 2, marks=pytest.mark.xfail),
     pytest.param(12, 6, 12, marks=pytest.mark.xfail)
     ])
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected


@pytest.mark.skip(reason="need to support")
def test_divide_by_zero(calculator):
    assert calculator.divide(10, 0)
