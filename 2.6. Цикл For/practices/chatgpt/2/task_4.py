sales: list[int] = [120, 540, 320, 150, 80]


# VERSION 1 | RANGE
max_sale: int = 0
for index in range(0, len(sales), 1): # range(0, 5, 1) range(start, stop, step)
    if max_sale < sales[index] or index == 0:
        max_sale = sales[index]

print("VERSION 1 | Max sale: {}".format(max_sale))

# VERSION 2 | NOT RANGE
max_sale = sales[0]
for sale in sales:
    if max_sale < sale:
        max_sale = sale
print("VERSION 2 | Max sale: {}".format(max_sale))
