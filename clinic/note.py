from datetime import datetime


class Note:
    def __init__(self, code, details):
        """
        Initialize a new Note with a code, details, and a timestamp.

        Args:
            code (int): The unique code for the note.
            details (str): The details of the note.
        """
        self.code = code
        self.details = details
        self.timestamp = datetime.now()

    def update_timestamp(self):
        """Update the timestamp of the note to the current time."""
        self.timestamp = datetime.now()

    def __str__(self):
        """
        Return a string representation of the Note.

        Returns:
            str: A formatted string containing the code, details, and timestamp of the note.
        """
        return f"Note(Code={self.code}, Details={self.details}, Timestamp={self.timestamp})"
