def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    #sorted does not work here as intended, currently it sorts the dict by ascending values, then accesses the value of the first item, also includes space characters
    #adding reverse = True sorts the dict by descending values, then switching to [1][0] will access the key of the first item where key is the letter
    #print(letter) letter = 1
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")



