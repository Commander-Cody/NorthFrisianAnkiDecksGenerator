import pandas
from dataclasses import dataclass
from typing import List

from anki.Models import SymmetricVocabularyNoteData
from anki.Decks import AnkiNotesData


@dataclass
class GoogleSpreadSheet:
    sheet_id: str

    def get_url_for(self, sheet_name: str) -> str:
        return f'https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

    def get_data_from(self, sheet_name: str):
        return pandas.read_csv(self.get_url_for(sheet_name))


class PandasVocabularyData(AnkiNotesData):
    def __init__(self, dataframe, column_headings: SymmetricVocabularyNoteData) -> None:
        self.df = dataframe
        self.column_headings = column_headings
    
    def get_notes_data(self) -> List[SymmetricVocabularyNoteData]:
        result = []
        for ind in self.df.index:
            row = PandasVocabularyDataRow(self.df, ind, self.column_headings)
            result.append(row.get_vocabulary_note_data())
        return result


class PandasVocabularyDataRow:
    def __init__(self, dataframe, index, column_headings: SymmetricVocabularyNoteData) -> None:
        self.dataframe = dataframe
        self.index = index
        self.column_headings = column_headings
    
    def get_vocabulary_note_data(self):
        return SymmetricVocabularyNoteData(
            word = self.get_column(self.column_headings.word),
            meaning = self.get_column(self.column_headings.meaning),
            word_alternatives = self.get_column(self.column_headings.word_alternatives),
            word_examples = self.get_column(self.column_headings.word_examples),
            translated_examples = self.get_column(self.column_headings.translated_examples),
        )
    
    def get_column(self, name) -> str:
        cell_value = self.dataframe[name][self.index]
        return '' if pandas.isna(cell_value) else cell_value
