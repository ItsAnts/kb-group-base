salaries = {
    "Иван": 70000,
    "Мария": 95000,
    "Олег": 60000,
    "Анна": 110000
}
keys: list[str] = list(salaries.keys())
list_salari: list[str] = []

index: int = 0
while index != len(keys):
    if salaries[keys[index]] > 80000: # if salaries[keys[0]] > 80000 -> if salaries["Иван"] > 80000 -> if 70000 > 80000 -> False
        list_salari.append(keys[index])
    index = index + 1
print(f"Список людей: {list_salari}")
