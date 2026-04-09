prices: list[int] = [1200, 5400, 800, 2300, 7600]
new_prices: list[int] = []

index: int = 0
while index != len(prices):
    
    if prices[index] > 3000:
        new_prices.append(prices[index])
    index = index + 1
print(f"Товары дороже 3000: {new_prices}")