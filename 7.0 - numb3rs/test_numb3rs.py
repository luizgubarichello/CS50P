from numb3rs import validate
import random


def test_valid():
    for _ in range(100):
        assert validate(f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}") == True


def test_invalid():
    assert validate("cat") == False
    assert validate("279.0.2.3") == False
    assert validate("cat.dog.bird.whatever") == False
    assert validate("1.1.1.") == False
    assert validate("1.") == False
    assert validate("1") == False