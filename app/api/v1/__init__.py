from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v1.views.meetup_views import AllMeetups

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(version1, catch_all_404s=True)

api.add_resource(AllMeetups, '/meetups', strict_slashes=False)
