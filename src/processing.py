def filter_by_state (data, state: str ) -> list [str]:
    """ Принимает список словарей, возвращает новый список словарей у которых ключ соответствует указанному значению"""

    sorted_list = []

    for item in data:
        if item [state] == 'EXECUTED':
            sorted_list.append(item)
    return sorted_list


def sort_by_date (date: list[str]) -> list:
    """" Которая принимает список словарей и сортирует по убывание """

    descending_dates = sorted (date, reverse=True)

    return descending_dates
