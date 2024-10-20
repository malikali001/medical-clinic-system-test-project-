from datetime import datetime


class Note:
    def __init__(self, code, details):
        self.code = code
        self.details = details
        self.timestamp = datetime.now()

    def update_timestamp(self):
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Note(Code={self.code}, Details={self.details}, Timestamp={self.timestamp})"
