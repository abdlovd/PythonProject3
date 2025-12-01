def filter_by_state (state: list[str] ) -> list[str]:
    """ Принимает список словарей, возвращает новый список словарей у которых ключ соответствует указанному значению"""

    sorted_list = []
    second_list = []

    if state == 'EXECUTED':
        sorted_list.append(state)
    else:
        second_list.append(state)
    return sorted_list, second_list


def sort_by_date (date: list[str]) -> list:
    """" Которая принимает список словарей и сортирует по убывание """

    descending_dates = sorted (date, reverse=True)

    return descending_dates
