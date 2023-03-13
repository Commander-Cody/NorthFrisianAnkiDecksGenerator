from anki.Models import SymmetricVocabularyNoteModel
from anki.Decks import HomogeneousDeck
from anki.pandasdata import PandasVocabularyGoogleSheet, GoogleSheet


def main():
    source_sheet = GoogleSheet(
        sheet_id = '1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs',
        sheet_name = 'FrascheUurde'
    )
    dataframe = PandasVocabularyGoogleSheet(source_sheet)
    model = SymmetricVocabularyNoteModel()
    deck = HomogeneousDeck(2059396110, 'Frasche uurde', model)
    deck.add_notes(dataframe.get_vocabulary_notes_data())
    deck.write_to_file('vocabulary.apkg')


if __name__ == '__main__':
    main()
