from project import (
    has_uppercase,
    has_lowercase,
    has_digit,
    has_special_char,
    evaluate_password
)

def test_has_uppercase():
    assert has_uppercase("Hello") is True
    assert has_uppercase("hello") is False


def test_has_lowercase():
    assert has_lowercase("HELLOa") is True
    assert has_lowercase("HELLO") is False


def test_has_digit():
    assert has_digit("abc1") is True
    assert has_digit("abc") is False


def test_has_special_char():
    assert has_special_char("abc@") is True
    assert has_special_char("abc") is False


def test_evaluate_password():
    assert evaluate_password("password") == "Very Weak"
    assert evaluate_password("Abc123") == "Medium"
    assert evaluate_password("Abc123@#") == "Strong"
