from lib.make_snippet import *

#test that an empty string is returned if string is empty

def test_mempty_string_returned():
    result = make_snippet("")
    assert result == ""

#if string is 4 words, it returns the string of 4 words

def test_string_less_than_5_words():
    result = make_snippet("one two three four")
    assert result == "one two three four"

#if string is 5 words, it returns the string of 5 words

def test_string_is_5_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

#if string is 5 words, it returns string of 5 words and ...

def test_string_more_than_5_words():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

#if string is delimited by commas, it returns same string

def test_delimited_by_commas():
    result = make_snippet("one,two,three,four,five,six")
    assert result == make_snippet("one two three four five...")