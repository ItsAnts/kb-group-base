sales: list[int] = [100, 200, 150, 50, 300]

# VERSION 1
sum_sales: int = 0
for sale in sales:
    sum_sales = sum_sales + sale 

print("Average sale: {}".format(sum_sales / len(sales)))


# VERSION 2
sum_sales = 0
for index in range(0, len(sales), 1):
    sum_sales = sum_sales + sales[index]

print("Average sale: {}".format(sum_sales / len(sales)))
