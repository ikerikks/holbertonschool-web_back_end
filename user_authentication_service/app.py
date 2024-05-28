#!/usr/bin/env python3
""" basic flask app
"""
from flask import Flask, request, jsonify, abort,  make_response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/users", methods=["POST"])
def register_user():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = AUTH.register_user(email, password)

        response = {"email": user.email, "message": "user created"}
        return jsonify(response)
    except ValueError as err:
        response = {"message": "email already registered"}
        return jsonify(response)


def login():
    data = request.form
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return make_response(jsonify(message="Email and password are required"), 400)

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(500)
    else:
        abort(401)
