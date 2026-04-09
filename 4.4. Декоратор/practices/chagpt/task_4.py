# https://ru.stackoverflow.com/questions/736522/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%82%D1%8C-%D0%B0%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82-%D0%B2-%D0%B4%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80

def repeat(n):
    
    def wrap(function):
        def called(*args, **kwargs):    
            for _ in range(n):
                function(*args, **kwargs)
            return None
        return called
    return wrap
    
@repeat(n=3)
def hello() -> None:
    print("Hi")
    
hello()