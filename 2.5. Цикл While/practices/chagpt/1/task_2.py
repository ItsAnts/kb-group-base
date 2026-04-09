target: int = 100000
daily_income: int = 15000
current: int = 0
balance: int = 0

while balance < target:
    balance += daily_income
    current += 1
    
print(f"Итоговая сумма: {balance}\nКол-во дней: {current}")
