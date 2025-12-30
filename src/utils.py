import json
import logging
from src.external_api import api_information


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_json(way_to_open):
    try:
        with open(way_to_open, "r", encoding="utf-8") as f:
            logger.debug(f'Открыт файл по адресу {way_to_open}')
            return json.load(f)
    except Exception as e:
        logger.error(f'Произошла ошибка {e}')
        print(e)
        return []


def currency_in_rub(transactions: dict):
    amount = transactions.get("operationAmount", {}).get("amount", "0")
    currency = transactions.get("operationAmount", {}).get("currency", {}).get("code", "")
    if currency == "RUB":
        return float(amount)
    return api_information(currency, amount)

