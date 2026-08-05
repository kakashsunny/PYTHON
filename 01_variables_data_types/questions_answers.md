# Questions & Answers: Variables & Data Types

## MCQs
1. **What is the output of `type(1 / 2)` in Python 3?**
   - A) `<class 'int'>`
   - B) `<class 'float'>`
   - C) `<class 'double'>`
   - D) Error
   - **Answer**: B
   - **Explanation**: In Python 3, division using `/` always returns a float.

2. **Which of the following is an invalid variable name?**
   - A) `_user_1`
   - B) `user_name`
   - C) `1_user`
   - D) `User`
   - **Answer**: C
   - **Explanation**: Variable names cannot start with a digit.

## Beginner & Intermediate Questions
### Q1: What does dynamic typing mean in Python?
**Answer**: It means that the type of a variable is determined at runtime based on the value currently assigned to it, rather than being declared explicitly in code before usage.

### Q2: Explain the difference between `str()` and `repr()`.
**Answer**: `str()` is meant to return a user-friendly, readable string representation of an object, while `repr()` is meant to return an unambiguous string representation, often matching the code needed to recreate the object.

## Coding Practice & Solutions
### Problem: Swap two variables without using a third variable.
**Solution**:
```python
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")  # Output: a = 10, b = 5
```
