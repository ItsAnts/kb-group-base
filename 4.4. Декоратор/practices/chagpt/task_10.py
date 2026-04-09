import time
def retry(attempts: int, delay: int):
    
    def wrapper(func):
        def called(*args, **kwargs):
            nonlocal attempts
            while True:
                print(f"Попытка: {attempts}")
                try:
                    result = func(*args, **kwargs)
                    return result
                except ValueError as e:
                    if attempts == 0:
                        raise ValueError
                    attempts -= 1
                    time.sleep(delay)
        return called
    return wrapper


@retry(attempts=1, delay=1)
def unstable():
    import random
    
    if random.randint(0, 1) == 0:
        raise ValueError("Ошибка")
    
    print("Успех")

unstable()