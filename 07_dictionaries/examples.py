# Dictionaries Examples and Practice

# 1. Safe Access and Defaults
catalog = {"item_1": "Book", "item_2": "Pen"}
# Direct access fails with KeyError
try:
    print(catalog["item_3"])
except KeyError as e:
    print("Caught expected KeyError for key:", e)

# Use get() for safety
print("item_3:", catalog.get("item_3", "Not Available"))

# 2. Dictionary Iteration
employee = {"name": "Charlie", "department": "HR", "salary": 50000}
for key, value in employee.items():
    print(f"{key.capitalize()}: {value}")

# 3. Merging Dictionaries (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = d1 | d2  # Merge operator
print("Merged dictionary:", merged)

# Practice: Word Counter
def count_words(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

print(count_words("apple banana apple cherry banana apple"))
