step: int = int(input("Кол-во заказов: "))
total = 0

for _ in range(step):
    total += int(input("Стоимость заказа: "))

total_average = total / step
print("СРЕДНЯЯ СТОИМОСТЬ ЗАКАЗА: {}".format(total_average))
