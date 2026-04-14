step: int = int(input("Кол-во заказов: "))

category: int = [0, 0, 0] # small, medium, large

for _ in range(step):
    price_order = int(input("Стоимость заказа: "))
    if price_order < 50:
        category[0] += 1
    elif 50 <= price_order <= 200:
        category[1] += 1
    else:
        category[2] += 1

print("SMALL | MEDIUM | LARGE |\n| {} | {} | {} |".format(category[0], category[1], category[2]))
