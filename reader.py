import PyPDF2 as pdf
import textract
import re

#from pdfreader import simplePDFViewer#, PageDoesNotExist
#import pdfreader


run = True

mathpdf=pdf.PdfFileReader("Shareholders Agreement.pdf")

pages = mathpdf.getNumPages()
while run:
    String = input("Enter the text you want to search :")

    for i in range(0, pages):
        PageObj = mathpdf.getPage(i)
        print("Not found on page " + str(i))
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        
        for match in re.finditer(String, Text):
            print(f'Page no: {i} | Match: {match}')
            print(Text)
