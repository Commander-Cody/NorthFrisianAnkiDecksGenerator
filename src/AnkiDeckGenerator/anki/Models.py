import genanki
# import yaml
from abc import ABC, abstractmethod
from dataclasses import dataclass

from anki.htmlutils import var


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
    
    target_language_id = 'word'
    base_language_id = 'meaning'
    alternatives_id = 'alternatives'
    alternatives_hidden_attribute_id = 'alternatives_hidden_attribute'
    target_language_examples_id = 'word_example'
    base_language_examples_id = 'example_translation'
    examples_hidden_attribute_id = 'examples_hidden_attribute'

    note_css = """.card {
        font-family: arial;
        font-size: 20px;
        text-align: center;
        color: black;
        background-color: white;
    }
    """
    
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
                self._hidden_if_blank(note.word_alternatives),
                note.word_examples,
                note.translated_examples,
                self._hidden_if_blank(note.word_examples)
            ],
            guid = genanki.guid_for(note.word)
        )
    
    def _hidden_if_blank(self, string: str):
        return "" if string.strip() else " hidden"
    
    def _create_anki_model(self):
        card_front = '{{FrontSide}}<hr id="answer">'

        return genanki.Model(
            1607392319,  # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
            'Vocabulary Model',
            fields=[
                {'name': self.target_language_id},
                {'name': self.base_language_id},
                {'name': self.alternatives_id},
                {'name': self.alternatives_hidden_attribute_id},
                {'name': self.target_language_examples_id},
                {'name': self.base_language_examples_id},
                {'name': self.examples_hidden_attribute_id}
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': self._create_target_language_info(),
                    'afmt': card_front + self._create_base_language_info()
                },
                {
                    'name': 'Card 2',
                    'qfmt': self._create_base_language_info(),
                    'afmt': card_front + self._create_target_language_info()
                }
            ],
            css=self.note_css
        )
    
    def _create_target_language_info(self) -> str:
        return var(self.target_language_id) + '<span ' + var(self.alternatives_hidden_attribute_id) + '> (uk: ' + var(self.alternatives_id) + ')</span><br><br><span ' + var(self.examples_hidden_attribute_id) + '>Baispal(e): ' + var(self.target_language_examples_id) + '</span>'
    
    def _create_base_language_info(self) -> str:
        return var(self.base_language_id) + '<br><br><span ' + var(self.examples_hidden_attribute_id) + '>Beispiel(e): ' + var(self.base_language_examples_id) + '</span>'