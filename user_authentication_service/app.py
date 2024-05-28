#!/usr/bin/env python3
""" basic flask app
"""
from flask import Flask, request, jsonify, abort,  make_response
import uuid
from auth import Auth
from db import DB
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()
db = DB()


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


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    try:
        # Fetch user from the database
        user = db.find_user_by(email=email)
        
        # Check if the password matches
        if user.hashed_password != password:
            abort(401)
        
        # Create a new session ID
        session_id = db.create_session(user.email)
        
        # Create the response with the session ID cookie
        response = make_response(jsonify({"email": user.email, "message": "logged in"}))
        response.set_cookie('session_id', session_id)
        
        return response
    
    except NoResultFound:
        abort(401)

if __name__ == '__main__':
    app.run(debug=True)
