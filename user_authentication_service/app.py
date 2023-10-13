#!/usr/bin/env python3
""" basic flask app
"""
from flask import Flask, request, jsonify
from auth import Auth

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


if __name__ == "__main__":
    app.run(debug=True)
