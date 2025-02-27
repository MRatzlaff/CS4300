import context
import task1

# test task1.py
def test_task1(capfd):
    task1.hello_world()
    out, err = capfd.readouterr() # capture output from console
    assert out == "Hello, World!\n"