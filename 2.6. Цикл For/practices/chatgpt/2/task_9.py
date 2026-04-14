orders: list[int] = [120, 340, 80, 500, 270, 60, 310]
top_orders: list[int] = []

for order in orders:
    if order > 250:
        top_orders.append(order)

    if len(top_orders) >= 3:
        break

print("Top orders: {}".format(top_orders))
