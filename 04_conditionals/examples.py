# Conditionals Examples and Practice

# 1. Multi-way Conditional and Guard Clauses
def get_discount(membership_level, total_spend):
    # Guard clause
    if total_spend <= 0:
        return 0.0

    if membership_level == "Gold":
        return 0.20
    elif membership_level == "Silver":
        return 0.10
    else:
        return 0.05

print("Gold member discount:", get_discount("Gold", 150))

# 2. Ternary operator demo
score = 85
grade = "Pass" if score >= 50 else "Fail"
print(f"Score: {score}, Grade: {grade}")

# 3. Match Case pattern matching (Python 3.10+)
def handle_command(command):
    match command.split():
        case ["quit"]:
            return "Exiting application..."
        case ["load", filename]:
            return f"Loading file: {filename}"
        case ["save", filename, "force"]:
            return f"Force saving: {filename}"
        case _:
            return "Unknown command"

print(handle_command("load data.csv"))
print(handle_command("quit"))
