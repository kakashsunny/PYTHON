# File Handling in Python

## Definitions & Concepts
File handling allows programs to read from and write to files on disk. In Python, file operations are done using built-in functions, primarily `open()`.

## Core Operations
- **`open(filename, mode)`**: Opens a file and returns a file object.
  - Modes:
    - `'r'`: Read (default). Errors if the file does not exist.
    - `'w'`: Write. Creates a new file or overwrites an existing one.
    - `'a'`: Append. Adds content to the end of the file.
    - `'b'`: Binary mode (e.g., `'rb'`, `'wb'`) for non-text files like images.
    - `'+'`: Open for updating (reading and writing).
- **`close()`**: Closes the file, releasing system resources.

## The Context Manager (`with` statement)
Using the `with` statement is the best practice for file handling because it guarantees the file is closed automatically when the block is exited, even if exceptions occur.

## Syntax & Examples
```python
# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()

# Writing to a file
with open("output.txt", "w") as f:
    f.write("Hello, World!")
```

## Best Practices
- Always use the `with` statement for file operations to prevent file locks and memory leaks.
- Specify the encoding explicitly (e.g., `encoding="utf-8"`) to avoid platform-dependent bugs.

## Common Mistakes
- Not closing a file when opening it without the `with` statement.
- Overwriting existing file content by accidentally opening it in `'w'` mode instead of `'a'`.

## Interview Tips
- **Q**: What is the difference between `.read()`, `.readline()`, and `.readlines()`?
- **A**: `.read()` reads the entire file content as a single string. `.readline()` reads a single line from the file. `.readlines()` reads the entire file and returns a list of strings, where each string represents a line.
