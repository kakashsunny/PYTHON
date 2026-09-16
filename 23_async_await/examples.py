# Async/Await Examples and Practice
import asyncio
import time

# 1. Cooperative Multitasking Demo
async def worker(name, duration):
    print(f"Worker {name} started. Task takes {duration}s.")
    await asyncio.sleep(duration) # Non-blocking sleep
    print(f"Worker {name} finished.")
    return f"Result-{name}"

async def main():
    start = time.perf_counter()
    
    # Run three workers concurrently on a single thread
    task1 = asyncio.create_task(worker("A", 2))
    task2 = asyncio.create_task(worker("B", 1))
    task3 = asyncio.create_task(worker("C", 1.5))
    
    results = await asyncio.gather(task1, task2, task3)
    
    end = time.perf_counter()
    print(f"All workers finished in: {end - start:.2f} seconds (Max time should be 2.0s)")
    print("Results:", results)

if __name__ == "__main__":
    asyncio.run(main())
