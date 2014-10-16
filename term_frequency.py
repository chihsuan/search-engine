#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import os
import math

from modules import csv_io
from modules import json_io
from doc_preprocessing import get_docs_list

def tf(terms, output_path):
    term_tf = {}
    for term in terms:
        if term not in term_tf:
            term_tf[term] = 1.0
        else:
            term_tf[term] += 1.0

    length = len(terms)
    for term, count in term_tf.iteritems():
        count = count / length
    
    json_io.write_json(output_path+doc+'.json', term_tf)

if __name__=='__main__':
    doc_hash = csv_io.read_csv('output/doc_hash.json')
    document_list = get_docs_list('output/tokens/')

    doc_id = 0
    for doc in document_list:
        terms = csv_io.read_csv('output/tokens/'+doc)
        tf(terms, 'output/tf/')
        doc_id += 1
