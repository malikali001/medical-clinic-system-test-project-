from .patient_record import PatientRecord


class Patient:
    def __init__(self, phn, name, other_data):
        self.phn = phn
        self.name = name
        self.other_data = other_data
        self.record = PatientRecord()

    def update(self, updated_data):
        self.other_data.update(updated_data)

    def add_note(self, details):
        return self.record.add_note(details)

    def get_notes_by_text(self, text):
        return self.record.get_notes_by_text(text)

    def update_note(self, code, details):
        return self.record.update_note(code, details)

    def delete_note(self, code):
        return self.record.delete_note(code)

    def get_full_record(self):
        return self.record.get_all_notes()

    def __str__(self):
        return f"Patient(PHN={self.phn}, Name={self.name})"
