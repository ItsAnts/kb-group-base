tax_rate: float = 0.19  # 19% налог

orders: list[dict[str, str | int | float]] = [
    {"product": "book", "price": 30},
    {"product": "pen", "price": 5},
    {"product": "notebook", "price": 12},
]


def calculate_price_with_tax(price: int | float) -> float:
    return price + (tax_rate * price)


def get_all_prices_with_tax(
    orders: list[dict[str, str | int | float]],
) -> list[dict[str, str | int | float]]:
    for order in orders:
        if "price" in order and isinstance(order["price"], (int, float)):
            order["price"] = calculate_price_with_tax(price=order["price"])
    return orders


print("ДО НАЛОГА: {}".format(orders))

orders = get_all_prices_with_tax(orders=orders)
print("ПОСЛЕ НАЛОГА: {}".format(orders))


def apply_discount(price: float | int) -> float | int:
    discount: float = 0.1
    return price - (price * discount)


"""
3. Локальная скидка

Написать функцию:

def apply_discount(price):

Требования:

- создать локальную переменную discount = 0.1
- вернуть цену со скидкой


"""
