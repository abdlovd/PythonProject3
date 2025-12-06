def get_mask_card_number(number_card: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    if not number_card.isdigit():
        return "Только Цифры"
    elif len(number_card) != 16:
        return "Номер должен состоять из 16 цифр"
    return number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]


def get_mask_account(number_account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    return "**" + number_account[-4:]
