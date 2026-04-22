first_name: str = "Yury"
last_name: str = "Antsiferov"


def connect_string(first_str: str, second_str: str) -> str:
    """Функция обьеденяет две строки"""
    result: str = first_str + " " + second_str
    return result


# def_оператор название_функции(параметр_1, параметр_2):
#   тело функции
#   вернуть из функции значение result

full_name: str = connect_string(first_str=first_name, second_str=last_name)
print("Ваше полное имя: {}".format(full_name))


def sum_number(a: int, b: int) -> int:
    return a + b


def hello_message() -> None:
    print("Привет пользователь!")


x = sum_number(5, 5)
y = hello_message()


print("hello", sep="\n")

print(
    "Функция - {} | ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ: {}\nФункция - {} | ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ:{}".format(
        sum_number.__name__, x, hello_message.__name__, y
    )
)
