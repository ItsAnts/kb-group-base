my_numbers: list[int] = [5, 10, 15, 20]


# version 1
total: int = 0

for i in range(len(my_numbers)):
    total += my_numbers[i]
print("VERSION 1 | TOTAL = {}".format(total))

# version 2
total = 0

for i in my_numbers:
    total += i
print("VERSION 2 | TOTAL = {}".format(total))

# version 3
total = 0

for index, value in enumerate(my_numbers):
    total += value
print("VERSION 3 | TOTAL = {}".format(total))

# version 4
total = 0
index: int = 0

while index != len(my_numbers):
      total += my_numbers[index]
      index += 1
print("VERSION 4 | TOTAL = {}".format(total))

