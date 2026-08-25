# List & Dictionary Comprehensions

## Definitions & Concepts
Comprehensions provide a concise way to create lists, dictionaries, and sets from existing iterables. They are often faster than traditional loops because they are optimized in C under the hood.

## Syntax & Formulas
1. **List Comprehension**: `[expression for item in iterable if condition]`
2. **Dictionary Comprehension**: `{key_expr: val_expr for item in iterable if condition}`
3. **Set Comprehension**: `{expression for item in iterable if condition}`

## Syntax & Examples
```python
# List Comprehension
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]

# Comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]

# Dict Comprehension
square_dict = {x: x**2 for x in range(3)} # {0: 0, 1: 1, 2: 4}
```

## Best Practices
- Keep comprehensions simple. If it spans more than two lines or has nested logic, use standard loops for readability.
- Use comprehensions to write clean, declarative data transformations.

## Common Mistakes
- Writing nested comprehensions that are hard to read and debug.
- Using comprehensions solely for side effects (like printing), where a standard `for` loop should be used instead.

## Interview Tips
- **Q**: Are comprehensions faster than loops?
- **A**: Yes, generally. List comprehensions execute at C-level speed inside the Python interpreter, which eliminates some overhead of loop execution and list appends.
