# Lambda, Map, Filter & Reduce in Python

## Definitions & Concepts
- **Lambda Function**: An anonymous, single-expression function defined with the `lambda` keyword.
- **`map(function, iterable)`**: Applies a function to all items in an input iterable.
- **`filter(function, iterable)`**: Filters elements from an iterable for which the function returns `True`.
- **`reduce(function, iterable)`**: Sequentially applies a function to elements of an iterable, reducing the collection to a single cumulative value (requires importing from `functools`).

## Syntax & Examples
```python
# Lambda
square = lambda x: x**2

# Map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers)) # [1, 4, 9, 16]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers)) # [2, 4]

# Reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers) # 24
```

## Best Practices
- Prefer list comprehensions or generator expressions over `map` and `filter` when lambda functions are involved, as comprehensions are usually more readable.
- Use `reduce` sparingly; simple loops or built-in functions like `sum()` are preferred.

## Common Mistakes
- Forgetting that `map` and `filter` return lazy iterators in Python 3. You must cast them to lists or iterate over them to extract the values.
- Writing complex multiline logic in lambda functions (lambdas can only contain a single expression).

## Interview Tips
- **Q**: Why are lambda functions limited to a single expression?
- **A**: Python's design philosophy values readability. Keeping lambdas simple prevents developers from writing unreadable, inline functional code blocks.
