import context
import task5

# test that the first 3 books are printed
def test_slicebooks():
    assert task5.slice_books() == ["The Lacuna by Barbara Kingsolver", 
    "My Name is Asher Lev by Chaim Potok", "Ninth Street Women by Mary Gabriel"]


# test that student database variable is a dictionary 
# (I wasn't sure how else to test this)
def test_dictionary():
    assert type(task5.student_database) == dict
