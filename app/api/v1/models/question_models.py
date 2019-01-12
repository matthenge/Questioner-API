"""Question Models"""
import datetime
from app.api.v1.utils.utilities import Helpers


class QuestionModels(Helpers):
    """Class for question operations"""
    questions = {}

    def __init__(self, createdBy, meetup, title, body):
        """Initialize the questions models"""
        self.questionId = len(QuestionModels.questions)+1
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        self.createdBy = createdBy
        self.meetup = meetup
        self.title = title
        self.body = body
        self.votes = 0

    def save(self):
        """method to post question"""
        data = dict(
            questionId=self.questionId,
            createdOn=self.createdOn,
            createdBy=self.createdBy,
            meetup=self.meetup,
            title=self.title,
            body=self.body,
            votes=self.votes
        )
        self.questions.update({self.questionId: data})

    def upvote(self, questionId):
        """Method to upvote a question"""
        db = QuestionModels.questions
        question = Helpers().fetch(db, questionId)
        if question:
            question["votes"] += 1
            return question

    def downvote(self, questionId):
        """Method to downvote a question"""
        db = QuestionModels.questions
        question = Helpers().fetch(db, questionId)
        if question:
            question["votes"] -= 1
            return question
