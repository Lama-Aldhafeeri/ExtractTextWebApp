import pdfplumber
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextLineHorizontal, LTTextBoxHorizontal

content = ""
path = "C:\\Users\\lamay\\Downloads\\اختبار إسلامية ثاني متوسط الفصل الدراسي الاول.pdf"
# need to pass in laparams, otherwise pdfplumber page would not
# have high level pdfminer layout objects, only LTChars.
'''
#pdf = pdfplumber.open(path , laparams={})
with pdfplumber.open(path) as pdf:
 totalpages = len(pdf.pages)
 for i in range(0, totalpages):
        pageobj = pdf.pages[i].layout
#page = pdf.pages[0].layout
        for element in pageobj:
             if isinstance(element, LTTextBoxHorizontal):
                for line in element:
                        print(line.get_text()[::-1])
                        
'''
with pdfplumber.open(path) as pdf:
        totalpages = len(pdf.pages)
        for i in range(0, totalpages):
            pageobj = pdf.pages[i].layout
            for element in pageobj:
                if isinstance(element, LTTextLineHorizontal):
                    for line in element:
                        #if language_chosen == "Arabic":
                            print(line.get_text()[::-1])
                        #else:
                        #    content += line.get_text()
        print(content)