numbers: list[int] = [1, 2, 3, 4, 5, 6]
squares = list((x**2 for x in numbers))
print(squares)