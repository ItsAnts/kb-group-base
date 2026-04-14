days: int = int(input("Кол-во дней: "))
count: int = 0

for _ in range(days):
    profit: int = int(input("Ваша прибыль за день: "))
    if profit < 0:
        count += 1
print("КОЛ-ВО УБЫТОЧНЫХ ДНЕЙ: {}".format(count))
