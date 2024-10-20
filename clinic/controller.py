from .patient import Patient


class Controller:
    def __init__(self):
        """Initialize the Controller with an empty patient dictionary and no current patient."""
        self.patients = {}
        self.current_patient = None

    def login(self, username, password):
        """
        Authenticate the user with a username and password.

        Args:
            username (str): The username entered by the user.
            password (str): The password entered by the user.

        Returns:
            bool: True if the credentials are correct; otherwise, False.
        """
        if username == "admin" and password == "password":
            return True
        return False

    def logout(self):
        """Log out the current user by clearing the current patient."""
        self.current_patient = None

    def create_patient(self, phn, name, other_data):
        """
        Create a new patient record and store it in the system.

        Args:
            phn (str): The Personal Health Number of the patient.
            name (str): The name of the patient.
            other_data (dict): Other personal data related to the patient.

        Returns:
            Patient: The newly created Patient object.
        """
        patient = Patient(phn, name, other_data)
        self.patients[phn] = patient
        return patient

    def search_patient(self, phn):
        """
        Search for a patient by their Personal Health Number (PHN).

        Args:
            phn (str): The Personal Health Number of the patient to search for.

        Returns:
            Patient or None: The Patient object if found; otherwise, None.
        """
        return self.patients.get(phn)

    def retrieve_patients_by_name(self, name):
        """
        Retrieve a list of patients whose names contain the given substring.

        Args:
            name (str): The substring to search for in patient names.

        Returns:
            list: A list of Patient objects that match the search criteria.
        """
        return [patient for patient in self.patients.values() if name in patient.name]

    def update_patient(self, phn, updated_data):
        """
        Update the details of an existing patient.

        Args:
            phn (str): The Personal Health Number of the patient to update.
            updated_data (dict): The updated data for the patient.

        Returns:
            Patient or None: The updated Patient object if successful; otherwise, None.
        """
        patient = self.patients.get(phn)
        if patient:
            patient.update(updated_data)
            return patient
        return None

    def delete_patient(self, phn):
        """
        Delete a patient record from the system.

        Args:
            phn (str): The Personal Health Number of the patient to delete.

        Returns:
            bool: True if the patient was deleted; otherwise, False.
        """
        if phn in self.patients:
            del self.patients[phn]
            return True
        return False

    def list_all_patients(self):
        """
        List all patients currently stored in the system.

        Returns:
            list: A list of all Patient objects.
        """
        return list(self.patients.values())

    def choose_current_patient(self, phn):
        """
        Set the current patient based on their Personal Health Number (PHN).

        Args:
            phn (str): The Personal Health Number of the patient to set as current.

        Returns:
            Patient or None: The Patient object if found; otherwise, None.
        """
        patient = self.search_patient(phn)
        if patient:
            self.current_patient = patient
            return patient
        return None

    def create_note_for_current_patient(self, details):
        """
        Create a new note for the current patient.

        Args:
            details (str): The details of the note to be added.

        Returns:
            Note or None: The newly created Note object if successful; otherwise, None.
        """
        if self.current_patient:
            return self.current_patient.add_note(details)
        return None

    def retrieve_notes_by_text(self, text):
        """
        Retrieve notes from the current patient's record that contain the specified text.

        Args:
            text (str): The text to search for in the notes.

        Returns:
            list: A list of Note objects that contain the specified text.
        """
        if self.current_patient:
            return self.current_patient.get_notes_by_text(text)
        return []

    def update_note(self, code, details):
        """
        Update a note for the current patient.

        Args:
            code (int): The code of the note to update.
            details (str): The new details for the note.

        Returns:
            Note or None: The updated Note object if successful; otherwise, None.
        """
        if self.current_patient:
            return self.current_patient.update_note(code, details)
        return None

    def delete_note(self, code):
        """
        Delete a note from the current patient's record.

        Args:
            code (int): The code of the note to delete.

        Returns:
            bool: True if the note was deleted; otherwise, False.
        """
        if self.current_patient:
            return self.current_patient.delete_note(code)
        return None

    def list_full_patient_record(self):
        """
        List the full record of the current patient, including all notes.

        Returns:
            list: A list of all notes associated with the current patient.
        """
        if self.current_patient:
            return self.current_patient.get_full_record()
        return []
