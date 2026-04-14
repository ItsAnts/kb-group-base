weeks = [
    [120, 340, 560, 230, 150], # Неделя 1
    [90, 80, 300, 400, 500], # Неделя 2
    [600, 700, 200, 100, 50], # Неделя 3
    [500, 200, 100, 100, 50]
]

# VERSION 1
week_sums: list[int] = [0, 0, 0, 0]
best_week: int = 0
max_revenue: int = 0


for week_index in range(len(weeks)):
    for day_index in range(len(weeks[week_index])):
        week_sums[week_index] += weeks[week_index][day_index]
    if max_revenue < week_sums[week_index]:
        max_revenue = week_sums[week_index]
        best_week = week_index + 1
print("VERSION 1\nWeek sums: {}\nBest week: {}\nMax revenue: {}".format(week_sums, best_week, max_revenue))

# VERSION 2
week_sums = [0, 0, 0, 0]
best_week = 0
max_revenue = 0
count: int = 0
for week in weeks:
    for day in week:
        week_sums[count] += day
    if max_revenue < week_sums[count]:
        max_revenue = week_sums[count]
        best_week = count + 1
    count += 1


print("VERSION 2\nWeek sums: {}\nBest week: {}\nMax revenue: {}".format(week_sums, best_week, max_revenue))
