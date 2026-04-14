sales: list[int] = [120, 85, 40, 230, 75]
total: int = 0 

for sale in sales:
	total += sale

print("ВЫВОД:\nКОЛ-ВО ПРОДАЖ ЗА ДЕНЬ = {}\nНА СУММУ: {}".format(len(sales), total))
