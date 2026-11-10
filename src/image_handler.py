from src.file_handler import FileHandler


class ImageHandler(FileHandler):

    def extract_content(self):
        self.content = self.source_file
