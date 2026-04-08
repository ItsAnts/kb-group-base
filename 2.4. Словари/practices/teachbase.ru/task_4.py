student: dict[str, str | int] = {
    "name": "Ivan",
    "age": 20
}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

if student.get("name"):
    print("Данный ключ существует")
else:
    print("Данный ключ не существует")

print(f"Все ключи: {student.keys()}\nВсе значения: {student.values()}\nВсе пары ключ-значение: {student}")

