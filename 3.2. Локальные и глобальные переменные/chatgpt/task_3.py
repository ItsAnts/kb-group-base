"""2. Список бонусов
3. Общая сумма бонусов


Требования:

- локальная переменная total_bonus
- цикл
- суммирование бонусов

"""

BONUS_RATE: float = 0.05
MIN_SALES_FOR_BONUS: int = 1000
employees: list[dict[str, str | int | float]] = [
    {"name": "anna", "sales": 1200},
    {"name": "boris", "sales": 800},
    {"name": "dmitry", "sales": 2000},
    {"name": "elena", "sales": 950},
]


def generate_bonus_report(
    employees: list[dict[str, str | int | float]],
) -> list[dict[str, str | int | float]]:
    report: list[dict[str, str | int | float]] = []
    for employee in employees:
        print("if")
        if (
            "name" in employee
            and "sales" in employee
            and isinstance(employee["name"], str)
            and isinstance(employee["sales"], (int, float))
        ):
            print("check")
            bonus: dict[str, str | int | float] = {
                "name": employee["name"],
                "bonus": calculate_bonus(employee=employee),
            }
            report.append(bonus)
    return report


def calculate_bonus(employee: dict[str, str | int | float]) -> float | int:
    if "sales" in employee and isinstance(employee["sales"], (int, float)):
        if employee["sales"] >= MIN_SALES_FOR_BONUS:
            return employee["sales"] * BONUS_RATE
        return 0
    return 0


def calculate_total_bonuses(
    employees: list[dict[str, str | int | float]],
) -> int | float:
    total_bonus: float = 0.0
    reports: list[dict[str, str | int | float]] = generate_bonus_report(
        employees=employees
    )
    for report in reports:
        if "bonus" in report and isinstance(report["bonus"], (int, float)):
            total_bonus += report["bonus"]
    return total_bonus


print("СУММА БОНУСОВ: {}".format(calculate_total_bonuses(employees=employees)))


report = generate_bonus_report(employees=employees)
print("РЕПОРТ\n{}".format(report))
