from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter,PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import *

#'D:/nj/paper/01.pdf','rb
pdf='D:/nj/paper/01.pdf'
pdf0 = open(pdf,'rb')
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

for i in range(len(texts)):
    if i < len(texts) - 2:
        search=texts[i].get_text()
        print(texts[i])
        if 'Keywords' in search:
            print(search)
            i+=1
            abtract=texts[i].get_text()
            if 'Introduction' in abtract:
                abtract = texts[i + 1].get_text()
                print(abtract)
            else:
                abtract = texts[i].get_text()
                print(abtract)



