from src.utils import currency_in_rub, open_json

from unittest.mock import patch, mock_open


def test_currency_in_rub():
    transactions = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {
            "amount": "70946.18",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366"
    }]
    assert currency_in_rub (transactions[0]) == 31957.58

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {'result': 245.0}
        assert currency_in_rub(transactions[1]) == 245.0

def test_open_json():
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert open_json('{"1":"2"}') == {"1": "2"}
    assert open_json(" ") == []
