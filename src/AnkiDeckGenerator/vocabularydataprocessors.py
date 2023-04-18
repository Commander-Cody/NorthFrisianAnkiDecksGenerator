from anki.models import SymmetricVocabularyNoteData


def default_processor(note_data: SymmetricVocabularyNoteData):
    if not note_data.word.strip() and not note_data.meaning.strip():
        return None
    if note_data.translated_examples.strip() and not note_data.word_examples.strip():
        raise ValueError(f'Data for {note_data.word} has a translated example but no actual examples.')
    return note_data


def lenient_processor(note_data: SymmetricVocabularyNoteData):
    if not note_data.word.strip() or not note_data.meaning.strip():
        return None
    if not note_data.word_examples.strip():
        note_data.translated_examples = ''
    return note_data
