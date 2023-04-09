import genanki

from anki.Models import NoteModel
from interfaces import AnkiNotesData


class HomogeneousDeck:
    """Homogeneous Deck, i.e. all notes are assumed to follow the same model"""
    def __init__(self, id: int, name: str, model: NoteModel) -> None:  # NoteModel[NoteType]
        self.deck = genanki.Deck(id, name)
        self.model = model
        self.notes = []

    def add_note(self, note):  # NoteType
        self.deck.add_note(self.model.create_note(note))

    def add_notes(self, notes: list):  # list[NoteType]
        for note in notes:
            self.add_note(note)
    
    def add_notes_from_data(self, data: AnkiNotesData):
        self.add_notes(data.get_notes_data())

    def write_to_file(self, file_name: str):
        self.deck.write_to_file(file_name)