from pathlib import Path
from config_files.paths_config import PROJECT_ROOT

class OutputHandler:

    def __init__(self):
        pass

    @staticmethod
    def _check_output_folder() -> None:
        Path(PROJECT_ROOT / "output").mkdir(exist_ok=True)

    @staticmethod
    def _json2tsv(model_output: dict) -> str:
        tsv_output = ""
        for item in model_output["items"]:
            tsv_output += f"{item['japanese_word']}\t{item['reading']}\t{item['translation']}\n"

        return tsv_output

    @staticmethod
    def create_tsv(model_output: dict, filename: str) -> None:
        OutputHandler._check_output_folder()
        with open(PROJECT_ROOT / "output" / f"{filename}.tsv", "w") as outfile:
            outfile.write(OutputHandler._json2tsv(model_output))
