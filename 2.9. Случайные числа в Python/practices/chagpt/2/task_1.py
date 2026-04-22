"""
Задача 1: Доход кофейни за рабочую неделю

Контекст

Кофейня продаёт чашки кофе.
Количество проданных чашек каждый день случайное.

Вводные данные

- Дней: 6
- Продажи в день: 30–80 чашек
- Цена одной чашки: 4.5 €

Задача

1. Сгенерировать количество проданных чашек на каждый день.
2. Сохранить данные в список.
3. Рассчитать:
   - выручку за каждый день
   - общую выручку
   - день с максимальными продажами

Использовать

- random.randint
- список
- цикл for
"""

import random

input_data: dict = {"days": 6, "sales_day": [30, 80], "price": 4.5}
sales: list = []

for _ in range(input_data["days"]):
    sale = random.randint(a=input_data["sales_day"][0], b=input_data["sales_day"][1])
    sales.append(sale)

result: dict = {"total_revenue": 0, "revenue": [], "max_sales": [-1, -1]}
for index in range(len(sales)):
    result["revenue"].append(sales[index] * input_data["price"])
    print(index, len(sales), len(result["revenue"]))
    result["total_revenue"] += result["revenue"][index]
    if result["max_sales"][0] == -1:
        result["max_sales"] = [index + 1, result["revenue"][index]]
    else:
        if result["max_sales"][1] < result["revenue"][index]:
            result["max_sales"] = [index + 1, result["revenue"][index]]
print("КОЛ-ВО ПРОДАЖ ПО ДНЯМ: {}".format(sales))
print(
    "ВЫРУЧКА ПО ДНЯМ: {}\nОБЩАЯ ВЫРУЧКА: {}\nДЕНЬ С МАКСИМАЛЬНЫМИ ПРОДАЖАМИ: {}".format(
        result["revenue"], result["total_revenue"], result["max_sales"]
    )
)
