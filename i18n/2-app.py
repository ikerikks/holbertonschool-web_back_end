#!/usr/bin/env python3
""" Flask app"""
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


@app.route('/')
def index():
    """Returns html"""
    return '<title>Welcome to Holberton</title>'


class Config:
    """ Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Returns locale  string"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
