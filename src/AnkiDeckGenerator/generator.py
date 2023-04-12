from anki.models import SymmetricVocabularyNoteModel, SymmetricVocabularyNoteData
from anki.decks import HomogeneousDeck, NoteModel
from data.pandasdata import PandasVocabularyData, GoogleSpreadSheet


def frasch_from_german_symmetric_model() -> NoteModel:
    return SymmetricVocabularyNoteModel(
        id = 1607392319,  # ID for Anki; generate with: import random; random.randrange(1 << 30, 1 << 31)
        alternatives_description = 'uk',
        examples_description_target = 'Baispal(e)',
        examples_description_base = 'Beispiel(e)'
    )


def create_sprachkurs1_vocabulary_deck():
    source_sheet = GoogleSpreadSheet(
        sheet_id = '1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs'
    )
    column_headings = SymmetricVocabularyNoteData(
        word='Frasch uurd',
        meaning='Tjüsch ouerseeting',
        word_alternatives='Ålternatiiwe',
        word_examples='Frasche baispale',
        translated_examples='Tjüsche baispale'
    )
    laks1_words = PandasVocabularyData(
        source_sheet.get_data_from('FriesischerSprachkurs1Laks1'),
        column_headings
    )
    laks2_words = PandasVocabularyData(
        source_sheet.get_data_from('FriesischerSprachkurs1Laks2'),
        column_headings
    )
    
    deck = HomogeneousDeck(
        id = 2059396110,
        name = 'Friesischer Sprachkurs - Frasch 1',
        model = frasch_from_german_symmetric_model()
    )
    deck.add_notes_from_data(laks1_words)
    deck.add_notes_from_data(laks2_words)
    deck.write_to_file('sprachkurs1-uurde.apkg')


def main():
    create_sprachkurs1_vocabulary_deck()


if __name__ == '__main__':
    main()
