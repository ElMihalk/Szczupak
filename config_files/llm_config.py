from pydantic import BaseModel

class VocabularyOutput(BaseModel):
    japanes_word: str
    reading: str
    translation: str


class LLMConfig:
    def __init__(
        self,
        translation_language: str = "Polish",
        model: str = "gemma4:e4b",
        system_prompt: str = "",
    ):
        self.translation_language = translation_language
        self.model = model
        self.system_prompt = f"""
            You are perfectly capable of reading a PDF and image files contents and providing a json output according to the provided schema.
            The input files 
            The data you are looking for is the Japanese vocabulary that will be later used for educational purposes. 
            It is crucial that you extract all the vocabulary items without losses. 
            You must find the Japanese vocabulary and format it according to the schema. 
            If {self.translation_language} translation is missing, you must provide it. 
            If a japanese_word contains kanji characters, the reading field is mandatory - you must provide the reading if it's missing.
            You must ensure that the translation part is in {self.translation_language}.
            "examples": [
                
                    "japanese_word": "増える",
                    "reading": "ふえる",
                    "translation": "to increase"
                ,
                
                    "japanese_word": "大人",
                    "reading": "おとな",
                    "translation": "adult"
                ,

                    "japanese_word": "タオル",
                    "reading": "",
                    "translation": "towel"

            ]
        """
        self.json_schema: dict = VocabularyOutput.model_json_schema()
