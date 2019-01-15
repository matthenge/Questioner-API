"""User models"""

users = []


class UserModels():
    """Class for user operations"""

    def __init__(self):
        """Initialize the users models"""
        self.db = users

    def signup(self, email, username, password, confirm_password):
        """method to signup"""
        data = {
            'userId': len(self.db) + 1,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'isAdmin': True
        }
        self.db.append(data)
        return self.db

    def fetch_username(self, username):
        """Method to fetch username"""
        for user in self.db:
            if user["username"] == username:
                return user

    def fetch_email(self, email):
        """Method to fetch email"""
        for user in self.db:
            if user["email"] == email:
                return user

    def fetch_userId(self, userId):
        """Method to fetch user by Id"""
        for user in self.db:
            if user["userId"] == userId:
                return user
