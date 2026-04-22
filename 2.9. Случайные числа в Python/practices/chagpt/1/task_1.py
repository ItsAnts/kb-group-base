from random import randint

data: dict[str, int] = {"min_sale": 5, "max_sale": 20, "price": 35, "period": 7}

sales: list[int] = []
revenue: int | float = 0
report: str = ""
count_sales: int = 0
for number_day in range(data["period"]):
    day_sales = randint(data["min_sale"], data["max_sale"])
    count_sales += day_sales
    revenue += day_sales * data["price"]
    report += "ДЕНЬ: {} | КОЛ-ВО ПРОДАЖ: {}\n".format(number_day + 1, day_sales)

report += "ОБЩАЯ ВЫРУЧКА ЗА НЕДЕЛЮ: {}\n".format(revenue)
report += "СРЕДНИЕ КОЛ-ВО ПРОДАЖ: {}\n".format(count_sales / data["period"])
print(report)
