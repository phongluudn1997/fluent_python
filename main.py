import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):
    """docstring for SentenceIterator"""

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


sentence = Sentence(
    '"Hello World!", the stronggest man around the World said.')

print(sentence.__iter__().__next__())
