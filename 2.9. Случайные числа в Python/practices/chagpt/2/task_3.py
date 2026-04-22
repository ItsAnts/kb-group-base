"""
Уровень 2 — Средний

Задача 3: Распределение рекламного бюджета

Контекст

Компания распределяет рекламный бюджет по каналам.

Вводные данные

Каналы:

channels = [
"Google Ads",
"Facebook",
"Instagram",
"YouTube",
"LinkedIn"
]

Параметры:

- Бюджет на канал: 500–5000 €

Задача

1. Для каждого канала:
   - сгенерировать бюджет
   - сохранить в словарь
2. Рассчитать:
   - общий бюджет
   - канал с максимальным бюджетом
   - канал с минимальным бюджетом

Использовать

- dict
- random.randint
- цикл for
"""

import random
from typing import Optional

channels = ["Google Ads", "Facebook", "Instagram", "YouTube", "LinkedIn"]

budget_marketing: tuple[int, int] = (500, 5000)

marketing: dict[str, int] = {}
analysis: dict[str, Optional[int | str]] = {
    "total_revenue": None,
    "max_budget": None,
    "min_budget": None,
}
for channel in channels:
    marketing[channel] = random.randint(a=budget_marketing[0], b=budget_marketing[1])

for channel, budget in marketing.items():
    if analysis.get("total_revenue") is None:
        analysis["total_revenue"] = budget
        analysis["max_budget"] = channel
        analysis["min_budget"] = channel
    else:
        if (
            type(analysis["total_revenue"]) == int
            and type(analysis["min_budget"]) == str
            and type(analysis["max_budget"]) == str
        ):
            analysis["total_revenue"] += budget
            if marketing[analysis["max_budget"]] < budget:
                analysis["max_budget"] = channel
            if marketing[analysis["min_budget"]] > budget:
                analysis["min_budget"] = channel
print("МАРКЕТИНГ: {}\nАНАЛИЗ МАРКЕТИНГА: {}".format(marketing, analysis))
