from output_handler import json2tsv

class TestFormatTransformation():

    def test_json_to_tsv(self, json_input):
        assert json2tsv(json_string=json_input) == ""
