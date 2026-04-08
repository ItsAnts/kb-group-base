from typing import Generator


def fibonacci_gen(n: int) -> Generator:
    a: int = 0
    b: int = 1
    step = 0
    while n != step:
        yield a
        c = a
        a = b
        b = b + c
        step += 1
        
x = fibonacci_gen(10)
print('До for')
for i in x:
    print(f"Шаг {i}")
    