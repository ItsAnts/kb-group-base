"""
Task::1
Напиши программу, которая определяет
попадает ли введенное пользователем число
в диапозон от 10 до 20 включительно
"""

"""
# CODE
user_number: int = int(input("Введите число для проверки диапозона: ")) # "15" => int("15") => 15 
result: bool = 10 <= user_number <= 20 # 10 <= 15 <= 20 => True
# result: bool = 9 < user_number < 21
print(
    "Резульат проверки, входит ли число {} в диапозон от 10 до 20 включительно равен {}".format(
        user_number, result
    )
)
"""

"""
Task::2
Напиши программу, которая определяет, является ли введенный пользователем
год високосный

Год считается високосный, если выполняется одно из условий:
- делится на 4, но не делится на 100
- делится на 400
"""
"""
# CODE
year: int = int(input("Введите год, который надо определить на високосность: ")) # 2024
check_one: bool = (year % 4) == 0 and (year % 100) != 0 # 2024 % 4 == 0 and 2024 % 100 != 0 => 0 == 0 and "ЧИСЛО" != 0 => True and True => True
check_two: bool = year % 400 == 0 # 2024 % 400 == 0 => "ЧИСЛО" == 0 => False
result: bool = check_one or check_two # True or False => True

# result = ((year % 4) == 0 and (year % 100) != 0) or year % 400 == 0 
print(
    "Результат проверки является ли год {} високосным равен = {}".format(year, result)
)

# year = 100 | rs = year % 4 => rs = 100 % 4 => 0
# year = 105 | rs = year % 4 => rs = 105 % 4 => "ЧИСЛО"
"""
"""
Task::3
Напиши программу, которая проверяет введенные пользователем логин и пароль 
Правильный логин: admin
Правильный пароль: qwerty
"""
login: str = input("Введите пожалуйста ваш логин: ")
password: str = input("Введите пожалуйста ваш пароль: ")
auth_user: bool = login == "admin" and password == "qwerty"
# use case
# 1. login = "test", password = "look"
# 2. auth_user = "test" == "admin" and "look" == "qwerty" => False and False => False
#
# next use case
# 1. login = "test", password = "qwerty"
# 2. auth_user = "test" == "admin" and "qwerty" == "qwerty" => False and True => False
#
# next use case
# 1. login "admin", passwprd = "qwerty"
# 2. auth_user = "admin" == "admin" and "qwerty" == "qwerty" => True and True => True
print(
    "Резульат запроса на авторизацию пользователя в системе равен: {}\nВведенный логин: {}\nВведенный пароль: {}".format(
        auth_user, login, password
    )
)
