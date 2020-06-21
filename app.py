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
                cmd = "python3 main.py --filename="
                cmd += image.filename
                os.system(cmd)
                return render_template("1.html")
    return render_template("upload.html")



if __name__ == '__main__':
    # load_model()
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.debug = True
    app.config["IMAGE_UPLOADS"] = "upload/"
    app.run(threaded=False,debug=False)
