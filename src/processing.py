from typing import List, Dict, Any

def filter_by_state (dict_list: List [str, Any], state: str = "EXECUTED" ) -> List[Dict[str, Any]]:
    """ Функция филтрует список словоря по ключу с указонным значением"""

    filtered_list = []
    for item in dict_list:
        if item.get("state") == state:
            filtered_list.append(item)

    return filtered_list



def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """ Принимает список словарей и сортирует их по ключу 'date'.
    По умолчанию сортировка по убыванию (descending=True).
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
