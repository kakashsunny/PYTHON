# Lambda, Map, Filter & Reduce Examples and Practice
from functools import reduce

# 1. Map example: Conversions
temp_celsius = [0, 10, 20, 30]
temp_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temp_celsius))
print("Fahrenheit:", temp_fahrenheit)

# 2. Filter example: Removing empty values
words = ["apple", "", "banana", " ", "cherry", None]
valid_words = list(filter(lambda x: x and x.strip(), words))
print("Valid Words:", valid_words)

# 3. Reduce example: Find maximum in a list
nums = [4, 12, 97, 3, 15]
max_num = reduce(lambda a, b: a if a > b else b, nums)
print("Max value via reduce:", max_num)

# Practice Exercise: Sort list of tuples by second element using lambda
data = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
data.sort(key=lambda item: item[1])
print("Sorted by age:", data)
