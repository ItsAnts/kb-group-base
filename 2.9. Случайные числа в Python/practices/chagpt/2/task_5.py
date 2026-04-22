"""

Уровень 3 — Тяжёлый

Задача 5: Анализ продаж по филиалам

Контекст

Компания имеет несколько филиалов.
Каждый филиал делает продажи ежедневно.

Вводные данные

Филиалы:

branches = [
"Berlin",
"Hamburg",
"Munich",
"Cologne"
]

Параметры:

- Дней: 10
- Продажи филиала в день: 1000–7000 €

Структура хранения

{
"Berlin": [список продаж по дням],
...
}

Задача

1. Для каждого филиала:
   - сгенерировать продажи на каждый день
   - сохранить в словарь
2. Рассчитать:
   - общую выручку по каждому филиалу
   - самый прибыльный филиал
   - самый прибыльный день среди всех филиалов
   - среднюю выручку на день
"""

import random
from typing import Optional

branches = ["Berlin", "Hamburg", "Munich", "Cologne"]
parametr: dict[str, list[int]] = {"days": [10], "sales_day": [1000, 7000]}

data: dict[str, list[int]] = {}
for branch in branches:
    data[branch] = []
    for day in range(parametr["days"][0]):
        data[branch].append(
            random.randint(parametr["sales_day"][0], parametr["sales_day"][1])
        )

analysis: dict[str, Optional[str | int]] = {
    "max_profit_branch": None,
    "max_profit_day_branches": None,
    "revenue": 0,
}
for branch, sales in data.items():
    analysis[branch] = sum(sales)
    if type(analysis["revenue"]) == int:
        analysis["revenue"] += sum(sales)
    if analysis["max_profit_branch"] is None:
        analysis["max_profit_branch"] = branch
        analysis["max_profit_day_branches"] = max(sales)
    else:
        if (
            type(analysis["max_profit_branch"]) == str
            and type(analysis["max_profit_day_branches"]) == int
        ):
            if sum(sales) > sum(data[analysis["max_profit_branch"]]):
                analysis["max_profit_branch"] = branch
            if max(sales) > analysis["max_profit_day_branches"]:
                analysis["max_profit_day_branches"] = max(sales)

report: str = (
    "ОБЩАЯ ВЫРУЧКА ПО КАЖДОМУ ФИЛИАЛУ: {}\nСАМЫЙ ПРИБЫЛЬНЫЙ ФИЛИАЛ: {}\nСАМЫЙ ПРИБЫЛЬНЫЙ ДЕНЬ СРЕДИ ФИЛИАЛОВ: {}\nСРЕДНЯЯ ВЫРУЧКА ЗА ДЕНЬ: {}".format(
        analysis,
        analysis["max_profit_branch"],
        analysis["max_profit_day_branches"],
        analysis["revenue"] / parametr["days"][0],
    )
)
print(report)
