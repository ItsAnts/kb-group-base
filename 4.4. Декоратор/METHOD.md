Декораторы в Python — методический материал

⸻

1. Что такое декоратор

Декоратор — это функция, которая принимает другую функцию, добавляет к ней функциональность и возвращает новую функцию без изменения исходного кода функции.

Основа — функции являются объектами.

⸻

2. Базовая схема декоратора

def decorator(func):
    def wrapper():
        print("До вызова функции")

        func()

        print("После вызова функции")

    return wrapper

Использование:

def hello():
    print("Hello")

hello = decorator(hello)

hello()

Результат:

До вызова функции
Hello
После вызова функции


⸻

3. Синтаксис @decorator

Python предоставляет короткий синтаксис.

@decorator
def hello():
    print("Hello")

Эквивалент:

hello = decorator(hello)


⸻

4. Универсальный декоратор (*args, **kwargs)

Чтобы работать с любыми функциями:

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Старт")

        result = func(*args, **kwargs)

        print("Финиш")

        return result

    return wrapper

Пример:

@decorator
def add(a, b):
    return a + b

print(add(2, 3))


⸻

5. Сохранение имени функции — functools.wraps

Без wraps теряются:
	•	__name__
	•	__doc__

Исправление:

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")

        return func(*args, **kwargs)

    return wrapper

Проверка:

@decorator
def test():
    """Описание функции"""
    pass

print(test.__name__)
print(test.__doc__)


⸻

6. Декоратор с параметрами

Декоратор может принимать аргументы.

Структура:

def decorator(param):

    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            print(param)

            return func(*args, **kwargs)

        return wrapper

    return actual_decorator

Пример:

@decorator("Логирование")
def hello():
    print("Hello")


⸻

7. Несколько декораторов

Порядок важен.

@decorator1
@decorator2
def func():
    pass

Эквивалент:

func = decorator1(decorator2(func))

Выполнение:

decorator1
decorator2
func
decorator2
decorator1


⸻

8. Практические примеры декораторов

⸻

8.1 Логирование вызова функции

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Вызов функции {func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")

        result = func(*args, **kwargs)

        print(f"Результат: {result}")

        return result

    return wrapper

Использование:

@logger
def multiply(a, b):
    return a * b

multiply(3, 4)


⸻

8.2 Замер времени выполнения

import time
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Время: {end - start:.5f} сек")

        return result

    return wrapper


⸻

8.3 Ограничение доступа (пример авторизации)

from functools import wraps

def require_auth(func):

    @wraps(func)
    def wrapper(user):

        if not user.get("is_authenticated"):
            raise PermissionError("Нет доступа")

        return func(user)

    return wrapper


⸻

8.4 Кэширование результата

from functools import wraps

def cache(func):

    memory = {}

    @wraps(func)
    def wrapper(*args):

        if args in memory:
            print("Из кэша")
            return memory[args]

        result = func(*args)

        memory[args] = result

        return result

    return wrapper

Пример:

@cache
def fib(n):

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

print(fib(10))


⸻

9. Декораторы методов класса

Работают аналогично функциям.

from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):

        print(f"Метод {func.__name__}")

        return func(self, *args, **kwargs)

    return wrapper

Использование:

class User:

    @logger
    def login(self):
        print("Login")

u = User()
u.login()


⸻

10. Встроенные декораторы Python

⸻

10.1 @staticmethod

Метод без self.

class Math:

    @staticmethod
    def add(a, b):
        return a + b

Вызов:

Math.add(2, 3)


⸻

10.2 @classmethod

Получает cls.

class User:

    count = 0

    def __init__(self):
        User.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


⸻

10.3 @property

Делает метод свойством.

class User:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

Использование:

u = User(25)

print(u.age)


⸻

11. Декораторы класса

Можно декорировать классы.

def add_method(cls):

    def hello(self):
        print("Hello")

    cls.hello = hello

    return cls

Использование:

@add_method
class User:
    pass

u = User()
u.hello()


⸻

12. Частые ошибки

⸻

Ошибка 1 — забыли return wrapper

def decorator(func):

    def wrapper():
        pass

    # забыли return wrapper

Результат:

TypeError: 'NoneType' object is not callable


⸻

Ошибка 2 — нет *args **kwargs

def decorator(func):

    def wrapper():
        return func()

Функция с аргументами сломается.

⸻

Ошибка 3 — нет wraps

Теряются:
	•	имя функции
	•	документация
	•	аннотации

⸻

13. Практические задания

⸻

Задание 1 — простой логгер

Написать декоратор:

log_call

Который выводит:

Функция <name> вызвана


⸻

Задание 2 — повтор функции

Написать декоратор:

repeat(n)

Который вызывает функцию n раз.

Пример:

@repeat(3)
def hello():
    print("Hi")

Результат:

Hi
Hi
Hi


⸻

Задание 3 — проверка типов

Создать декоратор:

check_types

Который проверяет:
	•	все аргументы — int

Иначе:

TypeError


⸻

Задание 4 — ограничение времени

Создать декоратор:

timeout(seconds)

Если функция выполняется дольше — ошибка.

⸻

14. Итоговая структура понимания

Минимальный уровень:
	•	функции как объекты
	•	вложенные функции
	•	return функции
	•	@decorator

Средний уровень:
	•	*args **kwargs
	•	wraps
	•	декораторы с параметрами
	•	стек декораторов

Продвинутый уровень:
	•	кэширование
	•	контроль доступа
	•	классовые декораторы
	•	метапрограммирование