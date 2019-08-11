"""
Test the add, subtract, multiply, divide

$ cd 03-Fixtures
$ python -m pytest
"""


def test_add(calculator):
    """Test functionality of add."""
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 2) == 4
    assert calculator.add(9, 2) == 11


def test_add_fail(calculator):
    """Test functionality of add."""
    assert calculator.add(1, 2) != 6
    assert calculator.add(2, 2) != 5
    assert calculator.add(2, 7) != 2


def test_subtract(calculator):
    """Test functionality of subtract."""
    assert calculator.subtract(5, 1) == 4
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(10, 2) == 8


def test_subtract_fail(calculator):
    """Test functionality of subtract."""
    assert calculator.subtract(5, 1) != 6
    assert calculator.subtract(3, 2) != 2
    assert calculator.subtract(13, 3) != 1


def test_multiply(calculator):
    """Test functionality of multiply."""
    assert calculator.multiply(2, 2) == 4
    assert calculator.multiply(5, 6) == 30
    assert calculator.multiply(9, 3) == 27


def test_multiply_fail(calculator):
    """Test functionality of multiply."""
    assert calculator.multiply(2, 2) != 0
    assert calculator.multiply(5, 6) != 31
    assert calculator.multiply(9, 3) != 12


def test_divide(calculator):
    """Test functionality of divide."""
    assert calculator.divide(8, 2) == 4
    assert calculator.divide(9, 3) == 3
    assert calculator.divide(12, 6) == 2


def test_divide_fail(calculator):
    """Test functionality of divide."""
    assert calculator.divide(8, 2) != 9
    assert calculator.divide(9, 3) != 2
    assert calculator.divide(12, 6) != 1
