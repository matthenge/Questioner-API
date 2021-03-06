from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v1.models.question_models import QuestionModels
from flask_restful.reqparse import RequestParser
from app.api.v1.utils.validator import Validators

validate = Validators()


class AllQuestions(Resource):
    """Class for questions endpoints"""

    def __init__(self):
        """Initialize the meetup class"""
        self.parser = RequestParser()
        self.parser.add_argument("createdBy", type=int, required=True,
                                 help="please input a valid userId")
        self.parser.add_argument("meetupId", type=int, required=True,
                                 help="please input a valid meetupId")
        self.parser.add_argument("title", type=str, required=True,
                                 help="please input a valid title")
        self.parser.add_argument("body", type=str, required=True,
                                 help="Describe your question")

    def post(self):
        """Create meetup endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        createdBy = args["createdBy"]
        meetupId = args["meetupId"]
        title = args["title"]
        body = args["body"]

        if validate.validate_user(createdBy):
            return validate.validate_user(createdBy)
        if validate.validate_meetup(meetupId):
            return validate.validate_meetup(meetupId)
        if validate.valid_strings(title) == "empty":
            return {
                "status": 400,
                "title": "Field cannot be empty"
            }, 400
        if validate.valid_strings(body) == "empty":
            return {
                "status": 400,
                "body": "Field cannot be empty"
            }, 400
        newQuestion = QuestionModels(createdBy, meetupId, title, body)
        newQuestion.save()

        return {
            "status": 201,
            "message": "Question Posted Successfully",
            "question": newQuestion.__dict__
        }, 201


class Upvote(Resource):
    """Upvode question operation"""

    def patch(self, questionId):
        """Upvote question method"""
        question = QuestionModels.upvote(self, questionId)
        if not question:
            return {
                "status": 404,
                "error": "Question does not exist"
            }, 404
        return {
            "status": 200,
            "message": "Upvote Successful",
            "question": question
        }, 200


class Downvote(Resource):
    """Downvote question Class"""

    def patch(self, questionId):
        """Downvote question method"""
        question = QuestionModels.downvote(self, questionId)
        if not question:
            return {
                "status": 404,
                "error": "Question does not exist"
            }, 404
        return {
            "status": 200,
            "message": "Downvote Successful",
            "question": question
        }, 200
