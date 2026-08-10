# Strings & Formatting in Python

## Definitions & Concepts
Strings in Python are sequences of Unicode characters. They are immutable, meaning once created, they cannot be altered in-place.

## String Formatting Methods
1. **Old style (% formatting)**: `"%s is %d years old" % (name, age)`
2. **New style (`.format()`)**: `"{0} is {1} years old".format(name, age)`
3. **f-Strings (formatted string literals - Python 3.6+)**: `f"{name} is {age} years old"`

## Useful String Methods
- `.strip()`: Removes leading/trailing whitespace.
- `.split(separator)`: Splits a string into a list.
- `.join(iterable)`: Joins elements of an iterable into a string.
- `.lower()`, `.upper()`: Conversions.
- `.find()`, `.replace()`: Searching and replacing.

## Syntax & Examples
```python
# Immutable behavior
s = "hello"
# s[0] = 'H' -> TypeError

# f-strings with expressions
x = 10
y = 20
print(f"Sum of {x} and {y} is {x + y}")

# Aligning and padding with f-strings
text = "python"
print(f"{text:>10}")  # Right-aligned, width 10
print(f"{text:*^10}") # Centered, padded with '*'
```

## Best Practices
- Always prefer f-Strings for readability and performance.
- Use raw strings `r"..."` for regular expressions or Windows file paths to avoid escape sequence issues.

## Common Mistakes
- Attempting to modify a string character directly.
- Forgetting that string methods return a new string rather than modifying the original.

## Interview Tips
- **Q**: Why are strings immutable in Python?
- **A**: Immutability makes strings hashable (so they can be keys in dictionaries), safe for multithreading, and allows memory optimization (string interning).
