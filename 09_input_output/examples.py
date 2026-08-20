# Input/Output Examples and Practice

# 1. Customizing print function parameters
print("Part A", "Part B", sep="---")
print("First line", end=" >>> ")
print("Same line output")

# 2. Handling Safe Input Conversion
def get_user_age():
    # Simulating input for validation
    mock_inputs = ["twenty", "25"]
    for val in mock_inputs:
        try:
            print(f"User inputs: '{val}'")
            age = int(val)
            print("Successfully parsed age:", age)
            return age
        except ValueError:
            print("Invalid number! Please enter an integer.")

get_user_age()

# Practice: Format table-like output
data = [("Alice", 25, "HR"), ("Bob", 30, "IT"), ("Charlie", 22, "Sales")]
print(f"{'Name':<10} {'Age':<5} {'Department':<12}")
print("-" * 30)
for name, age, dept in data:
    print(f"{name:<10} {age:<5} {dept:<12}")
