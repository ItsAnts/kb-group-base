stock: list[int] = [5, 12, 7, 3, 9]
if len(stock) == 0:
    print("Склад пустой")
else:
    general_count_goods: int = 0
    max_stock: int = stock[0]
    min_stock: int = stock[0]
    index: int = 0
    
    while index != len(stock):
        general_count_goods = general_count_goods + stock[index]
        
        if max_stock < stock[index]:
            max_stock = stock[index]
        
        if min_stock > stock[index]:
            min_stock = stock[index]
        
        index = index + 1
    
    print(f"Общее кол-во товаров: {general_count_goods}\nМаксимальный остаток: {max_stock}\nМинимальный остаток: {min_stock}")
