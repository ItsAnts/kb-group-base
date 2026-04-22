"""
Составь функцию, которая принимает имя и возраст, и выводит строку в формате 'Имя: {имя}, Возраст: {возраст}'.
определение функции с параметрами, вывод информации
"""


def print_user_info(name: str, age: int) -> None:
    print("Имя: {}, Возраст: {}".format(name, age))


def sum_number(a: int, b: int) -> None:
    x: int = a + b


result = sum_number(a=5, b=10)
