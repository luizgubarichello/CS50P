from twttr import shorten


def test_shorten():
    assert shorten("abc") == "bc"
    assert shorten("AVc") == "Vc"
    assert shorten("abc10") == "bc10"
    assert shorten(".abc") == ".bc"
