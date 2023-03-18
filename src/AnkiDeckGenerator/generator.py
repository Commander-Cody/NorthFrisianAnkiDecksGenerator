from AnkiDeckGenerator.anki.Models import SymmetricVocabularyNoteModel
from AnkiDeckGenerator.anki.Decks import HomogeneousDeck
from AnkiDeckGenerator.data.pandasdata import PandasVocabularyData, GoogleSpreadSheet


def main():
    source_sheet = GoogleSpreadSheet(
        sheet_id = '1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs'
    )
    dataframe = PandasVocabularyData(source_sheet.get_data_from('Lesebuch1Laks1'))
    model = SymmetricVocabularyNoteModel()
    deck = HomogeneousDeck(
        id = 2059396110,
        name = 'Frasche uurde',
        model = model
    )
    deck.add_notes(dataframe.get_vocabulary_notes_data())
    deck.write_to_file('vocabulary.apkg')


if __name__ == '__main__':
    main()
