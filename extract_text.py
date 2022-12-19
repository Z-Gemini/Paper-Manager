from pdfminer.high_level import extract_text

pdf=pdfminer(r'D:\nj\paper\01.pdf')
text=extract_text(pdf)
print(text)
