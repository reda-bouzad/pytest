import pytest
import source.my_functions as my_functions


def test_add():
    pass


def test_add_2():
    result = my_functions.add_numbers(1, 4)
    assert result == 5


def test_add_3():
    result = my_functions.add_numbers(2, 8)
    assert result == 5
