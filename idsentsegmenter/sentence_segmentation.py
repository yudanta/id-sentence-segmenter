#!/usr/bin/env python
import sys
from os import path

# app_path = path.dirname( path.dirname( path.abspath(__file__) ) )
# sys.path.append( app_path )

import re
import string

from idsentsegmenter.utils.string_utils import StringUtils

ABBREVIATIONS_PATH = "idsentsegmenter/res/wordlists/abbreviations.txt"
TLD_PATH = "idsentsegmenter/res/wordlists/tld.txt"

FIRST_CHAR_TOKEN = ['"']
END_CHARS_TOKEN = [".", "?", "!"]
POTENTIAL_END_QUOTE = [","]
QUOTE_TRANSLATION = ["\u201d", "\u201c"]


class SentenceSegmentation:
    def __init__(self):

        self.abbreviations_dict = []
        f = open(ABBREVIATIONS_PATH, "r")
        abr_word = f.read().splitlines(True)
        for abbr in abr_word:
            self.abbreviations_dict.append(abbr.rstrip("\n"))

        f.close()

        self.tld_dict = []
        f = open(TLD_PATH, "r")
        tld_word = f.read().splitlines(True)
        for tld in tld_word:
            self.tld_dict.append(tld.rstrip("\n"))

        f.close()

        self.wordLists = []
        self.processedWordLists = []
        self.sentenceLists = []

        self.stringUtils = StringUtils()

    def get_sentences(self, document=""):
        # remove \n\t
        document = re.sub("\s+", " ", document.strip())

        # replace quotes
        document = document.replace(QUOTE_TRANSLATION[0], '"')
        document = document.replace(QUOTE_TRANSLATION[1], '"')

        self.strings = document

        self.wordLists = []
        self.processedWordLists = []
        self.sentenceLists = []

        self.wordLists = self.stringUtils.splitStringBySpaces(self.strings)

        self.findEndOfSentence()
        return self.sentenceLists

    # def get_sentences(self):
    #     self.findEndOfSentence()
    #     return self.sentenceLists

    def findEndOfSentence(self):
        quoteWord = False
        firstQuote = False
        quoteStop = True
        firstWordIndex = 0
        lastWordIndex = 0

        lenWords = len(self.wordLists)

        for x in range(0, len(self.wordLists)):
            # print(self.wordLists[x])
            if "." in self.wordLists[x] and self.wordLists[x][-1] != ".":
                splitItem = self.wordLists[x].split(".")

                # merge
                if len(splitItem) != 2:
                    endlist = splitItem[-1]
                    startlist = ".".join(splitItem[:-1])

                    splitItem = [startlist, endlist]

                # print(splitItem)

                # test tld
                str_item_1 = splitItem[1].translate(
                    str.maketrans("", "", string.punctuation)
                )
                str_item_1 = "".join([".", str_item_1.lower()])

                if str_item_1 not in self.tld_dict:
                    # if abbreviations
                    if (splitItem[0].lower() not in self.abbreviations_dict) and (
                        splitItem[1][0].isupper() or splitItem[1][0] in ['"']
                    ):
                        split_str = ["".join([splitItem[0], "."]), splitItem[1]]
                        self.processedWordLists.append(split_str[0].strip())
                        self.processedWordLists.append(split_str[1].strip())

                # in a tld domain
                else:
                    split_str = "".join([splitItem[0], ".", splitItem[1]])
                    self.processedWordLists.append(split_str.strip())

            else:
                self.processedWordLists.append(self.wordLists[x].strip())

        #         print(self.processedWordLists)

        lenWords = len(self.processedWordLists)
        for i in range(0, lenWords):
            #             print(self.processedWordLists[i])
            # check first char of words, if first char is ('"') then find close quote, it might before ('.') char
            firstChar = self.processedWordLists[i][0]

            if not quoteWord and firstChar in FIRST_CHAR_TOKEN:
                if self.processedWordLists[i].count('"') > 1:
                    # just single quote
                    quoteWord = False
                    firstQuote = False
                    quoteStop = False

                else:
                    quoteWord = True
                    firstQuote = True
                    quoteStop = False
                    pass

            if firstQuote and quoteWord:
                quoteWord = True
                firstQuote = False
                quoteStop = False
                pass

            # find anoother close '"'
            if not firstQuote and quoteWord:
                if '"' in self.processedWordLists[i]:
                    if self.processedWordLists[i][-1] in END_CHARS_TOKEN:
                        lastWordIndex = i + 1
                        # print('terminate on token: ', self.processedWordLists[lastWordIndex])
                        sentence = " ".join(
                            self.processedWordLists[firstWordIndex:lastWordIndex]
                        )
                        self.sentenceLists.append(sentence)

                        firstWordIndex = lastWordIndex

                        # set false
                        quoteWord = False
                        firstQuote = False
                        quoteStop = True
                        pass

                    elif (
                        self.processedWordLists[i][-1] == '"'
                        or self.processedWordLists[i][-1] in POTENTIAL_END_QUOTE
                    ):
                        quoteWord = False
                        firstQuote = False
                        quoteStop = True
                        pass

                else:
                    pass

            if not quoteWord and not firstQuote:
                if i == (lenWords - 1):
                    lastWordIndex = i + 1
                    sentence = " ".join(
                        self.processedWordLists[firstWordIndex:lastWordIndex]
                    )
                    self.sentenceLists.append(sentence)
                    break

                else:
                    if self.checkIsEndOfSentence(self.processedWordLists[i]):
                        lastWordIndex = i + 1

                        sentence = " ".join(
                            self.processedWordLists[firstWordIndex:lastWordIndex]
                        )
                        self.sentenceLists.append(sentence)

                        firstWordIndex = lastWordIndex

                    else:
                        pass

    def checkIsEndOfSentence(self, word):
        endChar = word[-1]

        if endChar in END_CHARS_TOKEN:
            # print(word[:-1])
            if word[:-1].lower() not in self.abbreviations_dict:
                if word[:-1].isdigit():
                    if len(word[:-1]) > 2:
                        return True
                    else:
                        return False

                # short name such as J. Jr. L. K. etc
                else:
                    if len(word[:-1]) > 2:
                        return True
                    else:
                        return False

        else:
            return False


# test
# test_str = """
# Pada kompetisi ini tersedia hadiah utama berupa 1 unit Vivo V15, hadiah kedua 7 unit Headphone, dan hadiah ketiga berupa 7 unit Backpack eksklusif Vivo.Aktivitas digital selanjutnya adalah Go Guess, Go Up! yang telah berjalan di akun media sosial dari JD.ID, Akulaku, Shopee, Tokopedia, Lazada, dan Blibli.com.
# """
# print('raw text: ')
# print(test_str)
# print('-' * 64)
# print('sentences: ')
# test = SentenceSegmentation(test_str).get_sentences()
# for i in range(0, len(test)):
#     print('{} - {}'.format(i + 1, test[i]))
