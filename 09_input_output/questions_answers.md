# Questions & Answers: Input/Output

## MCQs
1. **What is the default separator parameter in `print()`?**
   - A) `\n`
   - B) `\t`
   - C) `' '` (space)
   - D) `','`
   - **Answer**: C
   - **Explanation**: The default parameter for `sep` in print is a single space `' '`.

2. **If a user inputs `12.34` into `input()`, what is its type?**
   - A) `float`
   - B) `int`
   - C) `str`
   - D) `None`
   - **Answer**: C
   - **Explanation**: `input()` always returns a string, regardless of what the user types.

## Beginner & Intermediate Questions
### Q1: How can you write console output to a file using the `print()` function?
**Answer**: You can pass a file handler to the `file` parameter of `print()`. E.g.:
```python
with open("output.txt", "w") as f:
    print("Hello File", file=f)
```

### Q2: What is the purpose of the `flush=True` parameter in the `print()` function?
**Answer**: By default, standard output is buffered for efficiency. `flush=True` bypasses buffer buffering and forces the output to write immediately to the stream, which is useful for progress bars.

## Coding Practice & Solutions
### Problem: Write a program that reads a list of numbers from input separated by commas and returns their sum.
**Solution**:
```python
def sum_input(csv_string):
    try:
        numbers = [float(x.strip()) for x in csv_string.split(",")]
        return sum(numbers)
    except ValueError:
        return "Invalid characters in input"

print(sum_input("1.5, 2, 3.5"))  # 7.0
```
