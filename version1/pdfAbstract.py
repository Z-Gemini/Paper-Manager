from PyPDF2 import PdfReader

reader = PdfReader("D:/nj/paper/02.pdf")
page = reader.pages[0]
print(page.extract_text())