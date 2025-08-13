#User story:

"As a user so that I can improve my grammar, I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark."

#Function signature:

# def verify_grammar():
#     parameter: string containing text
#     return: True or False if the text starts with a capital letter and ends with a suitable punctuation mark.

#Create examples as text:

from lib.verify_grammar import *
import pytest

#Test if string is empty then an error is raised.
def test_empty_string():
    with pytest.raises(Exception) as err:
        verify_grammar("")
    message = str(err.value)
    assert message == "There is no text!"


#Test if string has a starting capital letter but no suitable punctuation mark at end. Should return False.

def test_starting_capital_letter_only():
    result = verify_grammar("Hello, this sentence does not have a suitable ending")
    assert result == False

#Test if string has a suitable punctuation mark at end but not a starting capital letter. Should return False.

def test_ending_punct_only():
    result = verify_grammar("hello, this sentence does not have a starting capital letter.")
    assert result == False

#Test if string has both starting capital letter and suitable punctuation mark at end. Should return True.

def test_perfect_sentence():
    result = verify_grammar("Hello, this sentence has a tarting capital letter and suitable punctuation at the end...")
    assert result == True