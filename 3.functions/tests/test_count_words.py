from lib.count_words import *

#Test that an empty string returns 0 words

def test_empty_string():
    result = count_words(" ")
    assert result == 0

#Test that a string with one word returns 1.

def test_one_word_string():
    result = count_words("Hello")
    assert result == 1

#Test that a string with 5 words returns 5.

def test_five_word_string():
    result = count_words("Hello my name is Abdullah")
    assert result == 5

#Test that a text with punctuation returns the correct number of words

def test_five_word_string_with_punctuation():
    result = count_words("Hello, my name is Abdullah!")
    assert result == 5

#Test if text has commas as delimiter

def test_five_word_string_with_commas_delimiter():
    result = count_words("Hello,my,name,is,abdullah", ",")
    assert result == 5
