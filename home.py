from flask import Flask, render_template, request

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":
        print(request.files)

        return render_template("DesignThePage.html")