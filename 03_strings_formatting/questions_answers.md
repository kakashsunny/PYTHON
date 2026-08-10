# Questions & Answers: Strings & Formatting

## MCQs
1. **What is the output of `"hello"[::-1]`?**
   - A) `"h"`
   - B) `"olleh"`
   - C) `"o"`
   - D) Error
   - **Answer**: B
   - **Explanation**: This syntax represents slicing with a step of `-1`, which reverses the string.

2. **Which of the following is correct for f-string formatting in Python 3.6+?**
   - A) `f"{val:.2f}"`
   - B) `"{val:.2f}".f()`
   - C) `f(val, ".2f")`
   - D) `f"{val:%2f}"`
   - **Answer**: A
   - **Explanation**: `f"{variable:.2f}"` formats a float variable to 2 decimal places.

## Beginner & Intermediate Questions
### Q1: What is string interning?
**Answer**: String interning is an optimization technique where Python stores only one copy of distinct string values in memory. If multiple variables point to the same string literal, they point to the exact same memory location.

### Q2: What is a raw string, and when do we use it?
**Answer**: A raw string is prefixed with `r` (e.g., `r"C:\new\folder"`). It treats backslashes as literal characters instead of escape sequences. It is commonly used for regex patterns and file paths.

## Coding Practice & Solutions
### Problem: Count the frequency of each character in a string.
**Solution**:
```python
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
