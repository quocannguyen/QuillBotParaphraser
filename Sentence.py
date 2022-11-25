class Sentence:
    def __init__(self, text, index):
        self.text = text
        self.index = index

    def length(self):
        return self.text.count(" ") + self.text.count("\n") + 1

    def __str__(self):
        return (self.text, self.index).__str__()
