#!/usr/bin/env python
# coding: utf-8
# pip3 install pypdf  

import os
from pypdf import PdfMerger as pm

pdf_path = './pdf/'
pdf_list = ['aaa.pdf','bbb.pdf']

pdf_merger = pm()
for pdf in pdf_list:
    path = pdf_path + pdf
    pdf_merger.append(path, outline_item=False)
    
pdf_merger.write('./out_file.pdf')