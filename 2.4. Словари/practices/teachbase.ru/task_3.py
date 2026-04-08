student: dict[str, str | int] = {
    "name": "Ivan",
    "age": 21,
    "city": "Moscow",
    "email": "ivan@example.com",
    "phone": "123-456-789"
}
profile: dict[str, str | int] = {
    "username": "ivan123",
    "status": "active",
    "points": 250
}

phone = student.pop("phone")
print(f"Телефон студент: {phone}")

if student.get("adress"):
    del student["adress"]

last_item = student.popitem()
profile.clear()

print(student, profile)