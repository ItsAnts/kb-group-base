debt: int = 120000
count_payment: int = 0
# payment: int = 

while debt != 0:
    payment: int = int(input("Введите сумму платежа: "))
    count_payment += 1
    if payment >= debt:
        transaction = payment - debt
        debt = 0
        print(f"Cумму к возврату: {transaction}")
    else:
        debt = debt - payment
    
print(f"Кол-во платежей: {count_payment}\nИтоговоый долг: {debt}")
