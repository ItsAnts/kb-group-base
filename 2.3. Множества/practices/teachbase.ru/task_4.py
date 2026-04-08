a: set[int] = {1, 2, 3, 4}
b: set[int] = {3, 4, 5, 6}
# объединение
set_union = a.union(b)
# пересечение
set_intersection = a.intersection(b)
# разность
set_difference = a.difference(b)
# симметрическая разность
set_symmetric_difference = a.symmetric_difference(b)

report: str = f"Множество a: {a}\nМножество b: {b}\nОбъединение: {set_union}\nПересечение: {set_intersection}\nРазность: {set_difference}\nСимметрическая разность: {set_symmetric_difference}"
print(report)