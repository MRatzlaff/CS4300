import context
import task3
import pytest

# test task3.py
# test if number is negative, positive, or 0
@pytest.mark.parametrize("test_input,expected", 
    [(3, "+"), (-10, "-"), (0, "0"), (100, "+"), (-5.4, "-")]) # pass various numbers to function

def test_whatisit(test_input, expected):
    assert task3.what_is_it(test_input) == expected
