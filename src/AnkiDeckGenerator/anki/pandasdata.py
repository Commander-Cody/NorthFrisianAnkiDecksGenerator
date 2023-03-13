import pandas
from dataclasses import dataclass

from anki.Models import SymmetricVocabularyNoteData


@dataclass
class GoogleSheet:
    sheet_id: str
    sheet_name: str

    def get_url(self) -> str:
        return f'https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.sheet_name}'


class PandasVocabularyGoogleSheet:

    def __init__(self, sheet: GoogleSheet) -> None:
        url = sheet.get_url()
        self.df = pandas.read_csv(url)
    
    def get_vocabulary_notes_data(self):
        result = []
        for ind in self.df.index:
            row = PandasVocabularyGoogleSheetRow(self.df, ind)
            result.append(row.get_vocabulary_note_data())
        return result


class PandasVocabularyGoogleSheetRow:
    def __init__(self, dataframe, index) -> None:
        self.dataframe = dataframe
        self.index = index
    
    def get_vocabulary_note_data(self):
        return SymmetricVocabularyNoteData(
            word = self.get_column('Frasch uurd'),
            meaning = self.get_column('Tjüsch ouerseeting'),
            word_alternatives = self.get_column('Ålternatiiwe'),
            word_examples = self.get_column('Frasche baispale'),
            translated_examples = self.get_column('Tjüsche baispale'),
        )
    
    def get_column(self, name) -> str:
        cell_value = self.dataframe[name][self.index]
        return '' if pandas.isna(cell_value) else cell_value
