sales = {
    "Ноутбук": 5,
    "Мышь": 18,
    "Клавиатура": 9
}

values = list(sales.values())
sum_values = sum(values)
print(f"Кол-во продаж: {sum_values}")

max_value = max(values)
index_max_value = values.index(max_value)
print(f"Товар - {list(sales.keys())[index_max_value]} с максимальным число продаж")

sales.update({"Монитор": 7})
print(sales)