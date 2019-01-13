"""Shared methods"""
import hashlib


class Helpers:
    """Helper methods"""
    def fetch(self, db, id):
        """Fetch using item"""
        for key in db:
            if key == id:
                return db[key]

    def check_username(self, users, username):
        """check for email in the database"""
        for user in users:
            if username == user["username"]:
                return user

    def hash_password(self, password, username):
        """method to hash user passwords"""
        salt = password + username
        hashed = hashlib.md5(str.encode(salt)).hexdigest()
        return hashed

    def check_hash_password(self, password, hashed):
        """Compare hashed passwords"""
        if password == hashed:
            return True
        else:
            return False

    def check_email(self, users, email):
        """check for email in the database"""
        for user in users:
            if email == user["email"]:
                return user
