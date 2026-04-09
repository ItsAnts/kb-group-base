profits = [500, -200, 700, -150, 300, -500, 300, -400, -400]

index: int = 0

while index != len(profits):
    if profits[index] < 0:
        profits.pop(index)
    else:
        index = index + 1
print(profits)