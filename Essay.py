import re
from Sentence import Sentence


class Essay:
    def __init__(self, filename):
        file = open(filename, "r", encoding="utf8")
        self.text = file.read()
        # sentences = file.read().split(". ")
        text = re.split("\. ", self.text)

        self.sentences = []
        for i in range(len(text)):
            # if len(text[i]) > 0:
            self.sentences.append(Sentence(text[i], i))

    def sort_by_length(self, increasing=True):
        self.sentences.sort(key=lambda sentence: sentence.length(), reverse=not increasing)

    def sort_by_index(self, increasing=True):
        self.sentences.sort(key=lambda sentence: sentence.index, reverse=not increasing)

    def get_next_sentences_under_limit(self, starting_index, word_limit):
        result = []
        word_count = 0
        index = starting_index
        while word_count + self.sentences[index].length() < word_limit:
            result.append(self.sentences[index])
            word_count += self.sentences[index].length()
            index += 1
            if index == len(self.sentences):
                break
        return result, index
