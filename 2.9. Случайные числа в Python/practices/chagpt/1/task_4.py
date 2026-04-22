"""
Задача 4: Симуляция клиентов

Контекст
Компания получает клиентов случайным образом.

Каждый клиент:
- делает покупку
- или уходит без покупки

Вводные данные
- Клиенты в день: 20
- Вероятность покупки: 60%
- Средний чек: 30–120 €

Задача
1. Для каждого клиента:
   - случайно определить покупку (True/False)
   - если покупка — сгенерировать сумму
2. Подсчитать:
   - количество покупателей
   - общую выручку
   - процент конверсии

Что использовать
- random.random()
- списки
- условные операторы

"""

import random

data: dict[str, list[int]] = {
    "clients": [20],
    "probability_purchase": [60],
    "average_check": [30, 120],
}
result: dict = {"buyer": 0, "total_revenue": 0}
for client in range(data["clients"][0]):
    purchase = random.random()  # 0.1 - 1.0
    if purchase <= data["probability_purchase"][0] / 100:
        result["buyer"] += 1
        check = random.randint(a=data["average_check"][0], b=data["average_check"][1])
        result["total_revenue"] += check
result["conversion"] = result["buyer"] / data["clients"][0]

print(
    "КОЛ-ВО КЛИЕНТОВ: {}\nПОКУПАТЕЛЕЙ: {} | ОБЩАЯ ВЫРУЧКА: {}\nКОНВЕРСИЯ: {}".format(
        data["clients"][0],
        result["buyer"],
        result["total_revenue"],
        result["conversion"],
    )
)
