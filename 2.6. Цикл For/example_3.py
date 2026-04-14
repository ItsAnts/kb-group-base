import time

my_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(my_numbers)):
    my_numbers.append("VALUE")
    print("ЦИКЛ FOR | ЗНАЧЕНИЕ: {}".format(my_numbers[i]))
    time.sleep(0.5)

print(my_numbers)


my_numbers_next: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in my_numbers_next:
    my_numbers_next.append("VALUE")
    print("ЦИКЛ FOR_2 | ЗНАЧЕНИЕ: {}".format(number))
    time.sleep(0.5)

print(my_numbers_next)
