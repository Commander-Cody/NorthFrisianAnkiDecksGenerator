from anki.Models import SymmetricVocabularyNoteData, SymmetricVocabularyNoteModel
from anki.Decks import HomogeneousDeck



def main():
    model = SymmetricVocabularyNoteModel()
    deck = HomogeneousDeck(2059396110, 'Frasche uurde', model)
    deck.add_note(SymmetricVocabularyNoteData(
        word = 'Risem',
        meaning = 'Risum',
        word_examples = 'e Risem Moore',
        translated_examples = 'das Risum Moor'
    ))
    deck.write_to_file('vocabulary.apkg')


if __name__ == '__main__':
    main()
