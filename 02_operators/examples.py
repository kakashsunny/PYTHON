# Operators Examples and Practice

# 1. Floor Division and Modulo
dividend = 17
divisor = 5
quotient = dividend // divisor
remainder = dividend % divisor
print(f"{dividend} = {divisor} * {quotient} + {remainder}")

# 2. Identity vs Equality
x = [10, 20]
y = [10, 20]
z = x

print("x == y:", x == y)  # True
print("x is y:", x is y)  # False
print("x is z:", x is z)  # True

# 3. Membership Operators
fruits = ["apple", "banana", "cherry"]
print("Is apple in list?", "apple" in fruits)
print("Is grape not in list?", "grape" not in fruits)

# Practice: Bitwise operations
# 5 is 0101, 3 is 0011
# 5 & 3 = 0001 (1)
# 5 | 3 = 0111 (7)
print("5 & 3:", 5 & 3)
print("5 | 3:", 5 | 3)
