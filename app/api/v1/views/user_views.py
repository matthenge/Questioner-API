from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from app.api.v1.models.user_models import UserModels

parser = RequestParser()
parser.add_argument("email", type=str, required=True,
                    help="please input an email")
parser.add_argument("username", type=str, required=True,
                    help="please input a username")
parser.add_argument("password", type=str, required=True,
                    help="please input a password")
parser.add_argument("confirm_password", type=str, required=True,
                    help="confirm your password")


class Users(Resource):
    """Class for user endpoints"""

    def __init__(self):
        """Initialize the user class"""
        pass

    def post(self):
        """Register user endpoint"""
        args = parser.parse_args()
        args = request.get_json()
        email = args["email"]
        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]

        newUser = UserModels(email, username, password, confirm_password)
        newUser.save()

        return {
            "message": "User registered Successfully",
            "User": newUser.__dict__
        }, 201
