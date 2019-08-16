"""
Test the add, subtract, multiply, divide

$ cd 04-Parameterize
$ python -m pytest

ids: optional parameter to parametrize() to make our own identifiers
"""
import pytest

add_test_data = [
    (1, 2, 3),
    (2, 2, 4),
    (2, 7, 9),
    pytest.param(1, 2, 6, marks=pytest.mark.xfail),
    pytest.param(2, 2, 5, marks=pytest.mark.xfail),
    pytest.param(2, 7, 2, marks=pytest.mark.xfail)
]


@pytest.mark.parametrize(
    "a, b, expected", add_test_data,
    ids=[
        "1 add 2 is 3",
        "2 add 2 is 4",
        "2 add 7 is 9",
        "1 add 2 is not 6",
        "2 add 2 is not 5",
        "2 add 7 is not 2"
    ]
)
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


subtract_test_data = [
    pytest.param(5, 1, 4, id="5 subtract 1 is 4"),
    pytest.param(3, 2, 1, id="3 subtract 2 is 1"),
    pytest.param(10, 2, 8, id="10 subtract 2 is 8"),
    pytest.param(5, 1, 6, marks=pytest.mark.xfail, id="5 subtract 1 is 6"),
    pytest.param(3, 2, 2, marks=pytest.mark.xfail, id="3 subtract 2 is 2"),
    pytest.param(10, 2, 1, marks=pytest.mark.xfail, id="10 subtract 2 is 1")
]


@pytest.mark.parametrize(
    "a, b, expected", subtract_test_data
)
def test_subtract(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected


multiply_test_data = [
    (2, 2, 4),
    (5, 6, 30),
    (9, 3, 27),
    pytest.param(2, 2, 0, marks=pytest.mark.xfail),
    pytest.param(5, 6, 31, marks=pytest.mark.xfail),
    pytest.param(9, 3, 12, marks=pytest.mark.xfail)
]


@pytest.mark.parametrize(
    "a, b, expected", multiply_test_data,
    ids=[
        "2 times 2 is 4",
        "5 times 5 is 30",
        "9 times 3 is 27",
        "2 times 2 is not 0",
        "5 times 5 is not 31",
        "9 times 3 is not 12"
    ])
def test_multiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected


divided_test_data = [
    pytest.param(8, 2, 4, id="8 divided by 2 is 4"),
    pytest.param(9, 3, 3, id="9 divided by 3 is 3"),
    pytest.param(12, 6, 2, id="12 divided by 6 is 2"),
    pytest.param(8, 2, 9, marks=pytest.mark.xfail, id="8 divided by 2 is not 9"),
    pytest.param(9, 3, 2, marks=pytest.mark.xfail, id="9 divided by 3 is not 2"),
    pytest.param(12, 6, 12, marks=pytest.mark.xfail, id="12 divided by 6 is not 12")
]


@pytest.mark.parametrize(
    "a, b, expected", divided_test_data
)
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected
