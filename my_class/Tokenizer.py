#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import nltk
from modules import csv_io
from nltk.stem import PorterStemmer

class Tokenizer:

    def __init__(self):
        self.relative_path = os.path.join("my_class/")
        self.stopword_list = csv_io.read_csv(self.relative_path + 'stopword.csv') + [u',']
        self.stemmer = PorterStemmer()

    def is_stop_word(self, word):
        if word.lower() in self.stopword_list:
            return True
        else:
            return False

    def stemming(self, token):
        return self.stemmer.stem(token)

    def to_tokens(self, sentence):
        return nltk.word_tokenize(sentence)

    def is_zh (self,c):
        c_unicode = ord (c)

        # unicode range
        zh_range = [[0x2e80, 0x33ff], [0xff00, 0xffef], [0x4e00, 0x9fbb], \
                    [0xf900, 0xfad9], [0x20000, 0x2a6d6], [0x2f800, 0x2fa1d]]
        for lower, upper in zh_range:
            if c_unicode >= lower and c_unicode <= upper:
                return True
        return False


