"""
number: int = 0
try:
    number = int(input("Введите число: "))
    print("Введеное число: {}".format(number))
except ValueError:
    print("При вводе числа была произвденна ошибка {}".format(number))
finally:
    print("Закрываю программу.")
"""

# Task::4
"""
role: str = input("Введите вашу роль: ")

match role:
    case "admin":
        print("Полный доступ")
    case "editor":
        print("Редактирование")
    case "viewer":
        print("Просмотр")
    case _:
        print("Нет доступа")
"""
# Task::5
try:
    temperature: int = int(input("Введите значение температуры: "))
except ValueError:
    temperature: int = 0
    print(
        "Из за не корретного введенного значения температуры, temperature = {}".format(
            temperature
        )
    )

unit: str = input("Введите единица измерения C | F: ")

match unit:
    case "F":
        c: float = (temperature - 32) * (5 / 9)
        print("{}{}={}C".format(temperature, unit, c))
    case "C":
        f: float = (temperature * (9 / 5)) + 32
        print("{}{}={}F".format(temperature, unit, f))
    case _:
        print("Ошибка формата. Используйте например '25C' или '77F'")
