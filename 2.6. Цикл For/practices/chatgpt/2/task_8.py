employee_sales: list[int] = [450, 600, 300, 800]
bonuses: list[float | int] = []
for sale in employee_sales:
    if sale > 500:
        bonuses.append(sale * 0.1)
    else:
        bonuses.append(sale * 0.05)
print("Bonuses: {}".format(bonuses))
