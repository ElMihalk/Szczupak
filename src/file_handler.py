from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, source_file: str):
        self.source_file = source_file
        self._content: str

    @abstractmethod
    def extract_content(self):
        pass

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, text):
        self._content = text
