# Questions & Answers: Functions

## MCQs
1. **What is the output of the following code?**
   ```python
   def func(x, y=2):
       return x * y
   print(func(y=3, x=4))
   ```
   - A) 8
   - B) 12
   - C) Error
   - D) 6
   - **Answer**: B
   - **Explanation**: Arguments are matched by keyword name, so `x = 4` and `y = 3`. 4 * 3 = 12.

2. **How are variables bound inside functions resolved?**
   - A) Scope Hierarchy: LEGB rule
   - B) Random lookup
   - C) Statically only
   - D) Global space only
   - **Answer**: A
   - **Explanation**: LEGB stands for Local, Enclosing, Global, and Built-in scopes.

## Beginner & Intermediate Questions
### Q1: Explain the difference between `global` and `nonlocal`.
**Answer**: `global` allows code to bind a variable in the global (module) namespace. `nonlocal` allows binding a variable in the nearest enclosing namespace (excluding global) of a nested function.

### Q2: Why is it bad to use a list as a default argument?
**Answer**: Because Python evaluates default arguments only once during function definition. Subsequent calls share the same list object, leading to unintended accumulation of items.

## Coding Practice & Solutions
### Problem: Write a recursive function to calculate the factorial of a number.
**Solution**:
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```
