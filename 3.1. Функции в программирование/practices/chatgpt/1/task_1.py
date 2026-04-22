orders: list[dict[str, str | int]] = [
    {"product": "Laptop", "quantity": 2, "price": 900},
    {"product": "Mouse", "quantity": 5, "price": 20},
    {"product": "Keyboard", "quantity": 3, "price": 45},
    {"product": "Monitor", "quantity": 1, "price": 300},
]


def calculate_order_total(order: dict) -> int | None:
    if order.get("quantity") and order.get("price"):
        return order["quantity"] * order["price"]
    return None


def calculate_total_revenue(orders: list[dict]) -> int:
    result: int = 0
    for order in orders:
        if order.get("quantity") and order.get("price"):
            result = result + (order["quantity"] * order["price"])
    return result


def find_large_orders(
    orders: list[dict[str, str | int]], threshold: int
) -> list[dict[str, str | int]]:
    result: list[dict[str, str | int]] = []
    for order in orders:
        if (
            order.get("quantity")
            and order.get("price")
            and type(order["quantity"]) == int
            and type(order["price"]) == int
        ):
            if order["quantity"] * order["price"] > threshold:
                result.append(order)
    return result


print(
    "Заказы больше 150 рублей: {}".format(
        find_large_orders(orders=orders, threshold=150)
    )
)


print("ОБЩАЯ ВЫРУЧКА: {}".format(calculate_total_revenue(orders=orders)))


for order in orders:
    result: int | None = calculate_order_total(order=order)
    print("ПРОДУКТ: {}, РЕЗУЛЬТАТ: {}".format(order["product"], result))
