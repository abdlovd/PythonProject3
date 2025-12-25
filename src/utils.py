import json

from src.external_api import api_information


def open_json(way_to_open):
    try:
        with open(way_to_open, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []


def currency_in_rub(transactions):
    amount = transactions.get("amount")
    currency = transactions.get("currency")
    if currency == "RUB":
        return amount
    elif "USD" in currency.value():
        return amount
    elif "EUR" in currency.value():
        return api_information(currency, amount)
    elif "EUR" in currency.value():
        return api_information(currency, amount)
    return transactions
