from abc import ABC, abstractmethod

class VocabularyData(ABC):
    @abstractmethod
    def get_vocabulary_notes_data(self) -> list:  # list[NoteType]
        pass