# Variables & Data Types Examples and Practice

# 1. Variable Assignment and Dynamic Typing
age = 25
print("Age is of type:", type(age))

age = "Twenty-five"
print("Age is now of type:", type(age))

# 2. Strong Typing Demonstration
try:
    result = "Age: " + 25
except TypeError as e:
    print("Caught expected TypeError:", e)
    # Correct way:
    result = "Age: " + str(25)
    print("Corrected concatenation:", result)

# 3. NoneType check
user_profile = None
if user_profile is None:
    print("No user profile found.")

# Practice Exercise: Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Formula: (C * 9/5) + 32
    return (celsius * 9/5) + 32

temp_c = 25.0
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}C is equal to {temp_f}F")
