import genanki
from dataclasses import dataclass
from abc import ABC, abstractmethod
# import yaml


class NoteModel(ABC):
    @abstractmethod
    def create_note(self, note) -> genanki.Note:
        pass


class HomogeneousDeck:
    """Homogeneous Deck, i.e. all notes are assumed to follow the same model"""
    def __init__(self, id: int, name: str, model: NoteModel) -> None:
        self.deck = genanki.Deck(id, name)
        self.model = model
        self.notes = []
    
    def add_note(self, note):
        self.deck.add_note(self.model.create_note(note))

    def write_to_file(self, file_name: str):
        self.deck.write_to_file(file_name)


@dataclass
class SymmetricVocabularyNoteData:
    """Data corresponding to SymmetricVocabularyNoteModel"""
    word: str
    meaning: str


class SymmetricVocabularyNoteModel(NoteModel):
    """Symmetric model for creating vocabulary notes, 
    i.e. each data set also generates a note with 'word' and 'meaning' reversed"""
    def __init__(self) -> None:
        self.model = self._create_anki_model()
    
    def create_note(self, note: SymmetricVocabularyNoteData):
        return genanki.Note(
            model = self.model,
            fields = [note.word, note.meaning]
        )
    
    def _create_anki_model(self):
        target_language = 'Mooring'
        base_language = 'Deutsch'
        note_css = """.card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        """

        return genanki.Model(
            1607392319, # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
            'Vocabulary Model',
            fields=[
                {'name': target_language},
                {'name': base_language}
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{' + target_language + '}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{' + base_language + '}}'
                },
                {
                    'name': 'Card 2',
                    'qfmt': '{{' + base_language + '}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{' + target_language + '}}'
                }
            ],
            css=note_css
        )


def main():
    model = SymmetricVocabularyNoteModel()
    deck = HomogeneousDeck(2059396110, 'Frasche uurde', model)
    deck.add_note(SymmetricVocabularyNoteData(
        word = 'Risem',
        meaning = 'Risum'
    ))
    deck.write_to_file('vocabulary.apkg')

if __name__ == '__main__':
    main()
