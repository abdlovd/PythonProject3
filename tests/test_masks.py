from unittest import result

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, result",
    [
        ("12345678998765432112345", "Номер должен состоять из 16 цифр"),
        ("12345678998в6543", "Только Цифры"),
        ("1234567899886543", "1234 56** **** 6543"),
    ],
)
def test_get_mask_card_number(number_card: str, result: str) -> None:
    assert get_mask_card_number(number_card) == result


@pytest.mark.parametrize(
    "number_account, result", [("123456789987654321", "**4321"), ("123456789987652222", "**2222")]
)
def test_get_mask_account(number_account: str, result: str) -> None:
    assert get_mask_account(number_account) == result
