equipment = {
    "Принтер": {
        "count": 4,
        "price": 15000
    },
    "Сканер": {
        "count": 2,
        "price": 22000
    }
}

keys: list[str] = list(equipment.keys()) # ["Принтер", "Сканер"]
index: int = 0
result: int = 0
while index != len(keys):
    result = result + (equipment[keys[index]]["count"] * equipment[keys[index]]["price"])
    # result = 0 + (equipment[keys[0]]["count"] * equipment[keys[0]]["price"]) ->
    # result = 0 + (equipment["Принтер"]["count"] * equipment["Принтер"]["price"]) ->
    # result = 0 + (4 * 15000)
    index = index + 1
print(result)


if len(keys) > 0:
    min_item = equipment[keys[0]]["count"]
    now_index: int = 0
    now_result: str = ""
    while now_index != len(keys):
        if equipment[keys[now_index]]["count"] < min_item:
            min_item = equipment[keys[now_index]]["count"]
            now_result = keys[now_index]
        now_index += 1
    print(f"Минимальное кол-во: {now_result}")
else:
    print("Товаров нету")
    
equipment.update({"Телевизор": {"count": 10, "price": 15000}})
equipment["Принтер"]["count"] += 1