import ollama


class OllamaClient:
    def __init__(
        self, model: str = "gemma4:e4b", system_prompt: str = "", schema: dict = dict()
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.schema = schema

    def transform_pdf_content(self, file_content: str):
        prompt = f"""
        Process this file:
        [FILE CONTENT START]
        {file_content}
        [FILE CONTENT END]
        """
        result = ollama.generate(
            model=self.model,
            prompt=prompt,
            format=self.schema,
            system=self.system_prompt,
            options={
                "temperature": 0,
            },
        )
        print(result["response"])
