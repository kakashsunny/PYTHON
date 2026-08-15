# Loops in Python

## Definitions & Concepts
Loops are control structures used to repeat a block of code. Python supports two main loop structures: `for` loops (for definite iteration) and `while` loops (for indefinite iteration).

## Loop Types & Statements
1. **`for` loop**: Iterates over sequence/iterable.
2. **`while` loop**: Repeats as long as a condition is True.
3. **`break`**: Terminates the loop prematurely.
4. **`continue`**: Skips the rest of the current iteration and jumps to the next.
5. **`else` with loops**: Executes code after the loop completes normally (without encountering a `break`).

## Syntax & Examples
```python
# For loop with range
for i in range(3):
    print(i) # 0, 1, 2

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# Loop Else structure
for num in [1, 3, 5]:
    if num % 2 == 0:
        print("Found an even number!")
        break
else:
    print("No even numbers found.") # This executes
```

## Best Practices
- Prefer `for` loops over `while` loops when iterating over known collections.
- Avoid using `else` in loops if it compromises readability; instead, use boolean flags or functions with early returns.

## Common Mistakes
- Creating infinite `while` loops by forgetting to update the control variable.
- Modifying a list while iterating over it (creates skipping bugs).

## Interview Tips
- **Q**: What is the purpose of the `else` block in a `for` or `while` loop?
- **A**: The `else` block runs only if the loop runs to completion without encountering a `break` statement. It is useful for search loops.
