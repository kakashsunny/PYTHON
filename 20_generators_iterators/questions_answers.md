# Questions & Answers: Generators & Iterators

## MCQs
1. **What exception is raised when a generator runs out of items?**
   - A) `IndexError`
   - B) `GeneratorExit`
   - C) `StopIteration`
   - D) `EOFError`
   - **Answer**: C
   - **Explanation**: The iterator protocol dictates that when a sequence ends, `__next__()` raises `StopIteration`.

2. **Which method is used to manually advance an iterator?**
   - A) `advance()`
   - B) `__next__()` or `next()`
   - C) `yield()`
   - D) `get_next()`
   - **Answer**: B
   - **Explanation**: Built-in `next(iterator)` calls the object's `__next__()` method.

## Beginner & Intermediate Questions
### Q1: What is the difference between a generator function and a generator object?
**Answer**: A generator function is the function defined with `yield` inside it. A generator object is what is returned when you call a generator function; it conforms to the iterator protocol.

### Q2: Can you run a `for` loop on a generator?
**Answer**: Yes. Python's `for` loops are designed to automatically call `__iter__()` and `__next__()` on objects and catch the `StopIteration` exception silently.

## Coding Practice & Solutions
### Problem: Write a generator function that yields running averages of numbers sent to it.
**Solution**:
```python
def running_average():
    total = 0.0
    count = 0
    while True:
        val = yield (total / count if count > 0 else 0.0)
        if val is not None:
            total += val
            count += 1

avg = running_average()
next(avg)  # Prime generator
print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
```
