import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

from anki.Models import SymmetricVocabularyNoteData

class AnkiDeckDefinitionSheet:
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/drive'
    ]
    key_file = "north-frisian-anki-deck-78eb15aad07e.json"

    def __init__(self, name) -> None:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key_file, self.scopes)
        file = gspread.authorize(credentials)
        self.workbook = file.open(name)

    def get_vocabulary_notes_data(self):
        sheet = self.workbook.sheet1
        # print(sheet.acell('A1').value)
        return [SymmetricVocabularyNoteData(
            word = sheet.acell('A2').value,
            meaning = sheet.acell('B2').value,
            word_examples = '',
            translated_examples = ''
        )]