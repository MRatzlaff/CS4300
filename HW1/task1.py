def hello_world():
    print("Hello, World!")


def test_task1(capfd):
    hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"
