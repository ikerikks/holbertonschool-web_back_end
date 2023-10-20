#!/usr/bin/env python3
""" basic flask app
"""
from flask import Flask, request, jsonify, abort
from auth import Auth
import uuid


app = Flask(__name__)
AUTH = Auth()


@app.route("/users", methods=["POST"])
def register_user():
    try:
        # Get email and password from form data
        email = request.form.get("email")
        password = request.form.get("password")

        # Register the user using the Auth object
        user = AUTH.register_user(email, password)

        response = {"email": user.email, "message": "user created"}
        return jsonify(response)
    except ValueError as err:
        response = {"message": "email already registered"}
        return jsonify(response)


users_db = {
    "bob@bob.com": {"email": "bob@bob.com", "password": "mySuperPwd"},
}

active_sessions = {}


@app.route('/sessions', methods=['POST'])
def login():
    data = request.form

    if "email" not in data or "password" not in data:
        return abort(400)

    user_email = data["email"]
    user_password = data["password"]

    user = users_db.get(user_email)

    if user is None or user["password"] != user_password:
        return abort(401)

    # Create a new session for the user
    session_id = str(uuid.uuid4())
    active_sessions[session_id] = user

    response = jsonify({"email": user_email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == '__main__':
    app.run(debug=True)
