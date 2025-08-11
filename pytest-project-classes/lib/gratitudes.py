# File: lib/gratitudes.py

class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted

gratitudes = Gratitudes()
gratitudes.format()

#Test that a list is initialised.
#Test that a gratitude is added.
#Test that mulitple gratitudes are added.