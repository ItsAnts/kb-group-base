"""
Task::1
Напиши программу калькулятор
которая:
1. Запрашивает у пользователя два числа
2. Запрашивает операцию (+, -, *, /)
3. Вычисляет резульат и выводи его
4. Обрабатывает ошибки:
- Деление на ноль -> ошибка Деление на ноль
- Неверный ввод числа -> Ошибка ввода
-> Незивестая операция -> Ошибка ввоад: Незиветсяа операция
"""

type_message_error: str = "TYPE MESSAGE: [ERROR]"
type_message_info: str = "TYPE MESSAGE: [INFO]"
line: str = "=" * 15
try:
    one_number: float = float(
        input("{}\n{}\nВведите первое число\nВвод: ".format(line, type_message_info))
    )
except ValueError:
    print("{}\n{}\nОшибка ввода")
    one_number: float = 1.0
try:
    two_number: float = float(
        input("{}\n{}\nВведите второе число\nВвод: ".format(line, type_message_info))
    )
except ValueError:
    print("{}\n{}\nОшибка ввода")
    two_number: float = 1.0

operation: str = input("Введите необходимую операцию: ")
result: float = 0
match operation:
    case "+":
        result: float = one_number + two_number
    case "-":
        result: float = one_number - two_number
    case "*":
        result: float = one_number * two_number
    case "/":
        try:
            result: float = one_number / two_number
        except ZeroDivisionError:
            print("Ошибка деление на ноль")
            result: float = one_number / 1
    case _:
        print("Неизвестная операция")
response: str = "{} {} {} = {}".format(one_number, operation, two_number, result)
print(response)
