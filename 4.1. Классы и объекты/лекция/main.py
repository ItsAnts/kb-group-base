class Cat:
    onwer: str = "Крейг"
    
    def __init__(self, name: str, weight: float) -> None:
        self.name: str = name
        self.weight: float = weight
        
    def eat(self, food: str) -> None:
        self.weight += 1.0
        print("{} поел {}".format(self.name, food))
        
object1: Cat = Cat(name="Тур", weight=15.3)
object2: Cat = Cat(name="Уур", weight=13.2)

print(object1.onwer)
print(object2.onwer)
object2.onwer = "Лолтул"
print(object1.onwer)
print(object2.onwer)

print(object1.weight)
print(object2.weight)
object1.eat("Капуста")
print(object1.weight)
print(object2.weight)
