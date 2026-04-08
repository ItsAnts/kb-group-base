"""
Task::1
Напиши программу, которая проверяет, может ли
человек получить водительские права
"""

"""
age_user: int = int(input("Сколько вам лет?: "))

# 1 Версия
if age_user >= 18: # if 15 >= 18: => if False !!! следовательно мы переходим на ветку else 
    print("Можно получить права")
else:
    print("Ещё рано получать права")

# 2 Версия
check: bool = age_user > 18
if check:
    print("Можно получить права")
else:
    print("Ещё рано получать права")
"""

"""
Task::2
Напиши программу, которая определяет размер скидки в 
зависимости от суммы покупки:
"""
"""
purchase_amount: float = float(input("Введите сумму покупки: "))
message: str = "Сумма покупки {}\n% сидки: {}\nИтоговая сумма к оплате: {}"
if purchase_amount < 1000:
    print(message.format(purchase_amount, 0, purchase_amount * 1))
    # 1. purchase_amount = 1500.0
    # 2. print(...) => Сумма покупки 1500.0\n% скидки: 0\nИтоговая сумму к оплате: 1500.0\n
elif 1000 < purchase_amount < 5000:
    print(message.format(purchase_amount, 5, purchase_amount * 0.95))
else:
    print(message.format(purchase_amount, 10, purchase_amount * 0.90))
"""
"""
Task::5
Напиши программу, которая переводит числовой балл (от0 до 100)
в буквенную оценку по шкале:
90-100 A; 80-89 B; 70-79 C; 60-69 D; Меньше 60: F
"""
point: int = int(input("Введите кол-во баллов: "))
grade: str = ""

if 90 <= point <= 100:
    grade = "A"
elif 80 <= point <= 89:
    grade = "B"
elif 70 <= point <= 79:
    grade = "C"
elif 60 <= point <= 69:
    grade = "D"
else:
    grade = "F"

print("Ваша оценка за экзамен с {} баллов равна: '{}'".format(point, grade))
