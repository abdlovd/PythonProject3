import json
import logging
from src.external_api import api_information


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_json(way_to_open):
    """Для обработки выбран JSON-файл"""
    try:
        with open(way_to_open, "r", encoding="utf-8") as f:
            reader: list[dict] = json.load(f)
            for i in reader:
                i["amount"] = i.get("operationAmount", {}).get("amount", 0)
                i["currency_name"] = i.get("operationAmount", {}).get("currency", {}).get("name", 0)
                i["currency_code"] = i.get("operationAmount", {}).get("currency", {}).get("code", 0)
            logger.debug(f"Открыт файл по адресу {way_to_open}")
            return reader
    except Exception as e:
        logger.error(f"Произошла ошибка {e}")
        print(e)
        return []


def currency_in_rub(transactions: dict) -> list[dict]:
    result = []
    amount = transactions.get("operationAmount", {}).get("amount", "0")
    currency = transactions.get("operationAmount", {}).get("currency", {}).get("code", "")
    if currency == "RUB":
        result.append(amount)
        return result
    return api_information(currency, result)
