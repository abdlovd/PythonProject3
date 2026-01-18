import pandas as pd
from pandas import DataFrame


def csv_reader(road_to_file: str) -> list:
    """Для обработки выбран CSV-файл"""

    transactions = pd.read_csv(road_to_file)
    return transactions.to_dict("records")


def excel_reader(road_to_file: str) -> list:
    """Для обработки выбран EXCEL-файл"""
    data_: DataFrame = pd.read_excel(road_to_file)
    return data_.to_dict(orient="records")
