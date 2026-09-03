# Questions & Answers: Decorators

## MCQs
1. **What is a decorator syntactically?**
   - A) A class method only
   - B) A function that takes another function as an argument and returns a new function
   - C) An import statement wrapper
   - D) A compiler directive
   - **Answer**: B
   - **Explanation**: A decorator takes a callable object as its input and returns a callable object wrapping it.

2. **Which module helps preserve the decorated function's original name and docstring?**
   - A) `sys`
   - B) `inspect`
   - C) `functools`
   - D) `types`
   - **Answer**: C
   - **Explanation**: `functools.wraps` is designed for this exact purpose.

## Beginner & Intermediate Questions
### Q1: What is the equivalent code of using `@my_decorator` on `def my_func()`?
**Answer**:
```python
def my_func():
    pass
my_func = my_decorator(my_func)
```

### Q2: Can a class act as a decorator?
**Answer**: Yes. Any object that implements the `__call__` method can be used as a decorator. Inside the class, `__init__` receives the function, and `__call__` executes when the function is called.

## Coding Practice & Solutions
### Problem: Write a decorator `require_auth` that checks if a kwargs dictionary contains `authenticated=True`, raising a `PermissionError` if not.
**Solution**:
```python
import functools

def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("authenticated", False):
            raise PermissionError("User is not authenticated!")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def get_sensitive_data(authenticated=False):
    return "Secret Database Records"

try:
    print(get_sensitive_data(authenticated=False))
except PermissionError as e:
    print("Caught:", e)
```
