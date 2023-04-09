from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

AnkiNoteData = TypeVar('AnkiNoteData')

class AnkiNotesData(ABC, Generic[AnkiNoteData]):
    @abstractmethod
    def get_notes_data(self) -> List[AnkiNoteData]:
        pass