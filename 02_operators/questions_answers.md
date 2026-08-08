# Questions & Answers: Operators

## MCQs
1. **What is the output of `3 ** 2 ** 3` in Python?**
   - A) 729
   - B) 6561
   - C) 512
   - D) 243
   - **Answer**: B
   - **Explanation**: Exponentiation operators are right-associative, so it is evaluated as `3 ** (2 ** 3)` which is `3 ** 8 = 6561`.

2. **What does `is` evaluate?**
   - A) Values
   - B) Data Types
   - C) Memory address equality
   - D) Logical equivalence
   - **Answer**: C
   - **Explanation**: The `is` operator checks if two references point to the same object in memory.

## Beginner & Intermediate Questions
### Q1: What is the output of `bool([])` and `bool(0)`?
**Answer**: Both evaluate to `False`. Empty lists and zero values are falsy in Python.

### Q2: What is operator precedence and how can we override it?
**Answer**: Operator precedence determines the order in which operators are evaluated. We can override this using parentheses `()`.

## Coding Practice & Solutions
### Problem: Write a function to check if a given number is even without using the `%` operator.
**Solution**:
```python
def is_even_bitwise(n):
    # If the least significant bit is 0, the number is even
    return (n & 1) == 0

print(is_even_bitwise(4))  # True
print(is_even_bitwise(7))  # False
```
