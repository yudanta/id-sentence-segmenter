#!/usr/bin/env python

import sys
from os import path


class NGram:
    def __init__(self):
        pass

    def get_ngram(self, wordlist, n):
        return list(zip(*[wordlist[i:] for i in range(n)]))


# test ngram
# tokens = ['saya', 'makan', 'bakso', 'bersama', 'dia', '.']

# ngram = NGram()
# print(ngram.get_ngram(tokens, 2))
