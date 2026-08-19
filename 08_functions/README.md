# Functions in Python

## Definitions & Concepts
A function is a block of organized, reusable code used to perform a single, related action. Functions provide modularity and code reuse.

## Function Anatomy & Parameters
1. **Positional Arguments**: Assigned by position.
2. **Keyword Arguments**: Assigned by matching parameters names.
3. **Default Parameters**: Fallback values when arguments are omitted.
4. **`*args`**: Variadic positional parameters (tuple).
5. **`**kwargs`**: Variadic keyword parameters (dictionary).
6. **Positional-Only & Keyword-Only Arguments** (using `/` and `*`).

## Syntax & Examples
```python
# Basic function with default values
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Variadic arguments
def calculate_sum(*args):
    return sum(args)

# Positional-Only and Keyword-Only parameters
def func(pos_only, /, standard, *, kw_only):
    print(pos_only, standard, kw_only)
```

## Scope & Lifetime
- **Local scope**: Variables defined inside functions.
- **Global scope**: Variables defined at module root.
- **`global` keyword**: Re-binds local variables to global scope.
- **`nonlocal` keyword**: Re-binds local variables to enclosing local scope (closures).

## Best Practices
- Write functions that do one thing and do it well (Single Responsibility Principle).
- Use docstrings (`"""docstring"""`) to describe parameters, outputs, and behavior.
- Avoid using mutable objects (like lists or dicts) as default arguments.

## Common Mistakes
- **Mutable Default Arguments**: E.g. `def add_item(item, lst=[])`. The list `lst` is instantiated once when the function is defined, causing items to persist across calls. Correct pattern: `lst=None` and initialize inside function.

## Interview Tips
- **Q**: What happens when you pass arguments to a function in Python? (Pass by value or reference?)
- **A**: Python uses "Pass-by-Object-Reference" or "Object Reference by Value". If you pass a mutable object, changes inside the function affect the caller. If you pass an immutable object, changes do not affect the caller.
