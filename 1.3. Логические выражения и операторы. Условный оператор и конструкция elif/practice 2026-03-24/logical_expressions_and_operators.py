"""
Task::1
Напиши программу, которая определяет, попадает ли введенное
пользователем число в диапазон от 10 до 20 включительно.
"""

"""
user_number: int = int(
    input("Введите число для проверки находится ли оно в диапазоне: ")
)
result: bool = 10 <= user_number <= 20
# result: bool = 9 < user_number < 21
message: str = "Проверка на то, что число <{}> входит в диапазон показало результат: {}"
print(message.format(user_number, result))
"""

"""
Task::2
Напиши программу, которая определяет, является ли введенный
пользоваталем год високосным.
Год считается високосным, если выполняется ОДНО ИЗ УСЛОВИЙ:
- делится на 4, но не делится на 100
- делится на 400
"""

year: int = int(input("Введите год: "))
# yaer = 2024
check_one: bool = year % 4 == 0 and year % 100 != 0
# 1. check_one = 2024 % 4 == 0 and 2024 % 100 != 0
# 2. check_one = 0 == 0 and "какой то остаток" != 0
# 3. check_one = True and True
# 4. check_one = True
check_two: bool = year % 400 == 0
# 1. check_two = 2024 % 400 == 0
# 2. check_two = "какой то остаток" == 0
# 3. check_two = False
result: bool = check_one or check_two
# 1. result = True or False
# 2. result = True
message: str = "Результат проверки на то, что год {} присланый является високосным - {}"
print(message.format(year, result))
"""
example %
year = 2025
check_one = 2025 % 4 => получится число с остатком и мы это мы этот остаток получим
"""

"""
Task::4
Напиш программу, которая получает координаты точки 
X и Y и проверяет в какой четверти она находится
I: x > 0 and y > 0
II: x < 0 and y > 0
III: x < 0 and y < 0
IV: x > 0 and y < 0
"""

x: float = float(input("Введите координату X: "))
# 1. x = -15.0
y: float = float(input("Введите координату Y: "))
# 2. y = 7.0
quarter_one: bool = x > 0 and y > 0
# 1. quarter_one = -15.0 > 0 and 7.0 > 0
# 2. quarter_one = False and True
# 3. quarter_one = False
quarter_two: bool = x < 0 and y > 0
# 1. quarter_two = -15.0 < 0 and 7.0 > 0
# 2. quarter_two = True and True
# 3. quarter_two = True
quarter_three: bool = x < 0 and y < 0
# 1. quarter_three = -15.0 < 0 and 7.0 < 0
# 2. quarter_three = True and False
# 3. quarter_three = False
quarter_four: bool = x > 0 and y < 0
# 1. quarter_four = -15 > 0 and 7.0 < 0
# 2. quarter_four = False and False
# 3. quarter_four = False
message: str = "Точка X: {}, Y: {} находится в четвертях:\nI четверть: {}\nII четверть: {}\nIII четверть: {}\nIV четверть: {}"
print(message.format(x, y, quarter_one, quarter_two, quarter_three, quarter_four))
# print("Точка X: -15.0, Y: 7.0 находится в четвертях:\nI четверть: False\nII четверть: True\nIII четверть: False\nIV четверть: False")
