Уровень 1 — Лёгкий

Тема: расчёт выручки по заказам

Вводные

Интернет-магазин продаёт товары.
Есть список заказов за день.
Каждый заказ содержит:

- название товара
- количество
- цену за единицу

Нужно автоматизировать расчёт выручки.

⸻

Данные

orders = [
{"product": "Laptop", "quantity": 2, "price": 900},
{"product": "Mouse", "quantity": 5, "price": 20},
{"product": "Keyboard", "quantity": 3, "price": 45},
{"product": "Monitor", "quantity": 1, "price": 300}
]

⸻

Задачи

1. Написать функцию:

def calculate_order_total(order):

Функция должна:

- принимать один заказ
- возвращать сумму заказа

Формула:

quantity \* price

⸻

2. Написать функцию:

def calculate_total_revenue(orders):

Функция должна:

- пройти по списку заказов
- использовать calculate_order_total()
- вернуть общую выручку

⸻

3. Написать функцию:

def find_large_orders(orders, threshold):

Функция должна:

- вернуть список заказов
- у которых сумма больше threshold

⸻

Уровень 2 — Средний

Тема: анализ продаж по сотрудникам

Вводные

Компания ведёт учёт продаж сотрудников.
Каждая продажа содержит:

- имя сотрудника
- сумма продажи

Нужно определить эффективность сотрудников.

⸻

Данные

sales = [
{"employee": "Anna", "amount": 1200},
{"employee": "Boris", "amount": 800},
{"employee": "Anna", "amount": 700},
{"employee": "Dmitry", "amount": 1500},
{"employee": "Boris", "amount": 400},
{"employee": "Anna", "amount": 600},
]

⸻

Задачи

1. Написать функцию:

def total_sales_by_employee(sales):

Функция должна:

- вернуть словарь:

{
"Anna": 2500,
"Boris": 1200,
"Dmitry": 1500
}

Использовать:

- цикл
- словарь

⸻

2. Написать функцию:

def find_top_employee(employee_totals):

Функция должна:

- вернуть имя сотрудника
- с максимальными продажами

⸻

3. Написать функцию:

def employees_above_average(employee_totals):

Функция должна:

- вычислить среднюю выручку
- вернуть список сотрудников
- выше среднего значения

⸻

Уровень 3 — Тяжёлый

Тема: управление складом и прибыльностью

Вводные

Компания хранит данные о товарах на складе.
Для каждого товара известны:

- название
- закупочная цена
- цена продажи
- количество на складе
- проданное количество

Нужно рассчитать прибыль и определить проблемные товары.

⸻

Данные

products = [
{
"name": "Laptop",
"cost_price": 700,
"sell_price": 900,
"stock": 10,
"sold": 6
},
{
"name": "Mouse",
"cost_price": 10,
"sell_price": 20,
"stock": 50,
"sold": 30
},
{
"name": "Keyboard",
"cost_price": 25,
"sell_price": 45,
"stock": 20,
"sold": 5
},
{
"name": "Monitor",
"cost_price": 200,
"sell_price": 300,
"stock": 15,
"sold": 2
}
]

⸻

Задачи

1. Прибыль по товару

Написать функцию:

def calculate_product_profit(product):

Функция должна вернуть:

(sell_price - cost_price) \* sold

⸻

2. Общая прибыль компании

Написать функцию:

def calculate_total_profit(products):

Функция должна:

- использовать calculate_product_profit()
- вернуть суммарную прибыль

⸻

3. Неликвидные товары

Написать функцию:

def find_slow_moving_products(products, min_sales):

Функция должна вернуть список товаров:

- у которых sold < min_sales

⸻

4. Рейтинг товаров по прибыли

Написать функцию:

def rank_products_by_profit(products):

Функция должна:

- вернуть список товаров
- отсортированный по прибыли
- по убыванию

Использовать:

- функцию
- сортировку
- lambda

⸻

Дополнительные задачи (усложнение уровня 3)

1. Добавить функцию:

def calculate_stock_value(products):

Вернуть:

cost_price \* stock

Для всех товаров — общая стоимость склада.

⸻

2. Добавить функцию:

def find_loss_products(products):

Вернуть товары:

sell_price < cost_price
