import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    logger.info(f"Запущенна функция get_mask_card_number с аргументами {number_card}")
    """Принимает на вход номер карты и возвращает ее маску"""
    if not number_card.isdigit():
        logger.info("Сработал if not")
        return "Только Цифры"
    elif len(number_card) != 16:
        logger.info("Сработал elif количество цифр не 16")
        return "Номер должен состоять из 16 цифр"
    logger.debug("Ok")
    return number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]


def get_mask_account(number_account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    return "**" + number_account[-4:]
