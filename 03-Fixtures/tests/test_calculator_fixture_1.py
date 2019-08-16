"""
Test the add, subtract, multiply, divide

$ cd 03-Fixtures
$ python -m pytest
"""
from src.calculator import Calculator


def test_add():
    calculator = Calculator()
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 2) == 4


def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 1) == 4
    assert calculator.subtract(3, 2) == 1


def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(2, 2) == 4
    assert calculator.multiply(5, 6) == 30


def test_divide():
    calculator = Calculator()
    assert calculator.divide(8, 2) == 4
    assert calculator.divide(9, 3) == 3
