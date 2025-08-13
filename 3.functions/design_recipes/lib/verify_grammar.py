def verify_grammar(text):
    if text == "":
        raise Exception("There is no text!")
    else:
        return text[-1] in '.!?...' and text[0].isupper()
