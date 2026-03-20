"""
Task::1
Выведите на экран строку Hello, World! С помощью
функции print().
Формат входных данных:
Выввода нет

Формат выходных данных:
Одна строка с текстом
"""

# Task::1
print("Hello, World!")

"""
Task::2
Создайтеайте переменную name = "Alice" и age = 25. Выведите на одной строке:
Name: Alice Age: 25

example JS print() ----->
console.log("Hello world")
const name = "Alice";
console.log(`Name: ${name}`)
"""
# Task::2
name: str = "Alice"
age: int = 25
print("Name:", name, "Age:", age)
print(f"Name: {name} Age: {age}")
print("Name: {} Age: {}".format(name, age))

# example вычисление f-строке
print(f"Мне сколько то лет: {15-40+age}, age: {age}")
print("Мне сколько то лет: {}, Возраст: {}".format(15-40+age, age))

"""
Task::3
Выведите двумя строками текст:
First line
Second line

Используйте один вызов print() и управляющую последовательность \n внутри строки
"""
# Task::3
# print("First line Second line", sep="\n") # dont work, ->
# print("First line", "Secod line", sep="\n")
print("First line\nSecond line")



"""
Task::Four
Сделайте два вывода так, что бы итог оказался в одной строке:
Loading... Done!
"""
print("Loading...", end=" ")
print("Done!")

"""
Task::5
Создайте перемнную price = 19.99. С помощью f-строки вывведите строку:
Price: 19.99 USD
Форматируйте цену так, что бы было ровно 2 знана после точки
"""

# Task::5
price: float = 19.99999
print("Price: {} USD".format(price))
print(f"Price: {price:.2f} USD")


# Task::8
"""
Запросить у пользователя его
имя и выведите приветствие в формате
Hello, <имя>!
"""
username: str = input("Введите ваше имя: ")
print("Hello,", username)
print(f"Hello, {username}")
print("Hello, {}".format(username))



"""
Task::9
Запросите у пользователя возраст.
Вывдите, сколько ему будет через 5 лет
"""
user_age: int = int(input("Сколько вам сейчас лет: "))
print("Через 5 лет вам будет:", user_age + 5)
print(f"Через 5 лет вам будет: {user_age + 5}")
print("Через 5 лет вам будет: {}".format(user_age + 5))


"""
Task::10
Пользователь вводить два числа
через пробел. Программа должна вывести
их сумму.
"""
# user_number_one: int = int(input("Первое число")) | Не корректно по ТЗ
# user_number_two: int = int(input("Второе число")) | Не корректно по ТЗ

# user_numbers: int = int(input("Введите два числа через пробел")) | "5 5" -> int("5 5") -> Ошибка 

user_numbers: str = input("Введите два числа через пробел") # "5 5"
list_numbers: list[str] = user_numbers.split() # "5 5" -> ["5", "5"]
print("Сумма чисел пользователя равна: {}".format(int(list_numbers[0]) + int(list_numbers[1]))) # list_numbers[0] -> "5" => int("5") -> 5, list_numbers[1] -> "5"


