print("Введите запрашиваемые данные для анкеты: ")
first_name: str = input("Имя: ")
last_name: str = input("Фамилия: ")
age: int = int(input("Возраст: "))
live_city: str = input("Город проживания: ")
favorite_subject_school: str = input("Любимый предмет в школе: ")
grade_favorite_subject: int = int(input("Оценка по любимому предмету в школе: "))
height: int = int(input("Рост(СМ): "))
weight: int = int(input("Вес(КГ): "))


# Вариант, которые мне не нравятся
# anketa: str = "=====================\nАНТЕТА ПОЛЬЗОВАТЕЛЯ\n=================\nИмя"

# Варианты, которые мне не нравятся
# print("=" * 25, "АНКЕТА ПОЛЬЗОВАТЕЛЯ", "=" * 25, "Имя: {}".format(first_name), sep="\n")

# Вариант, который нравится
anketa: str = f"""
{"=" * 25}
АНКЕТА ПОЛЬЗОВАТЕЛЯ
{"=" * 25}
Имя: {first_name}
Фамилия: {last_name}
Город: {live_city}

Возраст: {age} лет
Через 5 лет: {age + 5} лет

Любимый предмет: {favorite_subject_school}
Оценка: {grade_favorite_subject}

Рост: {height} см ({height / 100} м)
Вес: {weight} кг

Индекс массы тела: {weight / ((height / 100) ** 2)}

{"=" * 25}
"""
print(anketa)

file = open("data.txt", "w")
print(anketa, file=file)
file.close()
