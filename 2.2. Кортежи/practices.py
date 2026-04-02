### 01

my_tuple: tuple = (10, 20, 30, 20, 40)

if 20 in my_tuple:
    print(True)
else:
    print(False)
count_number: int = my_tuple.count(20)
my_tuple_slice: tuple[()] = my_tuple[1:4]

try:
    my_tuple[3] = 50

except TypeError:
    print("[ERROR] Нельзя изменять значение кортежа")

### 02

numbers: tuple = (5, 2, 8, 1, 9)
max_number: int = max(numbers)
min_number: int = min(numbers)
sum_numbers: int = sum(numbers)
report_02: str = "Кортеж {} имеет такие характеристики\nМаксимальное число: {}\nМинимальное число: {}\nСумма всех чисел {}".format(
    numbers, max_number, min_number, sum_numbers
)

### Альтернативное решение
if len(numbers) > 0:
    print(numbers)
    alter_max_number: int = numbers[0]
    alter_min_number: int = numbers[0]
    alter_sum_numbers: int = 0
    for index in range(len(numbers)):
        if alter_max_number < numbers[index]:
            alter_max_number = numbers[index]
        if alter_min_number > numbers[index]:
            alter_min_number = numbers[index]
        alter_sum_numbers = alter_sum_numbers + numbers[index]
    print(report_02)
else:
    print(
        "[INFO] Кол-во элементов в коллекции 0, из-за чего нельзя определить максимальное/минимальное/сумма значений"
    )

### 03

t2 = (1, 2, 4)
t1 = (1, 2, 3)
t3 = (1, 2)
print(t2 < t1)
print(t3 < t1)

### 04
# (x, y)
p1 = (3, 5)
p2 = (1, 2)
p3 = (4, 0)

left_point = ()

if p1[0] < p2[0] and p1[0] < p3[0]:
    left_point = p1
elif p2[0] < p1[0] and p2[0] < p3[0]:
    left_point = p2
elif p3[0] < p1[0] and p3[0] < p2[0]:
    left_point = p3

print("Самая левая точка: {}".format(left_point))

### Альтернативное решение

points: tuple = ((5, 3), (2, 3), (1, 4))

result: tuple = points[0]
for point in points:
    if point[0] < result[0]:
        result = point
print("Альтернативное решение: {}".format(result))
