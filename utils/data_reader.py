import json
import pytest

@pytest.fixture(scope="session")
def test_data():
    with open("testdata/data.json", "r", encoding="utf-8") as file:
        return json.load(file)
