from um import count


def test_one():
    assert count("uM") == 1
    assert count("hello, um, world") == 1
    assert count("hello, um, paulum") == 1


def test_two():
    assert count("um um") == 2
    assert count("UM, hello, um, world") == 2
    assert count("um! hello, um, paulum") == 2


def test_three():
    assert count("um brain um meltiung um") == 3
    assert count("um, hello, um, world, um....") == 3
    assert count("um! hello, UM, paulum, lorem ipson, um") == 3