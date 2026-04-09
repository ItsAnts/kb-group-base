"""
while True:
    a: float = float(input())
    b: float = float(input())
    print(f"Результат: {(a + b):.2f}")
    command = input()
    if command == "нет":
        break
"""


while True:
    command = input()
    if command == "нет":
        break
    elif command == "да":
        a: float = float(input())
        b: float = float(input())
        print(f"Результат: {(a + b):.2f}")
