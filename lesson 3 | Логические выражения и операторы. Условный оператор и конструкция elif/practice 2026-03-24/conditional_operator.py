"""
Task::1
Напиши программу, которая
проверяет, может ли человек
получить водительские права
"""

age: int = int(input("Сколько полных лет: "))
if age >= 18:
    print("Вы можете получить права")
else:
    print("Вы не можите получить права\nТы ещё мал")

"""
age = Преобразоваем_данную_строку_в_число(Запрашиваем_данные_из_консоли_ввода("Сколько полных лет: "))
Если подставляем_значение_переменой_age >= 18 то:
    распечатай_сообщение("Вы можете получить права")
Иначе_выполни вот это действие:
    распечатай_сообщение("Вы не можете получить права\nТы ещё мал")
"""

"""
Task::2
Напиши программу, которая определяет размер скидки в зависимости от суммы
покупки:
- если суммка покупки меньше 1000 р = 0%
  от 1000 до 5000 = 5%
  Выше 5000 = 10%
"""
"""
purchase_amount: float = float(input("Сумма вашей покупки ?: "))
message: str = "За покупку на сумму: {} руб, вы получайте скидку в размере {}%\nИтого сумма к оплате: {} руб."
if purchase_amount < 1000:
    print(message.format(purchase_amount, 0, purchase_amount * 1))
elif 1000 <= purchase_amount <= 5000:
    print(message.format(purchase_amount, 5, purchase_amount * 0.95))
else:
    print(message.format(purchase_amount, 10, purchase_amount * 0.90))
"""
"""
Task::3
Напиши програму, которая по номеру месяца (от 1 до 12)
определяет, какой сейчас время года
- Декабрь, январь, февраль -> зима
- март, апрель, май -> весна
- июнь, июль, август -> лето
- сентабрь, октябрь, нобярь -> осень
"""
number_month: int = int(input("Введите номер месяца: "))
if number_month == 1 or number_month == 2 or number_month == 12:
    print("Время года: Зима")
elif number_month == 3 or number_month == 4 or number_month == 5:
    print("Время года: Весна")
elif number_month == 6 or number_month == 7 or number_month == 8:
    print("Время года: Лето")
elif number_month == 9 or number_month == 10 or number_month == 11:
    print("Время года: Осень")
else:
    print("Не корректнйы ввод")

message: str = "Время года {}"
if 3 <= number_month <= 5:
    print(message.format("Весна"))
elif 6 <= number_month <= 8:
    print(message.format("Лето"))
elif 9 <= number_month <= 11:
    print(message.format("Осень"))
elif number_month == 1 or number_month == 2 or number_month == 12:
    print(message.format("Зима"))
else:
    print("Не корректный ввоод")
