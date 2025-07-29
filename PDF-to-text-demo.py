import PyPDF2

pdfFileObject = open('combinedBSUniDocs.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObject)

print('The number of pages in this book is ', pdfReader.pages, 'pages')

pageObject = pdfReader.pages[2]

print(pageObject.extract_text())

pdfFileObject.close()

