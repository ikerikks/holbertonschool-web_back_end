#!/usr/bin/env python3
"""Main app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration module
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match('LANGUAGES')


def get_user():
    """
    """
    try:
        user_nb = int(request.args.get('login_as'))
        if user_nb in users.keys() and user_nb is not None:
            return users[user_nb]
    except Exception:
        return None


@app.before_request
def before_request():
    """
    """
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def index():
    """Generate template
    """
    try:
        username = g.user['name']
    except Exception:
        username = None
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run()