from PyPDF2 import PdfReader, PdfWriter, PdfFileMerger, PdfMerger
# from merger import PdfFileMerger, PdfMerger
# from reader import PdfReader
# from xmp import XmpInformation
# from xml.parsers.expat import ExpatError

reader = PdfReader('My Admission Letter.pdf')
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()
    writer.add_page(page)

with open('My_Admission_Letter.pdf', 'wb') as f:
    writer.write(f)
'''
# print("This is a file Compressor")
file1 = open("Artificial Intelligence on Azure.docx", "r")
text = file1.read()
file1.close()
'''
'''
code = base64.base64encode(zlib.compress(text.encode("utf-8"), 9))
code = code.decode("utf-8")
'''
'''
f = open("compressed.pdf", "w")
f.write(code)
f.close()
'''