from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v1.models.meetup_models import MeetupModels
from flask_restful.reqparse import RequestParser
from datetime import datetime
from app.api.v1.utils.validator import Validators

validate = Validators()


class AllMeetups(Resource):
    """Class for meetup endpoints"""
    def __init__(self):
        """Initialize the meetup class"""
        self.parser = RequestParser()
        self.parser.add_argument("location", type=str, required=True,
                                 help="please input a valid location")
        self.parser.add_argument("images", type=str,
                                 help="please input a valid image url")
        self.parser.add_argument("topic", type=str, required=True,
                                 help="please input a valid topic")
        self.parser.add_argument("happeningOn",
                                 type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M"),
                                 required=True, help="Format yyyy-mm-dd hh:mm")
        self.parser.add_argument("userId", type=int, required=True,
                                 help="please input a valid userId(Integer)")

    def post(self):
        """Create meetup endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        location = args["location"]
        images = args["images"]
        topic = args["topic"]
        happeningOn = args["happeningOn"]
        userId = args["userId"]

        if validate.valid_strings(location) == "empty":
            return {
                "location": "Field cannot be empty"
            }, 400
        if validate.valid_strings(images) == "empty":
            return {
                "images": "Field cannot be empty"
            }, 400
        if validate.valid_strings(topic) == "empty":
            return {
                "topic": "Field cannot be empty"
            }, 400
        if validate.valid_time(happeningOn):
            return validate.valid_time(happeningOn)
        if validate.validate_user(userId):
            return validate.validate_user(userId)
        newMeetup = MeetupModels(location, images, topic, happeningOn, userId)
        newMeetup.save()

        return {
            "message": "Meetup Created Successfully",
            "meetup": newMeetup.__dict__
        }, 201

    def get(self):
        """Fetch all meetups"""
        meetups = MeetupModels.get_all(self)
        if not meetups:
            return {
                "Error": "No meetups posted yet",
                "status": 404
            }, 404
        return {
            "Message": "Success",
            "status": 200,
            "Meetups": meetups
        }, 200


class OneMeetup(Resource):
    """Class for single Meetup operations"""

    def get(self, meetupId):
        """Method to fetch specific meetup"""
        meetup = MeetupModels.fetch_one(self, meetupId)
        if not meetup:
            return {
                "Error": "Meetup does not exist",
                "status": 404
            }, 404
        return {
                "Message": "Success",
                "status": 200,
                "Meetup": meetup
            }, 200


class Upcoming(Resource):
    """Class for Upcoming meetups"""

    def get(self):
        """Method to fetch only upcoming meetups"""
        meetups = MeetupModels.upcoming_meetups(self)
        if not meetups:
            return {
                "Error": "No Upcoming Meetups",
                "status": 404
            }, 404
        return {
                "Message": "Success",
                "status": 200,
                "Meetups": meetups
            }, 200
