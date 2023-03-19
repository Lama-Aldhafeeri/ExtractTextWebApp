<<<<<<< HEAD
import arabic_reshaper
from bidi.algorithm import get_display
import os
import os.path
import pdfplumber as pdfplumber
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
from flask_babel import Babel, gettext
from pdfminer.layout import LTTextLineHorizontal, LTTextBoxHorizontal
from ArabicOcr import arabicocr
from numba import jit, cuda
from pdf2image import convert_from_path
import PyPDF4
from lama_chat import *

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = 'files/'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # if session.get('lang') == 'ar':
    #    return 'ar'
    # else:
    #    return 'en'
    return request.accept_languages.best_match(['en', 'ar'])
    # return 'ar'

# @jit(target_backend='cuda')
def extract_text_from_img(path):
    out_image = 'out.jpg'
    results = arabicocr.arabic_ocr(path, out_image)
    print(results)
    words = []
    text = ""
    for i in range(len(results)):
        word = results[i][1]
        words.append(word)
    for w in range(len(words)):
        wordi = words[w]
        text += wordi + " "
    return text

def extract_text_from_pdf_method1(pdf_path):


    # Open the PDF file in read-binary mode

    with open('pdf_path', 'rb') as file:
        # Create a PDF reader object

        pdf_reader = PyPDF4.PdfFileReader(file)

        # Get the total number of pages in the PDF file

        num_pages = pdf_reader.getNumPages()

        # Loop through each page in the PDF file

        for page_num in range(num_pages):
            # Get the text from the current page

            page = pdf_reader.getPage(page_num)

            text = page.extractText()

            # Preprocess the text

            text = text.replace('\n', ' ').replace('\r', '')

            text = ' '.join(text.split())

            # Print the text from the current page

            print(text)
def setPages(pages):
    pass

def extract_text_from_pdf_method2(pdf_path, language_chosen):
    content = ""
    with pdfplumber.open(pdf_path) as pdf:
        totalpages = len(pdf.pages)
        for i in range(0, totalpages):
            pageobj = pdf.pages[i].layout
            for element in pageobj:
                if isinstance(element, LTTextBoxHorizontal):
                    for line in element:
                        if language_chosen == "Arabic":
                            content += line.get_text()[::-1]
                        else:
                            content += line.get_text()
        return content
import webbrowser

# Open URL in a new tab, if a browser window is already open.

@app.route('/', methods=['POST', 'GET'])
def upload_file():

    if request.method == "POST":
        print(request.files)
        pdf_file = request.files['file']  # Access the file
        #language_chosen = request.form['Language_chosen']  # Access the value of radio button
        # lang = request.form['lang']
        # language = get_user_lang(lang)

        if pdf_file.filename == '':
            print("File name is invalid")
            return render_template("DesignThePage.html", variable=gettext("No file chosen"))
       # elif language_chosen is None:
          #  print("No language coden")
           # return render_template("DesignThePage.html", variable=gettext("Please choose the language of your pdf file"))

        # Upload The file
        filename = secure_filename(pdf_file.filename)
        pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        path = f'files\\{filename}'
        text = ''
        if filename[-3: len(filename)] == 'pdf':
            text = extract_text_from_pdf_method1(path)
        result = final_result(text)

        if result == '':
            return render_template("DesignThePage.html", variable=gettext("Sorry We Couldn't Find Text In Your File.."))
        return render_template("testFrom.html", variable=result)
    # delete the file
    mypath = "files"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    return render_template("DesignThePage.html")

app.run()
=======
import arabic_reshaper
from bidi.algorithm import get_display
import os
import os.path
import pdfplumber as pdfplumber
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
from flask_babel import Babel, gettext
from pdfminer.layout import LTTextLineHorizontal, LTTextBoxHorizontal
from ArabicOcr import arabicocr
from numba import jit, cuda
from pdf2image import convert_from_path
import PyPDF4
from lama_chat import *

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = 'files/'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # if session.get('lang') == 'ar':
    #    return 'ar'
    # else:
    #    return 'en'
    return request.accept_languages.best_match(['en', 'ar'])
    # return 'ar'

# @jit(target_backend='cuda')
def extract_text_from_img(path):
    out_image = 'out.jpg'
    results = arabicocr.arabic_ocr(path, out_image)
    print(results)
    words = []
    text = ""
    for i in range(len(results)):
        word = results[i][1]
        words.append(word)
    for w in range(len(words)):
        wordi = words[w]
        text += wordi + " "
    return text

def extract_text_from_pdf_method1(pdf_path):


    # Open the PDF file in read-binary mode

    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object

        pdf_reader = PyPDF4.PdfFileReader(file)

        # Get the total number of pages in the PDF file

        num_pages = pdf_reader.getNumPages()

        # Loop through each page in the PDF file

        for page_num in range(num_pages):
            # Get the text from the current page

            page = pdf_reader.getPage(page_num)

            text = page.extractText()

            # Preprocess the text

            text = text.replace('\n', ' ').replace('\r', '')

            text = ' '.join(text.split())

            # Print the text from the current page

            print(text)
def setPages(pages):
    pass

def extract_text_from_pdf_method2(pdf_path, language_chosen):
    content = ""
    with pdfplumber.open(pdf_path) as pdf:
        totalpages = len(pdf.pages)
        for i in range(0, totalpages):
            pageobj = pdf.pages[i].layout
            for element in pageobj:
                if isinstance(element, LTTextBoxHorizontal):
                    for line in element:
                        if language_chosen == "Arabic":
                            content += line.get_text()[::-1]
                        else:
                            content += line.get_text()
        return content
import webbrowser

# Open URL in a new tab, if a browser window is already open.

@app.route('/', methods=['POST', 'GET'])
def upload_file():

    if request.method == "POST":
        print(request.files)
        pdf_file = request.files['file']  # Access the file
        #language_chosen = request.form['Language_chosen']  # Access the value of radio button
        # lang = request.form['lang']
        # language = get_user_lang(lang)

        if pdf_file.filename == '':
            print("File name is invalid")
            return render_template("DesignThePage.html", variable=gettext("No file chosen"))
       # elif language_chosen is None:
          #  print("No language coden")
           # return render_template("DesignThePage.html", variable=gettext("Please choose the language of your pdf file"))

        # Upload The file
        filename = secure_filename(pdf_file.filename)
        pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        path = f'files\\{filename}'
        text = ''
        if filename[-3: len(filename)] == 'pdf':
            text = extract_text_from_pdf_method1(path)
        result = final_result(text)

        if result == '':
            return render_template("DesignThePage.html", variable=gettext("Sorry We Couldn't Find Text In Your File.."))
        return render_template("testFrom.html", variable=result)
    # delete the file
    mypath = "files"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    return render_template("DesignThePage.html")

app.run()
>>>>>>> eb884ab (update)
