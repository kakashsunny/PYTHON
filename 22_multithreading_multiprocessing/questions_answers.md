# Questions & Answers: Multithreading & Multiprocessing

## MCQs
1. **Which CPython mechanism restricts multithreading performance for CPU-bound tasks?**
   - A) Garbage Collector
   - B) JIT Compiler
   - C) GIL (Global Interpreter Lock)
   - D) SSL Socket Lock
   - **Answer**: C
   - **Explanation**: The GIL allows only one thread to control the Python interpreter at a time.

2. **Which module provides high-level interfaces for asynchronous execution pools?**
   - A) `multiprocessing`
   - B) `threading`
   - C) `concurrent.futures`
   - D) `subprocess`
   - **Answer**: C
   - **Explanation**: `concurrent.futures` contains the cleaner Executor interfaces.

## Beginner & Intermediate Questions
### Q1: What is a race condition?
**Answer**: A race condition occurs when multiple threads or processes access and modify shared data concurrently, and the final outcome depends on the timing of execution, which can cause data corruption.

### Q2: How do you resolve a race condition?
**Answer**: By using synchronization primitives like locks (e.g. `threading.Lock()`). A thread acquires the lock before updating shared state and releases it afterwards.

## Coding Practice & Solutions
### Problem: Use ThreadPoolExecutor to download content from a list of URLs concurrently.
**Solution**:
```python
from concurrent.futures import ThreadPoolExecutor
import requests

urls = ["https://www.google.com", "https://www.github.com"]

def get_status(url):
    try:
        return url, requests.get(url, timeout=3).status_code
    except Exception:
        return url, None

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(get_status, urls))

print(results)
```
