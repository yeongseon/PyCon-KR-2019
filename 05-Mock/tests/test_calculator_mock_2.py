"""

"""
import pytest

from src.calculator_2 import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator


def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


def test_add_with_str(mocker, calculator):
    info_spy = mocker.spy(ValueError)
    with pytest.raises(ValueError):
        calculator.add('a', 'b')
