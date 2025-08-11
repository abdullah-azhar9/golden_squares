from lib.password_checker import *
import pytest

def test_for_greater_than_8_chars():
    password_checker = PasswordChecker()
    result = password_checker.check("abcdefghi")
    assert result == True

def test_for_less_than_8_chars():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        password_checker.check("abcdef")
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."


