products: dict[str, int | float] = {
    "Ноутбук": 75000,
    "Мышь": 1200,
    "Клавиатура": 3500
}

print(f"Список товаров: {list(products.keys())}")

keys = list(products.keys())
values = list(products.values())
max_price = max(values)
max_index_value = values.index(max_price)
print(f"Товар с максимальной стоимостью: {keys[max_index_value]}, {values[max_index_value]} руб")

products["Мышь"] = products["Мышь"] * 1.10
print(products)

if products.get("Монитор"):
    print("Монитор есть на складе")
else:
    print("Данного товара нет на складе")