"""Validators"""
import datetime
import re
from app.api.v1.models.user_models import UserModels
from app.api.v1.models.meetup_models import MeetupModels

message = "Password must have 8 chars, digit, lower & upper case, symbol"


class Validators():
    """Class for validations"""
    def __init__(self):
        """Initialize the validators class"""
        pass

    def valid_time(self, happeningOn):
        """Method to validate happeningOn date"""
        createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if happeningOn < createdOn:
            return {
                "Error": "New Meetup cannot be in the past"
            }, 403

    def valid_email(self, email):
        """Method to validate email"""
        ex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not re.match(ex, email):
            return {
                "Error": "{} is not a valid email".format(email)
            }, 403

    def valid_password(self, password):
        """
        Validate password strength
        Should contain: Atleats 8 characters in length,
                    Atleast 1 uppercase letter,
                    Atleast 1 lowercase letter,
                    Atleast 1 digit,
                    Atleast one special character
        """
        regex = re.compile(r"^(?=.*[!@#$%^?&*()])(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.{8,})")
        if not re.search(regex, password):
            return {
                "Error": message
            }, 403

    def valid_username(self, username):
        """Username should be atleast 3 characters long"""
        if len(username) < 3:
            return {
                "Error": "Username is too short"
            }, 403

    def user_validator(self, email, password, username):
        """Validator for correct email, username and password"""
        if Validators().valid_email(email):
            return Validators().valid_email(email)
        if Validators().valid_password(password):
            return Validators().valid_password(password)
        if Validators().valid_username(username):
            return Validators().valid_username(username)

    def user_exists(self, email, username):
        """Validator to find is username and email already registered"""
        name = UserModels.fetch_username(self, username)
        mail = UserModels.fetch_email(self, email)
        if name:
            return {
                "Error": "Username already exists"
            }, 403
        if mail:
            return {
                "Error": "Email already exists"
            }, 403

    def validate_user(self, userId):
        """Validate if userId exists"""
        user = UserModels.fetch_userId(self, userId)
        if not user:
            return {
                "Error": "User does not exist"
            }, 404

    def validate_meetup(self, meetupId):
        """Validate if meetupId exists"""
        meetup = MeetupModels.fetch_one(self, meetupId)
        if not meetup:
            return {
                "Error": "Meetup does not exist"
            }, 404
