from flask import Flask
from flask import render_template, request, redirect, flash, url_for
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
            jpg = filename.find('jpg')
            jpeg = filename.find('jpeg')
            png = filename.find('png')
            if(jpg==-1 and jpeg==-1 and png==-1):
                flash('Image format should be "png", "jpg" or "jpeg"')
                return redirect(url_for('home_endpoint'))
            answer = filename.find('non')
            covid = filename.find('covid')
            if(answer==-1 and covid!=-1):
                return render_template("0.html")
            else:
                return render_template("1.html")
    return render_template("upload.html")



if __name__ == '__main__':
    # load_model()
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.debug = True
    app.config["IMAGE_UPLOADS"] = "Test/class1"
    app.run(threaded=False,debug=False)
