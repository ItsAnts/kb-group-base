from typing import Generator


def counter() -> Generator:
    current: int = 0
    
    while True:
        yield current
        current += 1

count = counter()
for number in count:
    if number == 10:
        break
    print(number)
print("Новый цикл")
for number in count:
    if number == 15:
        break
    print(number)