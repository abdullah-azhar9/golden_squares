def estimate_reading_time(text):
    if text == "":
        raise Exception("Can't estimate a reading time for an empty text!")
    else:
        words = text.split()
        length = len([word for word in words if word.isalpha() or word.isnumeric()]) / 200
        if length > 60:
            in_hours = length/60
            if in_hours > 1:
                return f'The estimated reading time is {round(in_hours, 1)} hours.'
            else:
                return f'The estimated reading time is {round(in_hours, 1)} hour.'
        else:
            if length == 1:
                return f'The estimated reading time is {round(length, 1)} minute.'
            else:
                return f'The estimated reading time is {round(length, 1)} minutes.'