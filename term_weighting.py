#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import math

import term_frequency
from modules import csv_io
from modules import json_io
from doc_preprocessing import get_docs_list
from my_class.DataDB import DataDB


def idf():
    doc_id = 0
    term_idf = {}
    for doc in document_list:
        terms = json_io.read_json('output/tf/'+doc)
        for term in terms:
            if term not in term_idf:
                term_idf[term] = []
            term_idf[term].append(term)
    return term_idf

if __name__=='__main__':

    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
    else:
        input_dir = 'output/zh_tf/'

    config = json_io.read_json('config.json')[u'database']
    doc_hash = json_io.read_json('output/doc_hash.json')
    document_list = get_docs_list(input_dir)

    mydb = DataDB( config[u'dbtype'], config[u'host'], config[u'dbname'], \
            config[u'username'], config[u'password'], config[u'encoding'], "")

    #Get idf
    term_doc_list = idf()

    term_hash= {}
    term_id = 1
    doc_number = len(document_list)
    for term, doc in term_doc_list.iteritems():
        term = term.replace("'", "")
        if len(term) > 255:
            term = term[:254]
        
        idf = round(math.log(doc_number/(len(doc) + 1)), 4)
        sql = "INSERT INTO terms (term,idf) VALUES (" + "'" + term + "','" + str(idf) + "');"
        mydb.exe_sql(sql)

        term_hash[term] = term_id
        term_id += 1
    
    term_frequency.to_db(mydb, term_hash, document_list, doc_hash)
    mydb.close()
    
