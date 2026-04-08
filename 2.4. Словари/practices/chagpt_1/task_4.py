employees = {
    "Иван": {
        "position": "Менеджер",
        "salary": 70000
    },
    "Мария": {
        "position": "Аналитик",
        "salary": 85000
    }
}

print(f"Должность Марии: {employees["Мария"]["position"]}")

employees["Иван"]["salary"] = employees["Иван"]["salary"] * 1.15
print(employees)

employees.update({"Михаил": {"position": "Слоняра", "salary": 66666}})
print(employees)

iteratio: int = 0
result: list = []
keys = list(employees.keys())
while iteratio != len(employees):
    if employees[keys[iteratio]]["salary"] > 80000:
        result.append({keys[iteratio]:employees[keys[iteratio]]})
    iteratio = iteratio + 1
print(result)