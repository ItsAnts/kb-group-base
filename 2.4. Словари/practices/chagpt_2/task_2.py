managers = {
    "Сергей": 12,
    "Алексей": 7,
    "Наталья": 15
}

print(f"Список менеджеров: {list(managers.keys())}")

keys: list[str] = list(managers.keys()) # ["Сергей", "Алексей", "Наталья"]
values: list[int] = list(managers.values()) # [12, 7, 15]
max_value: int = max(values) # 15
max_index_value: int = values.index(max_value) # 2
print(f"Менеджер с максимальным кол-во продаж: {keys[max_index_value]}")

managers["Алексей"] = managers["Алексей"] + 3
managers["Ольга"] = 9

values = list(managers.values())
print(f"Сумма продаж за месяц: {sum(values)}")