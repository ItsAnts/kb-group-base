"""
Проверка на возраст и доступ к сайту
"""

"""
# If else
age: int = int(input("Введите сколько вам лет: "))

if age >= 18: # Принцып работы идёт через True | False
    print("Доступ на сайт разрешен")
else:
    print("Доступ на сайт запрещен")

match age:
    case 18: # age == 18 
        print("Доступ на сайт разрешен")
    case 17:
        print("Доступ на сайт запрещен")
    case _:
        print("Доступ на сайт запрещен")

"""

"""

command: int = int(input("Введите номер комманды:\n1. Меню:\n 2. Настройки:\n 3. Выход"))
if command == 1:
    print("Вы зашли в меню")
elif command == 2:
    print("Вы зашли в Настройки")
elif command == 3:
    print("Вы вышли из программа")
else:
    print("Не корректная команда")

match command:
    case 1:
        print("Вы зашли в меню")
    case 2:
        print("Вы зашли в Настройки")
    case 3:
        print("Вы вышли из программы")
    case _:
        print("Не корректная команда")
"""

try:
    purchare_amount: int = int(input("Введите сумму покупки: "))
except:
    purchare_amount = 0
    print("Данные обновленны из за не корректности")

if purchare_amount < 1000:
    print("Скидка 0%")
elif 1000 < purchare_amount <= 5000:
    print("Скидка 5%")
else:
    print("Скидка 10%")
