"""
Задача 2: Проверка количества возвратов товаров

Контекст

Интернет-магазин фиксирует количество возвратов товаров ежедневно.

Вводные данные

- Дней: 8
- Возвраты в день: 0–7
- Стоимость одного возврата: 20 €

Задача

1. Сгенерировать количество возвратов на каждый день.
2. Сохранить в список.
3. Рассчитать:
   - общее количество возвратов
   - общий убыток
   - среднее количество возвратов в день

"""

import random

data_input: dict[str, list[int]] = {"days": [8], "returns": [0, 7], "price_item": [20]}
returns_list: list[int] = []
for _ in range(data_input["days"][0]):
    returns_list.append(
        random.randint(data_input["returns"][0], data_input["returns"][1])
    )

report = "Общее кол-во возвратов: {}\nОбщий убыток: {}\nСреднее кол-во возвратов в день: {}".format(
    sum(returns_list),
    sum(returns_list) * data_input["price_item"][0],
    sum(returns_list) / len(returns_list),
)
print(report)
