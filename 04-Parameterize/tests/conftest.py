"""
sharing fixtures through conftest.py
"""
import pytest

from src.calculator import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator
