# Context Managers in Python

## Definitions & Concepts
Context Managers are Python structures that allocate and release resources precisely when required. They are typically invoked using the `with` statement.

## The Context Manager Protocol
An object must implement two methods to be a context manager:
1. **`__enter__(self)`**: Set up resources, returns target variable.
2. **`__exit__(self, exc_type, exc_val, exc_tb)`**: Tears down resources, closes files, handles exceptions. If it returns `True`, exceptions raised inside the block are suppressed.

## Syntax & Examples
```python
# Custom class context manager
class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileLogger("log.txt") as f:
    f.write("Log line")
```

## Alternative: `contextlib`
The `@contextmanager` decorator in the standard library's `contextlib` module allows you to define a context manager using a generator function.

```python
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
```

## Best Practices
- Use context managers to handle files, database connections, sockets, locks, and temporary configurations.
- Return `True` from `__exit__` only if you intentionally want to swallow exceptions.

## Common Mistakes
- Failing to use `finally` or resource cleanup inside generator context managers.

## Interview Tips
- **Q**: What are the arguments passed to `__exit__`?
- **A**: `__exit__` receives `exc_type` (the class of the exception), `exc_val` (the exception instance), and `exc_tb` (the traceback object). They are all `None` if the code runs successfully.
