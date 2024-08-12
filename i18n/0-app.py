#!/usr/bin/env python3
"""Main app"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


@app.route('/')
def index():
    """Generate template"""
    
    return render_template('0-index.html')
