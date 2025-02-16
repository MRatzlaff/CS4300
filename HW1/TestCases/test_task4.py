import context
import task4
import pytest

@pytest.mark.parametrize("price_input,discount_input,expected", 
    [(3, .5, 1.5), (10.50, .75, 7.875), (5.50, 2, 11), (0, .5, 0)])
    
def test_calculatediscount(price_input, discount_input, expected):
    assert task4.calculate_discount(price_input, discount_input) == expected
