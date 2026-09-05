# Generators & Iterators Examples and Practice

# 1. Custom Iterator Class (Fibonacci)
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val

print("Fibonacci sequence (first 5 numbers):")
for num in FibonacciIterator(5):
    print(num)

# 2. Generator Function (Lazy evaluation)
def read_large_file_simulation():
    # Simulating yielding lines from a giant file
    lines = ["Line A", "Line B", "Line C"]
    for line in lines:
        print("--> Generating line...")
        yield line

gen = read_large_file_simulation()
print(next(gen))
print(next(gen))

# 3. Generator Expression
squares_gen = (x**2 for x in range(1000000))
print("Type of squares_gen:", type(squares_gen))
print("First element:", next(squares_gen))
