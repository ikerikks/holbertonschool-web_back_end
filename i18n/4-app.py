#!/usr/bin/env python3
"""
Basic Flask app Module.
"""
from flask import Flask, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


LANGUAGES = {
    'en': 'English',
    'fr': 'French'
}


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = LANGUAGES.keys()

@babel.localeselector
def get_locale():

    locale_param = request.args.get('locale')
    if locale_param in LANGUAGES:
        return locale_param

    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    return _("Hello, World!")


if __name__ == '__main__':
    app.run(debug=True)
