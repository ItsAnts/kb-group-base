profits: list[int] = [200, -50, 300, -20, -100, 400]
count: int = 0

for profit in profits:
    if profit < 0:
        count += 1

print("Loss days: {}".format(count))
