from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from app.api.v1.models.user_models import UserModels
from app.api.v1.utils.utilities import Helpers
from app.api.v1.utils.validator import Validators

helpers = Helpers()
validate = Validators()


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

        if validate.user_validator(email, password, username):
            return validate.user_validator(email, password, username)
        if validate.user_exists(email, username):
            return validate.user_exists(email, username)
        password = helpers.hash_password(password, username)
        confirm_password = helpers.hash_password(confirm_password, username)
        check = helpers.check_hash_password(password, confirm_password)
        if not check:
            return {
                "status": 403,
                "error": "Passwords do not match"
            }, 403

        newUser = UserModels(email, username, password, confirm_password)
        newUser.signup()

        return {
            "status": 201,
            "message": "User registered Successfully",
            "user": newUser.__dict__
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

        user = UserModels.fetch_username(self, username)
        if user:
            hashed = helpers.hash_password(password, username)
            check = helpers.check_hash_password(user["password"], hashed)
            if check is True:
                return {
                    "status": 200,
                    "message": "Logged in as {}".format(username),
                    "data": user
                }, 200
            return {
                    "status": 404,
                    "error": "Wrong password"
            }, 401
        return {
            "status": 404,
            "Error": "user not found: Please register"
        }, 404
