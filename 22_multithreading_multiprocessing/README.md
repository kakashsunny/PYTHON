# Multithreading & Multiprocessing in Python

## Definitions & Concepts
- **Thread**: The smallest unit of execution within a process. Threads share the same memory space.
- **Process**: An independent program instance with its own isolated memory space.
- **GIL (Global Interpreter Lock)**: A mutex in CPython preventing multiple threads from executing Python bytecodes at once.

## GIL Implications
Because of the GIL, Python threads are excellent for **I/O-bound tasks** (like reading files, APIs, web scraping) but do not provide speedups for **CPU-bound tasks** (math, image processing). For CPU-bound tasks, you must use multiprocessing to bypass the GIL and utilize multiple CPU cores.

## Syntax & Examples
```python
import threading
import multiprocessing

# 1. Threading
def io_task():
    print("Doing IO...")

t = threading.Thread(target=io_task)
t.start()
t.join()

# 2. Multiprocessing
def cpu_task():
    print("Doing math...")

p = multiprocessing.Process(target=cpu_task)
p.start()
p.join()
```

## Best Practices
- Use `concurrent.futures.ThreadPoolExecutor` and `ProcessPoolExecutor` for managing pools of workers cleanly.
- Keep shared states to a minimum to avoid race conditions. Use locks (`threading.Lock`) when state sharing is necessary.

## Common Mistakes
- Using multithreading to speed up mathematical or CPU-intensive computations (which fails because of the GIL).
- Forgetting to join threads or processes, causing main thread termination problems.

## Interview Tips
- **Q**: What is the difference between Multithreading and Multiprocessing in Python?
- **A**: Multithreading shares the memory space, has low creation overhead, but is restricted by the GIL (useful for I/O). Multiprocessing spawns completely separate OS processes, bypassing the GIL to run truly parallel code on multiple cores (useful for CPU bound tasks), but has high memory overhead and requires IPC (Inter-Process Communication) to share state.
