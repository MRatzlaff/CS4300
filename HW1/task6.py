# task 6
import pytest

#count number of words in file

def count_words(file_name):
    f = open(file_name, "r")
    file = f.read()
    num_of_words = file.split()
    return len(num_of_words)
