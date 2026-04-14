personals: dict[int, int] = {}
step: int = int(input("Кол-во сотрудников: "))

for i in range(step):
    sum_sale: int = int(input("Сумма продаж сотрудника под номером {} ".format(i) ))
    if sum_sale > 1000:
        personals[i] = sum_sale * 0.1
    else:
        personals[i] = sum_sale * 0.05

for key in personals.keys():
    print(personals[key])


