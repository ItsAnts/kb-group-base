MONTHLY_BUDGET: int = 5000

expenses: list[dict[str, str | int]] = [
    {"type": "Office Supplies", "amount": 600},
    {"type": "Software", "amount": 1200},
    {"type": "Marketing", "amount": 1800},
    {"type": "Travel", "amount": 700},
]


def increase_budget(amount: int) -> None:
    if isinstance(amount, int):
        global MONTHLY_BUDGET
        MONTHLY_BUDGET += amount


def is_budget_exceeded(expenses: list[dict[str, str | int]]) -> bool:
    result: int = calculate_total_expenses(expenses=expenses)
    if MONTHLY_BUDGET - result >= 0:
        return True
    return False


def calculate_total_expenses(expenses: list[dict[str, str | int]]) -> int:
    total: int = 0
    for expens in expenses:
        if "amount" in expens and isinstance(expens["amount"], int):
            total += expens["amount"]
    return total


def calculate_remaining_budget(expenses: list[dict[str, str | int]]) -> int:
    result: int = calculate_total_expenses(expenses=expenses)
    return MONTHLY_BUDGET - result


print("ОСТАТОК БЮДЖЕТА: {}".format(calculate_remaining_budget(expenses=expenses)))
