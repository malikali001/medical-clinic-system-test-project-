import unittest
from clinic.patient import Patient


class PatientTest(unittest.TestCase):
    def setUp(self):
        self.patient = Patient("12345", "John Doe", {"age": 30})

    def test_str(self):
        self.assertEqual(str(self.patient), "Patient(PHN=12345, Name=John Doe)")

    def test_update(self):
        self.patient.update({"age": 31})
        self.assertEqual(self.patient.other_data["age"], 31)


if __name__ == "__main__":
    unittest.main()
