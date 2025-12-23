# import json
# import pytest
# from pathlib import Path
#
# @pytest.fixture(scope="session")
# def test_data():
#     project_root = Path(__file__).resolve().parent.parent
#     data_file = project_root / "test-data" / "testData.json"
#
#     with open(data_file, encoding="utf-8") as f:
#         return json.load(f)
#


# import json
#
#
# def read_json_data(file_path: str):
#     """
#     Reads test data from a JSON file and returns a list of tuples.
#     Example JSON structure:
#     [
#         {"email": "test1@example.com", "password": "abc123", "validity": "valid"},
#         {"email": "test2@example.com", "password": "xyz123", "validity": "invalid"}
#     ]
#     """
#     data = []
#     try:
#         file= open(file_path, "r")
#         json_data = json.load(file)
#         for record in json_data:
#             #data.append((record["email"], record["password"], record["validity"]))
#             data.append(tuple(record.values())) # Convert dictionary values to tuple (preserve order of keys)
#     except Exception as e:
#         print(f"Error reading JSON file: {e}")
#     return data

import json
import pytest

@pytest.fixture(scope="session")
def test_data():
    with open("testdata/data.json", "r", encoding="utf-8") as file:
        return json.load(file)
