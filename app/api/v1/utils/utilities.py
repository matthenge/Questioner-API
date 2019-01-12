"""Shared methods"""


class Helpers:
    """Helper methods"""
    def fetch(self, db, id):
        """Fetch one item"""
        for key in db:
            if key == id:
                return db[key]
