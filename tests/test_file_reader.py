from unittest.mock import patch

from src.file_reader import csv_reader, excel_reader


@patch("pandas.read_excel")
@patch("pandas.read_csv")
def test_csv_reader(mock_read_csv, mock_read_excel) -> None:
    mock_read_csv.return_value.to_dict.return_value = []
    assert [] == csv_reader("")
    mock_read_excel.return_value.to_dict.return_value = []
    assert [] == excel_reader("")
