my_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# VERSION 1 | WHILE
index: int = 0
report_1: str = "VERSION 1 | WHILE: "
while index != len(my_numbers):
    report_1 += "{}, ".format(my_numbers[index])
    index += 1

# VERSION 2 | FOR | RANGE
report_2: str = "VERSION 2 | FOR RANGE: "
for index in range(0, len(my_numbers)): # range(start, stop, step) => range(0, len(my_numbers) => range(0, 10)
    report_2 += "{}, ".format(my_numbers[index])

# VERSION 3 | FOR | IN
report_3: str = "VERSION 3 | FOR IN: "
for number in my_numbers:
    report_3 += "{}, ".format(number)


print(report_1, report_2, report_3, sep="\n")
