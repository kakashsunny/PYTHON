# Generators & Iterators in Python

## Definitions & Concepts
- **Iterable**: An object capable of returning its members one at a time. It implements `__iter__`.
- **Iterator**: A stateful helper object that produces values on call to `__next__`. It implements both `__iter__` and `__next__`.
- **Generator**: A simple and powerful tool for creating iterators. They are written like regular functions but use the `yield` statement to return data.

## Generators vs Lists
Lists load all elements into memory at once. Generators yield elements one at a time lazily on demand. This gives generators an O(1) memory footprint regardless of the size of the sequence.

## Syntax & Examples
```python
# Custom Generator
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1

counter = count_up_to(3)
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3
# next(counter) raises StopIteration
```

## Best Practices
- Use generators when processing huge datasets (like reading giant logs, DB streams) to prevent out-of-memory crashes.
- Use generator expressions `(x for x in iterable)` for simple inline pipelines.

## Common Mistakes
- Trying to index into a generator (e.g. `gen[0]` raises `TypeError`). Generators do not support indexing.
- Trying to re-use or iterate over a generator after it has been exhausted. You must create a new instance of the generator.

## Interview Tips
- **Q**: What does the `yield` statement do?
- **A**: It suspends the function's execution, saves its local state (variables, instruction pointer), and returns a value to the caller. When `next()` is called again on the generator, it resumes execution immediately after the `yield` statement.
