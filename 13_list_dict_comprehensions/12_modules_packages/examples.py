# Modules & Packages Examples and Practice
import sys
import math

# 1. Inspecting module paths
print("Python Search Path (first 3 entries):")
for path in sys.path[:3]:
    print("-", path)

# 2. Math module usage
print("Square root of 16:", math.sqrt(16))
print("Sine of pi/2:", math.sin(math.pi / 2))

# 3. Simulating package exports
# Creating inline helper dictionary mimicking module namespace
dummy_module_namespace = {
    "__all__": ["public_func"],
    "public_func": lambda: "I am public",
    "_private_func": lambda: "I am private"
}
print("Exported symbols:", dummy_module_namespace["__all__"])
