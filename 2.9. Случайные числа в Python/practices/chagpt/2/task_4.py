"""

задача 4: работа службы доставки

контекст

служба доставки получает случайное число заказов.
каждый заказ имеет случайное время доставки.

вводные данные

- заказы в день: 12–25
- время доставки одного заказа: 10–60 минут

задача

1. сгенерировать список времени доставки.
2. рассчитать:
   - общее время доставки
   - среднее время доставки
   - количество заказов дольше 40 минут

использовать

- список
- random.randint
- условие if

"""

import random

input_data: dict[str, list[int]] = {
    "day_orders": [12, 25],
    "dilivery_time": [10, 60],
}

list_time_dilivery: list[int] = []
for _ in range(
    random.randint(input_data["day_orders"][0], input_data["day_orders"][1])
):
    list_time_dilivery.append(
        random.randint(input_data["dilivery_time"][0], input_data["dilivery_time"][1])
    )

count_dilivery: int = 0
for dilivery in list_time_dilivery:
    if dilivery > 40:
        count_dilivery += 1

report: str = (
    "Общее время доставки: {}\nСреднее время доставки: {}\nКол-во заказов дольше 40 минут: {}".format(
        sum(list_time_dilivery),
        sum(list_time_dilivery) / len(list_time_dilivery),
        count_dilivery,
    )
)
print(report)
