__author__ = 'geoffreyboss'

import os
from flask import Flask


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(APP_ROOT, 'static/uploads')

from app import views

# songs =