from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v1.views.meetup_views import AllMeetups, OneMeetup
from app.api.v1.views.question_views import Downvote, Upvote
from app.api.v1.views.question_views import AllQuestions
from app.api.v1.views.user_views import Users, Login
from app.api.v1.views.rsvp_views import AllRsvps

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(version1, catch_all_404s=True)

api.add_resource(AllMeetups, '/meetups', strict_slashes=False)
api.add_resource(OneMeetup, '/meetups/<int:meetupId>', strict_slashes=False)
api.add_resource(AllQuestions, '/questions', strict_slashes=False)
api.add_resource(Upvote, '/questions/<int:questionId>/upvote',
                 strict_slashes=False)
api.add_resource(Downvote, '/questions/<int:questionId>/downvote',
                 strict_slashes=False)
api.add_resource(Users, '/auth/users', strict_slashes=False)
api.add_resource(Login, '/auth/users/login', strict_slashes=False)
api.add_resource(AllRsvps, '/meetups/rsvps', strict_slashes=False)
