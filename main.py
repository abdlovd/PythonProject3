import os
from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.widget import get_date
from src.utils import open_json
from src.file_reader import csv_reader
from src.file_reader import excel_reader
from typing import Callable


BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)

dict_file = {1: open_json, 2: csv_reader, 3: excel_reader}
path_file = {
    1: BASE_DIR + "/data/operations.json",
    2: BASE_DIR + "/data/transactions.csv",
    3: BASE_DIR + "/data/transactions_excel.xlsx",
}

status = ["EXECUTED", "CANCELED", "PENDING"]


def main():
    while True:
        transactions = []
        print(
            "Привет!\n"
            "Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файл\n"
        )
        user_input: int = int(input())
        get_func: Callable | None = dict_file.get(user_input)
        if get_func:
            print(get_func.__doc__)
            get_func()
            path_: str = path_file.get(user_input)
            transactions: list = get_func(path_)
            break

    while True:
        print(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {", ".join(status)}"
        )
        user_input_status: str = input().upper()
        if user_input_status in status:
            transactions = filter_by_state(transactions, user_input_status)
            print(f"Операции отфильтрованы по статусу '{user_input_status}'")
            break
        else:
            print(f"Статус операции '{user_input_status}' недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    user_input: bool = input().lower() == "да"
    if user_input:
        print("Отсортировать по возрастанию или по убыванию?")
        user_sort_reverse: bool = input().lower() == "по убыванию"
        transactions = sort_by_date(transactions, user_sort_reverse)

    print("Выводить только рублевые транзакции? Да/Нет")
    user_input: bool = input().lower() == "да"
    if user_input:
        transactions = list(filter_by_currency(transactions, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input: bool = input().lower() == "да"
    if user_input:
        print("Введите слово для фильтрации: ")
        user_word: str = input()
        transactions = process_bank_search(transactions, user_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for trans in transactions:
        date = get_date(trans.get("date"))
        amount = trans.get("amount")
        currency_name = trans.get("currency_name")
        to_from = trans.get("from") if isinstance(trans.get("from"), str) else None
        to = get_mask_account(trans.get("to"))
        description = trans.get("description")

        date_description = f"{date} {description}"
        check_to = f"{to}"
        check_from = " -> " + get_mask_card_number(to_from) if to_from else ""
        summ_print = f"Сумма: {amount} {currency_name}"
        print(f"{date_description}\n{check_to}{check_from}\n{summ_print}")


if __name__ == "__main__":
    main()
