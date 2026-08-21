# Exception Handling Examples and Practice

# 1. Handling Multiple Exceptions
def divide_values(a, b):
    try:
        val_a = float(a)
        val_b = float(b)
        result = val_a / val_b
    except ValueError as e:
        print(f"ValueError caught: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")
        return None
    else:
        print("Division completed successfully.")
        return result
    finally:
        print("Cleanup operations (if any) executed here.")

print("Divide 10 by 2:", divide_values(10, 2))
print("Divide 10 by 0:", divide_values(10, 0))
print("Divide 10 by 'abc':", divide_values(10, "abc"))

# 2. Custom Exception Class
class AgeRestrictionError(Exception):
    """Custom exception raised when age is less than required."""
    def __init__(self, age, required_age=18):
        self.age = age
        self.required_age = required_age
        super().__init__(f"Age {age} is below the required age of {required_age}.")

def check_voting_eligibility(age):
    if age < 18:
        raise AgeRestrictionError(age)
    return "Eligible"

try:
    check_voting_eligibility(15)
except AgeRestrictionError as e:
    print("Voting Error:", e)
