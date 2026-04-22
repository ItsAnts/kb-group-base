from threading import Thread
import time


def worker() -> None:
    time.sleep(5)
    print("Поток начал работу")


th = Thread(target=worker)
th.start()
print("Программа завершенна")
th.join()  # чтобы программа дождалась завершение потока, используется данный метод.
