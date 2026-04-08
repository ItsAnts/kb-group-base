users: set[str] = {"Alice", "Tom", "Alex", "Alice", "John"}
# {'Tom', 'John', 'Alice', 'Alex'}
print(users)
users.add("Loki")
print(users)
for user in users:
    print(user)
    
"""
students: set[str] = {f"дима", "даша", "алексей", "Ирина", "Олег", "Дима"}
student: str = "даша"
for student in students:
    students.remove(student)
print(students)
"""

set1: set[int] = {1, 2, 3, 4}
set2: set[int] = {1, 2, 3, 4}
result1 = set1.intersection(set2)
result2 = set1 & set2
print(result1, result2)