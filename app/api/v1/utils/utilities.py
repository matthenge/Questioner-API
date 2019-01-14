"""Shared methods"""
import hashlib


class Helpers:
    """Helper methods"""
    def fetch(self, db, id):
        """Fetch using item"""
        for key in db:
            if key == id:
                return db[key]

    def hash_password(self, password, username):
        """method to hash user passwords"""
        salt = password + username
        hashed = hashlib.md5(str.encode(salt)).hexdigest()
        return hashed

    def check_hash_password(self, password, hashed):
        """Compare hashed passwords"""
        if password == hashed:
            return True
