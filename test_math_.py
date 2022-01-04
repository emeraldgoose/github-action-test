import pytest
from math_ import sum_, list_sum


def test_list_sum_AssertionError():
    a = [1,2,3,4,5]
    b = [1,2,3]
    with pytest.raises(AssertionError):
        list_sum(a, b)


def test_sum_AssertionError():
    a = "1"
    b = 2
    with pytest.raises(TypeError):
        sum_(a, b)


def test_list_sum_pass():
    a = [1,2,3,4,5]
    b = [1,2,3,4,5]
    assert list_sum(a, b) == [2,4,6,8,10]


def test_sum_pass():
    a = 2
    b = 3
    assert sum_(a, b) == a + b


def test_sum_pass_2():
    a = -45
    b = 3
    assert sum_(a, b) == a + b


def test_sum_pass_2():
    a = [-1,-2,-3,-4,-5]
    b = [1,2,3,4,5]
    assert list_sum(a, b) == [0,0,0,0,0]
