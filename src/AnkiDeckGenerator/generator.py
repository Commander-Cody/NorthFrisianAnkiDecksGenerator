from anki.models import SymmetricVocabularyNoteData
from anki.decks import HomogeneousDeck
from data.pandasdata import PandasVocabularyData, GoogleSpreadSheet

import vocabularymodels as vocabulary_models


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

    deck = HomogeneousDeck(
        id = 2059396110,
        name = 'Friesischer Sprachkurs - Frasch 1',
        model = vocabulary_models.frasch_from_german()
    )
    for i in range(1,4):
        words_data = PandasVocabularyData(
            source_sheet.get_data_from(f'FriesischerSprachkurs1Laks{i}'),
            column_headings
        )
        deck.add_notes_from_data(words_data)
    deck.write_to_file('sprachkurs1-uurde.apkg')


def main():
    create_sprachkurs1_vocabulary_deck()


if __name__ == '__main__':
    main()
