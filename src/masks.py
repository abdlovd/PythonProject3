def get_mask_card_number(number_card: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    return number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]


def get_mask_account(number_account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    return "**" + number_account[-4:]
