from .note import Note


class PatientRecord:
    def __init__(self):
        """Initialize a new PatientRecord with an empty list of notes."""
        self.notes = []

    def add_note(self, details):
        """
        Add a new note to the patient record.

        Args:
            details (str): The details of the note to be added.

        Returns:
            Note: The newly created Note object.
        """
        code = len(self.notes) + 1
        note = Note(code, details)
        self.notes.append(note)
        return note

    def get_notes_by_text(self, text):
        """
        Retrieve all notes containing the specified text.

        Args:
            text (str): The text to search for in the note details.

        Returns:
            list: A list of Note objects that contain the specified text in their details.
        """
        return [note for note in self.notes if text in note.details]

    def update_note(self, code, details):
        """
        Update the details of an existing note identified by its code.

        Args:
            code (int): The code of the note to be updated.
            details (str): The new details for the note.

        Returns:
            Note or None: The updated Note object if found, otherwise None.
        """
        for note in self.notes:
            if note.code == code:
                note.details = details
                note.update_timestamp()
                return note
        return None

    def delete_note(self, code):
        """
        Delete a note from the patient record identified by its code.

        Args:
            code (int): The code of the note to be deleted.

        Returns:
            bool: True if the note was successfully deleted, otherwise False.
        """
        for i, note in enumerate(self.notes):
            if note.code == code:
                del self.notes[i]
                return True
        return False

    def get_all_notes(self):
        """
        Retrieve all notes in the patient record sorted by timestamp.

        Returns:
            list: A list of Note objects sorted in descending order by their timestamp.
        """
        return sorted(self.notes, key=lambda note: note.timestamp, reverse=True)
