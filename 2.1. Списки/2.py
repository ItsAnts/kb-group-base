# // 04
numbers: list[int] = [3, 7, 2, 9, 4, 5]
numbers.append(10)
numbers.remove(2)
numbers.sort()
print(numbers)

# // 05
numbers: list[int] = [10, 20, 30, 40, 50]
# // 01
print(numbers[0] + numbers[4])
print(numbers[0] + numbers[-1])
# // 02
print(numbers[1] + numbers[3])
print(numbers[1] + numbers[-2])
# // 03
numbers[0] = numbers[0] + 5
numbers[-1] = numbers[-1] - 5
print(numbers)

