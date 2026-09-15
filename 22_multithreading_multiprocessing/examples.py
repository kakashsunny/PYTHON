# Multithreading & Multiprocessing Examples and Practice
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def mock_io_bound_task(name):
    print(f"Task {name} starting...")
    time.sleep(1) # Simulates network request
    print(f"Task {name} completed.")
    return f"Result of {name}"

def mock_cpu_bound_task(n):
    # Calculations
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    # 1. Thread Pool for I/O tasks
    print("--- Running Thread Pool ---")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(mock_io_bound_task, f"Scraper_{i}") for i in range(3)]
        results = [f.result() for f in futures]
    end = time.perf_counter()
    print(f"Thread pool finished in: {end - start:.2f} seconds")
    print("Results:", results)

    # 2. Process Pool for CPU tasks
    print("--- Running Process Pool ---")
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(mock_cpu_bound_task, 5000000) for _ in range(2)]
        results = [f.result() for f in futures]
    end = time.perf_counter()
    print(f"Process pool finished in: {end - start:.2f} seconds")
