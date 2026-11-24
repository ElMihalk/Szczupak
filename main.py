from src.llm_client import OllamaClient
from config_files.llm_config import LLMConfig, VocabularyOutput
from src.pdf_handler import PDFHandler
from src.image_handler import ImageHandler
from src.file_handler import collect_files
from src.output_handler import OutputHandler

if __name__ == "__main__":
    model_conf = LLMConfig(translation_language="Polish")
    ollama_client = OllamaClient(
        system_prompt=model_conf.system_prompt,
        model=model_conf.model,
        schema=model_conf.json_schema,
    )

    for file_path in collect_files(suffix="Example_9.png"):
        print(f"File name: {file_path}")
        obj = ImageHandler(file_path)
        obj.extract_content()
        result=ollama_client.transform_image_content(obj.content)
        OutputHandler.create_tsv(result, filename=file_path.stem)

    # for file_path in collect_files(suffix="Example_2.pdf"):
    #     print(f"File name: {file_path}")
    #     obj = PDFHandler(file_path)
    #     obj.extract_content()
    #     result = ollama_client.transform_pdf_content(obj.content)
    #     OutputHandler.create_tsv(result, filename=file_path.stem)