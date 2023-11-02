import pytest
import source.my_functions as my_functions


def test_add():
    pass


def test_add_2():
    result = my_functions.add_numbers(1, 4)
    assert result == 5


def test_add_3():
    result = my_functions.add_numbers(2, 8)
    assert result == 10


def test_devide():
    result = my_functions.devide_numbers(8, 4)
    assert result == 2


def test_devide_2():
    with pytest.raises(ZeroDivisionError):
        my_functions.devide_numbers(10, 0)

