# Decorators in Python

## Definitions & Concepts
A decorator is a design pattern in Python that allows you to modify the behavior of a function or class without permanently modifying it. Decorators wrap another function, extending its behavior.

## Functions as First-Class Citizens
Decorators are possible in Python because functions are first-class objects, meaning they can be:
- Passed as arguments to other functions.
- Returned from functions.
- Assigned to variables.

## Syntax & Examples
```python
# Decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

# Applying decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## Best Practices
- Always use `functools.wraps` on the wrapper function. It preserves the original function's name, docstring, and metadata.
- Design decorators to accept `*args` and `**kwargs` so they can wrap any function signature.

## Common Mistakes
- Forgetting to return the result of the wrapped function inside the wrapper.
- Forgetting to return the wrapper function itself in the outer decorator.

## Interview Tips
- **Q**: What is the purpose of `@wraps` from `functools`?
- **A**: By default, when a function is decorated, it loses its identity (its `__name__` and `__doc__` attributes are overwritten by the wrapper's metadata). `@wraps` copies this metadata back to the decorated function, which is critical for debugging and reflection.
