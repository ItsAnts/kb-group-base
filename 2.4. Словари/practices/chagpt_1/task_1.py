clients = {
    "Иван": 12000,
    "Мария": 8500,
    "Олег": 23000
}

iteratio: int = 0
keys: list[str] = list(clients.keys())
while iteratio != len(clients):
    print(f"КЛИЕНТ: {keys[iteratio]} | БАЛАНС: {clients[keys[iteratio]]}")
    iteratio = iteratio + 1
    
print(f"Баланс клиента Мария: {clients['Мария']}")

clients["Анна"] = 15000
clients.pop("Олег", None)