#!/usr/bin/env python3
'''
'''

from flask import Flask, jsonify, redirect, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def hello_world():
    '''Main
    '''
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify(email=email, message='user created')
    except ValueError:
        return jsonify(message='email already registered'), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    ''' POST on session
    '''
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    if not email or not password:
        return abort(401)

    check: bool = AUTH.valid_login(email=email, password=password)
    if not check:
        abort(401)

    session_id: str = AUTH.create_session(email=email)
    res = jsonify(email=email, message='logged in')
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    '''Find the user with the requested session ID.
    If the user exists destroy the session and redirect the user to GET
    '''
    id = request.cookies.get('session_id')
    if id is None:
        abort(403)

    try:
        user = AUTH.get_user_from_session_id(id)
        AUTH.destroy_session(user_id=user.id)
        return redirect("/", 302)
    except:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    '''
    '''
    id = request.cookies.get('session_id')
    if id is None:
        abort(403)
    try:
        user = AUTH.get_user_from_session_id(id)
        return jsonify({"email": user.email})
    except:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    '''
    '''
    email: str = request.form.get('email')
    if not email:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route('./reset_password', methods=['GET'], strict_slashes=False)
def update_password():
    '''
    '''
    email: str = request.form.get('email')
    reset_token: str = request.form.get('reset_token')
    new_password: str = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token=get_reset_password_token, password=new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
