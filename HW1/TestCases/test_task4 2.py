import context
import task4
import pytest

# add several test cases and test with ints and floats
@pytest.mark.parametrize("price_input,discount_input,expected", 
    [(3, .5, 1.5), (10.50, .75, 7.875), (5.50, 2, 11), (0, .5, 0)])

#perform tests with inputs
def test_calculatediscount(price_input, discount_input, expected):
    assert task4.calculate_discount(price_input, discount_input) == expected
