orders: list[int] = [40, 150, 220, 90, 310, 70]
count: int = 0

# VERSION 1
for index in range(0, len(orders), 1): # range(0, 6, 1) # start=0, stop=6, step=1
    if orders[index] > 100: # if orders[0] > 100 -> if 40 > 100:
        count += 1

print("VERSION 1\nOrders > 100: {}".format(count))


# VERSION 2
count = 0 # переприсваиваю значение count 
for order in orders:
    if order > 100: # if 40 > 100
        count += 1

print("VERSION 2\nOrders > 100: {}".format(count))
