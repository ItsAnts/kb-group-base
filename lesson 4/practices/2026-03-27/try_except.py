try:
    age: int = int(input("Введите ваш возраст"))

    if age < 0:
        raise ValueError
    elif age < 13:
        print("Ты ребёнок")
    elif 13 <= age <= 17:
        print("Ты подросток")
    else:
        print("Ты взрослый")
except ValueError:
    print("Ошибка ввода")
