"""RSVP Models"""
from app.api.v1.utils.utilities import Helpers


class RsvpModels(Helpers):
    """Class for RSVP operations"""
    rsvps = {}

    def __init__(self, meetupId, userId):
        """Initialize the rsvps models"""
        self.rsvpId = len(RsvpModels.rsvps)+1
        self.meetupId = meetupId
        self.userId = userId
        self.response = "Yes"

    def save(self):
        """method to post rsvp"""
        data = dict(
            rsvpId=self.rsvpId,
            meetupId=self.meetupId,
            userId=self.userId,
            response=self.response
        )
        self.rsvps.update({self.rsvpId: data})
