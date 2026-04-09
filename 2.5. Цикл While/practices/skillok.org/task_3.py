"""
Создай цикл while, который запрашивает ввод числа до тех пор,
пока не будет введено положительное число.
"""

status: bool = True

while status:
    number: int = int(input("Введите число: "))
    if number >= 0:
        status = False

