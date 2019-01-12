"""Tests"""
import unittest
from app import create_app
from .base_test import BaseTest
import json


class TestViews(BaseTest):
    """Test views"""
    def test_signup(self):
        """Test signup endpoint"""
        response = self.signup()
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        """Test user login endpoint"""
        response = self.user_login()
        self.assertEqual(response.status_code, 200)

    def test_create_meetup(self):
        """Test create meetup endpoint"""
        response = self.create_meetup()
        self.assertEqual(response.status_code, 201)

    def test_get_meetup(self):
        """Test get specific meetup endpoint"""
        response = self.get_meetup()
        self.assertEqual(response.status_code, 200)

    def test_all_meetups(self):
        """Test get all meetups endpoint"""
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
        response = self.reserve_space()
        self.assertEqual(response.status_code, 200)
