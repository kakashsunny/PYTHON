# Async/Await in Python

## Definitions & Concepts
- **Asynchronous Programming**: A concurrent programming model where tasks can pause and yield control, allowing other tasks to run in the meantime on a single thread.
- **Event Loop**: The central controller of an async application. It manages and distributes execution of different tasks.
- **Coroutine**: A specialized function that can pause execution (using `await`) and resume later. Defined with `async def`.

## Sync vs Threading vs Async
- **Sync**: Blocking execution.
- **Threading**: OS preempts threads (concurrency via context switching, expensive memory).
- **Async**: Cooperative multitasking. Coroutines yield control voluntarily. Lightweight and scales to thousands of concurrent operations on a single thread.

## Syntax & Examples
```python
import asyncio

async def fetch_data(id):
    print(f"Start fetch {id}")
    await asyncio.sleep(1) # Simulated network sleep
    print(f"End fetch {id}")
    return {"data": id}

async def main():
    # Gather runs tasks concurrently
    results = await asyncio.gather(fetch_data(1), fetch_data(2))
    print(results)

asyncio.run(main())
```

## Best Practices
- Never use blocking functions (like `time.sleep()` or standard `requests`) inside async code. Use their async equivalents (e.g., `asyncio.sleep()`, `aiohttp`).
- Handle errors inside tasks to prevent the entire event loop from crashing.

## Common Mistakes
- Calling a coroutine function (e.g., `fetch_data(1)`) without using the `await` keyword. This returns a coroutine object without running it.

## Interview Tips
- **Q**: What does the `await` keyword do?
- **A**: It yields control back to the event loop. The event loop pauses the execution of the current coroutine until the awaited task (which must be an awaitable object) completes, letting other tasks execute in the meantime.
