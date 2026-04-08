from typing import Optional


client_orders = {
    "Иван": {
        "Ноутбук": 1,
        "Мышь": 2
    },
    "Мария": {
        "Клавиатура": 1,
        "Монитор": 2
    }
}

keys: list[str] = list(client_orders.keys()) # ["Иван", "Мария"]
index: int = 0
count_item: int = 0
while index != len(keys):
    nested: Optional[dict[str, int]] = client_orders.get(keys[index])
    # nested = client_orders.get("Иван") 
    # nested = {"Ноутбук": 1, "Мышь": 2}
    if nested:
        count_item = count_item + sum(list(nested.values()))
        #  count_item = 0 + sum([1, 2])
        # count_item = 3
        index += 1
    else:
        break
print(count_item)