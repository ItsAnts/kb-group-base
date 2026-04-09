balance: int = 0
day_count: int = 0
while True:
    income: int = int(input("Введите число: "))
    if income == 0:
        break
    day_count += 1
    balance += income

print(f"Общая выручка: {balance}\nКол-во дней: {day_count}")