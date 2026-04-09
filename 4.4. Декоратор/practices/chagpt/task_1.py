def log_call(func):
    
    def wrapper() -> None:
        print(f"Вызов функции: {func.__name__}")
        result = func()
        print("Функция завершена")
        return result
    return wrapper

@log_call
def hello() -> None:
    print("Hello")

hello()