from src.llm_client import OllamaClient
from config_files.llm_config import LLMConfig, VocabularyOutput
from src.pdf_handler import PDFHandler
from src.image_handler import ImageHandler
from pathlib import Path


def collect_files(suffix: str = ".pdf"):
    return Path("./source_files").glob(f"**/*{suffix}")


if __name__ == "__main__":
    model_conf = LLMConfig(translation_language="Polish")
    ollama_client = OllamaClient(
        system_prompt=model_conf.system_prompt,
        model=model_conf.model,
        schema=model_conf.json_schema,
    )

    for file_path in collect_files(suffix=".png"):
        print(f"File name: {file_path}")
        obj = ImageHandler(file_path)
        obj.extract_content()
        ollama_client.transform_image_content(obj.content)

    for file_path in collect_files(suffix=".pdf"):
        print(f"File name: {file_path}")
        obj = PDFHandler(file_path)
        obj.extract_content()
        ollama_client.transform_pdf_content(obj.content)
