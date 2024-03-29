from anki.models import SymmetricVocabularyNoteData
from anki.decks import HomogeneousDeck
from data.pandasdata import PandasVocabularyData, GoogleSpreadSheet

import vocabularymodels as vocabulary_models
import vocabularydataprocessors as data_processors


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
        data_transform = data_processors.default_processor
    )
    for i in range(1,6):
        partial_data_set = PandasVocabularyData(
            dataframe = source_sheet.get_data_from(f'FriesischerSprachkurs1Laks{i}'),
            column_headings = column_headings
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
        data_transform = data_processors.lenient_processor
    )
    partial_data_set = PandasVocabularyData(
        dataframe = source_sheet.get_data_from(f'FriesischerSprachkurs1Laks1'),
        column_headings = column_headings
    )
    deck.add_notes_from_data(partial_data_set)
    
    deck.write_to_file('languagecourse1-uurde.apkg')


def create_sprachkurs1_vocabulary_deck_halifreesk():
    source_sheet = GoogleSpreadSheet('1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs')
    column_headings = SymmetricVocabularyNoteData(
        word='Halifreesk üürd',
        meaning='Tjüsch ouerseeting',
        word_alternatives='Alternatiawe',
        word_examples='Halifreeske baispale',
        translated_examples='Tjüsche baispale'
    )

    deck = HomogeneousDeck(
        id = 2059396110,
        name = 'Friesischer Sprachkurs - Halifreesk 1',
        model = vocabulary_models.halifreesk_from_german(),
        data_transform = data_processors.lenient_processor
    )
    partial_data_set = PandasVocabularyData(
        dataframe = source_sheet.get_data_from(f'FriesischerSprachkurs1Laks1'),
        column_headings = column_headings
    )
    deck.add_notes_from_data(partial_data_set)
    
    deck.write_to_file('sprachkurs1-üürde.apkg')


def create_sprachkurs_copmlete_vocab_list_german():
    source_sheet = GoogleSpreadSheet('1lAsUOMYPuMcLSXa0jpXXjP4wGskT9OF1Wx2HscxTEmM')
    column_headings = SymmetricVocabularyNoteData(
        word='Frasch uurd',
        meaning='Tjüsch ouerseeting',
        word_alternatives='Ålternatiiwe',
        word_examples='Frasche baispale',
        translated_examples='Tjüsche baispale'
    )

    deck = HomogeneousDeck(
        id = 1659476110,
        name = 'Friesischer Sprachkurs I/II - Alle Vokabeln',
        model = vocabulary_models.frasch_from_german(),
        data_transform = data_processors.default_processor
    )
    partial_data_set = PandasVocabularyData(
        dataframe = source_sheet.get_data_from('Uurdelist'),
        column_headings = column_headings
    )
    deck.add_notes_from_data(partial_data_set)
    
    deck.write_to_file('sprachkurs-vokabelliste.apkg')



def main():
    create_sprachkurs_copmlete_vocab_list_german()
    create_sprachkurs1_vocabulary_deck()
    # create_sprachkurs1_vocabulary_deck_english()
    # create_sprachkurs1_vocabulary_deck_halifreesk()


if __name__ == '__main__':
    main()
