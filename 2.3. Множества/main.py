users = {"Олег", "Даша", "Настя", "Стас", "Никита", "Олег"}
print(users)
users.add("Настя")
print(users)
users.add("Кирилл")
print(users)

list_cart = ["iPhone", "Картошка", "Доширак", "Чипсы", "Печенья", "Картошка", "Огурцы", "Доширак"]
set_cart = set(list_cart)
print(len(list_cart), list_cart)
print(len(set_cart), set_cart)

new_user: frozenset = frozenset(users)
print(new_user, type(new_user))
my_frozenset = frozenset((1, 2, 3, 4, 5))
set1 = {1,2,3,4}    
set2 = {3,4,5,6}
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)
print(set2.difference(set1))


"""
Напиши код для проверки, есть ли дубликаты в списке с помощью множеств.
"""
products = ["milk", "egg", "apple", "chocolate", "milk"]
if len(products) == len(set(products)):
    print("Дубликатов нет")
else:
    print("Есть дубликаты")