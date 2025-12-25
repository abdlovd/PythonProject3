from src.utils import currency_in_rub

from unittest.mock import patch


@patch("src.utils.currency_in_rub")
def test_currency_in_rub(mock_random):
    mock_random.return_value = 31957.58
    transactions = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert currency_in_rub(transactions) == 31957.58
    mock_random.assert_called_once_with()
