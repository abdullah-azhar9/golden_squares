from lib.present import *
import pytest

def test_when_unwrapping():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."


def test_when_wrapping_first_item():
    present = Present()
    present.wrap("Toy")
    result = present.unwrap()
    assert result == "Toy"

def test_when_wrapping_second_item():
    present = Present()
    present.wrap("Toy")
    with pytest.raises(Exception) as err:
        present.wrap("Snack")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."