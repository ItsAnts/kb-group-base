list_one: list[str] = ["one", "two", "three", "four", "five"]
list_two: list[int] = [1, 2, 3, 4, 5]

the_dict: dict[str, int] = dict(zip(list_one, list_two))
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
new_dict: dict[int, str] = dict(zip(list_two, list_one))
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(the_dict)
print(new_dict)
print(new_dict[4])
print(the_dict["three"])

