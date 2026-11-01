import json
from pathlib import Path

import pytest


DATA_FILE = Path(__file__).with_name("test_cases.json")


def load_cases():
    with DATA_FILE.open(encoding="utf-8-sig") as f:
        data = json.load(f)

    return [(case["input"], case["expected"]) for case in data]


@pytest.mark.parametrize("text,expected", load_cases())
def test_uppercase(text, expected):
    assert text.upper() == expected