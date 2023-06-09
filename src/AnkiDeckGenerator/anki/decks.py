import genanki
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List


AnkiNoteData = TypeVar('AnkiNoteData')

class AnkiNotesData(ABC, Generic[AnkiNoteData]):
    @abstractmethod
    def get_notes_data(self) -> List[AnkiNoteData]:
        pass


class NoteModel(ABC, Generic[AnkiNoteData]):
    @abstractmethod
    def create_note(self, note: AnkiNoteData) -> genanki.Note:
        pass


class HomogeneousDeck(Generic[AnkiNoteData]):
    """Homogeneous Deck, i.e. all notes are assumed to follow the same model"""
    def __init__(self, id: int, name: str, model: NoteModel[AnkiNoteData], data_transform = lambda x : x) -> None:
        self.deck = genanki.Deck(id, name)
        self.model = model
        self.notes = []
        self.data_transform = data_transform

    def add_note(self, note_data: AnkiNoteData):
        prepared_data = self.data_transform(note_data)
        if not prepared_data is None:
            self.deck.add_note(self.model.create_note(note_data))

    def add_notes(self, notes: List[AnkiNoteData]):
        for note in notes:
            self.add_note(note)
    
    def add_notes_from_data(self, data: AnkiNotesData):
        self.add_notes(data.get_notes_data())

    def write_to_file(self, file_name: str):
        self.deck.write_to_file(file_name)
