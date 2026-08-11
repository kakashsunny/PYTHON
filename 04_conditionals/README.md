# Conditionals in Python

## Definitions & Concepts
Conditionals are control flow statements that allow code blocks to execute selectively based on boolean conditions.

## Syntax & Structures
1. **`if` Statement**: Evaluates a single condition.
2. **`elif` Statement**: Short for "else if", evaluates additional conditions if previous ones were False.
3. **`else` Statement**: Runs if all preceding conditions were False.
4. **Ternary Operator (Conditional Expression)**: Inline conditional expression.
5. **Pattern Matching (`match-case` - Python 3.10+)**: Structural pattern matching similar to switch-case.

## Syntax & Examples
```python
# Basic conditional
age = 20
if age >= 21:
    print("Allowed")
else:
    print("Not allowed")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Match-case (Python 3.10+)
status_code = 404
match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")
```

## Best Practices
- Avoid deep nesting of conditionals; use guard clauses to return early.
- Keep conditions readable; break complex expressions into variables.

## Common Mistakes
- Forgetting the colon `:` at the end of the `if`/`elif`/`else` clauses.
- Mixing up indentation (using tabs and spaces together).
- Using assignment `=` instead of equality `==` in conditions.

## Interview Tips
- **Q**: What does Python do when evaluating conditions in terms of truthiness?
- **A**: Python checks the boolean value of the expression. Objects like `0`, `None`, empty collections (`[]`, `{}`, `()`, `set()`), and `False` evaluate to `False`. All other objects evaluate to `True`.
