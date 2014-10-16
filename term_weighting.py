#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import math

from modules import csv_io
from modules import json_io
from doc_preprocessing import get_docs_list
from my_class.DataDB import DataDB

def tf(terms):
    terms_tf = {}
    for term in terms:
        if term not in words_tf:
            terms_tf[term] = 1.0
        else:
            terms_tf[term] += 1.0

    length = len(terms)
    for term, count in terms_tf.iteritems():
        count/length

    return terms_tf

def sub_idf(document_list):
    term_idf = {}
    doc_id = 0
    for doc in document_list:
        content = csv_io.read_csv('output/tokens/'+doc)
        for term in content:
            if term not in term_idf:
                term_idf[term] = doc_id
        json_io.write_json('output/sub_idf/'+doc+'.json', term_idf)

def idf(terms):
    doc_id = 0
    term_idf = {}
    for term in terms:
        term_idf[term] = []

    for doc in document_list:
        content = csv_io.read_csv('output/tokens/'+doc)
        for term in terms:
            if term in content:
                term_idf[term].append(doc_id)
    return term_idf

def create_term_set(document_list):
    term_set = []
    for doc in document_list:
        terms = csv_io.read_csv('output/tokens/'+doc)
        for term in terms:
            if term not in term_set:
                term_set.append(term)
    csv_io.write_csv('output/term_set.csv', [term_set])

if __name__=='__main__':

    doc_hash = csv_io.read_csv('output/doc_hash.json')
    document_list = get_docs_list('output/tokens/')
    config = json_io.read_json('config.json')[u'database']

    if len(sys.argv) > 1:

        if sys.argv[1] == '1':
            #create_term_set(document_list)
            sub_idf(document_list)
        
        elif sys.argv[1] == '2':
            mydb = DataDB( config[u'dbtype'], config[u'host'], config[u'dbname'], \
                    config[u'username'], config[u'password'], config[u'encoding'], "")

            term_set = csv_io.read_csv('output/term_set.csv')
            term_doc_list = term_idf(term_set)

            doc_number = len(document_list)
            for term, doc in term_doc_list.iteritems():
                idf = math.log(doc_number/(len(doc) + 1))
                sql = "INSERT INTO terms (term,idf) VALUES (" + "'" + term + "','" + str(idf) + "');"
                mydb.exe_sql(sql)
            mydb.close()
        else:
            term_id = json_io.read_json('output/term_id.json')
            doc_id = 0
            for doc in document_list:
                content = csv_io.read_csv('output/tokens/'+doc)
                terms_tf = tf(content)
                for term, tf in terms_tf.iteritems():
                    sql = "INSERT INTO doc_lookups (doc_id,tf,term_id) VALUES (" \
                        + "'" + str(doc_id) + "','" + str(tf) + "','" + str(term_id[term]) + "');"
                    mydb.exe_sql(sql)
                doc_id += 1
            mydb.close()
