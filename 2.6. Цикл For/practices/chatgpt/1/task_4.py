step: int = int(input("Кол-во заказов: "))
max_price: int = 0

for _ in range(step):
    order: int = int(input("Стоимость заказа: "))
    if order > max_price or step == 0:
        max_price = order

print("Максимальная стоимость заказа: {}".format(max_price))

