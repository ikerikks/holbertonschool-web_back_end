#/usr/bin/env python3
""" Flask app"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
