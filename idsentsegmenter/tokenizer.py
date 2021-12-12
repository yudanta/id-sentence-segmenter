#!/usr/bin/env python

import sys
from os import path

import string

app_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(app_path)

from idsentsegmenter.utils.tokens import END_OF_SENTENCE_CHARS_TOKEN
from idsentsegmenter.utils.tokens import PUNCTUATION_CHARS_TOKEN
from idsentsegmenter.utils.tokens import NOT_END_OF_SENTENCE
from idsentsegmenter.utils.tokens import ALPHANUMERIC_CHARS
from idsentsegmenter.utils.tokens import NUMERIC_CHARS

from idsentsegmenter.utils.char_analyzer import CharAnalyzer, GuessTokens

ABBREVIATIONS_PATH = path.join(app_path, "idsentsegmenter/res/wordlists/abbreviations.txt")
TLD_PATH = path.join(app_path, "idsentsegmenter/res/wordlists/tld.txt")


class Tokenizer:
    def __init__(self, sentence=""):
        self.sentence = sentence
        self.words = self.sentence.split()

        self.tokens = []
        self.abbreviations_dict = []
        self.tld_dict = []

        with open(ABBREVIATIONS_PATH, "r") as f:
            abr_word = f.read().splitlines(True)
            for abbr in abr_word:
                self.abbreviations_dict.append(abbr.rstrip("\n"))

        with open(TLD_PATH, "r") as f:
            tld_word = f.read().splitlines(True)
            for tld in tld_word:
                self.tld_dict.append(tld.strip())

        pass

    def get_tokens(self):
        self.parseToken()
        return self.tokens

    def parseToken(self):
        for x in range(0, len(self.words)):
            if (
                "." in self.words[x]
                and self.words[x][-1] not in END_OF_SENTENCE_CHARS_TOKEN
            ):
                splitItem = self.words[x].split(".")
                if len(splitItem) != 2:
                    endlist = splitItem[-1]
                    startlist = ".".join(splitItem[:-1])

                    splitItem = [startlist, endlist]

                # test tld
                str_item_1 = splitItem[1].translate(
                    str.maketrans("", "", string.punctuation)
                )
                str_item_1 = "".join([".", str_item_1.lower()])

                if str_item_1 in self.tld_dict:
                    self.tokens.append(self.words[x])
                    continue

            if x == (len(self.words) - 1):
                if self.words[x][-1] in END_OF_SENTENCE_CHARS_TOKEN:
                    if GuessTokens().isWordAbbr(self.words[x][:-1].lower()):
                        self.tokens.append(self.words[x])
                    else:
                        charAnalyzer = CharAnalyzer(self.words[x][:-1]).token_words()
                        if len(charAnalyzer) > 1:
                            numeric = GuessTokens(charAnalyzer).isNumericalValue()
                            if numeric:
                                if "".join(charAnalyzer) != "":
                                    self.tokens.append("".join(charAnalyzer))
                            else:
                                abbreviation = GuessTokens(
                                    charAnalyzer
                                ).isAbbreviation()
                                if abbreviation:
                                    if "".join(charAnalyzer) != "":
                                        self.tokens.append("".join(charAnalyzer))
                                else:
                                    for i in charAnalyzer:
                                        self.tokens.append(i)

                        else:
                            if "".join(charAnalyzer) != "":
                                self.tokens.append("".join(charAnalyzer))

                        self.tokens.append(self.words[x][-1])

            else:
                charAnalyzer = CharAnalyzer(self.words[x]).token_words()
                if len(charAnalyzer) > 1:
                    numeric = GuessTokens(charAnalyzer).isNumericalValue()
                    if numeric:
                        if "".join(charAnalyzer) != "":
                            self.tokens.append("".join(charAnalyzer))
                    else:
                        abbreviation = GuessTokens(charAnalyzer).isAbbreviation()
                        if abbreviation:
                            if charAnalyzer[-1] in NOT_END_OF_SENTENCE:
                                self.tokens.append("".join(charAnalyzer[:-1]))
                                self.tokens.append("".join(charAnalyzer[-1]))
                            else:
                                self.tokens.append("".join(charAnalyzer))

                        else:
                            for i in charAnalyzer:
                                self.tokens.append(i)

                else:
                    if "".join(charAnalyzer) != "":
                        self.tokens.append("".join(charAnalyzer))


# test
# sentence = "JAKARTA, KOMPAS.com - Mitsubishi Xpander masih mendominasi penjualan PT Mitsubishi Motors Krama Yudha Sales Indonesia (MMKSI) pada Januari 2019."
# test = Tokenizer(sentence).get_tokens()

# print(test)
