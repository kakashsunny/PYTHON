# Operators in Python

## Definitions & Concepts
Operators are special symbols that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

## Operator Types
1. **Arithmetic**: `+`, `-`, `*`, `/`, `%` (modulo), `//` (floor division), `**` (exponentiation).
2. **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
3. **Logical**: `and`, `or`, `not`.
4. **Bitwise**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift).
5. **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, etc.
6. **Identity**: `is`, `is not` (checks if two variables refer to the same object in memory).
7. **Membership**: `in`, `not in` (checks if a value is present in a sequence like a list or string).

## Syntax & Examples
```python
# Division vs Floor Division vs Modulo
print(5 / 2)   # 2.5
print(5 // 2)  # 2
print(5 % 2)   # 1

# Exponentiation
print(2 ** 3)  # 8

# Identity vs Comparison
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True (values are equal)
print(a is b)  # False (different memory addresses)
print(a is c)  # True (same object)
```

## Best Practices
- Use parentheses to clearly indicate precedence in complex boolean expressions.
- Prefer `is` and `is not` for comparisons with singletons like `None`.

## Common Mistakes
- Confusing `==` (equality) with `is` (identity).
- Forgetting that `/` returns a float, even if the division is clean.

## Interview Tips
- **Q**: What is the difference between `==` and `is`?
- **A**: `==` compares the actual values/content of the operands, whereas `is` compares their identity (memory addresses) to check if they refer to the exact same object.
