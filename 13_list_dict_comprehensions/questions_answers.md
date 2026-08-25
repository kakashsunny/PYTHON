# Questions & Answers: List/Dict Comprehensions

## MCQs
1. **What is the result of `[x for x in range(3) for y in range(2)]`?**
   - A) `[0, 1, 2]`
   - B) `[0, 0, 1, 1, 2, 2]`
   - C) `[0, 1, 0, 1, 0, 1]`
   - D) Error
   - **Answer**: B
   - **Explanation**: The nested loop evaluates outer loop first, then inner loop. Length is 3 * 2 = 6.

2. **Which of the following creates a dictionary matching lowercase characters to uppercase values using comprehension?**
   - A) `{c: c.upper() for c in "abc"}`
   - B) `[c: c.upper() for c in "abc"]`
   - C) `(c: c.upper() for c in "abc")`
   - D) `{c, c.upper() for c in "abc"}`
   - **Answer**: A
   - **Explanation**: Curly braces `{}` with `key: value` syntax defines dictionary comprehensions.

## Beginner & Intermediate Questions
### Q1: What is a generator expression and how does it differ from a list comprehension?
**Answer**: A generator expression uses parentheses `()` instead of square brackets `[]` (e.g. `(x**2 for x in range(100))`). It returns a generator object that computes values lazily (one at a time) rather than building the entire list in memory, making it highly memory efficient for large datasets.

### Q2: How do you add an `if-else` condition inside a list comprehension?
**Answer**: The conditional expression `val_1 if cond else val_2` must be placed BEFORE the `for` clause:
```python
[x if x > 0 else 0 for x in values]
```

## Coding Practice & Solutions
### Problem: Create a dictionary that contains numbers from 1 to 5 as keys and their factorials as values.
**Solution**:
```python
import math
fact_dict = {x: math.factorial(x) for x in range(1, 6)}
print(fact_dict)  # {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
```
