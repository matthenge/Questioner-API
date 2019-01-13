from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from app.api.v1.models.user_models import UserModels
from app.api.v1.utils.utilities import Helpers

users = UserModels()
helpers = Helpers()


class Users(Resource):
    """Class for user registration"""

    def __init__(self):
        """Initialize the user class"""
        self.parser = RequestParser()
        self.parser.add_argument("email", type=str, required=True,
                                 help="please input an email")
        self.parser.add_argument("username", type=str, required=True,
                                 help="please input a username")
        self.parser.add_argument("password", type=str, required=True,
                                 help="please input a password")
        self.parser.add_argument("confirm_password", type=str, required=True,
                                 help="confirm your password")

    def post(self):
        """Register user endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        email = args["email"]
        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]

        newUser = users.signup(email, username, password,
                               confirm_password)

        return {
            "message": "User registered Successfully",
            "user": newUser
        }, 201


class Login(Resource):
    """class for user login"""
    def __init__(self):
        """Initialize the login class"""
        self.parser = RequestParser()
        self.parser.add_argument("username", type=str, required=True,
                                 help="please input a username")
        self.parser.add_argument("password", type=str, required=True,
                                 help="please input a password")

    def post(self):
        """method to login user"""
        data = self.parser.parse_args()
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        _user = users.fetch_username(username)
        password = helpers.hash_password(password, username)
        if _user and password == _user["password"]:
            return {
                    "message": "Logged in as {}".format(username)
                }, 200
