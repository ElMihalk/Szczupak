from pydantic import BaseModel, Field
from typing import List


class WordItem(BaseModel):
    japanes_word: str = Field(description="The word in Japanese kanji or kana.")
    reading: str = Field(description="The hiragana reading of the word.")
    translation: str = Field(description="The translation of the word.")


class VocabularyOutput(BaseModel):
    items: List[WordItem]


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
            You are tasked with reading a PDF and image files contents and providing a json output according to the provided schema and the rules specified below.
            The PDF files will be passed in form of a string.
            It is crucial that you extract all the vocabulary items without losses. 
            CRITICAL: Each item must have exactly 3 fields named exactly: "japanese_word", "reading" and "translation".
            You must ensure that the translation part is in {self.translation_language}.
            If {self.translation_language} translation is missing, you must provide it. 
            If a japanese_word contains kanji characters, the reading field is mandatory - you must provide the reading if it's missing.

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
