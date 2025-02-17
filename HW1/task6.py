# task 6
import pytest

#count number of words in file

def count_words(file_name):
    f = open(file_name, "r")
    file = f.read()
    num_of_words = file.split() # splits file into individual words in a list
    return len(num_of_words) # count length of list of words
