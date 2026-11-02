import ollama
from config_files.llm_config import system_prompt


class OllamaClient:
    def __init__(self, model: str = "gemma4:e4b", translation_language: str = "Polish"):
        self.model = model
        self.system_prompt = system_prompt

    def transform_pdf_content(self):
        result = ollama.generate(model=self.model, prompt="Why is the sky blue?")
        print(result["response"])
