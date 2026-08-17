# Dictionaries in Python

## Definitions & Concepts
A dictionary is an unordered (ordered by insertion since Python 3.7), mutable collection of key-value pairs. Keys must be unique and hashable.

## Syntax & Examples
```python
# Creating dictionaries
user = {
    "name": "Bob",
    "age": 28,
    "email": "bob@example.com"
}

# Accessing keys
print(user["name"]) # Bob

# Accessing non-existing key (safely)
print(user.get("phone", "No Phone Provided")) # Returns default

# Adding and modifying
user["phone"] = "555-0199"
user["age"] = 29
```

## Useful Methods
- `.keys()`: Returns view of keys.
- `.values()`: Returns view of values.
- `.items()`: Returns view of key-value tuples.
- `.pop(key)`: Removes key and returns its value.
- `.update(other_dict)`: Merges another dictionary.

## Best Practices
- Use `.get(key, default)` when you are not sure if a key exists to avoid `KeyError`.
- Use dictionary comprehensions for creating dictionaries dynamically.

## Common Mistakes
- Modifying a dictionary while iterating over it (raises `RuntimeError`). Iterate over `.keys()` or a copy instead.
- Using unhashable types (like lists or sets) as keys.

## Interview Tips
- **Q**: How are dictionaries implemented in Python?
- **A**: Dictionaries are implemented as hash tables. This provides highly efficient O(1) average time complexity for lookups, insertions, and deletions.
