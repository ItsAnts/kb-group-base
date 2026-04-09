clients1 = ["Иван", "Мария", "Олег"]
clients2 = ["Анна", "Сергей"]

index: int = 0
while index != len(clients2):
    clients1.append(clients2[index])
    index += 1
print(clients1)