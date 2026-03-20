from _typeshed import StrPath


print("Моё имя Юрий")

# print() <- это функция/команда, которая позволяет выводить переданную в него информацию в консоль

list_names: list[str] = ["Николай", "Стас", "Тимур", "Максим"]
for name in list_names:
    print(name)

print(type(print)) # type() <- type() это функция, которая позволяет выводить типо обьекта
print(type(type))

print("Hello", "User", "Как твои дела?", sep="<->")

# Символы \n это символы которые в комбинации говорят о том что надо резделить строку
print("Who", "you", "man?", sep="\n", end="\n") # -> "Who\nyou\nman?\n"
print("Новое сообщение")

user: str = input("Ваше имя ? ")
age: int = int(input("Сколько лет"))
print("Моё имя:", user)

price: float = 19.99999
print("Price: {} USD".format(price))
print(f"Price: {price:.2f} USD")

user_age: int = input()
print("Через 5 лет вам будет:", user_age + 5)
print(f"Через 5 лет вам будет: {user_age + 5}")
print("Через 5 лет вам будет: {}".format(user_age + 5))

"""
Traceback (most recent call last):
  File "/Volumes/MacSSD/Projects/Develop/KB/Github/kb-group-base/lesson 2/practices/tasks.py", line 91, in <module>
    print("Через 5 лет вам будет:", user_age + 5)
                                    ~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
urijanciferov@Ancdev lesson 2 % 

"""