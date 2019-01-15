"""User models"""


class UserModels:
    """Class for user operations"""
    users = []

    def __init__(self, email, username, password, confirm_password):
        """Initialize the users models"""
        self.userId = len(UserModels.users) + 1
        self.email = email
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.isAdmin = True

    def signup(self):
        """method to signup"""
        data = dict(
            userId=self.userId,
            email=self.email,
            username=self.username,
            password=self.password,
            confirm_password=self.confirm_password,
            isAdmin=self.isAdmin
        )
        self.users.append(data)
        return self.users

    def fetch_username(self, username):
        """Method to fetch username"""
        for user in UserModels.users:
            if user["username"] == username:
                return user

    def fetch_email(self, email):
        """Method to fetch email"""
        for user in UserModels.users:
            if user["email"] == email:
                return user

    def fetch_userId(self, userId):
        """Method to fetch user by Id"""
        for user in UserModels.users:
            if user["userId"] == userId:
                return user
