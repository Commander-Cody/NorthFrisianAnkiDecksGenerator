from dataclasses import dataclass

import genanki
# import yaml

import dominate.tags as tags
from dominate.util import text

from anki.decks import NoteModel
from anki.htmlutils import var


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

    note_css = """
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        .hidden {
            display: none;
        }
        .additional_info {
            font-size: 0.8em;
        }"""
    
    def __init__(self, id, alternatives_description, examples_description_target, examples_description_base) -> None:
        self.id = id
        self.alternatives_description = alternatives_description
        self.examples_description_target = examples_description_target
        self.examples_description_base = examples_description_base
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
            self.id,
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
        root = tags.div()
        with root:
            text(var(self.target_language_id))
            with tags.span():
                tags.attr(cls=var(self.alternatives_hidden_attribute_id) + ' additional_info')
                tags.br()
                tags.br()
                text(' (' + self.alternatives_description + ': ' + var(self.alternatives_id) + ')')
            tags.br()
            tags.br()
            with tags.span():
                tags.attr(cls=var(self.examples_hidden_attribute_id) + ' additional_info')
                text(self.examples_description_target + ': ' + var(self.target_language_examples_id))
        return root.render()
    
    def _create_base_language_info(self) -> str:
        root = tags.div()
        with root:
            text(var(self.base_language_id))
            tags.br()
            tags.br()
            with tags.span():
                tags.attr(cls=var(self.examples_hidden_attribute_id) + ' additional_info')
                text(self.examples_description_base + ': ' + var(self.base_language_examples_id))
        return root.render()
