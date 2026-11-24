import pytest
import json

@pytest.fixture
def json_input():
    return json.loads("""{
      "items": [
        {
          "japanese_word": "一日",
          "reading": "いちにち",
          "translation": "jeden dzień"
        },
        {
          "japanese_word": "一日",
          "reading": "ついたち",
          "translation": "pierwszy dzień (miesiąca)"
        },
        {
          "japanese_word": "一人",
          "reading": "ひとり",
          "translation": "jedna osoba"
        },
        {
          "japanese_word": "一番",
          "reading": "いちばん",
          "translation": "numer jeden"
        }
      ]
    }
    """)