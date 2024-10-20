import unittest
from clinic.patient_record import PatientRecord


class PatientRecordTest(unittest.TestCase):
    def setUp(self):
        self.record = PatientRecord()

    def test_add_note(self):
        note = self.record.add_note("First visit")
        self.assertEqual(len(self.record.notes), 1)

    def test_delete_note(self):
        note = self.record.add_note("First visit")
        self.assertTrue
