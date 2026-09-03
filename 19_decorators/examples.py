# Decorators Examples and Practice
import functools
import time

# 1. Timer Decorator preserving metadata
def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper

@timer_decorator
def complex_computation(n):
    """Simulates a heavy calculation."""
    total = 0
    for i in range(n):
        total += i
    return total

print("Result:", complex_computation(100000))
print("Metadata check - name:", complex_computation.__name__)
print("Metadata check - doc:", complex_computation.__doc__)

# 2. Decorator with Arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
