from pathlib import Path
from typing import Any

from config_files.paths_config import PROJECT_ROOT

class OutputHandler:

    def __init__(self, *args):
        self._check_output_folder()
        self.content = {"items": []}
        for arg in args:
            self.add_to_content(arg)

    def _check_output_folder(self) -> None:
        Path(PROJECT_ROOT / "output").mkdir(exist_ok=True)

    def _json2tsv(self) -> str:
        tsv_output = ""
        print(self.content)
        for item in self.content["items"]:
            tsv_output += f"{item['japanese_word']} | {item['reading']}\t{item['translation']}\n"
        return tsv_output

    def create_tsv(self, filename: str) -> None:
        with open(PROJECT_ROOT / "output" / f"{filename}.tsv", "w") as outfile:
            outfile.write(self._json2tsv())

    def add_to_content(self, model_output: dict) -> None:
        self.content["items"].extend(model_output["items"])