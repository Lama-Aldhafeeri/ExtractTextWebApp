import os

import pdfplumber as pdfplumber
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import pyperclip

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = 'files/'

@app.route('/', methods =['POST', 'GET'])
def upload_file():
    if request.method == "POST":
        print(request.files)
        pdf_file = request.files['file'] # Access the file

        if pdf_file.filename == '':
            print("File name is invalid")
            return render_template("DesignThePage.html", variable="No file chosen")


        filename = secure_filename(pdf_file.filename)
        pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        content =""
        # open the pdf and then extract the text
        with pdfplumber.open(f"files\\{filename}") as pdf:
            totalpages = len(pdf.pages)
            for i in range(0, totalpages):
                pageobj = pdf.pages[i]
                content += pageobj.extract_text()
            text = content
        if text == " ":
            return render_template("DesignThePage.html", variable="Sorry We Couldn't Find Text In Your File..")
        return render_template("display_text_page.html", variable=text)
    # delete the file
    #os.remove(f"files\\{filename}")
    return render_template("DesignThePage.html")

app.run()
