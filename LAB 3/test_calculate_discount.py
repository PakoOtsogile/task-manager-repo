"""Lab 3: Dynamic analysis test design for calculate_discount."""
import pytest
from app.tasks import calculate_discount

def test_tc01_zero_price_premium():
    """TC01: price = 0, is_premium = True → 0"""
    assert calculate_discount(0, True) == 0


def test_tc02_zero_price_regular():
    """TC02: price = 0, is_premium = False → 0"""
    assert calculate_discount(0, False) == 0


def test_tc03_small_price_premium():
    """TC03: price = 0.01, is_premium = True → 0.008"""
    assert calculate_discount(0.01, True) == pytest.approx(0.008)


def test_tc04_small_price_regular():
    """TC04: price = 0.01, is_premium = False → 0.01"""
    assert calculate_discount(0.01, False) == 0.01


def test_tc05_normal_price_premium():
    """TC05: price = 100, is_premium = True → 80"""
    assert calculate_discount(100, True) == 80


def test_tc06_normal_price_regular():
    """TC06: price = 100, is_premium = False → 100"""
    assert calculate_discount(100, False) == 100


def test_tc07_large_price_premium():
    """TC07: price = 10000, is_premium = True → 8000"""
    assert calculate_discount(10000, True) == 8000


def test_tc08_large_price_regular():
    """TC08: price = 10000, is_premium = False → 10000"""
    assert calculate_discount(10000, False) == 10000

def test_tc09_negative_price_premium():
    """TC09: price = -10, is_premium = True → -8 (or error?)"""
    # The function does not validate negative prices
    # This test documents the current (potentially buggy) behaviour
    assert calculate_discount(-10, True) == -8


def test_tc10_negative_price_regular():
    """TC10: price = -10, is_premium = False → -10 (or error?)"""
    assert calculate_discount(-10, False) == -10


def test_tc11_non_numeric_price():
    """TC11: price = 'abc', is_premium = True → TypeError"""
    with pytest.raises(TypeError):
        calculate_discount("abc", True)


def test_tc12_non_boolean_premium():
    """TC12: price = 100, is_premium = 'yes' → 100 (truthy but not True)"""
    # Due to `== True` comparison, 'yes' != True, so no discount
    assert calculate_discount(100, "yes") == 100

def test_tc13_boundary_just_below_zero():
    """TC13: price = -0.01, is_premium = True → -0.008"""
    assert calculate_discount(-0.01, True) == pytest.approx(-0.008)


def test_tc14_boundary_just_above_zero():
    """TC14: price = 0.01, is_premium = True → 0.008"""
    assert calculate_discount(0.01, True) == pytest.approx(0.008)


def test_tc15_premium_is_integer_one():
    """TC15: price = 100, is_premium = 1 → 80 (1 == True in Python!)"""
    assert calculate_discount(100, 1) == 80


def test_tc16_premium_is_integer_zero():
    """TC16: price = 100, is_premium = 0 → 100 (0 == False in Python!)"""
    assert calculate_discount(100, 0) == 100