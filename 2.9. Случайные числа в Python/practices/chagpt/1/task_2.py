from random import randint

data: dict[str, list[int]] = {
    "count_day": [5],
    "count_order": [1, 10],
    "average_bill": [50, 150],
}

result: dict[str, list[int]] = {"sum_day": [], "total_amount": [0]}

for _ in range(data["count_day"][0]):
    random_count_order = randint(a=data["count_order"][0], b=data["count_order"][1])
    sum_day: int = 0
    for _ in range(random_count_order):
        random_average_bill = randint(
            a=data["average_bill"][0], b=data["average_bill"][1]
        )
        sum_day += random_average_bill
    result["sum_day"].append(sum_day)
    result["total_amount"][0] += sum_day

report: str = ""
for day in range(len(result["sum_day"])):
    report += "ДЕНЬ: {} | СУММ ЗА ДЕНЬ: {}\n".format(day + 1, result["sum_day"][day])
report += "ОБЩАЯ ВЫРУЧКА: {}\n".format(result["total_amount"][0])
print(report)
