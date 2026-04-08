expenses = {
    "Аренда": 80000,
    "Реклама": 35000,
    "Зарплаты": 240000
}

values: list[int] = list(expenses.values())
print(f"Сумма расходов: {sum(values)}")

keys: list[str] = list(expenses.keys())
max_value: int = max(values)
max_index_value: int = values.index(max_value)
print(f"Категория с самым большим расходом: {keys[max_index_value]}")

expenses["Реклама"] = expenses["Реклама"] - 5000
expenses["Логистика"] = 27000