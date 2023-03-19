from anki.Models import SymmetricVocabularyNoteModel
from anki.Decks import HomogeneousDeck
from data.pandasdata import PandasVocabularyData, GoogleSpreadSheet


def create_sprachkurs1_vocabulary_deck():
    source_sheet = GoogleSpreadSheet(
        sheet_id = '1WThbHIfG1n0XsOx5lN47h0GI-EluMkFzc_h72JpsWLs'
    )
    laks1_words = PandasVocabularyData(
        source_sheet.get_data_from('FriesischerSprachkurs1Laks1')
    )
    laks2_words = PandasVocabularyData(
        source_sheet.get_data_from('FriesischerSprachkurs1Laks2')
    )
    deck = HomogeneousDeck(
        id = 2059396110,
        name = 'Friesischer Sprachkurs Frasch 1',
        model = SymmetricVocabularyNoteModel()
    )
    deck.add_notes_from_data(laks1_words)
    deck.add_notes_from_data(laks2_words)
    deck.write_to_file('sprachkurs1-uurde.apkg')


def main():
    create_sprachkurs1_vocabulary_deck()


if __name__ == '__main__':
    main()
