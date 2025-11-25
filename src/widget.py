from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(coded_accounts: str) -> str:
    """Принимает один аргумент, возращает строку с замаскированным номером"""

    decoded = coded_accounts.split()
    only_numbers = decoded[-1]
    only_name = decoded[:-1]
    final_reveal = ""

    if "Счет" in coded_accounts.lower():
        masked_numbers = get_mask_account(only_numbers)
        final_reveal += only_numbers
        final_reveal += masked_numbers
    else:
        masked_numbers1 = get_mask_card_number(only_numbers)
        final_reveal += only_name
        final_reveal += masked_numbers1
    return final_reveal


def get_date(dates: str) -> str:
    """Принимает на вход строку с датой, и возвращает строку с датой в формате 'ДД.ММ.ГГГГ' """
    return dates[8:10] + "." + dates[5:7] + "." + dates[:4]
