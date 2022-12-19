from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter,PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import *
from pdfminer.high_level import extract_text,extract_pages

import re
#D:/nj/paper/01.pdf','rb

pdf0 = open('D:/nj/paper/01.pdf','rb')
parser = PDFParser(pdf0)
doc = PDFDocument(parser)
parser.set_document(doc)

resources = PDFResourceManager()
laparam = LAParams()
device = PDFPageAggregator(resources, laparams=laparam)
interpreter = PDFPageInterpreter(resources, device)

pages = []
for page in PDFPage.create_pages(doc):
    pages.append(page)

interpreter.process_page(pages[0])
layout=device.get_result()

texts=[]

for out in layout:
    if isinstance(out,LTTextBox):
        texts.append(out)

for text in texts:
    print(text)
    search=text.get_text()
    #print(text.get_text())
    if 'Keywords' in search:
        print(search)

