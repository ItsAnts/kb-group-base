while True:
    try:
        age: float = float(input("Введите возраст: "))
        break
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

print(age)