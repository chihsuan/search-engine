#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import os

class Document():
    
    def __init__(self, doc_id, doc_name, data_foldr):
        self.doc_id = doc_id
        self.data_foldr = data_foldr
        self.doc_name = doc_name
        self.terms = {}
        self.doc_lines = self.read_doc()


    def read(self):
        with open(self.data_foldr+self.doc_name, 'r') as f:
            self.content = f.read()
            return self.content

    def read_doc(self):
        with open(self.data_foldr+self.doc_name, 'r') as f:
            return f.readlines()

    def iter_line(self):
        for line in self.doc_lines:
            yield line
    
    def get_lines(self):
        return list(self.iter_line())

    def to_one_line(self):
        self.one_line = u''
        lines = self.get_lines()
        for line in lines:
            # append to one line and remove \n, ^M
            self.one_line += line.decode('utf-8').replace('\n','').replace(str(chr(13)), '')
        self.doc_lines = []
        #print self.one_line.encode('utf-8')

    def tokenizes(self, line):
        tokens = nltk.word_tokenize(line.decode('utf-8'))
        for token in tokens:
            if token in terms:
                self.terms[token] += 1
            else:
                self.terms[token] = 1 
    
    def output_one_line(self, output_foldr):
        with open(output_foldr+self.doc_name, 'w') as f:
            f.write(self.one_line.encode('utf-8'))
