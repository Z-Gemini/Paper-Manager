#!/usr/bin/python
#-*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
#获得目录（纲要）
# 打开一个pdf文件
fp = open(u'D:/nj/paper/02.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)

# .获得文档的目录（纲要）
outlines = document.get_outlines()
for (level,title,dest,a,se) in outlines:
    print (level, title)