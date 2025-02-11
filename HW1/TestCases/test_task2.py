import context
import task2

# test task2.py
def test_int():
    tester = task2.int_()
    assert isinstance(tester, int)

def test_float():
    tester = task2.float_()
    assert isinstance(tester, float)

def test_string():
    tester = task2.string_()
    assert isinstance(tester, str)

def test_bool_true():
    tester = task2.bool_true()
    assert isinstance(tester, bool)

def test_bool_false():
    tester = task2.bool_false()
    assert isinstance(tester, bool)