from typing import Generator


def even_numbers(n: int) -> Generator:
    step: int = 0
    if n % 2 != 0:
        n += 1
    while step != n:
        yield step
        step = step + 2
    
even = even_numbers(15)

def even_numbers_teachbase(n: int) -> Generator:
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
            
even = even_numbers(15)
even_teachbase = even_numbers_teachbase(15)

for i in even:
    print(i)
    
for j in even_teachbase:
    print(j)