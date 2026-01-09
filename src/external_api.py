import requests

from dotenv import load_dotenv

import os

load_dotenv()


def api_information(from_, amount):
    """ Конвертирует сумму из иностранной валюты в рубли (RUB).
       Функция использует внешний сервис Exchange Rates Data API
       для получения актуального курса валют."""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}"

    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers)
    return float(response.json().get("result", 0))
