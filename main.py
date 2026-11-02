from src.llm_client import OllamaClient
from pathlib import Path


def collect_files(suffix: str = ".pdf"):
    return Path("./source_files").glob(f"**/*{suffix}")


if __name__ == "__main__":
    # ollama_client = OllamaClient()
    # ollama_client.transform_pdf_content()
    print(list(collect_files(suffix=".pdf")))
