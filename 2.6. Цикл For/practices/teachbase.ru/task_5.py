text: str = "Программирование на Python"
vowels: str = "аеёиоуыэюя"

text = text.lower()
count: int = 0
for char in text:
    if char.lower() in vowels:
        count += 1

print("КОЛ-ВО ГЛАСНЫХ БУКВ = {}".format(count))
