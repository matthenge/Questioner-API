"""Set up test base"""
import unittest
from app import create_app
import json


class BaseTest(unittest.TestCase):
    """Test views"""
    def setUp(self):
        """Set up test variables"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app
        self.app.testing = True

        self.meetup = {
            "location": "Kisumu",
            "images": "www.image1.com",
            "topic": "data science",
            "happeningOn": "2019-10-22 10:00",
            "userId": 1
        }
        self.oneMeetup = {
            "meetupId": 3,
            "createdOn": "2019-01-10 08:34 AM",
            "location": "Kisumu",
            "images": "www.image1.com",
            "topic": "data science",
            "happeningOn": "2019-10-22 10:00",
            "userId": 1
        }
        self.user = {
            "email": "general@gmail.com",
            "username": "genmat",
            "password": "qwerty123",
            "confirm_password": "qwerty123"
        }
        self.question = {
            "createdBy": 1,
            "meetupId": 1,
            "title": "What is data science",
            "body": "please explain data science in length"
        }
        self.rsvp = {
            "rsvpId": "1",
            "meetup": "1",
            "user": "2",
            "response": "True"
        }
        self.login = {
            "username": "genorigi",
            "password": "qwerty123"
        }

    def signup(self):
        """user registration"""
        res = self.client.post(
            '/api/v1/auth/users',
            data=json.dumps(self.user),
            content_type='application/json')
        return res

    def create_meetup(self):
        """meetup creation"""
        res = self.client.post(
            '/api/v1/meetups',
            data=json.dumps(self.meetup),
            content_type='application/json')
        return res

    def post_question(self):
        """post question"""
        res = self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.question),
            content_type='application/json')
        return res

    def reserve_space(self):
        """reserve attendance"""
        res = self.client.post(
            '/api/v1/rsvps',
            data=json.dumps(self.rsvp),
            content_type='application/json')
        return res

    def get_meetup(self):
        """Fetch specific meetup"""
        res = self.client.get(
            '/api/v1/meetups/1')
        return res

    def get_all_meetups(self):
        """Fetch all upcomming meetups"""
        res = self.client.get(
            '/api/v1/meetups')
        return res

    def upvote_question(self):
        """Upvote a question"""
        res = self.client.patch(
            '/api/v1/questions/1/upvote')
        return res

    def downvote_question(self):
        """Downvote a question"""
        res = self.client.patch(
            '/api/v1/questions/1/downvote')
        return res

    def user_login(self):
        """login user"""
        res = self.client.post(
            '/api/v1/auth/users/login',
            data=json.dumps(self.login),
            content_type='application/json')
        return res
