from turtledemo.penrose import start
from typing import Iterator, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции.
       Возвращает итератор, который поочередно выдает транзакции,
       где валюта операции соответствует заданной."""
    return (i for i in transactions if i["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions (transactions: list[dict]) -> Iterator:
    """ Генератор, возвращающий описание каждой транзакции. """
    for i in transactions:
        yield i["description"]


def card_number_generator (start: int, stop: int) -> Generator:
    """
       Функция-генератор, которая последовательно возвращает номера банковских карт
       в установленном формате, начиная с начального значения и заканчивая конечным.
       """
    for i in range(start, stop+1):
        number = f"{i:016d}"
        yield number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:]

if __name__ == "__main__":
    card_number_gen = card_number_generator(start=1000, stop=1067)
    print(next(card_number_gen))
    print(next(card_number_gen))
    print(next(card_number_gen))
    print(next(card_number_gen))
