# Questions & Answers: Dictionaries

## MCQs
1. **What is the output of `dict.fromkeys(['a', 'b'], 0)`?**
   - A) `{'a': 0, 'b': 0}`
   - B) `{'a': None, 'b': None}`
   - C) `{'a', 'b'}`
   - D) Error
   - **Answer**: A
   - **Explanation**: `fromkeys` creates a dictionary with the keys from the iterable and all values initialized to the specified value.

2. **In Python 3.7+, dictionaries preserve:**
   - A) Alphabetic order
   - B) Insertion order
   - C) Value-based sort order
   - D) Hash-based random order
   - **Answer**: B
   - **Explanation**: Python 3.7+ guarantees dictionary iteration order matches insertion order.

## Beginner & Intermediate Questions
### Q1: What is a `defaultdict` and why is it useful?
**Answer**: `defaultdict` is a container from the `collections` module. It overrides dictionary lookup behavior by automatically initializing a key with a default factory function (like `list`, `int`) if the key doesn't exist, preventing `KeyError`.

### Q2: What are dictionary views?
**Answer**: Methods like `.keys()`, `.values()`, and `.items()` return view objects. They are dynamic views of the dictionary's entries, meaning if the dictionary changes, the view updates automatically.

## Coding Practice & Solutions
### Problem: Invert a dictionary (swap keys and values).
**Solution**:
```python
def invert_dict(d):
    return {v: k for k, v in d.items()}

print(invert_dict({'x': 1, 'y': 2}))  # {1: 'x', 2: 'y'}
```
