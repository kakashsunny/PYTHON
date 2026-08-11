# Questions & Answers: Conditionals

## MCQs
1. **Which of the following values is considered 'truthy' in a conditional check?**
   - A) `[]`
   - B) `0.0`
   - C) `[0]`
   - D) `""`
   - **Answer**: C
   - **Explanation**: A non-empty list `[0]` is truthy, even though its element is zero. Empty structures and zero floats are falsy.

2. **In Python 3.10+, what matches anything in a `match-case` statement?**
   - A) `case default`
   - B) `case *`
   - C) `case _`
   - D) `case else`
   - **Answer**: C
   - **Explanation**: The underscore `_` acts as a wildcard pattern to match anything.

## Beginner & Intermediate Questions
### Q1: What is short-circuit evaluation?
**Answer**: It is a behavior where logical operators (`and`, `or`) stop evaluating as soon as the outcome is determined. For example, in `A and B`, if `A` is False, `B` is not evaluated.

### Q2: Write a ternary expression to check if a number is positive, negative, or zero.
**Answer**:
```python
result = "Positive" if n > 0 else ("Negative" if n < 0 else "Zero")
```

## Coding Practice & Solutions
### Problem: Leap year check. Write a program to check if a year is leap.
**Solution**:
```python
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
```
