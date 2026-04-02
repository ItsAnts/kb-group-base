"""
// 01
"""

# x = list(range(5, 16))

x: list = []
for i in range(5, 16):
    x.append(i)
print(x)

"""
// 02
"""
"""
/// Code

numbers: list[int] = [4, 8, 15, 16, 23, 42]
# print(len(numbers)) ->  6
min_number = min(numbers)
max_number = max(numbers)
average_values: float = (sum(numbers)) / (len(numbers))
new_numbers: list[int] = []
if average_values < numbers[0]:
    new_numbers.append(numbers[0])
if average_values < numbers[1]:
    new_numbers.append(numbers[1])
if average_values < numbers[2]:
    new_numbers.append(numbers[2])
if average_values < numbers[3]:
    new_numbers.append(numbers[3])
if average_values < numbers[4]:
    new_numbers.append(numbers[4])
if average_values < numbers[5]:
    new_numbers.append(numbers[5])

print(f"Минимальное число в списке: {min_number}\nМаксимальное число в списке: {max_number}\nСреднее число в списке: {average_values}\nСписок с элементами, которые больше {average_values} = {new_numbers}")
"""
"""
/// Решение через цикл
"""
"""
/// Code

numbers: list[int] = [4, 8, 15, 16, 23, 42]
min_number = 0
max_number = 0
average_values = sum(numbers) / len(numbers)
new_numbers = []
for index in range(len(numbers)):
    if numbers[index] < min_number:
        min_number = numbers[index]
    if numbers[index] > max_number:
        max_number = numbers[index]
    if numbers[index] > average_values:
        new_numbers.append(numbers[index])
print(f"Минимальное число в списке: {min_number}\nМаксимальное число в списке: {max_number}\nСреднее число в списке: {average_values}\nСписок с элементами, которые больше {average_values} = {new_numbers}")
"""

# /// 03
words: list[str] = ["apple", "banana", "kiwi", "orange", "pear"]
new_words: list[str] = []
if len(words[0]) > 5:
    new_words.append(words[0].upper())
if len(words[1]) > 5:
    new_words.append(words[1].upper())
if len(words[2]) > 5:
    new_words.append(words[2].upper())
if len(words[3]) > 5:
    new_words.append(words[3].upper())
if len(words[4]) > 5:
    new_words.append(words[4].upper())

report: str = "Кол-во слов больше 5 символов = {}\nСами значения: {}".format(
    len(new_words), new_words
)
print(report)

# Альтернативное решение
current_step: int = 0
current_index: int = 0
lenght_word: int = len(words)
while current_step != lenght_word:
    print(
        "Index = {} | Шаг = {} | Список: {}".format(current_index, current_step, words)
    )
    if len(words[current_index]) < 6:
        words.pop(current_index)
        current_step = current_step + 1
    else:
        words[current_index] = words[current_index].upper()
        current_index = current_index + 1
        current_step = current_step + 1

report: str = "Ко-во слов больше 5 символов = {}\nСами значения: {}".format(
    len(words), words
)
print(report)
