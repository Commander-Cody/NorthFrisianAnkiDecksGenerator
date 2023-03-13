import genanki
# import yaml

from dataclasses import dataclass
from abc import ABC, abstractmethod


class NoteModel(ABC):
    @abstractmethod
    def create_note(self, note) -> genanki.Note:
        pass


@dataclass
class SymmetricVocabularyNoteData:
    """Data corresponding to SymmetricVocabularyNoteModel"""
    word: str
    meaning: str
    word_alternatives: str
    word_examples: str
    translated_examples: str


class SymmetricVocabularyNoteModel(NoteModel):
    """Symmetric model for creating vocabulary notes, 
    i.e. each data set also generates a note with 'word' and 'meaning' reversed"""
    def __init__(self) -> None:
        self.model = self._create_anki_model()
    
    def create_note(self, note: SymmetricVocabularyNoteData):
        if not note.word.strip() or not note.meaning.strip():
            raise ValueError(f"The combination of word '{note.word}' and meaning '{note.meaning}' is not allowed.")
        
        return genanki.Note(
            model = self.model,
            fields = [
                note.word, 
                note.meaning,
                note.word_alternatives,
                note.word_examples, 
                note.translated_examples
            ],
            guid = genanki.guid_for(note.word)
        )
    
    def _create_anki_model(self):
        target_language_id = 'word'
        base_language_id = 'meaning'
        alternatives_id = 'alternatives'
        target_language_examples_id = 'word_example'
        base_language_examples_id = 'example_translation'
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
                {'name': target_language_id},
                {'name': base_language_id},
                {'name': alternatives_id},
                {'name': target_language_examples_id},
                {'name': base_language_examples_id}
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{' + target_language_id + '}} (uk: {{' + alternatives_id + '}})<br><br>Baispal(e): {{' + target_language_examples_id + '}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{' + base_language_id + '}}<br><br>Beispiel(e): {{' + base_language_examples_id + '}}'
                },
                {
                    'name': 'Card 2',
                    'qfmt': '{{' + base_language_id + '}}<br><br>Beispiel(e): {{' + base_language_examples_id + '}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{' + target_language_id + '}} (uk: {{' + alternatives_id + '}})<br><br>Baispal(e): {{' + target_language_examples_id + '}}'
                }
            ],
            css=note_css
        )