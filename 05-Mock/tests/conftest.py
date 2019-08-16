"""
sharing fixtures through conftest.py
"""
import pytest

from src.calculator_1 import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator
