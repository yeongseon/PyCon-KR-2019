"""
Test the add, multiply

$ cd 01-Getting-Started
$ pytest
"""
import pytest
from calculator import add, divide


def test_add():
    """Test functionality of add."""
    # assert a == b
    assert add(1, 2) == 3
    assert not add(2, 2) == 3


def test_divide():
    """Test functionality of divide."""
    # pytest.raises(<expected exception>)
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
