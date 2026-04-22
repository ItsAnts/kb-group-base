from threading import Thread
import time
from random import randint


def worker(num: int) -> None:
    print("Поток {} работает".format(num))
    time.sleep(randint(1, 5))
    print("Поток {} - завершен".format(num))


th_list: list = []


for i in range(1, 4):
    th = Thread(target=worker, args=(i,))
    th.start()
    th_list.append(th)

for th in th_list:
    th.join()

# Дальнейшая какая то инструкция
