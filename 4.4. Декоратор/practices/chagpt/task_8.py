def timer(func):
    from time import time
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Функция: {func.__name__} выполнена за {end_time - start_time} сек")
        return result
    return wrapper

@timer
def slow():
    import time
    time.sleep(5)
    
slow()