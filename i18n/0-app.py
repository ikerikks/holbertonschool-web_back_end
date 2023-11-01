#!/usr/bin/env python3
"""App module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Returns html"""
    return '<title>Welcome to Holberton</title>'


if __name__ == '__main__':
    app.run(debug=True)
