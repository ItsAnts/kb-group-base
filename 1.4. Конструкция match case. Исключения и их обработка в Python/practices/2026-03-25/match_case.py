"""
Task::1

Напиши программу, которая
1. Спрашивает у пользователя код валюты(USD, EUR, GBP)
2. Спрашивает у пользователя сумму.
3. Конвертирует сумму в рубли по фиксированному курсу:
USD 75.5 руб
EUR 80.2
GBP 90.1
4. Если введена неизсветная валюта, выводите сообщение об ошибке
5. Обязательно используйте match case
"""

"""
type_message_error: str = "[ERROR]"
type_message_info: str = "[INFO]"

code_currency: str = input("{} Введите код валюты\n| USD | EUR | GBP |\nВвод: ".format(type_message_info))
try:
    sum_currency: float = float(input("{} Сумму, которую хотите конвертировать\nВвод: ".format(type_message_info)))
except ValueError:
    sum_currency = 0.0
    print("{} Сумма введена не корректно, сброшенно на ноль".format(type_message_error))


match code_currency:
    case "USD":
        result: float = sum_currency * 75.5
    case "EUR":
        result: float = sum_currency * 80.2
    case "GBP":
        result: float = sum_currency * 90.1
    case _:
        code_currency = "NULL"
        result: float = 0.0
        print("{} Ошибка в воде валюты".format(type_message_error))


print(
    "{} Результат возможной конвертации\nВаша валюта: {}\nСумма на конвертацию: {}\nРезультат в RUB: {}".format(
        type_message_info, code_currency, sum_currency, result
    )
)
"""

"""
TASK::2
Напиши программу, которая:
1. Спрашивает у пользователя числовой код HTTP-статуса
2. Выводит соответсвующее сообщение:
200 ->OK
404 -> Not Found
500 - Server Error 
лбой другой код "Unknown Status"
"""
"""
type_message_info: str = "[INFO]"
type_message_error: str = "[ERROR]"
line: str = "=" * 15
respone_message: str = "{}\nTYPE_MESSAGE: {}\n{} RESPONSE {}"
try:
    code_HTTP_status: int = int(
        input(
            "{}\nTYPE_MESSAGE: {}\nВведите статус HTTP-запроса: ".format(
                line, type_message_info
            )
        )
    )
except ValueError:
    code_HTTP_status = 999
    print(
        "{}\nTYPE_MESSAGE: {}\nСтатус не корректный, сброшенно до 999".format(
            line, type_message_error
        )
    )
match code_HTTP_status:
    case 200:
        print(respone_message.format(line, type_message_info, code_HTTP_status, "OK"))
    case 404:
        print(
            respone_message.format(
                line, type_message_info, code_HTTP_status, "Not Found"
            )
        )
    case 500:
        print(
            respone_message.format(
                line, type_message_info, code_HTTP_status, "Server Error"
            )
        )
    case _:
        print(
            respone_message.format(
                line, type_message_error, code_HTTP_status, "Unknown Status"
            )
        )
"""

"""
Task::4
Напиши программу, которая
1. Запрашивает у пользователя строку с ролью:
"admin", "editor", "viewer"
2. В зависиости от роли выводи уровень доступа
- "admin" - Полный доступ 
  editor - Редактирование 
  viewer Просмотр 
  Любая другая строка - "Нет доступа"
"""
"""
user_role: str = input("Введите вашу роль: ")
match user_role:
    case "admin":
        print("Полный доступ")
    case "editor":
        print("Редактирование")
    case "viewer":
        print("Просмотр")
    case _:
        print("Нет доступа")
"""

"""
Task::3
Сегоня твоя программа будет работать с разными фуграми, кругом, прямоугольником и треугольником.
Тебе нужно получить от пользователя название фигуры и нужные числа, а потом выполнить 
правильный расчет
Типы фигур 
- cirly одно число r , 3.14
- rect два числа  a, b *
- triangle три числа a, b, c +
- Если фигура не известная -> Неизвестная фигура вывести
"""
type_shape: str = input("Введите название фигуры: ")
response: str = ""
match type_shape:
    case "cirly":
        try:
            r: float = float(input("Введите радиус круга: "))
        except ValueError:
            r: float = 0
        result: float = r * 3.14
        response: str = "Круг с радиусом {} имеет площадь: {}".format(r, result)
    case "rect":
        try:
            a: float = float(input("Введите сторону A: "))
            b: float = float(input("Введите сторону B: "))
        except ValueError:
            a: float = 0
            b: float = 0
        result: float = a * b
        response: str = (
            "Прямоугольник со сторонами A: {} и B: {} имеет площадь: {}".format(
                a, b, result
            )
        )
    case "triangle":
        try:
            a: float = float(input("Введите сторону A: "))
            b: float = float(input("Введите сторону B: "))
            c: float = float(input("Введите сторону C: "))
        except ValueError:
            a: float = 0
            b: float = 0
            c: float = 0
        result: float = a + b + c
        response: str = (
            "Треугольник со сторонами: A: {}, B: {}, C: {} имеет периметр: {}".format(
                a, b, c, result
            )
        )
    case _:
        respnonse: str = "Неизвестная фигура"

print(response)
