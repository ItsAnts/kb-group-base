GLOBAL_ID: int = 1005

orders = (
    (
        1001,
        "Иван",
        2500,
        "Москва",
    ),  # index 0 (1001 -> index 0, "Иван" -> index 1, 2500 -> index 2, "Москва" -> index 3)
    (1002, "Анна", 4200, "Казань"),  # index 1
    (1003, "Петр", 1800, "Москва"),  # index 2
    (1004, "Ольга", 5600, "Самара"),  # index 3
    (1005, "Мария", 3100, "Москва"),  # index 4
)
# orders[0][0] -> 1001
# orders [4][3] -> 3100

# 001 - ID: 1001 | Клиент: Иван | Сумма: 2500 | Город: Москва
for index in range(len(orders)):
    print(
        "ID: {} | Клиент: {} | Сумма: {} | Город: {}".format(
            orders[index][0], orders[index][1], orders[index][2], orders[index][3]
        )
    )

# 002 - Задание 2 — Найти общий доход магазина. Найти сумму всех заказов.Ожидаемый результат: Общий доход: 17200
total_income: int | float = 0
for index in range(len(orders)):
    total_income = total_income + orders[index][2]

print("Общй доход: {}".format(total_income))

# 003 Найти самый дорогой заказ. Вывести заказ с максимальной суммой. Формат вывода: Самый дорогой заказ: ID: XXXX | Клиент: XXXX | Сумма: XXXX
max_amount: int | float = 0
order_max_amount_index = 0
for index in range(len(orders)):
    if orders[index][2] > max_amount:
        order_max_amount_index = index
print(
    "Самый дорогой заказ: ID: {} | Клиент: {} | Сумма: {} | Город: {}".format(
        orders[order_max_amount_index][0],
        orders[order_max_amount_index][1],
        orders[order_max_amount_index][2],
        orders[order_max_amount_index][3],
    )
)

# 004 Задание 4 — Подсчитать количество заказов из Москвы. Найти сколько заказов сделано из города Москва. Ожидаемый результат: Количество заказов из Москвы: 3

count_city_sale: int = 0
city_name: str = "Москва"
for index in range(len(orders)):
    if orders[index][3] == city_name:
        count_city_sale = count_city_sale + 1
print("Количество заказов из Москвы: {}".format(count_city_sale))
