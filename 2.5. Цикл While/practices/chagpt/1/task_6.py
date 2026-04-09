plan: int = 50
total_sales: int = 0
day_count: int = 0
while total_sales < plan:
    sale: int = int(input("Введите кол-во продаж: "))
    total_sales += sale
    day_count += 1

print(f"Дней потребовалось: {day_count}\nИтоговое кол-во прода: {total_sales}")
