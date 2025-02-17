import context
import task6
import pytest

# test number of words in file
file_names = [("task6_read_me.txt", 104), ("task6_read_me1.txt", 33), 
    ("task6_read_me2.txt", 5)]

# creates test cases based on file names
def pytest_generate_tests(metafunc):
    if 'test_file' in metafunc.fixturenames:
        metafunc.parametrize('test_file,expected_output', file_names)

#executes tests
def test_wordcount(test_file, expected_output):
    result = task6.count_words(test_file)
    assert result == expected_output