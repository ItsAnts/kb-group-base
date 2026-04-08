student: dict[str, str | int] = {
    "name": "Ivan",
    "age": 20,
    "city": "Moscow"
}

student["group"] = "К643"
student["age"] = 21
student.update({"email": "IvanJob@yandex.ru", "phone": "79995554433"})

print(student)
if student.get("group"):
    print(student["group"])
else:
    print("Такого ключа нет")