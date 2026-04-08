warehouse = {
    "Ноутбук": {
        "price": 75000,
        "quantity": 4
    },
    "Мышь": {
        "price": 1200,
        "quantity": 25
    }
}

iteratio: int = 0
keys = list(warehouse.keys())
sum_warehouse = 0
while iteratio != len(warehouse):
    sum_warehouse = sum_warehouse + (warehouse[keys[iteratio]]["price"] * warehouse[keys[iteratio]]["quantity"])
    iteratio += 1
    
print(f"Cумма склада:  {sum_warehouse}")