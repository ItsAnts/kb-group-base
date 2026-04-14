database: list[int] = []
step: int = int(input("Кол-во заказов: "))
count: int = 0
for _ in range(step):
    print(_)
    sale: int = int(input("Стоимость заказа: "))
    if sale > 100:
        count += 1

print("КОЛ-ВО ЗАКАЗОВ ДОРОЖЕ 100 ЕВРО = {}\nКОЛ-ВО ЗАКАЗОВ: {}".format(count, step))

