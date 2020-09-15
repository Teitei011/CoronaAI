from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from Models.AI import AI
from flask_bootstrap import Bootstrap
from flask import jsonify, json
from datetime import datetime
# from flask_cors import CORS
import sys
import os

app = Flask(__name__)
Bootstrap(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = os.path.join('static', 'uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# CORS(app, expose_headers='Authorization')


def name_imgs():
    prefix = 'IMG'
    name = datetime.now().strftime("%Y%m%d_%H%M%S")
    return "{}_{}".format(prefix, name)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = secure_filename(file.filename)

    if (allowed_file(filename)):

        _, ext = os.path.splitext(filename)
        name = name_imgs()
        filename = "{}{}".format(name, ext)
        image = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image)
        result = AI(image)

        return render_template("upload.html", result=result, image=image)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True)  # threaded=True
