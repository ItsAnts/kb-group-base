def count_args(func):
    
    def wrapper(*args, **kwargs):
        lenght = len(args)
        print(f"Кол-во аргументов: {lenght}")
        result = func(*args, **kwargs)
        return result
    return wrapper
    
@count_args
def add(a: int, b: int, c: int) -> int:
    return a + b + c
    
add(1, 2, 3)