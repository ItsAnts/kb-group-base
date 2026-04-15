words: list[str] = ["банан", "яблоко", "вишня", "груша"]

for index in range(1, len(words)):
    key: str = words[index] # элемент для вставки
    j: int = index - 1

    # сдвиг элементов вправо
    while j >= 0 and words[j] > key:
        words[j + 1] = words[j]
        j -= 1

    # вставка элемента
    words[j + 1] = key

print(words)

numbers: list[str] = ["банан", "яблоко", "вишня", "груша"]

for i in range(1, len(numbers)):
    key = numbers[i]

    # ищем место для вставки элемента key среди предыдуших элементов
    for j in range(i - 1, -1, -1):
        if numbers[j] > key:
                numbers[j + 1] = numbers[j]
                if j == 0:
                    numbers[j] = key
        else:
            numbers[j + 1] = key
            break
print(numbers)
