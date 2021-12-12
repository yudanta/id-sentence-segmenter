#!/usr/bin/env python

import sys
from os import path

app_path = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(app_path)

from idsentsegmenter.utils.tokens import PUNCTUATION_CHARS_TOKEN
from idsentsegmenter.utils.tokens import SHOULD_SPLIT_PUNCTUATION_CHARS
from idsentsegmenter.utils.tokens import ALPHANUMERIC_CHARS
from idsentsegmenter.utils.tokens import NUMERIC_CHARS

ABBREVIATIONS_PATH = path.join(app_path, "idsentsegmenter/res/wordlists/abbreviations.txt")
TLD_PATH = path.join(app_path, "idsentsegmenter/res/wordlists/tld.txt")

abbreviations_dict = []
tld_dict = []

with open(ABBREVIATIONS_PATH, "r") as f:
    abbr_words = f.read().splitlines(True)
    for abbr in abbr_words:
        abbreviations_dict.append(abbr.rstrip("\n"))

with open(TLD_PATH, "r") as f:
    tld_words = f.read().splitlines(True)
    for tld in tld_words:
        tld_dict.append(tld.rstrip("\n"))


class CharAnalyzer:
    def __init__(self, word):
        self.wordToTokens = []
        self.splitTrue = 0
        self.splitFalse = 0
        self.numeric = 0

        self.word = word

    def token_words(self):
        firstIndexChar = 0
        lastIndexChar = 0

        for x in range(0, len(self.word)):
            self.checkAlphaNumeric(self.word[x])
            self.checkPunctuation(self.word[x])
            self.checkNumeric(self.word[x])

            if self.splitTrue > self.splitFalse and self.numeric == 0:
                lastIndexChar = x
                if lastIndexChar == len(self.word) - 1:
                    if self.word[firstIndexChar:lastIndexChar] != "":
                        self.wordToTokens.append(
                            self.word[firstIndexChar:lastIndexChar]
                        )
                else:
                    if self.word[firstIndexChar:lastIndexChar] != "":
                        self.wordToTokens.append(
                            self.word[firstIndexChar:lastIndexChar]
                        )
                    if self.word[x] != "":
                        self.wordToTokens.append(self.word[x])

                firstIndexChar = lastIndexChar + 1

            self.resetSplit()

        if lastIndexChar != (len(self.word) - 1) and self.word not in ["", " "]:
            self.wordToTokens.append(self.word[firstIndexChar : x + 1])
        elif lastIndexChar == (len(self.word) - 1):
            self.wordToTokens.append(self.word[-1])

        return self.wordToTokens

    def resetSplit(self):
        self.splitTrue = 0
        self.splitFalse = 0
        self.numeric = 0

    def checkAlphaNumeric(self, char):
        if char not in ALPHANUMERIC_CHARS:
            self.splitTrue += 1

        else:
            self.splitFalse += 1

    def checkPunctuation(self, char):
        if char in SHOULD_SPLIT_PUNCTUATION_CHARS:
            self.splitTrue += 1

        else:
            self.splitFalse += 1

    def checkNumeric(self, char):
        if char in NUMERIC_CHARS:
            self.numeric += 1

    def checkAbbreviation(self, char):
        return None


class GuessTokens:
    def __init__(self, tokens=None):
        self.tokens = tokens

    def isNumericalValue(self):
        string = 0
        numeric = 0

        for token in self.tokens:
            for x in token:
                if x in NUMERIC_CHARS:
                    numeric += 1
                else:
                    string += 1
        if numeric > string:
            return True

        return False

    def isAbbreviation(self):
        is_abr = 0
        not_abr = 0

        # remove last punctuation and check
        for x in range(0, len(self.tokens)):
            if self.tokens[-1] in [",", "!", "?"]:
                self.tokens = self.tokens[:-1]
            else:
                break

        check_words = "".join(self.tokens[:-1]).lower()
        if check_words in abbreviations_dict:
            is_abr += 1
            return True

        else:
            for x in self.tokens:
                if x != ".":
                    if x in abbreviations_dict:
                        is_abr += 1
                    else:
                        not_abr += 1

        if is_abr > not_abr:
            return True

        return False

    def isWordAbbr(self, word):
        if word in abbreviations_dict:
            return True

        return False

    def isTldDomain(self, word):
        if word in tld_dict:
            return True

        return False
