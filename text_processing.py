#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from my_class.Document import Document
from my_class.Tokenizer import Tokenizer
from doc_preprocessing import get_docs_list
from my_class.DataDB import DataDB
from modules import json_io
from modules import csv_io

if __name__=='__main__':
    if len(sys.argv) >= 1: 
        doc_input = sys.argv[1]
    else:
        doc_input = 'output/en_doc/'
   
    document_list = get_docs_list(doc_input)
    tokenizer = Tokenizer()
    doc_id = 0
    for doc in document_list:
        doc_obj = Document(doc_id, doc, doc_input)
        # tokenize
        normalize_tokens = []
        for line in doc_obj.get_lines():
            tokens = tokenizer.to_tokens(line.decode('utf-8'))
            for token in tokens:
                if tokenizer.is_stop_word(token) or token.isdigit():
                    token = ""
                else:
                    token = tokenizer.stemming(token)
                    normalize_tokens.append(token.encode('utf-8'))
        csv_io.write_csv('output/tokens/' + doc, [normalize_tokens])
        del doc_obj
        doc_id += 1
