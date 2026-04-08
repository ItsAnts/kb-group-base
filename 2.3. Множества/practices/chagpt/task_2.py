"""
Задача 2 — Общие клиенты двух филиалов

Уровень: средний
Контекст: сеть магазинов

Условие

Компания имеет два филиала.
Каждый филиал ведёт список клиентов, совершивших покупки за месяц.
branch_a_clients = {
    "Ivanov",
    "Petrov",
    "Sidorov",
    "Smirnov",
    "Kuznetsov"
}

branch_b_clients = {
    "Smirnov",
    "Popov",
    "Ivanov",
    "Volkov",
    "Fedorov"
}
Требуется
	1.	Найти клиентов, которые покупали в обоих филиалах.
	2.	Найти клиентов, которые покупали только в филиале A.
	3.	Найти клиентов, которые покупали только в одном из филиалов.
	4.	Определить общее количество уникальных клиентов по двум филиалам.

Бизнес-смысл

Используется для:
	•	анализа пересечения клиентских баз
	•	выявления лояльных клиентов
	•	планирования маркетинговых акций
"""

branch_a_clients = {
    "Ivanov",
    "Petrov",
    "Sidorov",
    "Smirnov",
    "Kuznetsov"
}

branch_b_clients = {
    "Smirnov",
    "Popov",
    "Ivanov",
    "Volkov",
    "Fedorov"
}
clients_union = branch_a_clients.union(branch_b_clients)
clients_only_bracnh_a = branch_a_clients.difference(branch_b_clients)
clients_only_branch_a_and_only_branch_b = branch_a_clients.symmetric_difference(branch_b_clients)
print(f"Список клиентов которые купили в обоих филилалах: {clients_union}")
print(f"Список клиентов которые купили только в филилале А: {clients_only_bracnh_a}")
print(f"Список клиентов, которые только покупали либо в филиале А или Б: {clients_only_branch_a_and_only_branch_b}")
print(f"Кол-во уникальный клиентов по двум филиалом: {len(clients_union)}")