import unittest
from clinic.patient import Patient


class PatientTest(unittest.TestCase):
    def setUp(self):
        """
        Set up a new Patient instance for each test.
        """
        self.patient = Patient("12345", "John Doe", {"age": 30})

    def test_str(self):
        """
        Test the string representation of the Patient instance.
        """
        self.assertEqual(str(self.patient), "Patient(PHN=12345, Name=John Doe)")

    def test_update(self):
        """
        Test updating the patient's other data.
        """
        self.patient.update({"age": 31})
        self.assertEqual(self.patient.other_data["age"], 31)

    def test_add_note(self):
        """
        Test that a note can be added to the patient's record.
        """
        note = self.patient.add_note("First visit")
        self.assertEqual(len(self.patient.record.notes), 1)
        self.assertEqual(note.details, "First visit")

    def test_get_notes_by_text(self):
        """
        Test retrieving notes by matching text from the patient's record.
        """
        self.patient.add_note("First visit")
        self.patient.add_note("Second visit")
        notes = self.patient.get_notes_by_text("visit")
        self.assertEqual(len(notes), 2)

    def test_update_note(self):
        """
        Test updating a note in the patient's record.
        """
        note = self.patient.add_note("First visit")
        updated_note = self.patient.update_note(note.code, "Updated visit")
        self.assertEqual(updated_note.details, "Updated visit")
        self.assertNotEqual(updated_note.timestamp, note.timestamp)

    def test_delete_note(self):
        """
        Test deleting a note from the patient's record.
        """
        note = self.patient.add_note("First visit")
        self.assertTrue(self.patient.delete_note(note.code))
        self.assertEqual(len(self.patient.record.notes), 0)

    def test_get_full_record(self):
        """
        Test retrieving the full record of the patient, which includes all notes.
        """
        self.patient.add_note("First visit")
        self.patient.add_note("Second visit")
        full_record = self.patient.get_full_record()
        self.assertEqual(len(full_record), 2)

if __name__ == "__main__":
    unittest.main()
