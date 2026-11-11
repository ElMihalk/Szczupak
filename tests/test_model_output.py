from src.llm_client import OllamaClient
from config_files.llm_config import LLMConfig, VocabularyOutput
from src.pdf_handler import PDFHandler
from src.image_handler import ImageHandler
from src.file_handler import collect_files
from pydantic import ValidationError, BaseModel

def follows_schema(raw: str, model: type[BaseModel]) -> bool:
    try:
        model.model_validate_json(raw)
        return True
    except ValidationError:
        return False

class TestModelOutput:

    def test_model_output_format_pdf(self):
        model_conf = LLMConfig(translation_language="Polish")
        ollama_client = OllamaClient(
            system_prompt=model_conf.system_prompt,
            model=model_conf.model,
            schema=model_conf.json_schema,
        )
        for file_path in collect_files(suffix="Example_1.pdf"):
            obj = PDFHandler(file_path)
            obj.extract_content()
            result = ollama_client.transform_pdf_content(obj.content)

        assert follows_schema(result, VocabularyOutput)

    def test_model_output_format_image(self):
        model_conf = LLMConfig(translation_language="Polish")
        ollama_client = OllamaClient(
            system_prompt=model_conf.system_prompt,
            model=model_conf.model,
            schema=model_conf.json_schema,
        )
        for file_path in collect_files(suffix="Example_6.png"):
            obj = ImageHandler(file_path)
            obj.extract_content()
            result = ollama_client.transform_image_content(obj.content)

        assert follows_schema(result, VocabularyOutput)
