#!/usr/bin/env python

import string

END_OF_SENTENCE_CHARS_TOKEN = [".", "?", "!"]

# punctuations
PUNCTUATION_CHARS_TOKEN = [c for c in string.punctuation]

SHOULD_SPLIT_PUNCTUATION_CHARS = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "'",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]

TWITTER_SHOULD_SPLIT_PUNCTUATION_CHARS = [
    "!",
    '"',
    "$",
    "%",
    "&",
    "'",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "[",
    "'",
    "\\",
    "]",
    "^",
    "`",
    "{",
    "|",
    "}",
    "~",
]

NOT_END_OF_SENTENCE = ['"', "'", ")", ";"]

ALPHANUMERIC_CHARS = "abcdefghijklmnopqrstuvwxyz1234567890"
NUMERIC_CHARS = "1234567890"
