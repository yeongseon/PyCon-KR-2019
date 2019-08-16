"""
pytest-mock

$ cd 05-Mock
# python -m pytest
"""
import pytest


def test_add_with_mocker1(mocker, calculator):
    """Test functionality of add."""
    mocker.patch.object(calculator, 'add', return_value=5)
    assert calculator.add(1, 2) is 5
    assert calculator.add(2, 2) is 5


def test_add_with_mocker2(mocker, calculator):
    """Test functionality of add."""
    mocker.patch.object(calculator, 'add', side_effect=[1, 2])
    assert calculator.add(1, 2) is 1
    assert calculator.add(2, 2) is 2


def test_add_with_mocker3(mocker, calculator):
    """Test functionality of add."""
    mocker.patch.object(calculator, 'add', side_effect=ZeroDivisionError())
    with pytest.raises(ZeroDivisionError):
        calculator.add(1, 2)
