# Questions & Answers: Lambda, Map, Filter, Reduce

## MCQs
1. **What is the output of `list(map(lambda x: x * 2, [1, 2]))`?**
   - A) `[1, 2, 1, 2]`
   - B) `[2, 4]`
   - C) `[1, 4]`
   - D) Error
   - **Answer**: B
   - **Explanation**: The lambda multiplies each item by 2, yielding 2 and 4.

2. **In which module is the `reduce` function located?**
   - A) `sys`
   - B) `math`
   - C) `functools`
   - D) `collections`
   - **Answer**: C
   - **Explanation**: `reduce` was moved from standard builtins to the `functools` module in Python 3.

## Beginner & Intermediate Questions
### Q1: What is an anonymous function?
**Answer**: An anonymous function is a function defined without a name. In Python, these are created using the `lambda` keyword.

### Q2: Write a list comprehension that is equivalent to `list(filter(lambda x: x % 2 == 0, range(10)))`.
**Answer**:
```python
[x for x in range(10) if x % 2 == 0]
```

## Coding Practice & Solutions
### Problem: Use `reduce` to compute the factorial of a number `n`.
**Solution**:
```python
from functools import reduce
def factorial_reduce(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial_reduce(5))  # 120
```
