def filter_by_state (dict_list: list [dict], state: str = "EXECUTED" ) -> list[dict]:
    """ Функция филтрует список словоря по ключу с указонным значением"""

    filtered_list = []
    for item in dict_list:
        if item.get("state") == state:
            filtered_list.append(item)

    return filtered_list



def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """ Принимает список словарей и сортирует их по ключу 'date'.
    По умолчанию сортировка по убыванию (descending=True).
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
