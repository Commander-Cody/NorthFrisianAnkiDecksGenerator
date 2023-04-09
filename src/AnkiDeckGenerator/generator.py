from anki.Models import SymmetricVocabularyNoteModel, SymmetricVocabularyNoteData
from anki.Decks import HomogeneousDeck
from data.pandasdata import PandasVocabularyData, GoogleSpreadSheet


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
        model = SymmetricVocabularyNoteModel(
            alternatives_description = 'uk',
            examples_description_target = 'Baispal(e)',
            examples_description_base = 'Beispiel(e)'
        )
    )
    deck.add_notes_from_data(laks1_words)
    deck.add_notes_from_data(laks2_words)
    deck.write_to_file('sprachkurs1-uurde.apkg')


def main():
    create_sprachkurs1_vocabulary_deck()


if __name__ == '__main__':
    main()
