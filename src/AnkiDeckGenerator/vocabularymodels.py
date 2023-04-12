from anki.models import SymmetricVocabularyNoteModel
from anki.decks import NoteModel


def frasch_from_german() -> NoteModel:
    return SymmetricVocabularyNoteModel(
        id = 1607392319,  # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
        alternatives_description = 'uk',
        examples_description_target = 'Baispal(e)',
        examples_description_base = 'Beispiel(e)'
    )


def frasch_from_english() -> NoteModel:
    return SymmetricVocabularyNoteModel(
        id = 1607392320,  # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
        alternatives_description = 'uk',
        examples_description_target = 'Baispal(e)',
        examples_description_base = 'Example(s)'
    )


def halifreesk_from_german() -> NoteModel:
    return SymmetricVocabularyNoteModel(
        id = 1607392321,  # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
        alternatives_description = 'ok',
        examples_description_target = 'Baispal(e)',
        examples_description_base = 'Beispiel(e)'
    )


def halifreesk_from_english() -> NoteModel:
    return SymmetricVocabularyNoteModel(
        id = 1607392322,  # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
        alternatives_description = 'ok',
        examples_description_target = 'Baispal(e)',
        examples_description_base = 'Example(s)'
    )
