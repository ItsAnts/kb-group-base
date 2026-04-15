def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half: list = arr[:mid]
        right_half: list = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


data = [38, 27, 43, 3, 9, 82, 10] * 500000
print("Кол-во элементов: {}".format(len(data)))
import time

start_time = time.time()
merge_data = merge_sort(data)
print("ВРЕМЯ: {}".format(time.time() - start_time))

start_time = time.time()
d = data.sort()
print("ВРЕМЯ: {}".format(time.time() - start_time))
