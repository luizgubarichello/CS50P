from plates import is_valid


def test_1():
    assert is_valid("A") == False
    assert is_valid("ab") == False
    assert is_valid("abcdefg") == False
    assert is_valid("ABCDeFGhI") == False
    assert is_valid("abcde") == True


def test_2():
    assert is_valid("12ab") == False
    assert is_valid("a12b") == False
    assert is_valid("ab12") == True


def test_3():
    assert is_valid("hdu.5") == False
    assert is_valid("ab!&ui") == False
    assert is_valid("petr4") == True


def test_4():
    assert is_valid("ab01") == False
    assert is_valid("ab12a") == False
    assert is_valid("unip6") == True
