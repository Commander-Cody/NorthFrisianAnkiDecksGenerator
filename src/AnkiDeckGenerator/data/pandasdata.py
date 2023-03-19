import pandas
from dataclasses import dataclass
from typing import List

from anki.Models import SymmetricVocabularyNoteData
from interfaces import VocabularyData


@dataclass
class GoogleSpreadSheet:
    sheet_id: str

    def get_url_for(self, sheet_name: str) -> str:
        return f'https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

    def get_data_from(self, sheet_name: str):
        return pandas.read_csv(self.get_url_for(sheet_name))


class PandasVocabularyData(VocabularyData):
    def __init__(self, dataframe) -> None:
        self.df = dataframe
    
    def get_vocabulary_notes_data(self) -> List[SymmetricVocabularyNoteData]:
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
