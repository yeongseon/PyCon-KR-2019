"""
mocker.spy
"""
import pytest

from src.calculator_1 import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator


add_test_data = [
    (1, 2, 3),
    (2, 2, 4),
    (2, 7, 9),
    pytest.param(1, 2, 6, marks=pytest.mark.xfail),
    pytest.param(2, 2, 5, marks=pytest.mark.xfail),
    pytest.param(2, 7, 2, marks=pytest.mark.xfail)
]


@pytest.mark.parametrize(
    "a, b, expected", add_test_data
)
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", add_test_data
)
def test_add_spy_logger(mocker, calculator, a, b, expected):
    spy_info = mocker.spy(calculator.logger, "info")
    assert calculator.add(a, b) == expected
    assert spy_info.called
    assert spy_info.call_count == 1

    calls = [mocker.call("add {a} to {b} is {expected}".format(
        a=a, b=b, expected=expected
    ))]
    assert spy_info.call_args_list == calls


@pytest.mark.parametrize(
    "a, b, expected", add_test_data
)
def test_add_spy_add(mocker, calculator, a, b, expected):
    spy_add = mocker.spy(calculator, "add")

    assert calculator.add(a, b) == expected
    assert spy_add.called
    assert spy_add.call_count == 1

    calls = [mocker.call(a, b)]
    assert spy_add.call_args_list == calls

