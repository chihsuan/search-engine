#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import os
import nltk

class Document():
    
    def __init__(self, doc_id, doc_name):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.terms = {}
        self.doc_content = self.read_doc()

    def read_doc(self):
        with open(self.doc_name, 'r') as f:
            return f.readlines()

    def to_one_line(self):
        for line in self.doc_content: 
            pass

    def tokenizes(self, line):
        tokens = nltk.word_tokenize(line.decode('utf-8'))
        for token in tokens:
            if token in terms:
                self.terms[token] += 1
            else:
                self.terms[token] = 1 
