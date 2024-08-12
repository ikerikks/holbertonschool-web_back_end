#!/usr/bin/env python3
"""
Basic Flask app Module.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Configuration for language support"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def hello():
    """Render a welcome message"""
    return render_template('3-index.html')

# Define the locale selector function
def get_locale():
    """Determine the best language for the user"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Set the locale selector function
babel.locale_selector_func = get_locale

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
