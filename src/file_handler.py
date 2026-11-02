from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, source_file: str):
        self.source_file = source_file
        self.content: str

    @abstractmethod
    def extract_content(self):
        pass
