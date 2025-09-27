import pytest


def calculate_commission(transaction_type, amount):
    # Версия с match н поддерживается в версиях ниже 3.10
    # match transaction_type:
    #     case "перевод":
    #         return max(amount * 0.01, 100)
    #     case "покупка":
    #         return amount * 0.02
    #     case _:
    #         return amount * 0.005
    if transaction_type == "перевод":
        return max(amount * 0.01, 100)
    if transaction_type == "покупка":
        return amount * 0.02
    return amount * 0.005


@pytest.mark.parametrize(
    'transaction_type, amount, expected_commission',
    [
        ("перевод", 5000, 100),
        ("перевод", 15000, 150),
        ("покупка", 5000, 100),
        ("вывод", 5000, 5000 * 0.005),
    ]
)
def test_calculate_commission(transaction_type, amount, expected_commission):
    assert calculate_commission(transaction_type, amount) == expected_commission
