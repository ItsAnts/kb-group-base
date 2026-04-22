from typing import Optional

sales: list[dict[str, str | int]] = [
    {"employee": "Anna", "amount": 1200},
    {"employee": "Boris", "amount": 800},
    {"employee": "Anna", "amount": 700},
    {"employee": "Dmitry", "amount": 1500},
    {"employee": "Boris", "amount": 400},
    {"employee": "Anna", "amount": 600},
]


def total_sales_by_employee(sales: list[dict[str, str | int]]) -> dict[str, int]:
    result: dict[str, int] = {}
    for sale in sales:
        if (
            sale.get("employee")
            and sale.get("amount")
            and type(sale["employee"]) == str
            and type(sale["amount"]) == int
        ):
            result[sale["employee"]] = sale["amount"]
    return result


def find_top_employee(
    employee_totals: list[dict[str, str | int]],
) -> Optional[str]:  # str | None
    employee: Optional[str] = None
    amount: Optional[int] = None
    for sale in employee_totals:
        if (
            sale.get("employee")
            and type(sale["employee"]) == str
            and sale.get("amount")
            and type(sale["amount"]) == int
        ):
            if amount == None or sale["amount"] > amount:
                amount = sale["amount"]
                employee = sale["employee"]
    return employee


def employees_above_average(employee_totals: list[dict[str, str | int]]) -> list:
    result: list = []
    total_amount: int = 0
    for sale in employee_totals:
        if sale.get("amount") and type(sale["amount"]) == int:
            total_amount += sale["amount"]
    average_amount: float = total_amount / len(employee_totals)
    print("СРЕДНЕЕ ЗНАЧЕНИЕ: {}".format(average_amount))
    for sale in employee_totals:
        if (
            sale.get("amount")
            and type(sale["amount"]) == int
            and float(sale["amount"]) > average_amount
        ):
            result.append(sale)
    return result


print(total_sales_by_employee(sales=sales))
print(find_top_employee(employee_totals=sales))
print(employees_above_average(employee_totals=sales))
