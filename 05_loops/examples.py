# Loops Examples and Practice

# 1. Break and Continue demo
for num in range(1, 10):
    if num == 5:
        print("Breaking loop at 5")
        break
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")

# 2. While loop with condition
password = ""
attempts = 0
while password != "secret" and attempts < 3:
    # Simulating input
    simulated_inputs = ["1234", "admin", "secret"]
    password = simulated_inputs[attempts]
    print(f"Attempt {attempts + 1}: Inputting '{password}'")
    attempts += 1

# 3. Else block execution
numbers = [1, 7, 9, 11]
for val in numbers:
    if val % 2 == 0:
        print(f"Even found: {val}")
        break
else:
    print("Normal Completion: All numbers were odd.")
