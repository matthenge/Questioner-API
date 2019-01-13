"""User models"""
from app.api.v1.utils.utilities import Helpers

users = []
helpers = Helpers()


class UserModels():
    """Class for user operations"""

    def __init__(self):
        """Initialize the users models"""
        pass

    def signup(self, email, username, password, confirm_password):
        """method to signup"""
        data = {
            'userId': len(users) + 1,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'isAdmin': False
        }
        password = helpers.hash_password(password, username)
        confirm_password = helpers.hash_password(confirm_password, username)
        users.append(data)
        return users

    def fetch_username(self, username):
        """Method to fetch username"""
        for user in users:
            if user["username"] == username:
                return user
