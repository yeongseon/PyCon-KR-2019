"""
Test the add, subtract, multiply, divide

$ cd 02-Project-Structure
$ python -m pytest
"""
from src.calculator import add, subtract, multiply, divide


def test_add():
    """Test functionality of add."""
    assert add(1, 2) == 3
    assert add(2, 2) == 4


def test_subtract():
    """Test functionality of subtract."""
    assert subtract(5, 1) == 4
    assert subtract(3, 2) == 1


def test_multiply():
    """Test functionality of multiply."""
    assert multiply(2, 2) == 4
    assert multiply(5, 6) == 30


def test_divide():
    """Test functionality of divide."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
