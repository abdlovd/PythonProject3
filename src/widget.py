from masks import get_mask_card_number


from masks import get_mask_account


def mask_account_card (coded_accounts: str) -> str:
    decoded = coded_accounts.split()
    only_numbers = decoded[-1]
    only_name = decoded[:-1]
    if only_name == "Счет":
        masked_numbers = get_mask_account(only_numbers)
    else:
        masked_numbers = get_mask_card_number(only_numbers)
    return f"{only_name} {masked_numbers}"
