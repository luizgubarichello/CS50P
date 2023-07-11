from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"