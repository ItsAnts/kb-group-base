my_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# While
index: int = 0
while index != len(my_numbers):
    print("ЦИКЛ WHILE | Значение: {}".format(my_numbers[index]))
    index += 1

# For 1
for i in range(0, len(my_numbers)):
    print("ЦИКЛ FOR | Значение: {}".format(my_numbers[i]))

# For 2 
for number in my_numbers:
    print("ЦИКЛ FOR_2 | Значение {}".format(number))
