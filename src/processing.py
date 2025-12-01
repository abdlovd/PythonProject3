def filter_by_state (data, state: str ) -> str :
    """ Принимает список словарей, возвращает новый список словарей у которых ключ соответствует указанному значению"""

    for item in data:
        sorted_list = []
        if item [state] == 'EXECUTED':
            sorted_list.append(item)
    return sorted_list


def sort_by_date (date: list[str]) -> list:
    """" Которая принимает список словарей и сортирует по убывание """

    descending_dates = sorted (date, reverse=True)

    return descending_dates
