"""
Task::01
"""

class Student(object):
    def __init__(self, name: str, age: int, average_grade) -> None:
        self.name: str = name
        self.age: int = age
        self.average_grade: float = average_grade
    
    def display_info(self) -> None:
        print(f"Студент: {self.name}\nВозраст: {self.age}\nСредний балл: {self.average_grade}")

    def update_grade(self, new_grade: float) -> None:
        if 0 >= self.average_grade >= 100:
            raise ValueError("Ошибка средний балл должен быть от 0 до 100")
        self.average_grade = new_grade
    

student_1: Student = Student(name="Никита", age=24, average_grade=4.3)
student_2: Student = Student(name="Стас", age=53, average_grade=3.5)
student_3: Student = Student(name="Олег", age=28, average_grade=5.0)
student_2.update_grade(new_grade=1.6)
group: list[Student] = [student_1, student_2, student_3]
for student in group:
    print(f"{"=" * 15}")
    student.display_info()
    


"""
Напиши класс 'Person', который будет иметь атрибуты 'name' и 'age' и метод 'say_hello', выводящий приветствие.
"""

class Person(object):
    
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        
    def say_hello(self) -> None:
        print(f"Приветствую всех!\nМеня зовут: {self.name} и мне {self.age}")
        
"""
Напиши статический метод в классе 'MathUtils', который будет складывать два числа.
"""

class MathUtils:
    
    @staticmethod
    def sum(a: float | int, b: float | int) -> int | float:
        return a + b
        
print(MathUtils.sum(5, 5))

class Student(object):
    def __init__(self, name: str, age: int, average_grade: float) -> None:
        self.name: str = name
        self.age: int = age
        self.average_grade: float = average_grade
    
    def display_info(self) -> None:
        print(f"Студент: {self.name}\nВозраст: {self.age}\nСредний балл: {self.average_grade}")

    def update_grade(self, grades: list[float]) -> None:
        r: float = 0.0
        for grade in grades:
            r += grade
        self.average_grade = r/len(grades)
        
        
"""
Задача: Реализация корзины интернет-магазина

Общая идея

Реализовать систему корзины покупателя, в которой можно:
	•	добавлять товары
	•	удалять товары
	•	изменять количество товаров
	•	считать общую стоимость
	•	оформлять покупку с учётом остатков товара

Логика должна быть приближена к реальному поведению интернет-магазина.

⸻

Бизнес-контекст

Есть интернет-магазин.
В магазине продаются товары с ограниченным количеством на складе.

Покупатель добавляет товары в корзину.
При оформлении заказа:
	•	проверяется наличие товара
	•	уменьшается количество товара на складе
	•	корзина очищается
"""
from enum import Enum
from typing import Optional

class ProductStatus(Enum):
    STOCK = "stock"
    CART = "cart"
    NO = "no"
    SOLD = "sold"

class Product(object):
    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price
        self.status: ProductStatus = ProductStatus.NO
        self.id: Optional[int] = None 

    def __str__(self) -> str:
        return f"{self.name}"
        
    def __repr__(self) -> str:
        return f"{self.name}"
        
class Warehouse(object):
    count: int = 0
    
    def __init__(self) -> None:
        self.products: list[Product] = []
        
    def add_product(self, product: Product) -> None:
        self.count += 1
        product.id = self.count
        product.status = ProductStatus.STOCK
        self.products.append(product)
    
    def move_product_cart(self, product_id: int) -> Optional[int]:
        for product in self.products:
            if product.id == product_id:
                product.status = ProductStatus.CART
                return product.id
        
    def get_products(self, filter: Optional[ProductStatus] = None) -> Optional[list[Product]]:
        result: list[Product] = []
        if filter is None:
            return self.products
        elif filter == ProductStatus.CART:
            for product in self.products:
                if product.status == filter:
                    result.append(product)
        elif filter == ProductStatus.STOCK:
            for product in self.products:
                if product.status == filter:
                    result.append(product)
        elif filter == ProductStatus.NO:
            for product in self.products:
                if product.status == filter:
                    result.append(product)
        elif filter == ProductStatus.SOLD:
            for product in self.products:
                if product.status == filter:
                    result.append(product)
        
class CartUser(object):
    def __init__(self) -> None:
        self.product_ids: list[int] = []
    
    def add_product(self, product_id: int) -> None:
        self.product_ids.append(product_id)
        
    def clear(self) -> None:
        pass
        
    
    
samsung = Product("Samsung", price=50000.50)
apple = Product("iPhone", price=2532.50)
xiomi = Product("Xiomi", price=42623.50)
    
warehouse = Warehouse()
warehouse.add_product(samsung)
warehouse.add_product(apple)
warehouse.add_product(xiomi)

print(warehouse.get_products())
class OrderUser(object):
    pass