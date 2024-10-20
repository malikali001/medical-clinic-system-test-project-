import unittest
from clinic.note import Note


class NoteTest(unittest.TestCase):
    def setUp(self):
        """
        Set up a new Note instance for each test.
        """
        self.note = Note(1, "First visit")

    def test_str(self):
        """
        Test the string representation of the Note.
        """
        self.assertIn("First visit", str(self.note))

    def test_update_timestamp(self):
        """
        Test that the timestamp updates correctly when the note is modified.
        """
        old_timestamp = self.note.timestamp
        self.note.update_timestamp()
        self.assertNotEqual(old_timestamp, self.note.timestamp)


if __name__ == "__main__":
    unittest.main()
