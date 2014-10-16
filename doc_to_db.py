#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

from my_class.DataDB import DataDB
from my_class.Document import Document
from modules import json_io
from doc_preprocessing import get_docs_list


if __name__=='__main__':
    if len(sys.argv) >= 2:
        data_dir = sys.argv[1]
        config = sys.argv[1]
    else:
        data_dir = 'output/processed_data/'
        config = json_io.read_json('config.json')[u'database']

    doc_hash = json_io.read_json('output/doc_hash.json')

    document_list = get_docs_list(data_dir)
    
    mydb = DataDB( config[u'dbtype'], config[u'host'], config[u'dbname'], \
            config[u'username'], config[u'password'], config[u'encoding'], "")
  
    table_name = "documents"
    key_list = ['doc_id', 'content']

    doc_id = 0
    for doc in document_list:
        doc_obj = Document(doc_id, doc, data_dir)
        content = doc_obj.read().replace("'", '"')
        data_list = [str(doc_hash[doc]),  content]

        mydb.insert_data(table_name, key_list, data_list)
        del doc_obj
        doc_id += 1
    mydb.close()
