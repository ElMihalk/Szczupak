from src.file_handler import FileHandler
import pypdf


class PDFHandler(FileHandler):

    def extract_content(self) -> None:
        try:
            with open(self.source_file, "rb") as file:
                text = ""
                reader = pypdf.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            self.content = text
        except FileNotFoundError:
            print("Error: PDF file not found.")
