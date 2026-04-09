some_tuple: tuple = ("p", "y", "t", "h", "o", "n")

# последний элемент кортежа
last_element: str = some_tuple[-1]
print(last_element)

# срез кортежа с первого элемент по третий элемент
tuple_slice: tuple[str] = some_tuple[0:3]
print(tuple_slice)

# меняем значение первого элемента
# some_tuple[0] = "C" -> Ошибка, потому что нельзя изменять значение элементов кортежа


my_tuple: tuple = ([0], [1], {"username": "Andrei"})
print(my_tuple)
my_tuple[0][0] = 10
my_tuple[2]["username"] = "Nikita"
print(my_tuple)


def data(a: str, b: str, c: str) -> tuple:
    return a, b, c


print(data(a="Hello", b="User", c="!"))
print(type(data(a="Hello", b="User", c="!")))
