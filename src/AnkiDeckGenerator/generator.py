from anki.models import SymmetricVocabularyNoteData
from anki.decks import HomogeneousDeck
from data.pandasdata import PandasVocabularyData, GoogleSpreadSheet

import vocabularymodels as vocabulary_models
from vocabularydataprocessors import default_processor, lenient_processor


def create_sprachkurs1_vocabulary_deck():
    source_sheet = GoogleSpreadSheet('1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs')
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
        model = vocabulary_models.frasch_from_german(),
        data_transform = default_processor
    )
    for i in range(1,4):
        partial_data_set = PandasVocabularyData(
            source_sheet.get_data_from(f'FriesischerSprachkurs1Laks{i}'),
            column_headings
        )
        deck.add_notes_from_data(partial_data_set)
    
    deck.write_to_file('sprachkurs1-uurde.apkg')


def create_sprachkurs1_vocabulary_deck_english():
    source_sheet = GoogleSpreadSheet('1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs')
    column_headings = SymmetricVocabularyNoteData(
        word='Frasch uurd',
        meaning='Änglisch ouerseeting',
        word_alternatives='Ålternatiiwe',
        word_examples='Frasche baispale',
        translated_examples='Änglische baispale'
    )

    deck = HomogeneousDeck(
        id = 2059396110,
        name = 'Frisian language course - Frasch 1',
        model = vocabulary_models.frasch_from_english(),
        data_transform = lenient_processor
    )
    partial_data_set = PandasVocabularyData(
        source_sheet.get_data_from(f'FriesischerSprachkurs1Laks1'),
        column_headings
    )
    deck.add_notes_from_data(partial_data_set)
    
    deck.write_to_file('languagecourse1-uurde.apkg')


def main():
    # create_sprachkurs1_vocabulary_deck()
    create_sprachkurs1_vocabulary_deck_english()


if __name__ == '__main__':
    main()
