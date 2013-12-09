__author__ = 'geoffreyboss'

import os
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files['file']
        if files.filename:
            filename = secure_filename(files.filename)
            files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)
    return render_template('index.html')

@app.route('/uploads/')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'],
                               filename), as_attachment=True)