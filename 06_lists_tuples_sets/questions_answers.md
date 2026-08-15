# Questions & Answers: Lists, Tuples & Sets

## MCQs
1. **Which operation on sets has a time complexity of O(1) on average?**
   - A) Sorting
   - B) Indexing
   - C) Membership checking (`in`)
   - D) Concatenation
   - **Answer**: C
   - **Explanation**: Sets use hash tables, allowing O(1) average lookup time.

2. **How do you define an empty set in Python?**
   - A) `s = {}`
   - B) `s = set()`
   - C) `s = []`
   - D) `s = set({})`
   - **Answer**: B
   - **Explanation**: `s = {}` creates an empty dictionary. An empty set must be declared using `set()`.

## Beginner & Intermediate Questions
### Q1: What is the difference between `.append()` and `.extend()`?
**Answer**: `.append()` adds its argument as a single element at the end of the list. `.extend()` iterates over its argument and adds each item to the list.

### Q2: Can a list be used as a key in a dictionary? Why or why not?
**Answer**: No, a list cannot be a key in a dictionary because lists are mutable and thus not hashable. Dictionary keys must be hashable objects (like strings, integers, or tuples).

## Coding Practice & Solutions
### Problem: Find common elements between three lists.
**Solution**:
```python
def common_elements(l1, l2, l3):
    return list(set(l1).intersection(l2).intersection(l3))

print(common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]))  # [3]
```
