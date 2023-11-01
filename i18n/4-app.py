#!/usr/bin/env python3
""" Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
import os

app = Flask(__name__)

babel = Babel(app)


class Config:
    """ Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Match user's language based on browser settings.
    """
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the main page of the application.
    """
    return render_template('4-index.html', title=_('home_title'),
                           header=_('home_header'))


if __name__ == '__main__':
    app.run()
