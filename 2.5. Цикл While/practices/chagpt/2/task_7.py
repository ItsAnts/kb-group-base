sales = {
    "Ноутбук": 5,
    "Мышь": 12,
    "Клавиатура": 7
}

prices = {
    "Ноутбук": 75000,
    "Мышь": 1200,
    "Клавиатура": 3500
}

keys: list[str] = list(sales.keys()) # ["Ноутбук", "Мышь", "Клавиатура"]
index: int = 0
revenue: dict = {}
general_revenue: float = 0

while index != len(keys):
    value = sales[keys[index]] * prices[keys[index]]
    # value = sales[keys[0]] * prices[keys[index]]
    # value = sales["Ноутбук"] * prices["Ноутбук"]
    # value = 5 * 75000 
    # value = 375000
    general_revenue += value
    # general_revenue = 0 + 375000
    revenue[keys[index]] = value
    # revenue[keys[0]] = 375000
    # revenue["Ноутбук"] = 375000
    # revenue -> {"Ноутбук": 375000}
    index += 1
    # index = 0 + 1

print(f"Вырчка по каждому товару: {revenue}\nОбщая выручка: {general_revenue}")