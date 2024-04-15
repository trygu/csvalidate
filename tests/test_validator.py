import pytest
from rfccsv.validator import validate_csv

@pytest.mark.parametrize("file_path, is_valid", [
    ("tests/test_files/valid_01.csv", True),
    ("tests/test_files/valid_02.csv", True),
    ("tests/test_files/invalid_01.csv", False),
    ("tests/test_files/invalid_02.csv", False)
])
def test_validate_csv(file_path, is_valid):
    result = validate_csv(file_path)
    if is_valid:
        assert result == "CSV is valid according to RFC 4180.", f"Validation failed for valid file: {file_path}"
    else:
        assert "Invalid CSV:" in result, f"Error not detected in invalid file: {file_path}"
