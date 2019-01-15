"""Tests"""
import unittest
from app import create_app
from .base_test import BaseTest
import json

message = "Password must have 8 chars, digit, lower & upper case, symbol"


class TestViews(BaseTest):
    """Test views"""

    def test_login(self):
        """Test user login endpoint"""
        self.signup()
        response = self.user_login()
        self.assertEqual(response.status_code, 200)

    def test_create_meetup(self):
        """Test create meetup endpoint"""
        self.register()
        response = self.create_meetup()
        self.assertEqual(response.status_code, 201)

    def test_get_meetup(self):
        """Test get specific meetup endpoint"""
        response = self.get_meetup()
        self.assertEqual(response.status_code, 200)

    def test_all_meetups(self):
        """Test get all meetups endpoint"""
        self.register()
        self.create_meetup()
        response = self.get_all_meetups()
        self.assertEqual(response.status_code, 200)

    def test_post_question(self):
        """Test post question endpoint"""
        self.create_meetup()
        response = self.post_question()
        self.assertEqual(response.status_code, 201)

    def test_upvote_question(self):
        """Test Upvote question endpoint"""
        self.post_question()
        response = self.upvote_question()
        self.assertEqual(response.status_code, 200)

    def test_downvote_question(self):
        """Test Downvote question endpoint"""
        self.post_question()
        self.upvote_question()
        response = self.downvote_question()
        self.assertEqual(response.status_code, 200)

    def test_reserve_space(self):
        """Test RSVP endpoint"""
        self.create_meetup()
        response = self.reserve_space()
        self.assertEqual(response.status_code, 201)

    def test_repeat_username(self):
        """Test signup repeat username"""
        response = self.signup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], "Username already exists")
        self.assertEqual(response.status_code, 403)

    def test_weak_password(self):
        """Test weak password"""
        response = self.weak_password()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], message)
        self.assertEqual(response.status_code, 403)

    def test_past_meetup_date(self):
        """Test past meetup date"""
        response = self.past_meetupdate()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], "New Meetup cannot be in the past")
        self.assertEqual(response.status_code, 403)

    def test_invalid_email(self):
        """Test an invalid email"""
        response = self.invalid_email()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"],
                         "martingmail.com is not a valid email")
        self.assertEqual(response.status_code, 403)
