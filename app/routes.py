from flask import render_template, current_app
from app import db
from app.models import CryptoData

@current_app.route('/')
def index():
    return render_template('index.html')
