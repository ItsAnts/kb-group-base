sales: list[int] = [120, 85, 230, 45, 99]
total: int = 0


# VERSION 1
for sale in sales:
    total += sale # 120 -> 85 -> 230 -> 45 -> 99

print("VERSION 1\nTotal revenue: {}".format(total))

# VERSION 2
total = 0
for index in range(len(sales)):
    total += sales[index] # sales[0] -> sales[1]
print("VERSION 2\nTotal revenue: {}".format(total))
