from flask import render_template
from app import db
from app.models import CryptoData
from flask import current_app

@current_app.route('/')
def index():
    return render_template('index.html')
