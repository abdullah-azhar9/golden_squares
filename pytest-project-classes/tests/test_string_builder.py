from lib.string_builder import *

def test_for_correct_length():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5

def test_for_correct_output():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(", World")
    assert string_builder.output() == "Hello, World"

#Add tests for initial empty string, for adding single string, multiple strings and total size when multiple strings added.