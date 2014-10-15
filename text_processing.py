#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from my_class.Document import Document
from my_class.Tokenizer import Tokenizer
from doc_preprocessing import get_docs_list
from my_class.DataDB import DataDB
from modules import json_io

    

if __name__=='__main__':
    if len(sys.argv) >= 2: 
        doc_input = sys.argv[1]
        config = json_io.read_json(sys.argv[2])[u'database']
    else:
        config = json_io.read_json('config.json')[u'database']
        doc_input = 'output/en_doc/'
    
    mydb = DataDB( config[u'dbtype'], config[u'host'], config[u'dbname'], \
            config[u'username'], config[u'password'], config[u'encoding'], "")
   
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
                    print token.encode('utf-8'),
        del doc_obj
        doc_id += 1

    mydb.close()
