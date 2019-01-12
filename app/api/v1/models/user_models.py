"""User Models"""


class UserModels():
    """Class for user operations"""
    users = {}

    def __init__(self, email, username, password, confirm_password):
        """Initialize the users models"""
        self.userId = len(UserModels.users)+1
        self.email = email
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.isAdmin = False

    def save(self):
        """method to signup user"""
        data = dict(
            userId=self.userId,
            email=self.email,
            username=self.username,
            password=self.password,
            confirm_password=self.confirm_password
        )
        self.users.update({self.userId: data})
