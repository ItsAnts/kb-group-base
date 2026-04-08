accounts = {
    "Основной": 250000,
    "Резервный": 120000,
    "Зарплатный": 98000
}
accounts_copy = accounts.copy()
print(accounts)
print(accounts["Резервный"])
accounts["Инвестиционный"] = 50000
del accounts["Зарплатный"]

if accounts.get("Кредитный"):
    print("Такого типа счет нет")
else:
    print("Такой счет есть")
    
# /// Через цикл 

iteratio: int = 0
keys: list[str] = list(accounts_copy.keys())
while iteratio != len(accounts_copy):
    print(f"СЧЕТ: {keys[iteratio]} имеет ОСТАТОК - {accounts_copy[keys[iteratio]]}")
    iteratio = iteratio + 1
