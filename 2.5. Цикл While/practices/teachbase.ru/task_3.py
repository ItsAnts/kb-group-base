numbers: list[int] = [1, 3, 5, 8, 7, 9]
index: int = 0
while index != len(numbers):
    if numbers[index] % 2 == 0:
        print(f"Первое четное число: {numbers[index]}")
        break
    index += 1

count: int = 1
inter = 0
while count < 500:
    inter += 1
    if count % 2 != 0:
        count += 1
        #print(count)
    else:
        count += 2
        #print(count)
print(f"Кол-во интераций: {inter}")

num = 1
inter_two = 0
while num <= 500:
    inter_two += 1
    if num % 2 != 0:
        num += 1
        continue
    #print(num)
    num += 2
print(f"Кол-во интераций: {inter_two}")