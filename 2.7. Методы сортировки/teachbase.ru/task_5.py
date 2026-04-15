numbers: list[int] = [12, 5, 18, 7, 25, 3, 10]

for i in range(1, len(numbers)):
    key: int = numbers[i]
    j: int = i - 1

    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
print(
    "Отсортированный список: {}\nНаибольшие первые 3 элемента: {}\nНаименьшие первые 3 элемента: {}".format(
        numbers, numbers[-3:], numbers[:3]
    )
)


"""
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key: int = arr[i]
        j: int = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
"""
