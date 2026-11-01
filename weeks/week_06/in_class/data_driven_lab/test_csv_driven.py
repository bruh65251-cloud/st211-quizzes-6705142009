import csv
from pathlib import Path

import pytest

from weeks.week_06.in_class.data_driven_lab.validate import is_valid_login


DATA_FILE = Path(__file__).with_name("logins.csv")


def load_login_cases():
    cases = []

    with DATA_FILE.open() as f:
        for row in csv.DictReader(f):
            expected = row["valid"] == "True"
            cases.append((row["username"], row["password"], expected))

    return cases


@pytest.mark.parametrize("username,password,expected", load_login_cases())
def test_login_validation(username, password, expected):
    assert is_valid_login(username, password) == expected