import pytest
from csvalidate.validator import validate_csv

@pytest.mark.parametrize("file_path, expected_result", [
    ("tests/test_files/valid_01.csv", "CSV is valid according to RFC 4180."),
    ("tests/test_files/valid_02.csv", "CSV is valid according to RFC 4180."),
    ("tests/test_files/invalid_01.csv", "Invalid CSV: Row 3 has incorrect number of fields."),
    ("tests/test_files/invalid_02.csv", "Invalid CSV: Field in row 2 needs to be quoted but is not.")
])
def test_validate_csv(file_path, expected_result):
    assert validate_csv(file_path) == expected_result

