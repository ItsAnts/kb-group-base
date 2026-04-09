orders: list[int] = [1200, 3400, 560, 2300, 780]
index: int = 0
sum_orders: int = 0
while index != len(orders):
    print(f"Сумма заказа под номером: {index + 1} = {orders[index]}")
    sum_orders = sum_orders + orders[index]
    index += 1
print(f"Итоговая сумма заказа: {sum_orders}")
