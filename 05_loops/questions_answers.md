# Questions & Answers: Loops

## MCQs
1. **How many times will the loop run? `for i in range(1, 6, 2):`**
   - A) 5
   - B) 3
   - C) 2
   - D) Infinite
   - **Answer**: B
   - **Explanation**: It starts at 1, increments by 2, and ends before 6. So values are 1, 3, 5 (3 iterations).

2. **What does the `continue` statement do?**
   - A) Breaks the loop completely
   - B) Skips the current iteration and goes to the next
   - C) Restarts the program
   - D) Passes execution to the else block
   - **Answer**: B
   - **Explanation**: `continue` skips only the remaining statements in the current iteration.

## Beginner & Intermediate Questions
### Q1: What is the difference between `range(5)` and `list(range(5))`?
**Answer**: `range(5)` returns a lazy range object (an iterable) that yields values on demand, saving memory. `list(range(5))` materializes all values immediately into a list in memory.

### Q2: How can we iterate over both index and value in a loop?
**Answer**: Use the `enumerate()` built-in function:
```python
for index, value in enumerate(my_list):
    print(index, value)
```

## Coding Practice & Solutions
### Problem: Find all prime numbers in a range using loops.
**Solution**:
```python
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(find_primes(10, 30))  # [11, 13, 17, 19, 23, 29]
```
