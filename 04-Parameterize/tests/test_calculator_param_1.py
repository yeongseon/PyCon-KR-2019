"""
Test the add, subtract, multiply, divide

$ cd 04-Parameterize
$ python -m pytest
"""
import pytest


# def test_add(calculator, a, b, expected):
def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 2) == 4
    assert calculator.add(9, 2) == 11


# pytest.mark marking test function
# A test can have more than one marker, and marker can be on multiple test
# pytest.mark.parametrize(argnames, argvalues): pass lots of data through the same test
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 6),
     (2, 2, 5),
     (2, 7, 2)])
def test_add_fail(calculator, a, b, expected):
    assert calculator.add(a, b) != expected


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


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 2, 4),
     (5, 6, 30),
     (9, 3, 27)])
def test_multiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 2, 0),
     (5, 6, 31),
     (9, 3, 12)])
def test_multiply_fail(calculator, a, b, expected):
    assert calculator.multiply(a, b) != expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(8, 2, 4),
     (9, 3, 3),
     (12, 6, 2)])
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(8, 2, 9),
     (9, 3, 2),
     (12, 6, 1)])
def test_divide_fail(calculator, a, b, expected):
    assert calculator.divide(8, 2) != 9
    assert calculator.divide(9, 3) != 2
    assert calculator.divide(12, 6) != 1
