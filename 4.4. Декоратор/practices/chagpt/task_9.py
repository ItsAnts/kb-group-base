def limit_calls(max_calls):
    count_called: int = 0
    def wraper(func):
        def called(*args, **kwargs):
            nonlocal count_called
            if count_called >= max_calls:
                raise RuntimeError
            count_called += 1
            result = func(*args, **kwargs)
            return result
        return called
    return wraper
    

@limit_calls(max_calls=2)
def hello():
    print("Hello")
    
hello()
hello()
hello()