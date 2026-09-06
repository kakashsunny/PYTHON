# Context Managers Examples and Practice
from contextlib import contextmanager

# 1. Custom Class Context Manager (measuring execution block time)
class CodeBlockTimer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.perf_counter()
        print(f"Elapsed block execution time: {self.end - self.start:.6f} seconds")

with CodeBlockTimer():
    total = sum(range(1000000))

# 2. Generator-based Context Manager using contextlib
@contextmanager
def db_transaction_mock():
    print("--- [DB Transaction Start] ---")
    try:
        yield "db_cursor"
        print("--- [DB Transaction Commit] ---")
    except Exception as e:
        print(f"--- [DB Transaction Rollback due to: {e}] ---")
        raise
    finally:
        print("--- [DB Connection Closed] ---")

try:
    with db_transaction_mock() as cursor:
        print(f"Writing data using {cursor}")
        raise ValueError("Simulated DB Write Error")
except ValueError:
    print("Transaction error caught safely.")
