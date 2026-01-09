import pandas as pd


def csv_reader(road_to_file: str) -> list:
    """Загружает финансовые транзакции из CVS - файла. Функция считывает
    CVS- файл(.cvs) и преобразует данные из первой страницы в список
    словарей, где каждая строка соответствует одной транзакции."""

    transactions = pd.read_csv(road_to_file)
    return transactions.to_dict("records")


def excel_reader(road_to_file: str) -> list:
    """Загружает финансовые транзакции из EXCEL - файла. Функция считывает
       EXCEL- файл(.xlsx) и преобразует данные из первой страницы в список
       словарей, где каждая строка соответствует одной транзакции."""
    data_ = pd.read_excel(road_to_file)
    return data_.to_dict("records")
