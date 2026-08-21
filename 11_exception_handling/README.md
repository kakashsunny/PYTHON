# Exception Handling in Python

## Definitions & Concepts
Errors that occur at runtime are called exceptions. Exception handling allows a program to respond to exceptions gracefully instead of crashing.

## The Exception Hierarchy Block
- **`try`**: Code block that might raise an exception.
- **`except`**: Code block to handle specific exceptions.
- **`else`**: Code block to run if no exception was raised in the `try` block.
- **`finally`**: Code block that ALWAYS executes, regardless of whether an exception occurred or was handled. Often used for clean-up.

## Syntax & Examples
```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid format! Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution complete.")
```

## Best Practices
- Never use a bare `except:` clause (e.g. `except Exception:`). Always specify the exact exception classes to avoid hiding unexpected bugs (like `KeyboardInterrupt`).
- Avoid using exception handling to control normal program flow; exceptions should be reserved for exceptional cases.

## Common Mistakes
- Catching general exceptions when a specific exception class could be targeted.
- Raising custom exceptions without inheriting from the base `Exception` class.

## Interview Tips
- **Q**: What is the difference between `except Exception as e` and a bare `except:`?
- **A**: A bare `except:` catches absolutely all errors, including system-exiting exceptions like `SystemExit` and `KeyboardInterrupt`. `except Exception` catches only standard application-level errors, allowing keyboard interrupts to function normally.
