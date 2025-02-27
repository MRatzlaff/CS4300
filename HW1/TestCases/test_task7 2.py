#test task 7
import context
import task7
import pytest

#test add
@pytest.mark.parametrize("n1,n2,expected", 
    [(1, 3, 4), (7, 3, 10), (0, 0, 0), (100, 1, 101), (-5.4, -3, -8.4)]) # pass various numbers to function
def test_addwithnumpy(n1, n2, expected):
    result = task7.add_with_numpy(n1, n2)
    assert result == expected


#test subtract
@pytest.mark.parametrize("n1,n2,expected", 
    [(1, 3, -2), (7, 3, 4), (0, 0, 0), (100, 1, 99), (-5, -3, -2)]) # pass various numbers to function
def test_subwithnumpy(n1, n2, expected):
    result = task7.sub_with_numpy(n1, n2)
    assert result == expected


#test multiply
@pytest.mark.parametrize("n1,n2,expected", 
    [(1, 3, 3), (7, 3, 21), (0, 0, 0), (100, 1, 100), (-5, -3, 15)]) # pass various numbers to function
def test_multwithnumpy(n1, n2, expected):
    result = task7.mult_with_numpy(n1, n2)
    assert result == expected