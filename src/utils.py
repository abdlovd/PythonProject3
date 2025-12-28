import json

from src.external_api import api_information


def open_json(way_to_open):
    try:
        with open(way_to_open, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []


def currency_in_rub(transactions: dict):
    amount = transactions.get("operationAmount", {}).get("amount", "0")
    currency = transactions.get("operationAmount", {}).get("currency", {}).get("code", "")
    if currency == "RUB":
        return float(amount)
    return api_information(currency, amount)
