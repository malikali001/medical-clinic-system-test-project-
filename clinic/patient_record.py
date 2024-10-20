from .note import Note


class PatientRecord:
    def __init__(self):
        self.notes = []

    def add_note(self, details):
        code = len(self.notes) + 1
        note = Note(code, details)
        self.notes.append(note)
        return note

    def get_notes_by_text(self, text):
        return [note for note in self.notes if text in note.details]

    def update_note(self, code, details):
        for note in self.notes:
            if note.code == code:
                note.details = details
                note.update_timestamp()
                return note
        return None

    def delete_note(self, code):
        for i, note in enumerate(self.notes):
            if note.code == code:
                del self.notes[i]
                return True
        return False

    def get_all_notes(self):
        return sorted(self.notes, key=lambda note: note.timestamp, reverse=True)
