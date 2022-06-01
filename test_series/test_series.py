import pytest
from series.series import fibonacci, lucas, sum_series


def test_fibonacci():
    """
    Check "series.py" file
    """
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_case_2():
    """
    Check "series.py" file fibonacci
    """
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_normal_case():
    """
    Check "series.py" file fibonacci
    """
    actual = fibonacci(9)
    expected = 34
    assert actual == expected
# *-------------------------------------Lucas* ----------------------------------------------------------------*
def test_lucas():
    """Check "series.py" file lucas"""
    actual = lucas(0)
    expected = 2
    assert actual == expected
def test_lucas_case_2():
    """Check "series.py" file lucas"""
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_normal_case():
        """ Check "series.py" file lucas"""
        actual = lucas(8)
        expected = 47
        assert actual == expected


# *-------------------------------------sum_series* ----------------------------------------------------------------*


def test_sum_series():
        """Check "series.py" file sum_series"""
        actual = sum_series(0)
        expected = 0
        assert actual == expected


def test_sum_series_case_2():
    """Check "series.py" file sum_series"""
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_normal_case():
    """ Check "series.py" file sum_series"""
    actual = sum_series(20,2,4)
    expected = 35422
    assert actual == expected



