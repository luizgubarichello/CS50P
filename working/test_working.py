from working import convert
import random
import pytest


def test_valid():
    for _ in range(100):
        inicial_hour = random.randint(0,11)
        inicial_minute = random.randint(0,59)
        final_hour = random.randint(1,11)
        final_minute = random.randint(0,59)
        assert convert(f"{inicial_hour:02}:{inicial_minute:02} AM to {final_hour:02}:{final_minute:02} PM") == f"{inicial_hour:02}:{inicial_minute:02} to {12+final_hour:02}:{final_minute:02}"
        assert convert(f"{inicial_hour:02}:{inicial_minute:02} PM to {final_hour:02}:{final_minute:02} AM") == f"{12+inicial_hour:02}:{inicial_minute:02} to {final_hour:02}:{final_minute:02}"


def test_invalid():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("13 AM to 9 PM")


def test_special():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 PM to 12:10 AM") == "12:30 to 00:10"