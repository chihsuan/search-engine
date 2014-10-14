#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import re

from text_class.Document import Document
from doc_preprocessing import get_docs_list

def split_zh_en (zh_en_str):

    mark = {"en":1, "zh":2}
    zh_en_group = []
    zh_set = []
    en_set = []
    status = ""
    en = ""
    zh = ""
    for c in zh_en_str:
        if is_zh(c):
            if status == 'en':
                zh_en_group.append ([mark["en"], ''.join(en_set)])
                en += ''.join(en_set)
                en_set = []
            zh_set.append(c)
            status = 'zh'
        else:
            if status == 'zh':
                zh_en_group.append ([mark["zh"], ''.join(zh_set)])
                zh += ''.join(zh_set)
                zh_set = []
            en_set.append(c)
            status = 'en'
        
    if en_set:
        zh_en_group.append ([mark["en"], ''.join(en_set)])
    elif zh_set:
        zh_en_group.append ([mark["zh"], ''.join(zh_set)])

    return zh_en_group, en, zh

def is_zh (c):
    c_unicode = ord (c)

    # unicode range
    zh_range = [[0x2e80, 0x33ff], [0xff00, 0xffef], [0x4e00, 0x9fbb], \
                [0xf900, 0xfad9], [0x20000, 0x2a6d6], [0x2f800, 0x2fa1d]]
    for lower, upper in zh_range:
        if c_unicode >= lower and c_unicode <= upper:
            return True
    return False

def lan_output(foldr, file_name, content):
    with open(foldr+file_name, 'w') as f:
        f.write(content.encode('utf-8'))

if __name__=='__main__':
    #result = split_zh_en(sys.argv[1].decode('utf-8'))
    if len(sys.argv) >= 4:
        doc_input = sys.argv[1]
        en_output = sys.argv[2]
        zh_output = sys.argv[3]
    else:
        doc_input = 'output/processed_data/'
        en_output = 'output/en_doc/'
        zh_output = 'output/zh_doc/'


    document_list = get_docs_list(doc_input)
    for doc in document_list:
        doc_id = 0
        doc_obj = Document(doc_id, doc, doc_input)
        for line in doc_obj.get_lines():
            result, en, zh = split_zh_en(line.decode('utf-8'))
            lan_output(en_output, doc, en) 
            lan_output(zh_output, doc, zh) 
        doc_id += 1
