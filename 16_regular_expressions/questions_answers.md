# Questions & Answers: Regular Expressions

## MCQs
1. **Which regex metacharacter matches the start of a string?**
   - A) `$`
   - B) `.`
   - C) `^`
   - D) `*`
   - **Answer**: C
   - **Explanation**: `^` matches the beginning of the string.

2. **What does the pattern `r"\d+"` match?**
   - A) One or more digits
   - B) Zero or more digits
   - C) Exactly one digit
   - D) Hexadecimal digits
   - **Answer**: A
   - **Explanation**: `\d` matches digits and `+` specifies one or more occurrences.

## Beginner & Intermediate Questions
### Q1: What is the purpose of `re.compile()`?
**Answer**: It compiles a regular expression pattern into a regular expression object. This speeds up match operations when the pattern is used multiple times in the program.

### Q2: How do you perform a case-insensitive regex search?
**Answer**: Pass the `re.IGNORECASE` (or `re.I`) flag to functions like `re.search` or `re.findall`.

## Coding Practice & Solutions
### Problem: Extract all website URLs starting with `http` or `https` from a block of text.
**Solution**:
```python
import re

def extract_urls(text):
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*"
    return re.findall(pattern, text)

sample = "Check http://google.com and https://github.com/trending"
print(extract_urls(sample))  # ['http://google.com', 'https://github.com/trending']
```
