"""
def cache(func):
    storage = (None, None)
    def wrapper(*args, **kwargs):
        nonlocal storage
        if storage[0] == args:
            print("cache")
            return storage[1]
        print("no_chache")
        result = func(*args, **kwargs)
        storage = (args, result)
        return result
    return wrapper
"""
def cache(func):
    storage = {}
    def wrapper(*args, **kwargs):
        nonlocal storage
        print(storage)
        if storage.get(args):
            print("cache")
            return storage.get(args)
        print("no_chache")
        result = func(*args, **kwargs)
        storage[args] = result
        return result
    return wrapper


@cache
def square(x: int) -> int:
    return x * x
    
print(square(5))
print(square(563))
print(square(5))
print(square(15))
print(square(15))
print(square(5))
print(square(563))