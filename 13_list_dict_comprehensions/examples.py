# List & Dictionary Comprehensions Examples and Practice

# 1. Simple List and Set Comprehensions
nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in nums}
print("Unique Squares Set:", unique_squares)

# 2. Conditional List Comprehension with if-else (Note syntax order change!)
# Syntax: [expr_true if condition else expr_false for item in iterable]
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print("Labels:", labels)

# 3. Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flattened Matrix:", flat)

# Practice Exercise: Filter list of dicts
users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"}
]
admins = [u["name"] for u in users if u["role"] == "admin"]
print("Admins:", admins)
