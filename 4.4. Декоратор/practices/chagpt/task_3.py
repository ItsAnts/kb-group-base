def double_result(func):
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def get_number():
    return 5
    
print(get_number())