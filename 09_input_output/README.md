# Input/Output in Python

## Definitions & Concepts
Input and Output (I/O) handles interactions between the program and external environments (like users or terminals).

## Core I/O Functions
1. **`input(prompt)`**: Prompts user for console input. **Always returns a string.**
2. **`print(*objects, sep=' ', end='\n', file=None, flush=False)`**: Writes text to the output stream.

## Syntax & Examples
```python
# Console input
name = input("Enter name: ")
age = int(input("Enter age: ")) # Convert string to integer

# Print configurations
print("apple", "banana", sep=" | ") # apple | banana
print("Loading...", end="")
print(" Done!") # Loading... Done!
```

## Best Practices
- Always cast/convert `input()` to the required type immediately with checks to handle parsing errors.
- Use explicit separators and formatting to make output readable.

## Common Mistakes
- Forgetting that `input()` returns a string, leading to math errors (e.g. `input() + 5` raises `TypeError`).
- Using custom printing instead of log files for complex application outputs.

## Interview Tips
- **Q**: How does Python's `input()` function work under the hood?
- **A**: It reads a line from the standard input stream (typically keyboard), strips the trailing newline, and returns it as a string. It blocks execution until the user presses Enter.
