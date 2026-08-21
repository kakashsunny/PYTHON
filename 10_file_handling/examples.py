# File Handling Examples and Practice
import os

filename = "temp_demo.txt"

# 1. Writing to a file using context manager
with open(filename, "w", encoding="utf-8") as f:
    f.write("Line 1: Python File Handling\n")
    f.write("Line 2: Always use the with statement\n")

# 2. Reading files in different ways
print("--- Reading Entire File ---")
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())

print("--- Reading Line by Line ---")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Clean up
if os.path.exists(filename):
    os.remove(filename)

# Practice Exercise: Copy a file's content to a new file
def copy_file(src, dest):
    try:
        with open(src, "rb") as s, open(dest, "wb") as d:
            d.write(s.read())
        return True
    except FileNotFoundError:
        return False
