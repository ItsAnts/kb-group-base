from threading import Thread

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def worker(nums: list[int]) -> int:
    x = sum(nums)
    print(x)
    return x


th_list: list[Thread] = []
for _ in range(2):
    if _ == 1:
        th = Thread(target=worker, args=(numbers[:5],))
    else:
        th = Thread(target=worker, args=(numbers[5:],))
    th_list.append(th)
    th.start()

for th in th_list:
    th.join()
