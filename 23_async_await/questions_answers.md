# Questions & Answers: Async/Await

## MCQs
1. **How do you define a coroutine in Python?**
   - A) `def async my_func()`
   - B) `async def my_func()`
   - C) `coroutine def my_func()`
   - D) `@asyncio.coroutine`
   - **Answer**: B
   - **Explanation**: `async def` is the standard syntax for native coroutines in Python 3.5+.

2. **What happens if you run a blocking call like `time.sleep(5)` inside an async function?**
   - A) It runs concurrently on another thread.
   - B) It blocks the entire event loop for 5 seconds, stopping all concurrent tasks.
   - C) Raises `CoroutineBlockingError`.
   - D) Python automatically converts it to async sleep.
   - **Answer**: B
   - **Explanation**: Async runs on a single thread. Any blocking CPU/IO operation pauses the entire thread.

## Beginner & Intermediate Questions
### Q1: What is an Awaitable?
**Answer**: An object that can be used in an `await` expression. The three main types of awaitables are: Coroutines, Tasks, and Futures.

### Q2: What is the difference between `asyncio.create_task()` and awaiting a coroutine directly?
**Answer**: `asyncio.create_task()` schedules the coroutine to run immediately on the event loop concurrently, while directly awaiting a coroutine pauses execution until that specific coroutine finishes.

## Coding Practice & Solutions
### Problem: Write an async program to simulate a worker pool processing a queue of jobs.
**Solution**:
```python
import asyncio

async def worker(q):
    while not q.empty():
        item = await q.get()
        print(f"Processing job: {item}")
        await asyncio.sleep(0.5)
        q.task_done()

async def main():
    q = asyncio.Queue()
    for i in range(5):
        await q.put(f"Job-{i}")
    
    # Run worker
    await worker(q)

asyncio.run(main())
```
