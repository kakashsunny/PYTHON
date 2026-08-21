# Questions & Answers: Exception Handling

## MCQs
1. **Which block in exception handling will run no matter what?**
   - A) `else`
   - B) `finally`
   - C) `catch`
   - D) `except`
   - **Answer**: B
   - **Explanation**: The `finally` block is guaranteed to execute whether an exception is raised or not.

2. **How do you manually raise an exception in Python?**
   - A) `throw ValueError`
   - B) `raise ValueError`
   - C) `trigger ValueError`
   - D) `except ValueError`
   - **Answer**: B
   - **Explanation**: The `raise` keyword is used to trigger exceptions manually.

## Beginner & Intermediate Questions
### Q1: What is exception chaining?
**Answer**: Exception chaining allows you to associate a caught exception with a new exception that you raise, using the `raise NewException from old_exception` syntax.

### Q2: What happens if an exception is raised in the `try` block but not caught by any `except` block?
**Answer**: The exception propagates up the call stack. If it remains uncaught, the program terminates and prints a traceback.

## Coding Practice & Solutions
### Problem: Write a function that safely parses a string to a dictionary using json loading, returning an empty dictionary on failure.
**Solution**:
```python
import json

def safe_json_parse(json_str):
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return {}

print(safe_json_parse('{"name": "Alice"}'))  # {'name': 'Alice'}
print(safe_json_parse("invalid json"))      # {}
```
