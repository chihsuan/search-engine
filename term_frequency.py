#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import os
import math

from modules import csv_io
from modules import json_io
from doc_preprocessing import get_docs_list
from my_class.DataDB import DataDB

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

def to_db(mydb, term_id, document_list, doc_hash, input_dir):
    for doc in document_list:
        terms_tf = json_io.read_json(input_dir+doc)
        for term, tf in terms_tf.iteritems():
            term = term.replace("'", "")
            if len(term) > 255:
                term = term[:254]
            sql = "INSERT INTO doc_lookups (doc_id,title,tf,term_id) VALUES (" \
                    + "'" + str(doc_hash[doc[:-5]]) + "','" + doc[:-5]  + "','" + str(tf) + "','" + str(term_id[term]) + "');"
            mydb.exe_sql(sql)

if __name__=='__main__':
    if len(sys.argv) > 1:
        doc_hash = csv_io.read_csv('output/doc_hash.json')
        input_dir = sys.argv[1]
        output_dir = 'output/zh_tf/'
    else:
        doc_hash = csv_io.read_csv('output/doc_hash.json')
        input_dir = 'output/en_tokens/'
        output_dir = 'output/en_tf/'

    document_list = get_docs_list(input_dir)
    for doc in document_list:
        terms = csv_io.read_csv(input_dir+doc)
        tf(terms, output_dir)
