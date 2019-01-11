"""Shared methods"""


class Helpers:
    """Helper methods"""
    def fetch(self, db, id):
        """Fetch one question"""
        for key in db:
            if key == id:
                return db[key]
