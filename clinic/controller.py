from .patient import Patient


class Controller:
    def __init__(self):
        self.patients = {}
        self.current_patient = None

    def login(self, username, password):
        if username == "admin" and password == "password":
            return True
        return False

    def logout(self):
        self.current_patient = None

    def create_patient(self, phn, name, other_data):
        patient = Patient(phn, name, other_data)
        self.patients[phn] = patient
        return patient

    def search_patient(self, phn):
        return self.patients.get(phn)

    def retrieve_patients_by_name(self, name):
        return [patient for patient in self.patients.values() if name in patient.name]

    def update_patient(self, phn, updated_data):
        patient = self.patients.get(phn)
        if patient:
            patient.update(updated_data)
            return patient
        return None

    def delete_patient(self, phn):
        if phn in self.patients:
            del self.patients[phn]
            return True
        return False

    def list_all_patients(self):
        return list(self.patients.values())

    def choose_current_patient(self, phn):
        patient = self.search_patient(phn)
        if patient:
            self.current_patient = patient
            return patient
        return None

    def create_note_for_current_patient(self, details):
        if self.current_patient:
            return self.current_patient.add_note(details)
        return None

    def retrieve_notes_by_text(self, text):
        if self.current_patient:
            return self.current_patient.get_notes_by_text(text)
        return []

    def update_note(self, code, details):
        if self.current_patient:
            return self.current_patient.update_note(code, details)
        return None

    def delete_note(self, code):
        if self.current_patient:
            return self.current_patient.delete_note(code)
        return None

    def list_full_patient_record(self):
        if self.current_patient:
            return self.current_patient.get_full_record()
        return []
