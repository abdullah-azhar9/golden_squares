# def make_snippet(string):
#     string_list = string.split()
#     first_five_words = string_list[0:5]
#     if len(string_list) <=5:
#         return " ".join(first_five_words)
#     else:
#         return " ".join(first_five_words) + "..."


def make_snippet(string):
    if "," in string:
        words = string.split(",")
    else:
        words = string.split(" ")
    if len(words) > 5:
        first_five = words[0:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    else:
        return string