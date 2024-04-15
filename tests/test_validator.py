import pytest
from rfccsv import validate_csv

# This test handles parameterized cases including both valid and invalid files.
@pytest.mark.parametrize("file_path, expected_output", [
    ("tests/test_files/valid_01.csv", "Total rows checked: 3, Fields per row: 3. CSV is valid according to RFC 4180."),
    ("tests/test_files/valid_02.csv", "Total rows checked: 3, Fields per row: 3. CSV is valid according to RFC 4180."),
    ("tests/test_files/invalid_01.csv", "Total rows checked: 3, Fields per row: 3. Errors: Row 2 has incorrect number of fields., Row 3 has incorrect number of fields."),
    ("tests/test_files/invalid_02.csv", "Total rows checked: 3, Fields per row: 3. Errors: Row 3 has incorrect number of fields."),
    ("tests/test_files/empty_headers.csv", "Total rows checked: 3, Fields per row: 3. Errors: Empty header field detected.")
])
def test_detailed_csv_validation(file_path, expected_output):
    result = validate_csv(file_path)
    assert result == expected_output, f"Output mismatch for file: {file_path}"

# Dedicated test for specifically handling empty headers edge case.
def test_csv_empty_headers():
    file_path = 'tests/test_files/empty_headers.csv'
    expected_output = "Total rows checked: 3, Fields per row: 3. Errors: Empty header field detected."
    result = validate_csv(file_path)
    assert result == expected_output, f"Failed to detect empty headers: {result}"
