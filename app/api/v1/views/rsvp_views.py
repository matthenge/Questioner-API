from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v1.models.rsvp_models import RsvpModels
from flask_restful.reqparse import RequestParser
from app.api.v1.utils.validator import Validators

validate = Validators()

parser = RequestParser()
parser.add_argument("userId", type=int, required=True,
                    help="please input a valid userId")


class AllRsvps(Resource):
    """Class for rsvps endpoints"""

    def __init__(self):
        """Initialize the rsvps class"""
        pass

    def post(self, meetupId):
        """Create rsvp endpoint"""
        args = parser.parse_args()
        args = request.get_json()
        meetupId = meetupId
        userId = args["userId"]

        if validate.validate_meetup(meetupId):
            return validate.validate_meetup(meetupId)
        if validate.validate_user(userId):
            return validate.validate_user(userId)
        newRsvp = RsvpModels(meetupId, userId)
        newRsvp.save()

        return {
            "status": 201,
            "message": "RSVP created",
            "rsvp": newRsvp.__dict__
        }, 201
