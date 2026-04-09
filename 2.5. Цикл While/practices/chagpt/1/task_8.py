target_stock: int = 100
current_stock: int = 30
supplies_count: int = 0

while current_stock != target_stock:
    current_supplies = int(input("Введите кол-во поставки: "))
    supplies_count += 1
    if current_supplies + current_stock >= target_stock:
        return_goods = current_supplies + current_stock - target_stock
        current_stock = 100
        print(f"Склад заполнен, возрат обратно товара в кол-ве: {return_goods}")
    else:
        current_stock += current_supplies

print(f"Кол-во поставок: {supplies_count}\nИтоговый остаток: {current_stock}")
