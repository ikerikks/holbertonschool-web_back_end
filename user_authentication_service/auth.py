#!/usr/bin/env python3
"""authentication module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from bcrypt import checkpw
import uuid


def _hash_password(password: str) -> bytes:
    """return password hashed
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user
        """
        try:
            # Check if a user with the given email already exists
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)

        new_user = self._db.add_user(email, hashed_password)

        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Check if a user already exists"""
        try:
            user = self._db.find_user_by(email=email)

            if user:
                return checkpw(password.encode('utf-8'), user.hashed_password)

            return False
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        new_uuid = uuid.uuid4()
        return str(new_uuid)

    def create_session(self, email):
        try:
            user = self._db.find_user_by(email=email)
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)

            return session_id
        except NoResultFound:
            return None
