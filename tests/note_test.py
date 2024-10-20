import unittest
from clinic.note import Note


class NoteTest(unittest.TestCase):
    def setUp(self):
        self.note = Note(1, "First visit")

    def test_str(self):
        self.assertIn("First visit", str(self.note))

    def test_update_timestamp(self):
        old_timestamp = self.note.timestamp
        self.note.update_timestamp()
        self.assertNotEqual(old_timestamp, self.note.timestamp)


if __name__ == "__main__":
    unittest.main()
