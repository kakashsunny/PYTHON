# Functions Examples and Practice

# 1. Mutable Default Arguments Bug & Fix
def bad_add_item(item, lst=[]):
    lst.append(item)
    return lst

print("Bad (1):", bad_add_item("apple"))
print("Bad (2):", bad_add_item("banana"))  # Persists!

def good_add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Good (1):", good_add_item("apple"))
print("Good (2):", good_add_item("banana"))  # Correctly isolated!

# 2. Args and Kwargs demonstration
def print_details(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

print_details(1, 2, 3, status="active", role="user")

# 3. Nonlocal Scope (Closure)
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()
print("Counter 1:", my_counter())
print("Counter 2:", my_counter())
