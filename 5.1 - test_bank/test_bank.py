from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello, jude") == 0
    assert value("HELLO world") == 0



def test_h():
    assert value("Hi frank") == 20
    assert value("hipopotamus frank") == 20


def test_other():
    assert value("arriba") == 100
    