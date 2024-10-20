import unittest
from clinic.patient_record import PatientRecord


class PatientRecordTest(unittest.TestCase):
    def setUp(self):
        """
        Set up a new PatientRecord instance for each test.
        """
        self.record = PatientRecord()

    def test_add_note(self):
        """
        Test that a note can be added to the patient record.
        """
        note = self.record.add_note("First visit")
        self.assertEqual(len(self.record.notes), 1)
        self.assertEqual(note.details, "First visit")

    def test_delete_note(self):
        """
        Test that a note can be deleted from the patient record.
        """
        note = self.record.add_note("First visit")
        self.assertTrue(self.record.delete_note(note.code))
        self.assertEqual(len(self.record.notes), 0)

    def test_update_note(self):
        """
        Test that a note can be updated in the patient record.
        """
        note = self.record.add_note("First visit")
        updated_note = self.record.update_note(note.code, "Updated visit")
        self.assertEqual(updated_note.details, "Updated visit")
        self.assertNotEqual(updated_note.timestamp, note.timestamp)

    def test_get_notes_by_text(self):
        """
        Test retrieving notes by matching text.
        """
        self.record.add_note("First visit")
        self.record.add_note("Second visit")
        notes = self.record.get_notes_by_text("visit")
        self.assertEqual(len(notes), 2)

    def test_get_all_notes(self):
        """
        Test that all notes can be retrieved, sorted by timestamp.
        """
        self.record.add_note("First visit")
        self.record.add_note("Second visit")
        notes = self.record.get_all_notes()
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].details, "Second visit")  # The most recent one

if __name__ == "__main__":
    unittest.main()
