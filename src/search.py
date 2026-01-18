import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    for i in data:
        pattern = re.compile(search, re.IGNORECASE)
        if pattern.search(str(i.get("description", ""))):
            result.append(i)
    return result


def process_bank_category(data: list[dict], category: str) -> Counter[dict]:
    description = []
    for i in data:
        if i.get("description", "") in category:
            description.append(i)
    count_description = Counter(description)
    return count_description
