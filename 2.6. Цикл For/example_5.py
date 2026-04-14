numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# VERSION 1 | FOR
for index in range(len(numbers) - 1, -1, -1):
    print("INDEX: {} | NUMBER: {}".format(index, numbers[index]))

# VERSION 2 | WHILE
index = len(numbers) - 1
while index != -1:
    print("INDEX: {} | NUMBER: {}".format(index, numbers[index]))
    index -= 1
