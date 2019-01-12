from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v1.models.question_models import QuestionModels
from app.api.v1.models.meetup_models import MeetupModels
from flask_restful.reqparse import RequestParser

parser = RequestParser()
parser.add_argument("createdBy", type=str, required=True,
                    help="please input a valid userId")
parser.add_argument("meetupId", type=int, required=True,
                    help="please input a valid meetupId")
parser.add_argument("title", type=str, required=True,
                    help="please input a valid title")
parser.add_argument("body", type=str, required=True,
                    help="Describe your question")


class AllQuestions(Resource):
    """Class for questions endpoints"""

    def __init__(self):
        """Initialize the meetup class"""
        pass

    def post(self):
        """Create meetup endpoint"""
        args = parser.parse_args()
        args = request.get_json()
        createdBy = args["createdBy"]
        meetupId = args["meetupId"]
        title = args["title"]
        body = args["body"]

        meetup = MeetupModels.fetch_one(self, meetupId)
        if not meetup:
            return {
                "Error": "Meetup does not exist",
                "status": 404
            }, 404

        newQuestion = QuestionModels(createdBy, meetupId, title, body)
        newQuestion.save()

        return {
            "message": "Question Posted Successfully",
            "Question": newQuestion.__dict__
        }, 201


class Upvote(Resource):
    """Upvode question operation"""

    def patch(self, questionId):
        """Upvote question method"""
        question = QuestionModels.upvote(self, questionId)
        if not question:
            return {
                "Error": "Question does not exist",
                "status": 404
            }, 404
        return {
            "message": "Upvote Successful",
            "Question": question
        }, 200


class Downvote(Resource):
    """Downvote question Class"""

    def patch(self, questionId):
        """Downvote question method"""
        question = QuestionModels.downvote(self, questionId)
        if not question:
            return {
                "Error": "Question does not exist",
                "status": 404
            }, 404
        return {
            "message": "Downvote Successful",
            "Question": question
        }, 200
