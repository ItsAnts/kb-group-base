my_dict = {"username": "Nikita", "age": 28}
new_dict = my_dict
print(my_dict, new_dict, sep="\n")

my_dict["age"] = 35
new_dict["username"] = "Stas"
print(my_dict, new_dict, sep="\n")

print("=" * 15)

test_my_dict = {"username": "Nikita", "age": 28}
test_new_dict = test_my_dict.copy()
print(test_my_dict, test_new_dict, sep="\n")
test_my_dict["age"] = 14
test_new_dict["username"] = "Stas"
print(test_my_dict, test_new_dict, sep="\n")