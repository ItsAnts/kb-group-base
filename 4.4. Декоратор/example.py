
def debug_decorator(func):
    
    def wrapper(x: int, y: int):
        print("TYT", x, y)
        print("Вызов функции: ", func.__name__)
        print("Аргументы: ", x, y)
        x = x**10
        y = y**10
        result = func(x=x, y=y)
        print("Результат: ", result)
        return result
    return wrapper
    

@debug_decorator
def add_numbers(x: int, y: int) -> int:
    print(f"x={x} | y={y}")
    return x + y

print(add_numbers(5, 15))


def outer():        # внешняя функция
    n = 5           # лексическое окружение - локальная переменная
 
    def inner():      # локальная функция
        nonlocal n
        n += 1        # операции с лексическим окружением
        print(n)
 
    return inner
 
 
fn = outer()   # fn = inner, так как функция outer возвращает функцию inner
fn_two = outer()
# вызываем внутреннюю функцию inner
fn()    # 6
fn()    # 7
fn()    # 8

fn_two()
fn_two()
fn_two()