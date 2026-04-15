numbers: list[int] = [34, 12, 5, 67, 23, 9, 18, 45, 2, 50, 11, 7, 30, 1, 88, 56, 14, 4, 72, 25]


for i in range(0, len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

