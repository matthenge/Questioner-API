"""Meetup Models"""
import datetime


class MeetupModels:
    """Class for meetup operations"""
    meetups = {}

    def __init__(self, location, images, topic, happeningOn, userId):
        """Initialize the questions models"""
        self.meetupId = len(MeetupModels.meetups)+1
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.userId = userId

    def save(self):
        """method to create metup"""
        data = dict(
            meetupId=self.meetupId,
            createdOn=self.createdOn,
            location=self.location,
            images=self.images,
            topic=self.topic,
            happeningOn=self.happeningOn,
            userId=self.userId
        )
        self.meetups.update({self.meetupId: data})
