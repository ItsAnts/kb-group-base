orders: list[int] = [50, 120, 340, 80, 260, 410, 95]
category: list[int] = [0, 0, 0]
# category[0] -> Small; category[1] -> Medium; category[2] -> Large

for order in orders:
    if order < 100:
        category[0] += 1
    elif 100 <= order <= 300:
        category[1] += 1
    else:
        category[2] += 1

print("Small: {}\nMedium: {}\nLarge: {}".format(category[0], category[1], category[2]))

