"""Meetup Models"""
import datetime


class MeetupModels:
    """Class for meetup operations"""
    meetups = {}

    def __init__(self, location, images, topic, happeningOn, userId):
        """Initialize the meetup models"""
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

    def get_all(self):
        """Method to fetch all meetups"""
        return MeetupModels.meetups

    def fetch_one(self, meetupId):
        """Method to fetch one meetup"""
        for key in MeetupModels.meetups:
            if key == meetupId:
                return MeetupModels.meetups[key]
