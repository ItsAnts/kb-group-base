COUNT: int = 10


def print_count() -> None:
    global COUNT
    COUNT = COUNT + 30
    local_value = 15
    print("COUNT ВНУТРИ ФУНКЦИИ: {}".format(COUNT))


print_count()
print("COUNT ЗА ФУНКЦИЕЙ: {}".format(COUNT))
print_count()
