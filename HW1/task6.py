# task 6

def count_words(file_name):
    f = open(file_name, "r")
    file = f.read()
    num_of_words = file.split()
    return len(num_of_words)
