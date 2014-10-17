#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from my_class.Document import Document
from doc_preprocessing import get_docs_list
from modules import csv_io

def n_gram(content, n):
    tokens = []
    for i in range(len(content)-n+1):
        tokens.append(content[i:i+n].encode('utf-8'))
    return tokens

if __name__=='__main__':
    if len(sys.argv) > 1: 
        doc_input = sys.argv[1]
    else:
        doc_input = 'output/zh_doc/'

    document_list = get_docs_list(doc_input)
    doc_id = 1
    for doc in document_list:
        doc_obj = Document(doc_id, doc, doc_input)
        content = doc_obj.read().decode('utf-8')
        tokens = n_gram(content, 2)
        csv_io.write_csv('output/zh_tokens/' + doc, [tokens])
        del doc_obj
        doc_id += 1

