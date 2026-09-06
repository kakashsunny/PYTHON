# Questions & Answers: Context Managers

## MCQs
1. **What must `__exit__` return to suppress exceptions raised inside a `with` block?**
   - A) `None`
   - B) `False`
   - C) `True`
   - D) `Exception`
   - **Answer**: C
   - **Explanation**: If `__exit__` returns `True`, Python swallows the exception. If it returns anything else (like `None` or `False`), the exception propagates.

2. **Which decorator converts a generator into a context manager?**
   - A) `@context`
   - B) `@contextmanager`
   - C) `@with_block`
   - D) `@contextlib`
   - **Answer**: B
   - **Explanation**: `contextlib.contextmanager` is the standard decorator.

## Beginner & Intermediate Questions
### Q1: What is the main benefit of using a context manager?
**Answer**: It guarantees resource cleanup (closing files, releasing locks, terminating connections) even if exceptions are raised within the block, eliminating resource leaks.

### Q2: Can a context manager be used without the `with` statement?
**Answer**: Yes, but you must call `__enter__()` and `__exit__()` manually, typically inside a `try-finally` block.

## Coding Practice & Solutions
### Problem: Create a context manager `temp_cwd` that temporarily changes the current working directory, then reverts it in the cleanup phase.
**Solution**:
```python
import os
from contextlib import contextmanager

@contextmanager
def temp_cwd(destination):
    original = os.getcwd()
    os.chdir(destination)
    try:
        yield
    finally:
        os.chdir(original)
```
