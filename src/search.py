import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    for i in data:
        pattern = re.compile(search, re.IGNORECASE)
        if pattern.search(str(i.get("description", ""))):
            result.append(i)
    return result


def process_bank_category(data: list[dict], list_category: list) -> dict:
    """Функцию, которая будет принимать список словарей с
    данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    description = []
    for i in data:
        get_description = i.get("description", "")
        if get_description in list_category:
            description.append(get_description)
    return dict(Counter(description))
