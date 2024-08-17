#!/usr/bin/env python3
"""Basic Flask app
"""

from flask import Flask, jsonify, request
from user import User
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """index
    """
    payload = {"message": "Bienvenue"}
    return jsonify(payload)

@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user_exist = AUTH.register_user(email=email, password=password)
        payload = {"email": user_exist.email, "message": "user created"}
        return jsonify(payload), 201
    except ValueError:
        payload = {"message": "email already registered"}
        return jsonify(payload), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
