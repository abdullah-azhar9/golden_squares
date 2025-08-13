# A function called count_words that takes a string as an argument and returns the number of words in that string.

def count_words(text, delimiter = " "):
    return len([word for word in text.split(delimiter) if any(char.isalnum() for char in word)])
