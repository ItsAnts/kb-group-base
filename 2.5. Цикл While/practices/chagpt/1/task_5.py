password: str = "admin123"

user_password: str = ""
while user_password != password:
    user_password = input("Введите пароль: ")

print("Доступ разрешен")