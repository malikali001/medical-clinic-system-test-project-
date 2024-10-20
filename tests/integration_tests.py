import unittest
from clinic.controller import Controller


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_login(self):
        self.assertTrue(self.controller.login("admin", "password"))
        self.assertFalse(self.controller.login("admin", "wrongpass"))

    def test_create_patient(self):
        patient = self.controller.create_patient("12345", "John Doe", {"age": 30})
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(len(self.controller.list_all_patients()), 1)

    def test_search_patient(self):
        self.controller.create_patient("12345", "John Doe", {})
        patient = self.controller.search_patient("12345")
        self.assertEqual(patient.name, "John Doe")

    def test_update_patient(self):
        self.controller.create_patient("12345", "John Doe", {})
        updated_patient = self.controller.update_patient("12345", {"age": 31})
        self.assertIsNotNone(updated_patient)

    def test_delete_patient(self):
        self.controller.create_patient("12345", "John Doe", {})
        self.assertTrue(self.controller.delete_patient("12345"))
        self.assertIsNone(self.controller.search_patient("12345"))

    def test_create_note(self):
        self.controller.create_patient("12345", "John Doe", {})
        self.controller.choose_current_patient("12345")
        note = self.controller.create_note_for_current_patient("First visit")
        self.assertIsNotNone(note)

    def test_retrieve_notes_by_text(self):
        self.controller.create_patient("12345", "John Doe", {})
        self.controller.choose_current_patient("12345")
        self.controller.create_note_for_current_patient("First visit")
        notes = self.controller.retrieve_notes_by_text("visit")
        self.assertEqual(len(notes), 1)

    def test_update_note(self):
        self.controller.create_patient("12345", "John Doe", {})
        self.controller.choose_current_patient("12345")
        note = self.controller.create_note_for_current_patient("First visit")
        updated_note = self.controller.update_note(note.code, "Updated visit")
        self.assertEqual(updated_note.details, "Updated visit")

    def test_delete_note(self):
        self.controller.create_patient("12345", "John Doe", {})
        self.controller.choose_current_patient("12345")
        note = self.controller.create_note_for_current_patient("First visit")
        self.assertTrue(self.controller.delete_note(note.code))


if __name__ == "__main__":
    unittest.main()
