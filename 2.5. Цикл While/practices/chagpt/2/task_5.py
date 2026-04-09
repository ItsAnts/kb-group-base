prices: list[int | float] = [1000, 2500, 3800, 4200]

index: int = 0
while index != len(prices):
    prices[index] = prices[index] * 1.10 # prices[0] = prices[0] * 1.10 => 10000 * 1.10
    index += 1

print(prices)

