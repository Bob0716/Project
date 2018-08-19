# _*_coding:utf8_*_
# readPdf.py
# python读取pdf格式的文档

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# with open('2.txt') as f:
#     pdfFile = f.readlines()
#     for line in pdfFile:
pdfFile = open("C:\example\\1203071779.PDF",encoding='utf-8',errors='ignore')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()