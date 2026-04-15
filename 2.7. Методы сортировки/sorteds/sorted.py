from time import time


def bubble_sort(arr: list) -> list:
    n: int = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key: int = arr[i]
        j: int = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_idx: int = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr: list[int] = [64, 34, 25, 12, 22, 11, 90] * 500000
report: str = ""

print("КОЛ-ВО ЭЛЕМЕНТОВ: {}".format(len(arr)))

start_time = time()
# orted_bubble = bubble_sort(arr)
# report += "ПУЗЫРЬКОВАЯ СОРТИРОВКА\nВРЕМЯ РАБОТЫ: {}\n".format(time() - start_time)
# print(sorted_bubble)

start_time = time()
# sorted_insertion = insertion_sort(arr)
# report += "ВСТАВКА СОРТИРОВКА\nВРЕМЯ РАБОТЫ: {}\n".format(time() - start_time)
# print(sorted_insertion)

start_time = time()
# sortend_selection = selection_sort(arr)
# report += "ВЫБОРОМ СОРТИРОВКА\nВРЕМЯ РАБОТЫ: {}\n".format(time() - start_time)
# print(sortend_selection)
print(report)

start_time = time()
sorts = arr.sort()
print(time() - start_time)
