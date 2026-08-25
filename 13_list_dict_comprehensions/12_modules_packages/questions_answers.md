# Questions & Answers: Modules & Packages

## MCQs
1. **Which variable contains the search paths Python searches for modules?**
   - A) `sys.paths`
   - B) `sys.path`
   - C) `os.path`
   - D) `env.path`
   - **Answer**: B
   - **Explanation**: `sys.path` is a list of strings specifying the search path for modules.

2. **What does `if __name__ == "__main__":` do?**
   - A) Defines the main function.
   - B) Runs the code block only if the file is run directly (not imported).
   - C) Prevents other modules from importing the file.
   - D) Compiles the script.
   - **Answer**: B
   - **Explanation**: When a module is run directly, its `__name__` variable is set to `"__main__"`.

## Beginner & Intermediate Questions
### Q1: What is the difference between relative and absolute imports?
**Answer**: Absolute imports specify the full path from the project's root folder (e.g., `from myapp.models import User`). Relative imports specify the path relative to the current module's position (e.g., `from .models import User`).

### Q2: What is the function of the `__all__` list in a module?
**Answer**: It defines which names are exported when a client uses `from module import *`.

## Coding Practice & Solutions
### Problem: Programmatically add a directory to the Python import search path.
**Solution**:
```python
import sys
# Append path to search space
sys.path.append("/path/to/custom/folder")
```
