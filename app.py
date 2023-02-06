import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_DEBUG'] = 1


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    fn = secure_filename(file.filename)
    file.save(os.path.join('uploads', fn))
    response = {
        "success": True,
        "message": fn
    }
    return response


if __name__ == '__main__':
    app.run()

import prediction
