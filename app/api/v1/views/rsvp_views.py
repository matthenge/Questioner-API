from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v1.models.rsvp_models import RsvpModels
from app.api.v1.models.meetup_models import MeetupModels
from flask_restful.reqparse import RequestParser

parser = RequestParser()
parser.add_argument("meetupId", type=int, required=True,
                    help="please input a valid meetupId")
parser.add_argument("userId", type=int, required=True,
                    help="please input a valid userId")


class AllRsvps(Resource):
    """Class for rsvps endpoints"""

    def __init__(self):
        """Initialize the rsvps class"""
        pass

    def post(self):
        """Create rsvp endpoint"""
        args = parser.parse_args()
        args = request.get_json()
        meetupId = args["meetupId"]
        userId = args["userId"]

        meetup = MeetupModels.fetch_one(self, meetupId)
        if not meetup:
            return {
                "Error": "Meetup does not exist",
                "status": 404
            }, 404

        newRsvp = RsvpModels(meetupId, userId)
        newRsvp.save()

        return {
            "message": "RSVP created",
            "RSVP": newRsvp.__dict__
        }, 201
