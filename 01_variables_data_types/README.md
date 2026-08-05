# Variables & Data Types in Python

## Definitions & Concepts
- **Variable**: A named location in memory used to store data. In Python, variables are dynamically typed, meaning you don't need to declare their type explicitly.
- **Dynamic Typing**: Python determines the data type of a variable at runtime based on the value assigned to it.
- **Data Type**: An attribute of data which tells the compiler or interpreter how the programmer intends to use the data.

## Core Data Types
1. **Integer (`int`)**: Whole numbers, e.g., `10`, `-5`.
2. **Float (`float`)**: Decimal numbers, e.g., `10.5`, `-0.01`.
3. **String (`str`)**: Text enclosed in single, double, or triple quotes, e.g., `"Hello"`, `'World'`.
4. **Boolean (`bool`)**: Logical values, `True` or `False`.
5. **NoneType (`None`)**: Represents the absence of a value.

## Syntax & Examples
```python
# Variable Assignment
x = 10          # Integer
pi = 3.14159    # Float
name = "Alice"  # String
is_active = True# Boolean
result = None   # NoneType

# Re-assignment to different type (dynamic typing)
x = "Now I am a string"
```

## Important Notes
- Variables are created when a value is assigned.
- Variable names are case-sensitive (`age` and `Age` are different).
- Must start with a letter or underscore, and can contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, and `_`).

## Best Practices
- Use descriptive snake_case names for variables (e.g., `user_age`, `total_price`).
- Avoid using Python keywords (like `class`, `import`, `def`) as variable names.
- Keep constants in uppercase (e.g., `MAX_RETRIES = 5`).

## Common Mistakes
- **NameError**: Referencing a variable before assigning a value to it.
- **TypeMismatch**: Trying to concatenate strings and integers without casting (e.g., `"Age: " + 25` raises a `TypeError`). Use `str(25)` or f-strings.

## Interview Tips
- **Q**: Is Python statically or dynamically typed? Strongly or weakly typed?
- **A**: Python is dynamically typed (types are checked at runtime) and strongly typed (implicit type conversions are not allowed, e.g., you cannot add a string and an integer directly).
