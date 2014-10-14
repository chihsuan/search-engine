#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import nltk

from my_class.Document import Document
from my_class.Tokenizer import Tokenizer
from doc_preprocessing import get_docs_list


def to_db():
    pass

if __name__=='__main__':
    if len(sys.argv) >= 2: 
        doc_input = sys.argv[1]
    else:
        doc_input = 'output/en_doc/'
        
    document_list = get_docs_list(doc_input)
    tokenizer = Tokenizer()
    for doc in document_list:
        doc_id = 0
        doc_obj = Document(doc_id, doc, doc_input)
        # tokenize
        for line in doc_obj.get_lines():
            tokens = tokenizer.to_tokens(line.decode('utf-8'))
            for token in tokens:
                if tokenizer.is_stop_word(token) or token.isdigit():
                    token = ""
                else:
                    token = tokenizer.stemming(token)
                    print token.encode('utf-8')
        del doc_obj
        break
        doc_id += 1
