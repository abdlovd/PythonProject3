from unittest import result

import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("number_card, result", [
    ("123456789987654321", "1234 56** **** 654321"),
    ("123456789987654321785784", "1234 56** **** 654321")
])
def test_get_mask_card_number(number_card: str, result: str) -> None:
    assert get_mask_card_number (number_card) == result


@pytest.mark.parametrize("number_account, result", [
    ("123456789987654321", "**4321"),
    ("123456789987652222", "**2222")
])
def test_get_mask_account(number_account: str, result: str) -> None:
    assert get_mask_account (number_account) == result
