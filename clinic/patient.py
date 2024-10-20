from .patient_record import PatientRecord


class Patient:
    def __init__(self, phn, name, other_data):
        """
        Initialize a new Patient with a Personal Health Number (PHN), name, and additional data.

        Args:
            phn (str): The Personal Health Number of the patient.
            name (str): The name of the patient.
            other_data (dict): Additional information about the patient.
        """
        self.phn = phn
        self.name = name
        self.other_data = other_data
        self.record = PatientRecord()

    def update(self, updated_data):
        """
        Update the patient's other data with the provided information.

        Args:
            updated_data (dict): A dictionary of updated patient data.
        """
        self.other_data.update(updated_data)

    def add_note(self, details):
        """
        Add a new note to the patient's record.

        Args:
            details (str): The details of the note to be added.

        Returns:
            Note: The newly created Note object.
        """
        return self.record.add_note(details)

    def get_notes_by_text(self, text):
        """
        Retrieve all notes from the patient's record that contain the specified text.

        Args:
            text (str): The text to search for in the note details.

        Returns:
            list: A list of Note objects that contain the specified text in their details.
        """
        return self.record.get_notes_by_text(text)

    def update_note(self, code, details):
        """
        Update the details of an existing note identified by its code.

        Args:
            code (int): The code of the note to be updated.
            details (str): The new details for the note.

        Returns:
            Note or None: The updated Note object if found, otherwise None.
        """
        return self.record.update_note(code, details)

    def delete_note(self, code):
        """
        Delete a note from the patient's record identified by its code.

        Args:
            code (int): The code of the note to be deleted.

        Returns:
            bool: True if the note was successfully deleted, otherwise False.
        """
        return self.record.delete_note(code)

    def get_full_record(self):
        """
        Retrieve the full record of notes for the patient.

        Returns:
            list: A list of Note objects in the patient's record, sorted by timestamp.
        """
        return self.record.get_all_notes()

    def __str__(self):
        """
        Return a string representation of the Patient.

        Returns:
            str: A formatted string containing the patient's PHN and name.
        """
        return f"Patient(PHN={self.phn}, Name={self.name})"
