#!/usr/bin/env python3
"""module application"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration module
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Generate template
    """
    return render_template('3-index.html')


def get_locale():
    """define the best language or use locale information"""
    
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match('LANGUAGES')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8001")