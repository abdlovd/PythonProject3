import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "coded_accounts, results",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(coded_accounts, results):
    assert mask_account_card(coded_accounts) == results


@pytest.mark.parametrize(
    "dates, results", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2012-08-20T02:26:18.671407", "20.08.2012")]
)
def test_get_date(dates, results):
    assert get_date(dates) == results
