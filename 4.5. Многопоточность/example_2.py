from threading import Thread
import time

RESULT: list[int] = []

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_worker(nums: list[int], second: int) -> None:
    time.sleep(second)
    RESULT.append(sum(nums))


th_one = Thread(target=sum_worker, args=(numbers[:5], 3))
th_two = Thread(target=sum_worker, args=(numbers[5:], 5))

th_one.start()
th_two.start()

th_two.join()

print(RESULT)
