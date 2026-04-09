"""
Напиши код с использованием оператора break, который завершает бесконечный цикл при вводе 'exit'.
"""

while True:
    command: str = input("Введите комманду")
    
    if command == "next":
        pass # набор какие то инструкций
    elif command == "exit":
        break
    else:
        pass