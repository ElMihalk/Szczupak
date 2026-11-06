from src.llm_client import OllamaClient
from config_files.llm_config import LLMConfig, VocabularyOutput
from src.pdf_handler import PDFHandler
from pathlib import Path


def collect_files(suffix: str = ".pdf"):
    return Path("./source_files").glob(f"**/*{suffix}")


if __name__ == "__main__":
    model_conf = LLMConfig()
    ollama_client = OllamaClient()
    
    for file_path in collect_files(suffix=".pdf"):
        obj = PDFHandler(file_path)
        obj.extract_content()
        ollama_client.transform_pdf_content(obj.content)
