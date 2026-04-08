fruits: set[str] = {'apple', 'banana', 'mango', 'kiwi', 'pear', 'orange'}
fruits.remove("apple")
fruits.discard("apple")
fruit_pop = fruits.pop()
fruits.clear()
print(fruit_pop, fruits)
