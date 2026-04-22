import random

products: list[str] = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
# - Поставка каждого товара: 10–100 шт
product_count_span: tuple[int, int] = (10, 100)
prices: dict[str, int] = {
    "Laptop": 600,
    "Mouse": 25,
    "Keyboard": 45,
    "Monitor": 300,
    "Headphones": 80,
}

warehouse: dict[str, dict[str, int]] = {}  # кол-во, общая стоимость, price

# //STEP 1
for product in products:
    count_product = random.randint(product_count_span[0], product_count_span[1])
    if prices.get(product) is None:
        continue
    warehouse[product] = {
        "count": count_product,
        "price": prices[product],
        "total_cost": count_product * prices[product],
    }

# //STEP 2
expensive_item: tuple[str, int] = ("None", 0)
total_revenue: int = 0
for item in warehouse.keys():
    total_revenue += warehouse[item]["total_cost"]
    if expensive_item[0] is None:
        expensive_item = (item, warehouse[item]["total_cost"])
    else:
        if expensive_item[1] < warehouse[item]["total_cost"]:
            expensive_item = (item, warehouse[item]["total_cost"])
print(warehouse)
print(expensive_item)
print(total_revenue)
