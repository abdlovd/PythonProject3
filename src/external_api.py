import requests

from dotenv import load_dotenv

import os

load_dotenv()

def api_information(from_, amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}"

    headers= {
      "apikey": os.getenv("API_KEY")
    }

    response = requests.get(url, headers=headers, data = {})
    return response.json().get("result")
