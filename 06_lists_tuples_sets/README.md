# Lists, Tuples & Sets in Python

## Definitions & Concepts
- **List**: An ordered, mutable sequence of items. Written with square brackets `[]`.
- **Tuple**: An ordered, immutable sequence of items. Written with parentheses `()`.
- **Set**: An unordered collection of unique, hashable items. Written with curly braces `{}`.

## Structural Differences
| Collection | Ordering | Mutability | Uniqueness | Duplicates Allowed |
|---|---|---|---|---|
| **List** | Ordered | Mutable | No | Yes |
| **Tuple** | Ordered | Immutable | No | Yes |
| **Set** | Ununordered | Mutable | Yes | No |

## Syntax & Examples
```python
# Lists
my_list = [1, 2, 2, 3]
my_list.append(4)  # [1, 2, 2, 3, 4]

# Tuples
my_tuple = (1, 2, 2, 3)
# my_tuple[0] = 5 -> TypeError

# Sets
my_set = {1, 2, 2, 3}  # {1, 2, 3} (duplicates automatically removed)
my_set.add(4)
```

## Useful Methods & Operations
- **List**: `.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`, `.sort()`.
- **Tuple**: `.count()`, `.index()`.
- **Set**: `.union()`, `.intersection()`, `.difference()`, `.symmetric_difference()`.

## Best Practices
- Use tuples for read-only data, records, or dictionary keys.
- Use sets to quickly check membership (since checking is O(1)) and to filter out duplicates.
- Use lists for sequential collections of homogeneous items.

## Common Mistakes
- Creating a single-element tuple incorrectly: `x = (5)` is an integer. Correct syntax is `x = (5,)`.
- Modifying list elements during loop iteration without using copies or list comprehensions.

## Interview Tips
- **Q**: Why are tuples faster and more memory efficient than lists?
- **A**: Lists are dynamic and allocate extra memory to accommodate growth, whereas tuples are static, immutable, and allocated with the exact size needed.
