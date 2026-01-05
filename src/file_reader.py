import pandas as pd


def csv_reader(road_to_file: str) -> list:
    transactions = pd.read_csv(road_to_file)
    return transactions.to_dict("records")


def excel_reader(road_to_file: str) -> list:
    data_ = pd.read_excel(road_to_file)
    return data_.to_dict("records")
