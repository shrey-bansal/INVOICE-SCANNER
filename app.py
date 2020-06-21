import sys, os
sys.path.append(os.path.abspath(os.path.join('./backend/ReceiptGenerator')))
from flask import Flask, Markup
from flask import render_template, request, redirect, flash, url_for
from crnn_processor import get_html
import os


app = Flask(__name__, template_folder='templates')


@app.route('/')
def home_endpoint():
    return redirect('/upload-image')


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            filename = image.filename
            filename = filename.lower()
            answer = filename.find('.jpg')
            answer += filename.find('.pdf')
            answer += filename.find('.png')
            answer += filename.find('.jpeg')
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            print(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            filename = image.filename
            if(answer==-4):
                return render_template("0.html")
            else:
                tbl = get_html(image.filename)
                return render_template("table.html",table = Markup(tbl))
    return render_template("upload.html")



if __name__ == '__main__':
    # load_model()
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.debug = True
    app.config["IMAGE_UPLOADS"] = "upload/"
    app.run(threaded=False,debug=False)
