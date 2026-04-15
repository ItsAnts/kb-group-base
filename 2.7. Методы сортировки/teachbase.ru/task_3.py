import time


numbers: list[int] = [45, 3, 29, 8, 15, 60] * 5000
start_time = time.time()
for i in range(len(numbers)):
    swapped: bool = False

    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    if not swapped:
        break

print(time.time() - start_time)


numbers = [45, 3, 29, 8, 15, 60] * 5000
start_time = time.time()
for i in range(len(numbers)):
 
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
print(time.time() - start_time)
